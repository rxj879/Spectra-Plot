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

import MyCustomLibraries.InsetPlotOptions_GUI as iplot_gui
# Import the Inset Plot Options Gui frame design

from MyCustomLibraries.SpectraDA_Func_Def import (InsetLineColourRev,
                                                  InsetLineColourArray)
# Import custom functions

class InsetPlotOptions(wx.Frame):
    """Control functions for the inset plot options"""    
    def __init__(self, parent=None):
        """Initialise the frame"""
        iplot_gui.InsetPlotOptions.__init__(self, parent)
    
    def On_CHKBox_InsetLabelBackgroundWhite(self, event):
        """Set label background white"""
        self.CHKBox_ForwardTruthApply('InsetLabelBackgroundWhite')
        self.OnRadioBox_NormChoices( event )

    def On_CHKBox_YInsetAxisTicksOption(self, event):
        """Add y axis ticks"""
        self.CHKBox_InverseTruthApply('YInsetAxisTicksOption')
        self.OnRadioBox_NormChoices( event )

    def OnSpinCtrl_Inset_LowerLeftX(self, event):
        """Position of the insets lower left corner x coordinate"""
        self.AdjustInsetDimension( event, 'LowerLeftX')
        
    def OnSpinCtrl_Inset_LowerLeftY(self, event):
        """Position of the insets lower left corner y coordinate"""
        self.AdjustInsetDimension( event, 'LowerLeftY')
        
    def OnSpinCtrl_Inset_Width(self, event):
        """Inset width"""
        self.AdjustInsetDimension( event, 'Width')

    def OnSpinCtrl_Inset_Height(self, event):
        """Inset height"""
        self.AdjustInsetDimension( event, 'Height')

    def InsetDimenstionSpinnorValueSet(self, DICT_Label):
        """Spinnor control - generic value set spinnor value"""
        Value = self.FullSpectrumGroup.ReturnInsetSize_Pos(DICT_Label)
        self.__dict__['m_SpinCtrl_Inset_' + DICT_Label].SetValue(Value)
        
    def AdjustInsetDimension(self, event, DICT_Label):
        """Spinnor control - generic value set inset param"""
        Value = self.__dict__['m_SpinCtrl_Inset_' + DICT_Label].GetValue()
        self.FullSpectrumGroup.ChangeInsetSize_Pos(DICT_Label , Value)
        self.OnRadioBox_NormChoices( event )

    def On_CHKBox_InsetPlotOption(self, event):
        """Checkbox true/false set"""
        self.CHKBox_ForwardTruthApply('InsetPlotOption')
        self.OnRadioBox_NormChoices( event )
        
    def OnSpinCtrl_InsetLabelsTextSize(self, event):
        """Spin control label text size"""
        self.ChangeNumericGeneralPlotOption ( event, 'InsetLabelsTextSize')
        
    def OnSpinCtrl_X_insetaxis_Label_Pad(self, event):
        """spin control label pad"""
        self.ChangeNumericGeneralPlotOption ( event, 'X_insetaxis_Label_Pad')
        
    def OnSpinCtrl_RShift_inset_Min(self, event):
        """Spin control - Raman shift minimum"""
        self.ChangeNumericGeneralPlotOption ( event, 'RShift_inset_Min')
        
    def OnSpinCtrl_RShift_inset_Max(self, event):
        """Spin control - Raman shift maxmimum"""
        self.ChangeNumericGeneralPlotOption ( event, 'RShift_inset_Max')
        
    def OnSpinCtrl_Inset_XAxis_NumInc(self, event):
        """Spin control - Raman shift increment"""
        self.ChangeNumericGeneralPlotOption ( event, 'Inset_XAxis_NumInc')

    def OnSpinCtrl_Inset_XAxis_MinorNumInc(self, event):
        """Spin control - Raman shift minor increment"""
        self.ChangeNumericGeneralPlotOption ( event, 'Inset_XAxis_MinorNumInc') 

    def OnSpinCtrl_Inset_YAxis_NumInc(self, event):
        """Spin control - Intensity axis increment"""
        self.ChangeNumericGeneralPlotOption ( event, 'Inset_YAxis_NumInc')
        
    def OnComboBoxSelect_InsetLineColour(self, event):
        """Drop list for inset line colour"""
        n = self.m_ComboBox_InsetLineColour.GetCurrentSelection()
        Colour = self.m_ComboBox_InsetLineColour.GetString(n)
        self.FullSpectrumGroup.SetNewInsetColour(Colour)
        self.OnRadioBox_NormChoices( event )
        
    def OnButtonClick_InsetLineJoin(self, event):
        """Switch control for the inset projection lines"""
        self.FullSpectrumGroup.InsetLineJoin_Switch()
        self.OnRadioBox_NormChoices( event )
        
    def InsetColourComboBoxSet(self ):
        """Set colour of inset line colour"""
        InsetLineColour = InsetLineColourRev(self.FullSpectrumGroup.InsetLineColour)
        ColoursList = InsetLineColourArray()
        self.m_ComboBox_InsetLineColour.SetSelection(ColoursList.index(InsetLineColour))

    def PopulateInsetPlotOptions(self):
        """Populate the inset frame options"""
        self.GenPlotOption_ForwardTruthSet('InsetPlotOption')
        self.GenPlotOption_ForwardTruthSet('InsetLabelBackgroundWhite')
        self.GenPlotOption_InverseTruthSet('YInsetAxisTicksOption')
        self.SetSpinnorGenPlotValueOnOpen ('InsetLabelsTextSize')
        self.SetSpinnorGenPlotValueOnOpen ('X_insetaxis_Label_Pad')
        self.SetSpinnorGenPlotValueOnOpen ('RShift_inset_Max')
        self.SetSpinnorGenPlotValueOnOpen ('RShift_inset_Min')
        self.SetSpinnorGenPlotValueOnOpen ('Inset_XAxis_NumInc')
        self.SetSpinnorGenPlotValueOnOpen ('Inset_XAxis_MinorNumInc')
        self.SetSpinnorGenPlotValueOnOpen ('Inset_YAxis_NumInc')
        self.InsetDimenstionSpinnorValueSet('LowerLeftX')
        self.InsetDimenstionSpinnorValueSet('LowerLeftY')
        self.InsetDimenstionSpinnorValueSet('Width')
        self.InsetDimenstionSpinnorValueSet('Height')
        self.InsetColourComboBoxSet()

    def InsetPlotOptionsQuit(self, event):
        """ vitrual override of the application exit close event"""
        event.Skip() 