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

import wx
# Import wx for the gui control

from MyCustomLibraries.SpectraDA_Func_Def import LineColourArray, LineStyleArray
# Import custom functions required

class MainFrame ( wx.Frame ):
    """wx frame design for the main gui"""
    
    def __init__( self, parent ):
        """initialise wx frame"""
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, 
                     title = u"Spectrum Analyser",
                     pos = wx.Point(10,10),#wx.DefaultPosition, 
                     size = wx.Size( 1000,600 ), 
                     style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        
################################################################
        """box and grid definitions"""
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
       
        bSizer10 = wx.BoxSizer( wx.VERTICAL )
        gSizer10 = wx.GridSizer( 0, 2, 0, 0 )

        bSizer20 = wx.BoxSizer( wx.VERTICAL ) 
        gSizer20 = wx.GridSizer( 0, 2, 0, 0 ) 
        bSizer21 = wx.BoxSizer( wx.VERTICAL ) 

        bSizer30 = wx.BoxSizer( wx.VERTICAL ) 
        gSizer30 = wx.GridSizer( 0, 7, 0, 0 )  
        bSizer31 = wx.BoxSizer( wx.VERTICAL ) 
        bSizer32 = wx.BoxSizer( wx.VERTICAL ) 
        bSizer33 = wx.BoxSizer( wx.VERTICAL ) 
        bSizer34 = wx.BoxSizer( wx.VERTICAL )
        bSizer35 = wx.BoxSizer( wx.VERTICAL )
        bSizer36 = wx.BoxSizer( wx.VERTICAL )

        bSizer40 = wx.BoxSizer( wx.VERTICAL )
        gSizer40 = wx.GridSizer( 0, 4, 0, 0 )
        
        bSizer50 = wx.BoxSizer( wx.VERTICAL )
        gSizer50 = wx.GridSizer( 0, 4, 0, 0 )
        bSizer51 = wx.BoxSizer( wx.VERTICAL )
        bSizer52 = wx.BoxSizer( wx.VERTICAL )
        bSizer53 = wx.BoxSizer( wx.VERTICAL )
        bSizer54 = wx.BoxSizer( wx.VERTICAL )

################################################################
        """wx widget definitions"""        
        self.m_staticText_DIR = wx.StaticText( self, wx.ID_ANY, u"Spectra Directory", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_DIR.Wrap( -1 )
                     
        self.m_textCtrl_DIR = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, (800, -1), 0 )
              
        self.m_button_select_directory = wx.Button( self, wx.ID_ANY, u"Select Directory", wx.DefaultPosition, wx.DefaultSize, 0 )
        
        self.m_button_Import_Data = wx.Button( self, wx.ID_ANY, u"Import Data", wx.DefaultPosition, wx.DefaultSize, 0 )
        
        """Add widgets to box and grid definitions"""
        bSizer10.Add( self.m_staticText_DIR, 0, wx.ALL, 5 )
        bSizer10.Add( self.m_textCtrl_DIR, 0, wx.ALL, 5 )
        gSizer10.Add( self.m_button_select_directory, 0, wx.ALL,5 )
        gSizer10.Add( self.m_button_Import_Data, 0, wx.ALL, 5 )
        bSizer10.Add( gSizer10, 1, wx.EXPAND, 5 )
        
        bSizer1.Add( bSizer10, 1, wx.EXPAND, 5 )

################################################################
        """Add horizontal line"""
        self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer1.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )       

################################################################
        """wx widget definitions"""
        self.m_ListCtrl_Spectra = wx.ListCtrl(self, wx.ID_ANY, wx.DefaultPosition, (800,-1),
                                              style = wx.LC_REPORT |wx.BORDER_SUNKEN)
        
        self.m_ListCtrl_Spectra.InsertColumn(0, 'File Name')
        self.m_ListCtrl_Spectra.SetColumnWidth(0, 500)
        self.m_ListCtrl_Spectra.InsertColumn(1, 'Series Name')
        self.m_ListCtrl_Spectra.SetColumnWidth(1, 500)
        
        """Add widgets to the box and grid definitions"""
        bSizer21.Add(self.m_ListCtrl_Spectra, 0, wx.ALL, 5)
        gSizer20.Add(bSizer21, 1, wx.ALL, 5 )
        bSizer20.Add( gSizer20, 1, wx.EXPAND, 5 )

        bSizer1.Add( bSizer20, 1, wx.EXPAND, 5 )

################################################################
        """wx widget definitions"""
        self.m_button_Move_UP = wx.Button( self, wx.ID_ANY, u"Move Up",  wx.DefaultPosition, wx.DefaultSize, 0 )
        
        self.m_button_Move_DOWN = wx.Button( self, wx.ID_ANY, u"Move Down", wx.DefaultPosition, wx.DefaultSize, 0 )

        Colour_List = LineColourArray()
        self.m_ComboBox_Colour = wx.ComboBox(self, wx.ID_ANY, "Colour", wx.DefaultPosition,
                                             wx.DefaultSize, Colour_List, 0)

        Style_List = LineStyleArray()
        self.m_ComboBox_LineSty = wx.ComboBox(self, wx.ID_ANY, "Style", wx.DefaultPosition,
                                             wx.DefaultSize, Style_List, 0)

        self.m_StaticText_LabelEntry =  wx.StaticText( self, wx.ID_ANY, u"Change Label --> Hit Enter", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_StaticText_LabelEntry.Wrap( -1 )
        
        self.m_textCtrl_SeriesLabel = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString , wx.DefaultPosition, wx.DefaultSize, 0 | wx.TE_PROCESS_ENTER   )
        
        self.m_button_MoveLabel = wx.Button( self, wx.ID_ANY, u"Move Label",  wx.DefaultPosition, wx.DefaultSize, 0 )
      
        self.m_button_TruncateSpectra = wx.Button( self, wx.ID_ANY, u"Truncate Spectra",  wx.DefaultPosition, wx.DefaultSize, 0 )
        
        self.m_CHKBox_IncludeSelectedSpectrum = wx.CheckBox(self, id=wx.ID_ANY, label="Include Selected Series", pos=wx.DefaultPosition,
                                                  size=wx.DefaultSize, style=0, validator=wx.DefaultValidator,
                                                  name='Include Selected Series')
        
        self.m_CHKBox_IncludeSelectedSpectrum_INSET = wx.CheckBox(self, id=wx.ID_ANY, label="Include Selected Series in Inset", pos=wx.DefaultPosition,
                                                  size=wx.DefaultSize, style=0, validator=wx.DefaultValidator,
                                                  name='Include Selected Series in Inset')
        

        
        """Add widgets to the box and grid definitions"""
        bSizer31.Add(self.m_button_Move_UP, 1, wx.EXPAND, 5 )
        bSizer31.Add(self.m_button_Move_DOWN, 1, wx.EXPAND, 5 )
        gSizer30.Add(bSizer31, 1, wx.EXPAND,5 )
        bSizer32.Add(self.m_ComboBox_Colour, 1, wx.EXPAND, 5 )
        bSizer32.Add(self.m_ComboBox_LineSty, 1, wx.EXPAND, 5 )
        gSizer30.Add(bSizer32, 1, wx.EXPAND, 5 )
        bSizer33.Add(self.m_StaticText_LabelEntry, 1, wx.EXPAND, 5 )
        bSizer33.Add(self.m_textCtrl_SeriesLabel, 1, wx.EXPAND, 5 )
        gSizer30.Add(bSizer33, 1, wx.EXPAND, 5 )
        bSizer34.Add(self.m_button_MoveLabel, 1, wx.ALL, 5 )
        gSizer30.Add(bSizer34, 1, wx.EXPAND, 5 )
        bSizer35.Add(self.m_button_TruncateSpectra, 1, wx.EXPAND, 5 )
        gSizer30.Add(bSizer35, 1, wx.EXPAND, 5 )
        bSizer36.Add(self.m_CHKBox_IncludeSelectedSpectrum, 0, wx.EXPAND, 5)
        bSizer36.Add(self.m_CHKBox_IncludeSelectedSpectrum_INSET, 0, wx.EXPAND, 5)
        gSizer30.Add(bSizer36, 1, wx.ALL, 5 )
        bSizer30.Add( gSizer30, 1, wx.EXPAND, 5 )

        bSizer1.Add( bSizer30, 1, wx.EXPAND, 5 )
        
################################################################     
        """Add horizontal line"""
        self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer1.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
        
################################################################        
        """wx widget definitions"""
        m_radioBox_NormChoices = [ u"None" , u"Vector Normalisation", u"Standard Normal Variate", u"Zero-to-One Normalisation" ]
        
        self.m_radioBox_Norm = wx.RadioBox( self, wx.ID_ANY, u"Normalisation Option", wx.DefaultPosition, wx.DefaultSize, m_radioBox_NormChoices, 1, wx.RA_SPECIFY_COLS )
        self.m_radioBox_Norm.SetSelection( 0 )
        
        m_radioBox_PlotChoices = [  u"Single Plot", u"Offset Plot", u"Multi- Plot" ]
        
        self.m_radioBox_Plot = wx.RadioBox( self, wx.ID_ANY, u"Plot Option", wx.DefaultPosition, wx.DefaultSize, m_radioBox_PlotChoices, 1, wx.RA_SPECIFY_COLS )
        self.m_radioBox_Plot.SetSelection( 0 )
                
        self.m_button_GeneralPlotOptions = wx.Button( self, wx.ID_ANY, u"General Plot Options",  wx.DefaultPosition, wx.DefaultSize, 0 )
        
        self.m_button_InsetPlotOptions = wx.Button( self, wx.ID_ANY, u"Inset Plot Options",  wx.DefaultPosition, wx.DefaultSize, 0 )
        
        """Add widgets to the box and grid definitions"""
        gSizer40.Add( self.m_radioBox_Norm, 0, wx.ALL, 5 )        
        gSizer40.Add( self.m_radioBox_Plot, 0, wx.ALL, 5 )        
        bSizer40.Add( self.m_button_GeneralPlotOptions, 0, wx.ALL, 5 )
        bSizer40.Add( self.m_button_InsetPlotOptions, 0, wx.ALL, 5 )
        gSizer40.Add( bSizer40, 1, wx.EXPAND, 5 )

        bSizer1.Add( gSizer40, 1, wx.EXPAND, 5 )        
        
################################################################     
        """Add horizontal line"""
        self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer1.Add( self.m_staticline1, 0, wx.EXPAND , 5 )

################################################################
        """wx widget definitions"""
        self.m_button_Export = wx.Button( self, wx.ID_ANY, u"Export Figure", wx.DefaultPosition, wx.DefaultSize, 0 )
        
        self.m_button_SavePrefs = wx.Button( self, wx.ID_ANY, u"Save Local Prefs Files", wx.DefaultPosition, wx.DefaultSize, 0 )

        self.m_button_RestoreDefaultGenPrefs = wx.Button( self, wx.ID_ANY, u"Restore Default General Plot Prefs", wx.DefaultPosition, wx.DefaultSize, 0 )

        self.m_button_RestoreDefaultSpecPrefs = wx.Button( self, wx.ID_ANY, u"Restore Default Spectra Plot Prefs", wx.DefaultPosition, wx.DefaultSize, 0 )
        
        """Add widgets to box and grid definitions"""
        bSizer51.Add( self.m_button_Export, 0, wx.ALL, 5 )
        gSizer50.Add( bSizer51, 1, wx.EXPAND, 5 )
        bSizer52.Add( self.m_button_SavePrefs, 0, wx.ALL, 5 )
        gSizer50.Add( bSizer52, 1, wx.EXPAND, 5 )
        bSizer53.Add( self.m_button_RestoreDefaultGenPrefs, 0, wx.ALL, 5 )
        gSizer50.Add( bSizer53, 1, wx.EXPAND, 5 )        
        bSizer54.Add( self.m_button_RestoreDefaultSpecPrefs, 0, wx.ALL, 5 )
        gSizer50.Add( bSizer54, 1, wx.EXPAND, 5 )      
        bSizer50.Add( gSizer50, 1, wx.EXPAND, 5 ) 
        
        bSizer1.Add( bSizer50, 1, wx.EXPAND, 5 ) 

################################################################

        self.SetSizer( bSizer1 )
        self.Layout()
        self.Centre( wx.BOTH )
        
################################################################
        """Bind widget event handlers to virtual functions"""
        self.Bind(wx.EVT_CLOSE, self.Quit)
        self.m_button_select_directory.Bind( wx.EVT_BUTTON, self.OnButtonClick_select_directory )
        self.m_button_Import_Data.Bind(wx.EVT_BUTTON, self.OnButtonClick_Import_Spectra_Data )
        self.m_radioBox_Norm.Bind( wx.EVT_RADIOBOX, self.OnRadioBox_NormChoices )
        self.m_radioBox_Plot.Bind(wx.EVT_RADIOBOX, self.OnRadioBox_PlotChoices)
        self.m_button_Export.Bind( wx.EVT_BUTTON, self.OnButtonClick_Export)
        self.m_ListCtrl_Spectra.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnListCtrl_SelectedSpectra)
        self.m_button_Move_UP.Bind(wx.EVT_BUTTON, self.OnButtonClick_MoveSpectraUp)
        self.m_button_Move_DOWN.Bind(wx.EVT_BUTTON, self.OnButtonClick_MoveSpectraDown)
        self.m_ComboBox_Colour.Bind(wx.EVT_COMBOBOX, self.OnComboBoxSelect_ColourSelect)
        self.m_ComboBox_LineSty.Bind(wx.EVT_COMBOBOX, self.OnComboBoxSelect_StyleSelect)
        self.m_textCtrl_SeriesLabel.Bind(wx.EVT_TEXT_ENTER, self.OnSeries_TextChange)
        self.m_button_MoveLabel.Bind(wx.EVT_BUTTON, self.OnButtonClick_MoveLabel)
        self.m_button_TruncateSpectra.Bind(wx.EVT_BUTTON, self.OnButtonClick_TruncateSpectra)
        self.m_button_GeneralPlotOptions.Bind(wx.EVT_BUTTON, self.OnButtonClick_GeneralPlotOptions)
        self.m_CHKBox_IncludeSelectedSpectrum.Bind(wx.EVT_CHECKBOX, self.On_CHKBox_IncludeSelectedSpectrum)
        self.m_CHKBox_IncludeSelectedSpectrum_INSET.Bind(wx.EVT_CHECKBOX, self.On_CHKBox_IncludeSelectedSpectrum_INSET)        
        self.m_button_InsetPlotOptions.Bind(wx.EVT_BUTTON, self.OnButtonClick_InsetPlotOptions)
        self.m_button_SavePrefs.Bind(wx.EVT_BUTTON, self.OnButtonClick_SavePrefs)
        self.m_button_RestoreDefaultGenPrefs.Bind(wx.EVT_BUTTON, self.OnButtonClick_RestoreDefaultGenPrefs)
        self.m_button_RestoreDefaultSpecPrefs.Bind(wx.EVT_BUTTON, self.OnButtonClick_RestoreDefaultSpecPrefs)
        
################################################################
    """Virtual event handlers - overridden in child class"""
    def Quit(self, event):
        event.Skip()
        
    def OnButtonClick_RestoreDefaultSpecPrefs(self, event):
        event.Skip()

    def OnButtonClick_RestoreDefaultGenPrefs(self, event):
        event.Skip()

    def OnButtonClick_SavePrefs(self, event):
        event.Skip()
        
    def OnButtonClick_select_directory( self, event ):
        event.Skip()
        
    def OnButtonClick_Import_Spectra_Data( self, event ):
        event.Skip()
    
    def OnRadioBox_NormChoices( self, event ):
        event.Skip()
        
    def OnButtonClick_select_BackGround_file( self, event ):
        event.Skip()
        
    def OnRadioBox_PlotChoices( self, event ):
        event.Skip()
        
    def OnButtonClick_Export( self, event ):
        event.Skip()
        
    def OnListCtrl_SelectedSpectra( self, event ):
        event.Skip()
        
    def OnButtonClick_MoveSpectraUp( self, event ):
        event.Skip()
        
    def OnButtonClick_MoveSpectraDown( self, event ):
        event.Skip()
        
    def OnComboBoxSelect_ColourSelect( self, event ):
        event.Skip()
                
    def OnComboBoxSelect_StyleSelect( self, event ):
        event.Skip()
        
    def OnSeries_TextChange( self, event ):
        event.Skip()        

    def OnButtonClick_MoveLabel( self, event ):
        event.Skip()     

    def OnButtonClick_TruncateSpectra( self, event ):
        event.Skip()     

    def OnButtonClick_GeneralPlotOptions( self, event ):
        event.Skip()     
        
    def On_CHKBox_IncludeSelectedSpectrum( self, event ):
        event.Skip() 
        
    def OnButtonClick_InsetPlotOptions( self, event ):
        event.Skip()    
        
    def On_CHKBox_IncludeSelectedSpectrum_INSET( self, event ):
        event.Skip() 
        