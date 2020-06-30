# -*- coding: utf-8 -*-
"""
   Copyright 2020 DR ROBIN RAFFE PRYCE JONES
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import os
# Used for exiting the program

import MyCustomLibraries.SpectraDA_GUI as gui
# The main GUI Design

import MyCustomLibraries.PositionControl_GUI_Control as pos_gui
# The controls for the lebals positions

import MyCustomLibraries.CropSpectra_GUI_Control as crop_gui
# The controls for cropping the spectra

import MyCustomLibraries.GeneralPlotOptions_GUI_Control as gplot_gui
# The controls for overal plot properties 

import MyCustomLibraries.InsetPlotOptions_GUI_Control as iplot_gui
# The controls for the inset plot properties

import MyCustomLibraries.Export_GUI_Control as export_gui
# The controls for file export

from MyCustomLibraries.SpectraDA_Class_Def import DataClass_Spectra
# The class with member functions for the spectra data

from MyCustomLibraries.SpectraDA_Func_Def import (Get_Dir, 
                                                  LineColourArray, 
                                                  LineColourRev, 
                                                  LineStyleArray , 
                                                  LineStyleRev,
                                                  Radio2NormOption_Y_Variable)
# Custom functions

class MainFrame(gui.MainFrame, export_gui.ExportFrame, gplot_gui.GenPlotOptions,
                iplot_gui.InsetPlotOptions, crop_gui.CropControl, pos_gui.PositionControl):
    """Control functions for the main frame importing all of the subframe classes"""

    def __init__(self,parent):
        """initialise with data and variabels"""
        self.frame_MainFrame = gui.MainFrame.__init__(self,parent)
        self.FullSpectrumGroup = None
        self.parent = parent
        self.frame_Posgui_open = None
        self.frame_Iplotgui_open = None
        self.frame_Cropgui_open = None
        self.frame_Gplotgui_open = None
        self.frame_Exportgui_open = None
        self.Y_Variable = ''
        self.Initital_directory = None

    def CheckandPopulateAllWindows(self):
        """Closes all sub windows"""
        if self.frame_Posgui_open != None:
            self.PopulatePositionControl()

        if self.frame_Iplotgui_open != None:
            self.PopulateInsetPlotOptions()
            
        if self.frame_Cropgui_open != None:
            self.PopulateCropControl()
            
        if self.frame_Gplotgui_open != None:
            self.PopulateGenPlotOptions()

    def Quit(self , event):
        """Exit all progam features"""
        os._exit(1)
        
    def OnButtonClick_RestoreDefaultSpecPrefs(self, event):
        """Restore spectra specific pickle file with default parameters"""
        self.FullSpectrumGroup.Delete_Spectra_Prefs()
        self.FullSpectrumGroup = DataClass_Spectra()
        self.OnButtonClick_Import_Spectra_Data(event)
        
    def OnButtonClick_RestoreDefaultGenPrefs(self, event):
        """Restore general plot options pickel file with default parameters"""
        self.FullSpectrumGroup.Delete_General_Prefs()
        self.FullSpectrumGroup = DataClass_Spectra()
        self.OnButtonClick_Import_Spectra_Data(  event )

    def OnButtonClick_SavePrefs(self, event):
        """Save all preferences to pickle files"""
        self.FullSpectrumGroup.save_General_prefs()
        self.FullSpectrumGroup.save_Spectra_prefs()
        
    def OnButtonClick_select_directory( self, event ):
        """Select the directory containing the spra data in text files"""
        self.FullSpectrumGroup = DataClass_Spectra()
        self.PopulateListSpectra()
        Text_Data_Directory = Get_Dir(self.Initital_directory);
        self.m_textCtrl_DIR.SetValue(Text_Data_Directory)

    def OnButtonClick_Import_Spectra_Data( self, event ):
        """Import the data from the selected directory"""
        Text_Data_Directory = self.m_textCtrl_DIR.GetValue()
        self.FullSpectrumGroup.Import_Data(Text_Data_Directory)
        self.OnRadioBox_NormChoices( event )
        self.PopulateListSpectra()
        self.m_ListCtrl_Spectra.Select(0)
        self.CheckandPopulateAllWindows()

    def OnRadioBox_NormChoices( self, event ):
        """Take the selected normalisation choice and proceed to crop data for the plot"""
        if self.FullSpectrumGroup == None:
            self.OnButtonClick_select_directory(event)
            
        else:
            Norm_RadioBoxOption = self.m_radioBox_Norm.GetSelection()
            self.Y_Variable = Radio2NormOption_Y_Variable(Norm_RadioBoxOption)
            self.CropXData( event )

    def CropXData(self, event):
        """ Apply the crop, normalise and proceed to plot"""
        self.FullSpectrumGroup.CropXBounds(self.Y_Variable)
        self.FullSpectrumGroup.DoSelectedNormalisation(self.Y_Variable)
        self.OnRadioBox_PlotChoices(event)
        
    def OnRadioBox_PlotChoices( self, event ):
        """Take the choice of plot and proceed to plot"""
        if self.FullSpectrumGroup == None or not self.FullSpectrumGroup.Raman_Intensity:
            self.OnButtonClick_select_directory(event)
            
        else:
            if self.m_radioBox_Plot.GetSelection() == 0:
                self.FullSpectrumGroup.Plot_Spectra(self.Y_Variable)

            elif self.m_radioBox_Plot.GetSelection() == 1:
                self.FullSpectrumGroup.Plot_OFFSET_Spectra(self.Y_Variable)
            
            elif self.m_radioBox_Plot.GetSelection() == 2:
                self.FullSpectrumGroup.SUB_Plot_Spectra(self.Y_Variable)
        
    def OnListCtrl_SelectedSpectra( self, event ):
        """Apply the various attributed of a spectra to the gui
        when a spectrum is selected from the list"""
        Series = self.m_ListCtrl_Spectra.GetFirstSelected()
        LineColourCode = self.FullSpectrumGroup.Series_Colour[Series]
        LineStyleCode = self.FullSpectrumGroup.Series_LineSty[Series]
        LineColour = LineColourRev(LineColourCode)
        LineStyle = LineStyleRev(LineStyleCode)
        ColoursList = LineColourArray()
        StyleList = LineStyleArray()
        self.m_ComboBox_Colour.SetSelection(ColoursList.index(LineColour))
        self.m_ComboBox_LineSty.SetSelection(StyleList.index(LineStyle))
        self.m_textCtrl_SeriesLabel.SetValue( self.FullSpectrumGroup.Series_Label[Series])
        Show_True_False = self.FullSpectrumGroup.IncludeSelectedSpectrum[Series]
        self.m_CHKBox_IncludeSelectedSpectrum.SetValue(Show_True_False)
        ShowINSET_True_False = self.FullSpectrumGroup.Series_InsetShow[Series]
        self.m_CHKBox_IncludeSelectedSpectrum_INSET.SetValue(ShowINSET_True_False)
        
        if self.frame_Posgui_open  != None:
            int_Y = self.FullSpectrumGroup.ReturnLegendMoveValue('Y')
            int_X = self.FullSpectrumGroup.ReturnLegendMoveValue('X')
            self.m_SpinCtrl_Y.SetValue(int_Y)
            self.m_SpinCtrl_X.SetValue(int_X)
            
        if self.frame_Cropgui_open != None:
            UpperBound = self.FullSpectrumGroup.ReturnBoundMoveValue('Upper', Series)
            LowerBound = self.FullSpectrumGroup.ReturnBoundMoveValue('Lower', Series)
            self.m_SpinCtrl_MoveUpperBound.SetValue(UpperBound)   
            self.m_SpinCtrl_MoveLowerBound.SetValue(LowerBound)

    def PopulateListSpectra(self):
        """Wipe and repopulate the list of spectra data"""
        self.m_ListCtrl_Spectra.DeleteAllItems()
        
        for i in range(self.FullSpectrumGroup.NumOfSpectra):
            n = self.m_ListCtrl_Spectra.GetItemCount()
            self.m_ListCtrl_Spectra.InsertItem(n, self.FullSpectrumGroup.Series_FileName[i])
            Colour = LineColourRev(self.FullSpectrumGroup.Series_Colour[i])
            self.m_ListCtrl_Spectra.SetItem(n, 1, self.FullSpectrumGroup.Series_Label[i])
            self.m_ListCtrl_Spectra.SetItemTextColour(i , Colour)

    def OnSeries_TextChange( self, event ):
        """Applies a new label to the selected spectrum"""
        Series = self.m_ListCtrl_Spectra.GetFirstSelected()
        
        if Series != -1:
            NewSeriesLabel = self.m_textCtrl_SeriesLabel.GetValue()
            self.FullSpectrumGroup.Series_Label[Series] = NewSeriesLabel
            self.PopulateListSpectra()
            self.m_ListCtrl_Spectra.Select(Series) 
            self.OnRadioBox_NormChoices( event )
            
        else :
            event.Skip()  

    def On_CHKBox_IncludeSelectedSpectrum( self, event ):
        """Check box option as to whether to include the selected specturm"""
        Show_True_False = self.m_CHKBox_IncludeSelectedSpectrum.GetValue()
        Series = self.m_ListCtrl_Spectra.GetFirstSelected()
        self.FullSpectrumGroup.IncludeSelectedSpectrum[Series] = Show_True_False
        self.FullSpectrumGroup.Series_InsetShow[Series] = Show_True_False
        self.OnRadioBox_NormChoices( event )
        
    def On_CHKBox_IncludeSelectedSpectrum_INSET( self, event ):
        """Check box option to include selected spectrum in the inset plot"""
        ShowINSET_True_False = self.m_CHKBox_IncludeSelectedSpectrum_INSET.GetValue()
        Series = self.m_ListCtrl_Spectra.GetFirstSelected()
        self.FullSpectrumGroup.Series_InsetShow[Series] = ShowINSET_True_False
        self.OnRadioBox_NormChoices( event )

    def OnComboBoxSelect_StyleSelect( self, event ):
        """Drop down box for the line style of the selected specturm"""
        Series = self.m_ListCtrl_Spectra.GetFirstSelected()
        
        if Series != -1:
            n = self.m_ComboBox_LineSty.GetCurrentSelection()
            Style = self.m_ComboBox_LineSty.GetString(n)
            self.FullSpectrumGroup.SetNewStyle( Series, Style)
            self.PopulateListSpectra()
            self.m_ListCtrl_Spectra.Select(Series)        
            self.OnRadioBox_NormChoices( event )

    def OnComboBoxSelect_ColourSelect( self, event ):
        """Drop down box for the colour of the selected spectrum"""
        Series = self.m_ListCtrl_Spectra.GetFirstSelected()
        
        if Series != -1:
            n = self.m_ComboBox_Colour.GetCurrentSelection()
            Colour = self.m_ComboBox_Colour.GetString(n)
            self.FullSpectrumGroup.SetNewColour( Series, Colour)
            self.PopulateListSpectra()
            self.m_ListCtrl_Spectra.Select(Series)
            self.OnRadioBox_NormChoices( event )
        
    def OnButtonClick_MoveSpectraUp( self, event ):
        """Move the selected spectrum up"""
        Series = self.m_ListCtrl_Spectra.GetFirstSelected()
        
        if Series != 0:
            self.FullSpectrumGroup.Move_Spectra_Up(Series)
            self.OnRadioBox_NormChoices( event )
            self.PopulateListSpectra()
            self.m_ListCtrl_Spectra.Select(Series-1)

    def OnButtonClick_MoveSpectraDown( self, event ):
        """ Move the selected spectrum down"""
        Series = self.m_ListCtrl_Spectra.GetFirstSelected()
        
        if Series != (self.FullSpectrumGroup.NumOfSpectra-1):
            self.FullSpectrumGroup.Move_Spectra_Down(Series)
            self.OnRadioBox_NormChoices( event )
            self.PopulateListSpectra()
            self.m_ListCtrl_Spectra.Select(Series+1)
            
####################################################################### - CROP SPECTRA
            
    def OnButtonClick_TruncateSpectra( self, event ):
        """open the gui for truncating spectra"""
        if self.frame_Cropgui_open == None:
            self.frame_Cropgui_open = True
            self.frame_Cropgui = crop_gui.CropControl.__init__(self, self.parent)
            if self.FullSpectrumGroup != None:
                self.PopulateCropControl()
                

    def BoundConQuit( self, event ):
        """Quit the crop spectra gui"""
        self.frame_Cropgui_open = None
        event.Skip()
                
####################################################################### - CROP SPECTRA

####################################################################### - INSET
  
    def OnButtonClick_InsetPlotOptions( self, event ):
        """Open the inset plot options gui"""
        if self.frame_Iplotgui_open == None:
            self.frame_Iplotgui_open = True
            self.frame_Iplotgui = iplot_gui.InsetPlotOptions.__init__(self, self.parent)
            if self.FullSpectrumGroup != None:
                self.PopulateInsetPlotOptions(event)


    def InsetPlotOptionsQuit(self, event):
        """Quit the inset plot options gui"""
        self.frame_Iplotgui_open = None
        event.Skip()
            
####################################################################### - INSET

####################################################################### - General Plot Options
        
    def OnButtonClick_GeneralPlotOptions( self, event ):
        """Open the General Plot Options Gui"""
        if self.frame_Gplotgui_open == None:
            self.frame_Gplotgui_open = True
            self.frame_Gplotgui = gplot_gui.GenPlotOptions.__init__(self, self.parent)
            if self.FullSpectrumGroup != None:
                self.PopulateGenPlotOptions()

                
    def GenPlotOptionsQuit(self, event):
        """Quit the General Plot Options Gui"""
        self.frame_Gplotgui_open = None
        event.Skip()
        
####################################################################### - General Plot Options

####################################################################### - LABEL POSITIONS

    def OnButtonClick_MoveLabel( self , event):
        """Open the Move Label Position Control Gui"""
        if self.frame_Posgui_open == None:
            self.frame_Posgui_open = True
            self.frame_Posgui = pos_gui.PositionControl.__init__(self, self.parent)
            self.PopulatePositionControl()

    def PosConQuit( self, event ):
        """Quit the Movel Label Position Control Gui"""
        self.frame_Posgui_open = None  
        event.Skip()
        
####################################################################### - LABEL POSITIONS

####################################################################### - EXPORT FIGURE

    def OnButtonClick_Export( self, event ):
        """Open the Export Figure Gui"""
        if self.FullSpectrumGroup != None and self.frame_Exportgui_open == None:
            self.frame_Exportgui_open = True
            self.frame_Exportgui = export_gui.ExportFrame.__init__(self, self.parent)

        else:
            print('Nothing to export')
            
    def ExportGuiQuit( self, event ):
        """Quit the Export Figure Gui"""
        self.frame_Exportgui_open = None
        event.Skip()
        
####################################################################### - EXPORT FIGURE
