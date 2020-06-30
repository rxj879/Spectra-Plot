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

import MyCustomLibraries.PositionControl_GUI as pos_gui
# import the position control gui frame design for adjusting the label positions

class PositionControl(wx.Frame):
    """Member functions for label position adjustments"""
    
    def __init__(self, parent=None):
        """Initialise the gui frame"""
        pos_gui.PositionControl.__init__(self, parent)
        
    def PopulatePositionControl(self):
        """Populate the position control gui widgets"""
        Series = self.m_ListCtrl_Spectra.GetFirstSelected()
        
        if Series != -1:
            if self.m_radioBox_Plot.GetSelection() == 0:
                int_Y = self.FullSpectrumGroup.ReturnLegendMoveValue('Y')
                int_X = self.FullSpectrumGroup.ReturnLegendMoveValue('X')
            
            elif self.m_radioBox_Plot.GetSelection() == 1 or 2:
                int_Y = self.FullSpectrumGroup.ReturnLabelMoveValue('Y', Series)
                int_X = self.FullSpectrumGroup.ReturnLabelMoveValue('X', Series)
            
            self.m_SpinCtrl_Y.SetValue(int_Y)   
            self.m_SpinCtrl_X.SetValue(int_X)

    def MoveAllLabels(self, event, XY = 'Y', Direction = 1.0):
        """Generic function for moving all labels"""
        Plot_Option = self.m_radioBox_Plot.GetSelection()
        self.FullSpectrumGroup.MoveAllLabels(XY, Direction , Plot_Option )
        Series = self.m_ListCtrl_Spectra.GetFirstSelected()
        
        if self.m_radioBox_Plot.GetSelection() == 0:
            self.FullSpectrumGroup.Legend_loc = 'None'
            int_XY = self.FullSpectrumGroup.ReturnLegendMoveValue(XY)
            
        elif self.m_radioBox_Plot.GetSelection() == 1 or 2:
            int_XY = self.FullSpectrumGroup.ReturnLabelMoveValue(XY, Series)
        
        self.__dict__['m_SpinCtrl_' + XY].SetValue(int_XY)
        self.OnRadioBox_NormChoices( event )  

    def OnSpin_MoveAllLabelsUp( self, event ):
        """Spin control for moving all labels up"""
        self.MoveAllLabels(event , XY = 'Y', Direction = 1.0)  

    def OnSpin_MoveAllLabelsDown( self, event ):
        """Spin control for moving all labels down"""
        self.MoveAllLabels(event , XY = 'Y', Direction = -1.0)  

    def OnSpin_MoveAllLabelsLeft( self, event ):
        """Spin control for moving all labels left"""
        self.MoveAllLabels(event , XY = 'X', Direction = 1.0)  

    def OnSpin_MoveAllLabelsRight( self, event ):
        """Spin control for moving all labels right"""
        self.MoveAllLabels(event  ,  XY = 'X', Direction = - 1.0)   

    def MoveSingleLabel(self, event, XY = 'Y' ):
        """Generic functionfor moving a single label"""
        Series = self.m_ListCtrl_Spectra.GetFirstSelected()
        Move = self.__dict__['m_SpinCtrl_' + XY].GetValue()
        Plot_Option = self.m_radioBox_Plot.GetSelection()
        self.FullSpectrumGroup.MoveOneLabel(XY, Series, Move, Plot_Option)
        self.OnRadioBox_NormChoices( event )           

    def OnSpinCtrl_Y( self, event ):
        """Spin control for moving a single label in y direction"""
        self.MoveSingleLabel( event, 'Y' )  

    def OnSpinCtrl_X( self, event ):
        """Spin control for moving a single label in x direction"""
        self.MoveSingleLabel( event, 'X' )    
        