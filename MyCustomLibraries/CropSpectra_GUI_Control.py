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

import MyCustomLibraries.CropSpectra_GUI as crop_gui
# Import the gui frame design for the truncation of the spectra

class CropControl(wx.Frame):
    """Member functions to truncate the spectra"""
    
    def __init__(self, parent=None):
        """Initialise the gui frame"""
        crop_gui.CropControl.__init__(self, parent)
    

    def MoveSpectralBound(self, event, Bound):
        """Generic functions - Move a spectral bound of an individual spectra"""
        Series = self.m_ListCtrl_Spectra.GetFirstSelected()
        Move = self.__dict__['m_SpinCtrl_Move' + Bound + 'Bound'].GetValue()
        self.FullSpectrumGroup.MoveBound( Series,  Move, Bound )
        self.OnRadioBox_NormChoices( event )

    def MoveALLSpectralBound(self, event, Direction, Bound):
        """Generic functions - Move all spectral bounds simultanously"""
        self.FullSpectrumGroup.MoveALLBound( Direction, Bound )
        Series = self.m_ListCtrl_Spectra.GetFirstSelected()
        BoundValue = self.FullSpectrumGroup.ReturnBoundMoveValue(Bound, Series)
        self.__dict__['m_SpinCtrl_Move' + Bound + 'Bound'].SetValue(BoundValue)   
        self.OnRadioBox_NormChoices( event )
        
    def PopulateCropControl(self):
        """Populate the gui control widgets"""
        Series = self.m_ListCtrl_Spectra.GetFirstSelected()
            
        if Series != -1:
            UpperBound = self.FullSpectrumGroup.ReturnBoundMoveValue('Upper', Series)
            LowerBound = self.FullSpectrumGroup.ReturnBoundMoveValue('Lower', Series)
            self.m_SpinCtrl_MoveUpperBound.SetValue(UpperBound)   
            self.m_SpinCtrl_MoveLowerBound.SetValue(LowerBound)

    def OnSpinCtrl_MoveUpperBound( self, event ):
        """Spin control move upper bound of selected spectra"""
        self.MoveSpectralBound( event, 'Upper')    

    def OnSpinCtrl_MoveLowerBound( self, event ):
        """Spin control move lower bound of selected spectra"""
        self.MoveSpectralBound( event, 'Lower') 

    def OnSpin_MoveAllUpperBounds_UP( self, event ):
        """Spin control move all upper bounds Up"""
        self.MoveALLSpectralBound(event, 1.0 , 'Upper')

    def OnSpin_MoveAllUpperBounds_DOWN( self, event ):
        """Spin control move all upper bounds down"""
        self.MoveALLSpectralBound(event, -1.0 , 'Upper')

    def OnSpin_MoveAllLowerBounds_UP( self, event ):
        """Spin control move all lower bounds up"""
        self.MoveALLSpectralBound(event, 1.0 , 'Lower')

    def OnSpin_MoveAllLowerBounds_DOWN( self, event ):
        """Spin control move all lower bounds down"""
        self.MoveALLSpectralBound(event, -1.0 , 'Lower')
        
    def BoundConQuit( self, event ):
        """Virtual function for handling the close event"""
        event.Skip()