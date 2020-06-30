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

class CropControl ( wx.Frame ):
    """Frame design for the transcating spectra gui"""
    
    def __init__(self,  parent=None):
        """initialise a wx frame"""
        wx.Frame.__init__(self, parent=parent, 
                          title= u"Crop Controls",
                          pos = wx.DefaultPosition, 
                          size = wx.Size( 300,300 ), 
                          style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL| wx.STAY_ON_TOP )
        
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

################################################################   
        """box and grid definitions"""
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
       
        bSizer10 = wx.BoxSizer( wx.VERTICAL )
        
        gSizer10 = wx.GridSizer( 0, 4, 0, 0 )
        
        bSizer11 = wx.BoxSizer( wx.VERTICAL )
        bSizer12 = wx.BoxSizer( wx.VERTICAL )

        gSizer20 = wx.GridSizer( 0, 4, 0, 0 )
        bSizer21 = wx.BoxSizer( wx.VERTICAL )
        bSizer22 = wx.BoxSizer( wx.VERTICAL )

################################################################ 
        """Widget definitions"""

        self.m_staticText_MoveUpperBound = wx.StaticText( self, wx.ID_ANY, u"Move Upper Bound", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_MoveUpperBound.Wrap( -1 )
                       
        self.m_SpinCtrl_MoveUpperBound = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=-10000, max=10000, initial=0,  name="Move Upper Bound")

        self.m_staticText_MoveAllUpperBounds = wx.StaticText( self, wx.ID_ANY, u"Move All Upper Bounds", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_MoveAllUpperBounds.Wrap( -1 )
        
        self.m_SpinButton_MoveAllUpperBounds = wx.SpinButton(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,  style= wx.SP_HORIZONTAL, name="All Upper Bounds")
        self.m_SpinButton_MoveAllUpperBounds.SetRange(-1000, 1000)
        
        self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
               
        self.m_staticText_MoveLowerBound = wx.StaticText( self, wx.ID_ANY, u"Move Lower Bound", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_MoveLowerBound.Wrap( -1 )               

        self.m_SpinCtrl_MoveLowerBound = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=-10, max=10000, initial=0,  name="Move Lower Bound")
        
        self.m_staticText_MoveAllLowerBounds = wx.StaticText( self, wx.ID_ANY, u"Move ALl Lower Bounds", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_MoveAllLowerBounds.Wrap( -1 )
        
        self.m_SpinButton_MoveAllLowerBounds = wx.SpinButton(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,  style= wx.SP_HORIZONTAL, name="All Lower Bounds")
        self.m_SpinButton_MoveAllLowerBounds.SetRange(-10, 1000)
        
        """Add widgets to the box and grid definitions"""
        bSizer11.Add( self.m_staticText_MoveUpperBound, 1, wx.EXPAND,5 )
        bSizer11.Add( self.m_SpinCtrl_MoveUpperBound, 1, wx.ALL,5 )
        gSizer10.Add( bSizer11, 1, wx.ALL,5 )
        gSizer10.AddSpacer( 30 )
        bSizer12.Add(self.m_staticText_MoveAllUpperBounds, 1, wx.ALL,5 )
        bSizer12.Add(self.m_SpinButton_MoveAllUpperBounds, 1, wx.EXPAND,5 )
        gSizer10.Add( bSizer12, 1, wx.ALL,5 )
        bSizer10.Add( gSizer10, 1, wx.EXPAND,5 )      
        bSizer10.Add( self.m_staticline1, 0, wx.EXPAND , 5 )
        
        bSizer21.Add( self.m_staticText_MoveLowerBound, 1, wx.EXPAND,5 )
        bSizer21.Add( self.m_SpinCtrl_MoveLowerBound, 1, wx.ALL,5 )
        gSizer20.Add( bSizer21, 1, wx.ALL,5 )
        gSizer20.AddSpacer( 30 )
        bSizer22.Add(self.m_staticText_MoveAllLowerBounds, 1, wx.ALL,5 )
        bSizer22.Add(self.m_SpinButton_MoveAllLowerBounds, 1, wx.EXPAND,5 )
        gSizer20.Add( bSizer22, 1, wx.ALL,5 ) 
        
        bSizer10.Add( gSizer20, 1, wx.EXPAND,5 )          
        
        bSizer1.Add(bSizer10, 1, wx.ALL, 5 )

        self.SetSizer( bSizer1 )
        self.Layout()
        self.Centre( wx.BOTH )
        
        """Bind the widgets to the virtual function and event handlers"""
        self.Bind( wx.EVT_CLOSE, self.BoundConQuit)
        self.m_SpinCtrl_MoveUpperBound.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_MoveUpperBound )
        self.m_SpinCtrl_MoveUpperBound.Bind(wx.EVT_TEXT_ENTER, self.OnSpinCtrl_MoveUpperBound )
        self.m_SpinCtrl_MoveLowerBound.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_MoveLowerBound )
        self.m_SpinCtrl_MoveLowerBound.Bind(wx.EVT_TEXT_ENTER, self.OnSpinCtrl_MoveLowerBound )
        self.m_SpinButton_MoveAllUpperBounds.Bind(wx.EVT_SPIN_UP, self.OnSpin_MoveAllUpperBounds_UP)
        self.m_SpinButton_MoveAllUpperBounds.Bind(wx.EVT_SPIN_DOWN, self.OnSpin_MoveAllUpperBounds_DOWN)
        self.m_SpinButton_MoveAllLowerBounds.Bind(wx.EVT_SPIN_UP, self.OnSpin_MoveAllLowerBounds_UP)
        self.m_SpinButton_MoveAllLowerBounds.Bind(wx.EVT_SPIN_DOWN, self.OnSpin_MoveAllLowerBounds_DOWN)        
        self.Show()

##############################################################################
        """Virtual function and event handlers - overriden in children classes"""
    def BoundConQuit( self, event ):
        event.Skip()      

    def OnSpinCtrl_MoveUpperBound( self, event ):
        event.Skip()
        
    def OnSpinCtrl_MoveLowerBound( self, event ):
        event.Skip()
        
    def OnSpin_MoveAllUpperBounds_UP( self, event ):
        event.Skip()
        
    def OnSpin_MoveAllUpperBounds_DOWN( self, event ):
        event.Skip()
        
    def OnSpin_MoveAllLowerBounds_UP( self, event ):
        event.Skip()
        
    def OnSpin_MoveAllLowerBounds_DOWN( self, event ):
        event.Skip()