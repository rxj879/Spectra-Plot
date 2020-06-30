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

from MyCustomLibraries.SpectraDA_Func_Def import InsetLineColourArray
# Import custom functions required

class InsetPlotOptions ( wx.Frame ):
    """Inset plot options gui design"""
    
    def __init__(self,  parent=None):
        """initialise wx frame"""
        wx.Frame.__init__(self, parent=parent, 
                          title= u"Inset Plot Controls",
                          pos = wx.DefaultPosition, 
                          size = wx.Size( 800,400 ), 
                          style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL| wx.STAY_ON_TOP )
        
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

################################################################    
        """box and grid definitions"""
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer10 = wx.BoxSizer( wx.VERTICAL )
        bSizer11 = wx.BoxSizer( wx.VERTICAL )
        gSizer10 = wx.GridSizer( 0, 3, 0, 0 )

        bSizer20 = wx.BoxSizer( wx.VERTICAL )
        bSizer21 = wx.BoxSizer( wx.VERTICAL )
        bSizer22 = wx.BoxSizer( wx.VERTICAL )
        bSizer23 = wx.BoxSizer( wx.VERTICAL )
        bSizer24 = wx.BoxSizer( wx.VERTICAL )
        bSizer25 = wx.BoxSizer( wx.VERTICAL )
        gSizer20 = wx.GridSizer( 0, 5, 0, 0 )
################################################################ 
        """wx widget definitions"""
        self.m_CHKBox_InsetPlotOption = wx.CheckBox(self, id=wx.ID_ANY, label="Add an inset plot", pos=wx.DefaultPosition,
                                                  size=wx.DefaultSize, style=0, validator=wx.DefaultValidator,
                                                  name='Add an inset plot')
        
        """Add widgets to box and grid definitions"""
        bSizer11.Add( self.m_CHKBox_InsetPlotOption, 1, wx.ALL,5 )
        gSizer10.Add( bSizer11, 1, wx.ALL,5 )
        bSizer10.Add(gSizer10, 1, wx.ALL, 5 )
        
        bSizer1.Add(bSizer10, 1, wx.ALL, 5 )
        
################################################################
        """Add a horizontal line"""
        self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        
        bSizer1.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )       

################################################################
        """wx widget definitions"""
        self.m_CHKBox_InsetLabelBackgroundWhite = wx.CheckBox(self, id=wx.ID_ANY, label="White label background", pos=wx.DefaultPosition,
                                                  size=wx.DefaultSize, style=0, validator=wx.DefaultValidator,
                                                  name='White label background')       
        
        self.m_CHKBox_YInsetAxisTicksOption = wx.CheckBox(self, id=wx.ID_ANY, label="y axis ticks", pos=wx.DefaultPosition,
                                                  size=wx.DefaultSize, style=0, validator=wx.DefaultValidator,
                                                  name='y axis ticks')     
        
        self.m_staticText_InsetLabelsTextSize = wx.StaticText( self, wx.ID_ANY, u"Inset Text Size", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_InsetLabelsTextSize.Wrap( -1 )
                       
        self.m_SpinCtrl_InsetLabelsTextSize = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=1, max=50, initial=10,  name="Inset Text Size")
        
        self.m_staticText_X_insetaxis_Label_Pad = wx.StaticText( self, wx.ID_ANY, u"x Label Pad", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_X_insetaxis_Label_Pad.Wrap( -1 )
                       
        self.m_SpinCtrl_X_insetaxis_Label_Pad = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=-50, max=50, initial=10,  name="x Label Pad")
        
        self.m_staticText_RShift_inset_Max = wx.StaticText( self, wx.ID_ANY, u"x maximum", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_RShift_inset_Max.Wrap( -1 )
                       
        self.m_SpinCtrl_RShift_inset_Max = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=-50, max=10000, initial=10,  name="x maxmimum")
        
        self.m_staticText_RShift_inset_Min = wx.StaticText( self, wx.ID_ANY, u"x minimum", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_RShift_inset_Min.Wrap( -1 )
                       
        self.m_SpinCtrl_RShift_inset_Min = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=-50, max=10000, initial=10,  name="x minimum")
        
        self.m_staticText_Inset_XAxis_NumInc = wx.StaticText( self, wx.ID_ANY, u"x axis ticks", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Inset_XAxis_NumInc.Wrap( -1 )
                       
        self.m_SpinCtrl_Inset_XAxis_NumInc = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=1, max=50, initial=10,  name="x axis ticks")
        
        self.m_staticText_Inset_XAxis_MinorNumInc = wx.StaticText( self, wx.ID_ANY, u"x axis minor ticks", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Inset_XAxis_MinorNumInc.Wrap( -1 )
                       
        self.m_SpinCtrl_Inset_XAxis_MinorNumInc = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=1, max=50, initial=10,  name="x axis minor ticks")

        self.m_staticText_Inset_YAxis_NumInc = wx.StaticText( self, wx.ID_ANY, u"y axis ticks", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Inset_YAxis_NumInc.Wrap( -1 )
                       
        self.m_SpinCtrl_Inset_YAxis_NumInc = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=1, max=50, initial=10,  name="y axis ticks")
        
        self.m_staticText_Inset_LowerLeftX = wx.StaticText( self, wx.ID_ANY, u"Position in x", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Inset_LowerLeftX.Wrap( -1 )
                       
        self.m_SpinCtrl_Inset_LowerLeftX = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=-500, max=500, initial=50,  name="Position in x")
        
        self.m_staticText_Inset_LowerLeftY = wx.StaticText( self, wx.ID_ANY, u"Position in y", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Inset_LowerLeftY.Wrap( -1 )
                       
        self.m_SpinCtrl_Inset_LowerLeftY = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=-500, max=500, initial=50,  name="Position in y")
        
        self.m_staticText_Inset_Width = wx.StaticText( self, wx.ID_ANY, u"Inset Width", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Inset_Width.Wrap( -1 )
                       
        self.m_SpinCtrl_Inset_Width = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=-500, max=500, initial=50,  name="Inset Width")
        
        self.m_staticText_Inset_Height = wx.StaticText( self, wx.ID_ANY, u"Inset Height", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Inset_Height.Wrap( -1 )
                       
        self.m_SpinCtrl_Inset_Height = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=-500, max=500, initial=50,  name="Inset Height")
        
        self.m_staticText_InsetLineColour = wx.StaticText( self, wx.ID_ANY, u"Inset Line Colour", 
                                                          wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_InsetLineColour.Wrap( -1 )        
        
        InsetColour_List = InsetLineColourArray()
        self.m_ComboBox_InsetLineColour = wx.ComboBox(self, wx.ID_ANY, "Inset Line Colour", wx.DefaultPosition,
                                             wx.DefaultSize, InsetColour_List, 0)
        
        self.m_button_InsetLineJoin = wx.Button( self, wx.ID_ANY, u"Switch Inset Tracer Lines",  wx.DefaultPosition, wx.DefaultSize, 0 )
      
        """Add widgets to the box and grid definitions"""
        bSizer21.Add( self.m_CHKBox_InsetLabelBackgroundWhite, 1, wx.ALL,5 )
        bSizer21.Add( self.m_CHKBox_YInsetAxisTicksOption, 1, wx.ALL,5 )
        bSizer21.Add(self.m_staticText_InsetLabelsTextSize, 1, wx.ALL,5 )
        bSizer21.Add(self.m_SpinCtrl_InsetLabelsTextSize , 1, wx.ALL,5 )
        bSizer21.Add(self.m_staticText_X_insetaxis_Label_Pad, 1, wx.ALL,5 )
        bSizer21.Add(self.m_SpinCtrl_X_insetaxis_Label_Pad , 1, wx.ALL,5 )
        gSizer20.Add( bSizer21, 1, wx.ALL,5 )
        bSizer22.Add(self.m_staticText_RShift_inset_Max, 1, wx.ALL,5 )
        bSizer22.Add(self.m_SpinCtrl_RShift_inset_Max , 1, wx.ALL,5 )
        bSizer22.Add(self.m_staticText_RShift_inset_Min, 1, wx.ALL,5 )
        bSizer22.Add(self.m_SpinCtrl_RShift_inset_Min , 1, wx.ALL,5 )
        bSizer22.Add(self.m_staticText_Inset_XAxis_NumInc, 1, wx.ALL,5 )
        bSizer22.Add(self.m_SpinCtrl_Inset_XAxis_NumInc , 1, wx.ALL,5 )
        gSizer20.Add( bSizer22, 1, wx.ALL,5 )
        bSizer23.Add(self.m_staticText_Inset_LowerLeftX, 1, wx.ALL,5 )
        bSizer23.Add(self.m_SpinCtrl_Inset_LowerLeftX, 1, wx.ALL,5 )
        bSizer23.Add(self.m_staticText_Inset_LowerLeftY, 1, wx.ALL,5 )
        bSizer23.Add(self.m_SpinCtrl_Inset_LowerLeftY, 1, wx.ALL,5 )
        bSizer23.Add(self.m_staticText_Inset_XAxis_MinorNumInc, 1, wx.ALL,5 )
        bSizer23.Add(self.m_SpinCtrl_Inset_XAxis_MinorNumInc, 1, wx.ALL,5 )
        gSizer20.Add( bSizer23, 1, wx.ALL,5 )
        bSizer24.Add(self.m_staticText_Inset_Width, 1, wx.ALL,5 )
        bSizer24.Add(self.m_SpinCtrl_Inset_Width, 1, wx.ALL,5 )
        bSizer24.Add(self.m_staticText_Inset_Height, 1, wx.ALL,5 )
        bSizer24.Add(self.m_SpinCtrl_Inset_Height, 1, wx.ALL,5 )
        bSizer24.Add(self.m_staticText_Inset_YAxis_NumInc, 1, wx.ALL,5 )
        bSizer24.Add(self.m_SpinCtrl_Inset_YAxis_NumInc , 1, wx.ALL,5 )
        gSizer20.Add( bSizer24, 1, wx.ALL,5 )
        bSizer25.Add( self.m_staticText_InsetLineColour , 1, wx.ALL,5 )
        bSizer25.Add( self.m_ComboBox_InsetLineColour , 1, wx.ALL,5 )
        bSizer25.Add( self.m_button_InsetLineJoin , 1, wx.ALL,5 )
        gSizer20.Add( bSizer25, 1, wx.ALL,5 )
        bSizer20.Add(gSizer20, 1, wx.EXPAND, 5 )
        
        bSizer1.Add(bSizer20, 1, wx.ALL, 5 )
        
        self.SetSizer( bSizer1 )
        self.Layout()
        self.Centre( wx.BOTH )
        
        """Bind widgets and event handlers to virtual functions"""
        self.Bind( wx.EVT_CLOSE, self.InsetPlotOptionsQuit)
        self.m_CHKBox_InsetPlotOption.Bind(wx.EVT_CHECKBOX, self.On_CHKBox_InsetPlotOption )
        self.m_CHKBox_InsetLabelBackgroundWhite.Bind(wx.EVT_CHECKBOX, self.On_CHKBox_InsetLabelBackgroundWhite )
        self.m_CHKBox_YInsetAxisTicksOption.Bind(wx.EVT_CHECKBOX, self.On_CHKBox_YInsetAxisTicksOption )
        
        self.m_SpinCtrl_InsetLabelsTextSize.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_InsetLabelsTextSize )
        self.m_SpinCtrl_InsetLabelsTextSize.Bind( wx.EVT_TEXT_ENTER, self.OnSpinCtrl_InsetLabelsTextSize )
        
        self.m_SpinCtrl_X_insetaxis_Label_Pad.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_X_insetaxis_Label_Pad )
        self.m_SpinCtrl_X_insetaxis_Label_Pad.Bind( wx.EVT_TEXT_ENTER, self.OnSpinCtrl_X_insetaxis_Label_Pad )
        
        self.m_SpinCtrl_RShift_inset_Max.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_RShift_inset_Max )
        self.m_SpinCtrl_RShift_inset_Max.Bind( wx.EVT_TEXT_ENTER, self.OnSpinCtrl_RShift_inset_Max )
        
        self.m_SpinCtrl_RShift_inset_Min.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_RShift_inset_Min )
        self.m_SpinCtrl_RShift_inset_Min.Bind( wx.EVT_TEXT_ENTER, self.OnSpinCtrl_RShift_inset_Min )
        
        self.m_SpinCtrl_Inset_XAxis_NumInc.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_Inset_XAxis_NumInc )
        self.m_SpinCtrl_Inset_XAxis_NumInc.Bind( wx.EVT_TEXT_ENTER, self.OnSpinCtrl_Inset_XAxis_NumInc )
        
        self.m_SpinCtrl_Inset_XAxis_MinorNumInc.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_Inset_XAxis_MinorNumInc )
        self.m_SpinCtrl_Inset_XAxis_MinorNumInc.Bind( wx.EVT_TEXT_ENTER, self.OnSpinCtrl_Inset_XAxis_MinorNumInc )
        
        self.m_SpinCtrl_Inset_YAxis_NumInc.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_Inset_YAxis_NumInc )
        self.m_SpinCtrl_Inset_YAxis_NumInc.Bind( wx.EVT_TEXT_ENTER, self.OnSpinCtrl_Inset_YAxis_NumInc )
        
        self.m_SpinCtrl_Inset_LowerLeftX.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_Inset_LowerLeftX )
        self.m_SpinCtrl_Inset_LowerLeftX.Bind( wx.EVT_TEXT_ENTER, self.OnSpinCtrl_Inset_LowerLeftX )
        
        self.m_SpinCtrl_Inset_LowerLeftY.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_Inset_LowerLeftY )
        self.m_SpinCtrl_Inset_LowerLeftY.Bind( wx.EVT_TEXT_ENTER, self.OnSpinCtrl_Inset_LowerLeftY )
        
        self.m_SpinCtrl_Inset_Width.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_Inset_Width )
        self.m_SpinCtrl_Inset_Width.Bind( wx.EVT_TEXT_ENTER, self.OnSpinCtrl_Inset_Width )
        
        self.m_SpinCtrl_Inset_Height.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_Inset_Height )
        self.m_SpinCtrl_Inset_Height.Bind( wx.EVT_TEXT_ENTER, self.OnSpinCtrl_Inset_Height )
        
        self.m_ComboBox_InsetLineColour.Bind(wx.EVT_COMBOBOX, self.OnComboBoxSelect_InsetLineColour)
        self.m_button_InsetLineJoin.Bind(wx.EVT_BUTTON, self.OnButtonClick_InsetLineJoin)
        self.Show()

##############################################################################
        """Virtual functions and event handlers - overridden in child classes"""
    def InsetPlotOptionsQuit(self, event):
        event.Skip() 
        
    def OnButtonClick_InsetLineJoin(self, event):
        event.Skip() 

    def OnComboBoxSelect_InsetLineColour(self, event):
        event.Skip() 
        
    def OnSpinCtrl_Inset_LowerLeftX(self, event):
        event.Skip() 
        
    def OnSpinCtrl_Inset_LowerLeftY(self, event):
        event.Skip() 
        
    def OnSpinCtrl_Inset_Width(self, event):
        event.Skip() 

    def OnSpinCtrl_Inset_Height(self, event):
        event.Skip() 

    def OnSpinCtrl_Inset_XAxis_MinorNumInc(self, event):
        event.Skip() 
        
    def OnSpinCtrl_Inset_XAxis_NumInc(self, event):
        event.Skip() 

    def OnSpinCtrl_Inset_YAxis_NumInc(self, event):
        event.Skip() 
        
    def OnSpinCtrl_RShift_inset_Min(self, event):
        event.Skip() 
        
    def OnSpinCtrl_RShift_inset_Max(self, event):
        event.Skip() 
        
    def OnSpinCtrl_X_insetaxis_Label_Pad(self, event):
        event.Skip() 
        
    def OnSpinCtrl_InsetLabelsTextSize(self, event):
        event.Skip() 
        
    def On_CHKBox_InsetPlotOption(self, event):
        event.Skip()   

    def On_CHKBox_InsetLabelBackgroundWhite(self, event):
        event.Skip() 

    def On_CHKBox_YInsetAxisTicksOption(self, event):
        event.Skip() 
