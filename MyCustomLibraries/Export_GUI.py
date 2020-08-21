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

#import wx.xrc

from MyCustomLibraries.SpectraDA_Func_Def import (ExportFormatList,
                                                  ExportResolutionList)
# Import the custom function definitions required

class ExportFrame ( wx.Frame ):
    """Export frame wx gui design"""
    def __init__(self,  parent=None):
        """initialise the wx frame"""
        wx.Frame.__init__(self, parent=parent, 
                          title= u"Export Figure",
                          pos = wx.DefaultPosition, 
                          size = wx.Size( 300,300 ), 
                          style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )
        
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

################################################################         
        """Box and grid definitions"""
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        bSizer10 = wx.BoxSizer( wx.VERTICAL )
        gSizer10 = wx.GridSizer( 0, 2, 0, 0 )
        bSizer11 = wx.BoxSizer( wx.VERTICAL )
        bSizer12 = wx.BoxSizer( wx.VERTICAL )
        gSizer20 = wx.GridSizer( 0, 2, 0, 0 )
        bSizer21 = wx.BoxSizer( wx.VERTICAL )

################################################################ 
        """wx widget definitions"""
        self.m_staticText_Format = wx.StaticText( self, wx.ID_ANY, u"Export Format", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Format.Wrap( -1 )
        
        FormatList = ExportFormatList()
        self.m_ComboBox_Format = wx.ComboBox(self, wx.ID_ANY, "Format", wx.DefaultPosition,
                                             (100,-1), FormatList, 1)
        self.m_ComboBox_Format.SetSelection(0)
        
        self.m_staticText_Resolution = wx.StaticText( self, wx.ID_ANY, u"Export Resolution", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Resolution.Wrap( -1 )
        
        ResolutionList = ExportResolutionList()
        self.m_ComboBox_Resolution = wx.ComboBox(self, wx.ID_ANY, "Resolution", wx.DefaultPosition,
                                             (100,-1), ResolutionList , 0)
        self.m_ComboBox_Resolution.SetSelection(3)
        
        self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        
        self.m_button_ExportFile = wx.Button( self, wx.ID_ANY, u"Export",  wx.DefaultPosition, wx.DefaultSize, 0 )

        """Add widgets to the box and grid sizers"""
        bSizer11.Add( self.m_staticText_Format, 1, wx.EXPAND,5 )
        bSizer11.Add( self.m_ComboBox_Format, 1, wx.ALL,5 )
        gSizer10.Add( bSizer11, 1, wx.ALL,5 )
        gSizer10.AddSpacer( 30 )
        bSizer12.Add(self.m_staticText_Resolution, 1, wx.ALL,5 )
        bSizer12.Add(self.m_ComboBox_Resolution, 1, wx.EXPAND,5 )
        gSizer10.Add( bSizer12, 1, wx.ALL,5 )
        bSizer10.Add( gSizer10, 1, wx.EXPAND,5 )      
        bSizer10.Add( self.m_staticline1, 0, wx.EXPAND , 5 )
        gSizer20.AddSpacer( 30 )        
        bSizer21.Add( self.m_button_ExportFile, 1, wx.EXPAND,5 )
        gSizer20.Add( bSizer21, 1, wx.ALL,5 )
        bSizer10.Add( gSizer20, 1, wx.EXPAND,5 )          
        bSizer1.Add(bSizer10, 1, wx.ALL, 5 )

        self.SetSizer( bSizer1 )
        self.Layout()
        self.Centre( wx.BOTH )
        
        """Bind the widgets event handlers to the virtual functions"""
        self.Bind( wx.EVT_CLOSE, self.ExportGuiQuit)
        self.m_ComboBox_Format.Bind( wx.EVT_COMBOBOX, self.OnComboBox_ExportFormat)
        self.m_ComboBox_Resolution.Bind( wx.EVT_COMBOBOX, self.OnComboBox_ExportResolution )
        self.m_button_ExportFile.Bind( wx.EVT_BUTTON, self.OnButtonClick_ExportFile )
     
        self.Show()
        
##############################################################################
        """Virtual event handler functions - overriden in child class"""
    def ExportGuiQuit( self, event ):
        event.Skip()   

    def OnComboBox_ExportFormat( self, event ):
        event.Skip()      

    def OnComboBox_ExportResolution( self, event ):
        event.Skip()
        
    def OnButtonClick_ExportFile( self, event ):
        event.Skip()
