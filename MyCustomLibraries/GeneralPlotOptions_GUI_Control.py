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

import MyCustomLibraries.GeneralPlotOptions_GUI as gplot_gui
# Import the general plot option frame design

from MyCustomLibraries.SpectraDA_Func_Def import (Legend_PositionOptionsArray,
                                                  InsetLineColourArray)
# Import the custom functions required

class GenPlotOptions(wx.Frame):
    """Member functions for the general plot options gui"""
    
    def __init__(self, parent=None):
        """initialise wx frame"""
        gplot_gui.GenPlotOptions.__init__(self, parent)

    def PopulateGenPlotOptions(self):
        """populate the general plot option widgets with values"""
        self.GenPlotOption_InverseTruthSet('BoxPlotOption')
        self.GenPlotOption_InverseTruthSet('YAxisTickLabelsOption')
        self.GenPlotOption_InverseTruthSet('YAxisTicksOption')
        self.GenPlotOption_ForwardTruthSet('LegendFrameOption')
        self.GenPlotOption_ForwardTruthSet('ShowLegendOption')
        self.GenPlotOption_ForwardTruthSet('YAxisExponentialOption')
        self.GenPlotOption_ForwardTruthSet('MultiPlot_shareyOption')
        self.GenPlotOption_ForwardTruthSet('MultiPlot_sharexOption')
        self.GenPlotOption_ForwardTruthSet('OverrideXAxisOption')
        self.GenPlotOption_ForwardTruthSet('OverrideYAxisOption')
        self.GenPlotOption_ForwardTruthSet('MajorXgridlinesOption')
        self.GenPlotOption_ForwardTruthSet('MajorYgridlinesOption')
        self.GenPlotOption_ForwardTruthSet('MinorXgridlinesOption')
        self.GenPlotOption_ForwardTruthSet('MinorYgridlinesOption')
        self.SetSpinnorGenPlotValueOnOpen ('PlotTextSize')
        self.SetSpinnorGenPlotValueOnOpen ('Num_X_MinorTicks')
        self.SetSpinnorGenPlotValueOnOpen ('Num_X_Ticks')
        self.SetSpinnorGenPlotValueOnOpen ('X_Axis_LowLim')
        self.SetSpinnorGenPlotValueOnOpen ('X_Axis_HiLim')
        self.SetSpinnorGenPlotValueOnOpen ('Num_Y_MinorTicks')
        self.SetSpinnorGenPlotValueOnOpen ('Num_Y_Ticks')
        self.SetSpinnorGenPlotValueOnOpen ('Y_Axis_LowLim')
        self.SetSpinnorGenPlotValueOnOpen ('Y_Axis_HiLim')
        self.SetSpinnorGenPlotValueOnOpen ('LabelsFontSize')
        self.SetSpinnorGenPlotValueOnOpen ('X_axis_Label_Pad')
        self.SetSpinnorGenPlotValueOnOpen ('Y_axis_Label_Pad')
        self.SetSpinnorGenPlotValueOnOpen ('X_axis_Title_Pad')
        self.SetSpinnorGenPlotValueOnOpen ('Y_axis_Title_Pad')
        self.SetSpinnorGenPlotValueOnOpen ('FigWidth')
        self.SetSpinnorGenPlotValueOnOpen ('FigHeight')
        self.SetAxisTitleTextCtrlEntry('X_AxisTitle')
        self.SetAxisTitleTextCtrlEntry('Y_AxisTitle')
        GridColourList = InsetLineColourArray()
        self.m_ComboBox_MajorGridColour.SetSelection(GridColourList.index(self.FullSpectrumGroup.MajorGridColour))
        self.m_ComboBox_MinorGridColour.SetSelection(GridColourList.index(self.FullSpectrumGroup.MinorGridColour))
        Leg_PosList = Legend_PositionOptionsArray()
        self.m_ComboBox_Legend_loc.SetSelection(Leg_PosList.index(self.FullSpectrumGroup.Legend_loc))
        
    def OnComboBoxSelect_Legend_loc(self, event):
        """Drop down box for the legend location presets"""
        n = self.m_ComboBox_Legend_loc.GetCurrentSelection()
        NewLegend_loc = self.m_ComboBox_Legend_loc.GetString(n)
        self.FullSpectrumGroup.Legend_loc = NewLegend_loc
        self.OnRadioBox_NormChoices( event )

    def On_CHKBox_MajorXgridlinesOption (self, event):
        """Check box for turning on and off major x axis grid lines"""
        self.CHKBox_ForwardTruthApply('MajorXgridlinesOption')
        self.OnRadioBox_NormChoices( event )

    def On_CHKBox_MajorYgridlinesOption (self, event):
        """Check box for turning on and off major y axis grid lines"""
        self.CHKBox_ForwardTruthApply('MajorYgridlinesOption')
        self.OnRadioBox_NormChoices( event )

    def On_CHKBox_MinorXgridlinesOption (self, event):
        """Check box for turning on and off minor x axis grid lines"""
        self.CHKBox_ForwardTruthApply('MinorXgridlinesOption')
        self.OnRadioBox_NormChoices( event )

    def On_CHKBox_MinorYgridlinesOption (self, event):
        """Check box for turning on and off minor y axis grid lines"""
        self.CHKBox_ForwardTruthApply('MinorYgridlinesOption')
        self.OnRadioBox_NormChoices( event )
        
    def OnComboBoxSelect_MajorGridColour (self, event):
        """Drop down box for the major grid lines colour"""
        n = self.m_ComboBox_MajorGridColour.GetCurrentSelection()
        NewColour = self.m_ComboBox_MajorGridColour.GetString(n)
        self.FullSpectrumGroup.MajorGridColour = NewColour
        self.OnRadioBox_NormChoices( event )   

    def OnComboBoxSelect_MinorGridColour (self, event):
        """Drop down box for the minor grid lines colour"""
        n = self.m_ComboBox_MinorGridColour.GetCurrentSelection()
        NewColour = self.m_ComboBox_MinorGridColour.GetString(n)
        self.FullSpectrumGroup.MinorGridColour = NewColour
        self.OnRadioBox_NormChoices( event )   
 
    def SetAxisTitleTextCtrlEntry(self,  AxisTitleDict):
        """Generic function for setting the text control widgets to the current axis titles"""
        CurrentSeriesLabel = self.FullSpectrumGroup.__dict__[AxisTitleDict]
        self.__dict__['m_textCtrl_' + AxisTitleDict].SetValue(CurrentSeriesLabel)

    def OnTextChange_X_AxisTitle(self, event):
        """Change the x axis title"""
        self.ChangeAxisTitle( event , 'X_AxisTitle')
        
    def OnTextChange_Y_AxisTitle(self, event):
        """change the y axis title"""
        self.ChangeAxisTitle( event , 'Y_AxisTitle')
        
    def ChangeAxisTitle(self, event , AxisTitleDict):
        """Generic function for changing the title of an axis from text control widget"""
        NewSeriesLabel = self.__dict__['m_textCtrl_' + AxisTitleDict].GetValue()
        self.FullSpectrumGroup.__dict__[AxisTitleDict] = NewSeriesLabel
        self.OnRadioBox_NormChoices( event )
        
    def SetSpinnorGenPlotValueOnOpen (self, NumDSN):
        """Generic function for setting a spin control widget value"""
        Value = self.FullSpectrumGroup.__dict__[NumDSN]
        self.__dict__['m_SpinCtrl_' + NumDSN].SetValue(Value)
        
    def OnSpinCtrl_Num_X_MinorTicks (self, event):
        """Spin control setting the number of minor x axis ticks"""
        self.TurnOn_OverRideAxisOption('X', event)
        self.ChangeNumericGeneralPlotOption ( event, 'Num_X_MinorTicks') 
        
    def OnSpinCtrl_Num_X_Ticks (self, event):
        """Spin control for setting the number of major x axis ticks"""
        self.TurnOn_OverRideAxisOption('X', event)
        self.ChangeNumericGeneralPlotOption ( event, 'Num_X_Ticks') 

    def OnSpinCtrl_X_Axis_LowLim (self, event):
        """Spin control for setting the lower limit of the x axis"""
        self.TurnOn_OverRideAxisOption('X', event)
        self.ChangeNumericGeneralPlotOption ( event, 'X_Axis_LowLim') 

    def OnSpinCtrl_X_Axis_HiLim (self, event):
        """Spin control for setting the upper limit of the x axis"""
        self.TurnOn_OverRideAxisOption('X', event)
        self.ChangeNumericGeneralPlotOption ( event, 'X_Axis_HiLim') 

    def OnSpinCtrl_Num_Y_MinorTicks (self, event):
        """Spin control for setting the number of minor y axis ticks"""
        self.TurnOn_OverRideAxisOption('Y', event)
        self.ChangeNumericGeneralPlotOption ( event, 'Num_Y_MinorTicks') 
        
    def OnSpinCtrl_Num_Y_Ticks (self, event):
        """Spin control for setting the number of major y axis ticks"""
        self.TurnOn_OverRideAxisOption('Y', event)
        self.ChangeNumericGeneralPlotOption ( event, 'Num_Y_Ticks') 

    def OnSpinCtrl_Y_Axis_LowLim (self, event):
        """Spin control for setting the lower limit of the y axis"""
        self.TurnOn_OverRideAxisOption('Y', event)
        self.ChangeNumericGeneralPlotOption ( event, 'Y_Axis_LowLim') 

    def OnSpinCtrl_Y_Axis_HiLim (self, event):
        """Spin control for setting upper limit of y axis"""
        self.TurnOn_OverRideAxisOption('Y', event)
        self.ChangeNumericGeneralPlotOption ( event, 'Y_Axis_HiLim') 

    def OnSpinCtrl_FigWidth(self, event):
        """Spin control  for setting the figure width"""
        self.ChangeNumericGeneralPlotOption ( event, 'FigWidth') 

    def OnSpinCtrl_FigHeight(self, event):
        """Spin control for setting the figure height"""
        self.ChangeNumericGeneralPlotOption ( event, 'FigHeight')  

    def OnSpinCtrl_PlotTextSize(self, event):
        """Spin control for setting the plot text size"""
        self.ChangeNumericGeneralPlotOption ( event, 'PlotTextSize')
        
    def OnSpinCtrl_LabelsFontSize(self, event):
        """Spin control for setting the label font size"""
        self.ChangeNumericGeneralPlotOption ( event, 'LabelsFontSize')
        
    def OnSpinCtrl_X_axis_Label_Pad(self, event):
        """Spin control for setting the x axis labels pad"""
        self.ChangeNumericGeneralPlotOption ( event, 'X_axis_Label_Pad')
        
    def OnSpinCtrl_Y_axis_Label_Pad(self, event):
        """Spin control for setting the y axis labels pad"""
        self.ChangeNumericGeneralPlotOption ( event, 'Y_axis_Label_Pad')
        
    def OnSpinCtrl_X_axis_Title_Pad(self, event):
        """Spin control for setting the x axis title pad"""
        self.ChangeNumericGeneralPlotOption ( event, 'X_axis_Title_Pad')
        
    def OnSpinCtrl_Y_axis_Title_Pad(self, event):
        """Spin control for setting the y axis title pad"""
        self.ChangeNumericGeneralPlotOption ( event, 'Y_axis_Title_Pad')

    def On_CHKBox_OverrideXAxisOption (self, event):
        """Check box for overriding the x axis default settings"""
        self.CHKBox_ForwardTruthApply('OverrideXAxisOption')
        self.OnSpinCtrl_X_Axis_LowLim(event)
        self.OnSpinCtrl_X_Axis_HiLim(event)
        self.OnRadioBox_NormChoices( event )
        
    def On_CHKBox_OverrideYAxisOption (self, event):
        """Check boc for overriding the y axis default settings"""
        self.CHKBox_ForwardTruthApply('OverrideYAxisOption')
        self.OnSpinCtrl_Y_Axis_LowLim(event)
        self.OnSpinCtrl_Y_Axis_HiLim(event)
        self.OnRadioBox_NormChoices( event )
        
    def On_CHKBox_sharexOption(self, event):
        """Check box for sharing the x axis limits and ticks in multiplot"""
        self.CHKBox_ForwardTruthApply('MultiPlot_sharexOption')
        self.OnRadioBox_NormChoices( event )
        
    def On_CHKBox_shareyOption(self, event):
        """Check box for sharing the y axis limits and ticks in multiplot"""
        self.CHKBox_ForwardTruthApply('MultiPlot_shareyOption')
        self.OnRadioBox_NormChoices( event )
        
    def On_CHKBox_ShowLegendOption(self, event):
        """Check box for showing the legend"""
        self.CHKBox_ForwardTruthApply('ShowLegendOption')
        self.OnRadioBox_NormChoices( event )
        
    def On_CHKBox_YAxisTicksOption(self, event):
        """Check box for turning on and off y axis ticks"""
        self.CHKBox_InverseTruthApply('YAxisTicksOption')
        self.OnRadioBox_NormChoices( event )    
        
    def On_CHKBox_YAxisExponentialOption(self, event):
        """Check box for setting Y axis labels to be exponent"""
        self.CHKBox_ForwardTruthApply('YAxisExponentialOption')
        self.OnRadioBox_NormChoices( event )
        
    def On_CHKBox_YAxisTickLabelsOption(self, event):
        """Check box for turning on and off the y axis labels appearence"""
        self.CHKBox_InverseTruthApply('YAxisTickLabelsOption')
        self.OnRadioBox_NormChoices( event )   
        
    def On_CHKBox_LegendFrameOption(self, event):
        """Check box for turning on and off legend frame box"""
        self.CHKBox_ForwardTruthApply('LegendFrameOption')
        self.OnRadioBox_NormChoices( event )
        
    def On_CHKBox_BoxPlotOption(self, event):
        """Check box for turning on and off the box plot frame option"""
        self.CHKBox_InverseTruthApply('BoxPlotOption')
        self.OnRadioBox_NormChoices( event )  
        
    def GenPlotOption_InverseTruthSet(self, Option):
        """Generic function for applying inverse truth"""
        if self.FullSpectrumGroup.__dict__[Option] == True:
            self.__dict__['m_CHKBox_' + Option].SetValue(False)
            
        else:
            self.__dict__['m_CHKBox_' + Option].SetValue(True)
            
    def GenPlotOption_ForwardTruthSet(self, Option):
        """Generic function for applying forward truth"""
        self.__dict__['m_CHKBox_' + Option].SetValue(self.FullSpectrumGroup.__dict__[Option])
            
    def ChangeNumericGeneralPlotOption (self, event, NumDSN):
        """Generic function for applying numeric value from spin controls"""
        Value = self.__dict__['m_SpinCtrl_' + NumDSN].GetValue()
        self.FullSpectrumGroup.__dict__[NumDSN] = Value
        self.OnRadioBox_NormChoices( event )    

    def CHKBox_ForwardTruthApply(self, Option):
        """Generic check box function for applying forward truth"""
        self.FullSpectrumGroup.__dict__[Option] = self.__dict__['m_CHKBox_' + Option].GetValue()
        
    def CHKBox_InverseTruthApply(self, Option):
        """Generic check box function for applying inverse truth"""
        if self.__dict__['m_CHKBox_' + Option].GetValue():
            self.FullSpectrumGroup.__dict__[Option] = False
            
        else:
            self.FullSpectrumGroup.__dict__[Option] = True
    
    def TurnOn_OverRideAxisOption(self, axis, event):
        """Override axis options when a charecteristic is changed"""
        BOOL = self.__dict__['m_CHKBox_Override' + axis + 'AxisOption'].GetValue()
        if BOOL == False:
            self.__dict__['m_CHKBox_Override' + axis + 'AxisOption'].SetValue(True)
        if axis == 'X':
            self.On_CHKBox_OverrideXAxisOption(event)
        elif axis == 'Y':
            self.On_CHKBox_OverrideYAxisOption(event)