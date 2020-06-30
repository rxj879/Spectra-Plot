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

class PositionControl ( wx.Frame ):
    """wx frame of position control gui design"""
    
    def __init__(self,  parent=None):
        """initialise wx frame"""
        wx.Frame.__init__(self, parent=parent, 
                          title= u"Move Plot Labels",
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
        """wx widget definitions"""
        self.m_staticText_MoveY = wx.StaticText( self, wx.ID_ANY, u"Move Label in y", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_MoveY.Wrap( -1 )
                       
        self.m_SpinCtrl_Y = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=-10000, max=10000, initial=0,  name="Move Label in y")

        self.m_staticText_MoveAllY = wx.StaticText( self, wx.ID_ANY, u"Move All Labels in y", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_MoveAllY.Wrap( -1 )
        
        self.m_SpinButton_MoveAllLabelsY = wx.SpinButton(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,  style= wx.SP_VERTICAL, name="All Labels")
        self.m_SpinButton_MoveAllLabelsY.SetRange(-1000, 1000)
        
        self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
               
        self.m_staticText_MoveX = wx.StaticText( self, wx.ID_ANY, u"Move Label in x", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_MoveX.Wrap( -1 )               

        self.m_SpinCtrl_X = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=-10000, max=10000, initial=0,  name="Move Label in x")
        
        self.m_staticText_MoveAllX = wx.StaticText( self, wx.ID_ANY, u"Move All Labels in x", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_MoveAllX.Wrap( -1 )
        
        self.m_SpinButton_MoveAllLabelsX = wx.SpinButton(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,  style= wx.SP_HORIZONTAL, name="All Labels")
        self.m_SpinButton_MoveAllLabelsX.SetRange(-1000, 1000)

        """Add widgets to the box and grid definitions"""
        bSizer11.Add( self.m_staticText_MoveX, 1, wx.EXPAND,5 )
        bSizer11.Add( self.m_SpinCtrl_X, 1, wx.ALL,5 )
        gSizer10.Add( bSizer11, 1, wx.ALL,5 )
        gSizer10.AddSpacer( 30 )
        bSizer12.Add(self.m_staticText_MoveAllX, 1, wx.ALL,5 )
        bSizer12.Add(self.m_SpinButton_MoveAllLabelsX, 1, wx.EXPAND,5 )
        gSizer10.Add( bSizer12, 1, wx.ALL,5 )
        bSizer10.Add( gSizer10, 1, wx.EXPAND,5 )      
        bSizer10.Add( self.m_staticline1, 0, wx.EXPAND , 5 )
        bSizer21.Add( self.m_staticText_MoveY, 1, wx.EXPAND,5 )
        bSizer21.Add( self.m_SpinCtrl_Y, 1, wx.ALL,5 )
        gSizer20.Add( bSizer21, 1, wx.ALL,5 )
        gSizer20.AddSpacer( 30 )
        bSizer22.Add(self.m_staticText_MoveAllY, 1, wx.ALL,5 )
        bSizer22.Add(self.m_SpinButton_MoveAllLabelsY, 1, wx.EXPAND,5 )
        gSizer20.Add( bSizer22, 1, wx.ALL,5 ) 
        bSizer10.Add( gSizer20, 1, wx.EXPAND,5 )          
        
        bSizer1.Add(bSizer10, 1, wx.ALL, 5 )

        self.SetSizer( bSizer1 )
        self.Layout()
        self.Centre( wx.BOTH )
        
        """Bind widgets and event handlers to virtual functions"""
        self.Bind( wx.EVT_CLOSE, self.PosConQuit)
        self.m_SpinCtrl_Y.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_Y )
        self.m_SpinCtrl_Y.Bind(wx.EVT_TEXT_ENTER, self.OnSpinCtrl_Y )
        self.m_SpinCtrl_X.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_X )
        self.m_SpinCtrl_X.Bind(wx.EVT_TEXT_ENTER, self.OnSpinCtrl_X )
        self.m_SpinButton_MoveAllLabelsY.Bind(wx.EVT_SPIN_UP, self.OnSpin_MoveAllLabelsUp)
        self.m_SpinButton_MoveAllLabelsY.Bind(wx.EVT_SPIN_DOWN, self.OnSpin_MoveAllLabelsDown)
        self.m_SpinButton_MoveAllLabelsX.Bind(wx.EVT_SPIN_UP, self.OnSpin_MoveAllLabelsLeft)
        self.m_SpinButton_MoveAllLabelsX.Bind(wx.EVT_SPIN_DOWN, self.OnSpin_MoveAllLabelsRight)        
       
        self.Show()

###############################################################################
        """Virutal event handler functions - overridden in child classes"""
    def PosConQuit( self, event ):
        event.Skip()      

    def OnSpinCtrl_X( self, event ):
        event.Skip()
        
    def OnSpinCtrl_Y( self, event ):
        event.Skip()
        
    def OnSpin_MoveAllLabelsUp( self, event ):
        event.Skip()
        
    def OnSpin_MoveAllLabelsDown( self, event ):
        event.Skip()
        
    def OnSpin_MoveAllLabelsLeft( self, event ):
        event.Skip()
        
    def OnSpin_MoveAllLabelsRight( self, event ):
        event.Skip()