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

from MyCustomLibraries.SpectraDA_Func_Def import (Legend_PositionOptionsArray,
                                                  InsetLineColourArray)
        
# Import the custom functions required

class GenPlotOptions ( wx.Frame ):
    """wx frame design for the general plot options"""
    
    def __init__(self,  parent=None):
        """initialise the wx frame"""
        wx.Frame.__init__(self, parent=parent, 
                          title= u"Plot Controls",
                          pos = wx.DefaultPosition, 
                          size = wx.Size( 800,600 ), 
                          style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL| wx.STAY_ON_TOP )
        
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

################################################################    
        """box and grid definitions"""
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer10 = wx.BoxSizer( wx.VERTICAL )
        bSizer11 = wx.BoxSizer( wx.VERTICAL )
        bSizer12 = wx.BoxSizer( wx.VERTICAL )
        bSizer13 = wx.BoxSizer( wx.VERTICAL )
        bSizer14 = wx.BoxSizer( wx.VERTICAL )
        bSizer15 = wx.BoxSizer( wx.VERTICAL )
        gSizer10 = wx.GridSizer( 0, 5, 0, 0 )

        bSizer20 = wx.BoxSizer( wx.VERTICAL )
        bSizer21 = wx.BoxSizer( wx.VERTICAL )
        bSizer22 = wx.BoxSizer( wx.VERTICAL )
        bSizer23 = wx.BoxSizer( wx.VERTICAL )
        bSizer24 = wx.BoxSizer( wx.VERTICAL )
        gSizer20 = wx.GridSizer( 0, 6, 0, 0 )
        
        bSizer30 = wx.BoxSizer( wx.VERTICAL )
        bSizer31 = wx.BoxSizer( wx.VERTICAL )
        bSizer32 = wx.BoxSizer( wx.VERTICAL )
        bSizer33 = wx.BoxSizer( wx.VERTICAL )
        bSizer34 = wx.BoxSizer( wx.VERTICAL )
        bSizer35 = wx.BoxSizer( wx.VERTICAL )
        bSizer36 = wx.BoxSizer( wx.VERTICAL )
        gSizer30 = wx.GridSizer( 0, 6, 0, 0 )
        
        bSizer40 = wx.BoxSizer( wx.VERTICAL )
        bSizer41 = wx.BoxSizer( wx.VERTICAL )
        bSizer42 = wx.BoxSizer( wx.VERTICAL )
        gSizer40 = wx.GridSizer( 0, 2, 0, 0 )
        
################################################################ 
        """widget definitions"""
        self.m_CHKBox_ShowLegendOption = wx.CheckBox(self, id=wx.ID_ANY, label="Show Legend", pos=wx.DefaultPosition,
                                                  size=wx.DefaultSize, style=0, validator=wx.DefaultValidator,
                                                  name='Show Legend')
        
        self.m_CHKBox_LegendFrameOption = wx.CheckBox(self, id=wx.ID_ANY, label="Frame Legend", pos=wx.DefaultPosition,
                                                  size=wx.DefaultSize, style=0, validator=wx.DefaultValidator,
                                                  name='Frame Legend')

        Legend_PositionOptions = Legend_PositionOptionsArray()
        self.m_ComboBox_Legend_loc = wx.ComboBox(self, wx.ID_ANY, "Legend_loc", wx.DefaultPosition,
                                             wx.DefaultSize, Legend_PositionOptions, 0)

        self.m_CHKBox_YAxisTickLabelsOption = wx.CheckBox(self, id=wx.ID_ANY, label="Y Axis tick labels", pos=wx.DefaultPosition,
                                                  size=wx.DefaultSize, style=0, validator=wx.DefaultValidator,
                                                  name='Y tick labels')

        self.m_CHKBox_YAxisExponentialOption =  wx.CheckBox(self, id=wx.ID_ANY, label="Exponent Y Labels", pos=wx.DefaultPosition,
                                                  size=wx.DefaultSize, style=0, validator=wx.DefaultValidator,
                                                  name='Exponent Y')
        
        self.m_CHKBox_YAxisTicksOption =  wx.CheckBox(self, id=wx.ID_ANY, label="Y Axis Tick Marks", pos=wx.DefaultPosition,
                                                  size=wx.DefaultSize, style=0, validator=wx.DefaultValidator,
                                                  name='Tick Marks Y')
        
        self.m_CHKBox_BoxPlotOption = wx.CheckBox(self, id=wx.ID_ANY, label="Box Plot", pos=wx.DefaultPosition,
                                                  size=wx.DefaultSize, style=0, validator=wx.DefaultValidator,
                                                  name='Box Plot')
        
        self.m_CHKBox_MultiPlot_shareyOption = wx.CheckBox(self, id=wx.ID_ANY, label="Multi Plot Share Y Axes", pos=wx.DefaultPosition,
                                                  size=wx.DefaultSize, style=0, validator=wx.DefaultValidator,
                                                  name='Multi Share Y')
        
        self.m_CHKBox_MultiPlot_sharexOption = wx.CheckBox(self, id=wx.ID_ANY, label="Multi Plot Share X Axes", pos=wx.DefaultPosition,
                                                  size=wx.DefaultSize, style=0, validator=wx.DefaultValidator,
                                                  name='Multi Share X')

        self.m_CHKBox_OverrideXAxisOption = wx.CheckBox(self, id=wx.ID_ANY, label="Override x axis limits", pos=wx.DefaultPosition,
                                                  size=wx.DefaultSize, style=0, validator=wx.DefaultValidator,
                                                  name='Override x axis limits')
        
        self.m_CHKBox_OverrideYAxisOption = wx.CheckBox(self, id=wx.ID_ANY, label="Override y axis limits", pos=wx.DefaultPosition,
                                                  size=wx.DefaultSize, style=0, validator=wx.DefaultValidator,
                                                  name='Override y axis limits')
        
        self.m_CHKBox_MajorXgridlinesOption = wx.CheckBox(self, id=wx.ID_ANY, label="Add major x axis grid", pos=wx.DefaultPosition,
                                                  size=wx.DefaultSize, style=0, validator=wx.DefaultValidator,
                                                  name='Add major x axis grid')

        self.m_CHKBox_MajorYgridlinesOption = wx.CheckBox(self, id=wx.ID_ANY, label="Add major y axis grid", pos=wx.DefaultPosition,
                                                  size=wx.DefaultSize, style=0, validator=wx.DefaultValidator,
                                                  name='Add major y axis grid')

        self.m_CHKBox_MinorXgridlinesOption = wx.CheckBox(self, id=wx.ID_ANY, label="Add minor x axis grid", pos=wx.DefaultPosition,
                                                  size=wx.DefaultSize, style=0, validator=wx.DefaultValidator,
                                                  name='Add minor x axis grid')

        self.m_CHKBox_MinorYgridlinesOption = wx.CheckBox(self, id=wx.ID_ANY, label="Add minor y axis grid", pos=wx.DefaultPosition,
                                                  size=wx.DefaultSize, style=0, validator=wx.DefaultValidator,
                                                  name='Add minor y axis grid')
        
        GridColours = InsetLineColourArray()
        self.m_ComboBox_MajorGridColour = wx.ComboBox(self, wx.ID_ANY, "Major grid colour", wx.DefaultPosition,
                                             wx.DefaultSize, GridColours, 0)
        
        self.m_ComboBox_MinorGridColour = wx.ComboBox(self, wx.ID_ANY, "Minor grid colour", wx.DefaultPosition,
                                             wx.DefaultSize, GridColours, 0)
        
        self.m_staticText_FigWidth = wx.StaticText( self, wx.ID_ANY, u"Figure Width", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_FigWidth.Wrap( -1 )
                       
        self.m_SpinCtrl_FigWidth = wx.SpinCtrlDouble(self, id=wx.ID_ANY, value="", pos=wx.DefaultPosition,
                                                     size=(100,-1), style=wx.SP_ARROW_KEYS| wx.ALIGN_LEFT ,
                                                     min=1, max=50, initial=2.5, inc=1, name="Figure Width")

        self.m_staticText_FigHeight = wx.StaticText( self, wx.ID_ANY, u"Figure Height", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_FigHeight.Wrap( -1 )
                       
        self.m_SpinCtrl_FigHeight = wx.SpinCtrlDouble(self, id=wx.ID_ANY, value="", pos=wx.DefaultPosition,
                                                     size=(100,-1), style=wx.SP_ARROW_KEYS| wx.ALIGN_LEFT,
                                                     min=1, max=50, initial=1.8, inc=1, name="Height")
        
        """Add widgets to the box and grid definitions"""
        bSizer11.Add( self.m_CHKBox_LegendFrameOption, 1, wx.EXPAND,5 )
        bSizer11.Add( self.m_CHKBox_ShowLegendOption , 1, wx.EXPAND,5 )
        bSizer11.Add( self.m_ComboBox_Legend_loc , 1, wx.EXPAND,5 )
        gSizer10.Add( bSizer11, 1, wx.ALL,5 )
        bSizer12.Add( self.m_CHKBox_YAxisTickLabelsOption, 1, wx.EXPAND,5 )
        bSizer12.Add( self.m_CHKBox_YAxisExponentialOption , 1, wx.EXPAND,5 )
        bSizer12.Add( self.m_CHKBox_YAxisTicksOption , 1, wx.EXPAND,5 )
        bSizer12.Add( self.m_CHKBox_BoxPlotOption, 1, wx.EXPAND,5 )
        gSizer10.Add( bSizer12, 1, wx.ALL,5 )
        bSizer13.Add( self.m_CHKBox_MultiPlot_shareyOption , 1, wx.EXPAND,5 )
        bSizer13.Add( self.m_CHKBox_MultiPlot_sharexOption , 1, wx.EXPAND,5 )
        gSizer10.Add( bSizer13, 1, wx.ALL,5 )
        bSizer14.Add( self.m_CHKBox_OverrideXAxisOption , 1, wx.EXPAND,5 )
        bSizer14.Add( self.m_CHKBox_OverrideYAxisOption , 1, wx.EXPAND,5 )
        bSizer14.Add( self.m_CHKBox_MajorXgridlinesOption , 1, wx.EXPAND,5 )
        bSizer14.Add( self.m_CHKBox_MajorYgridlinesOption , 1, wx.EXPAND,5 )
        bSizer14.Add( self.m_CHKBox_MinorXgridlinesOption , 1, wx.EXPAND,5 )
        bSizer14.Add( self.m_CHKBox_MinorYgridlinesOption , 1, wx.EXPAND,5 )
        bSizer14.Add( self.m_ComboBox_MajorGridColour , 1, wx.EXPAND,5 )
        bSizer14.Add( self.m_ComboBox_MinorGridColour , 1, wx.EXPAND,5 )
        gSizer10.Add( bSizer14, 1, wx.ALL,5 )
        bSizer15.Add(self.m_staticText_FigWidth, 1, wx.ALL,5 )
        bSizer15.Add(self.m_SpinCtrl_FigWidth , 1, wx.ALL,5 )
        bSizer15.Add(self.m_staticText_FigHeight, 1, wx.ALL,5 )
        bSizer15.Add(self.m_SpinCtrl_FigHeight , 1, wx.ALL,5 )
        gSizer10.Add( bSizer15, 1, wx.ALL,5 )
        bSizer10.Add(gSizer10, 1, wx.ALL, 5 )
        
        bSizer1.Add(bSizer10, 1, wx.ALL, 5 )
        
################################################################ 
        """Widget definitions"""
        self.m_staticText_X_Axis_LowLim = wx.StaticText( self, wx.ID_ANY, u"x low limit", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_X_Axis_LowLim.Wrap( -1 )
                       
        self.m_SpinCtrl_X_Axis_LowLim = wx.SpinCtrlDouble(self, id=wx.ID_ANY, value="", pos=wx.DefaultPosition,
                                                     size=(100,-1), style=wx.SP_ARROW_KEYS| wx.ALIGN_LEFT ,
                                                     min=-100000, max=100000, initial=0, inc=100, name="x axis lower limit")

        self.m_staticText_X_Axis_HiLim = wx.StaticText( self, wx.ID_ANY, u"x high limit", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_X_Axis_HiLim.Wrap( -1 )
                       
        self.m_SpinCtrl_X_Axis_HiLim = wx.SpinCtrlDouble(self, id=wx.ID_ANY, value="", pos=wx.DefaultPosition,
                                                     size=(100,-1), style=wx.SP_ARROW_KEYS| wx.ALIGN_LEFT,
                                                     min=-100000, max=100000, initial=0, inc=100, name="x axis higher limit")
        
        self.m_staticText_Num_X_Ticks = wx.StaticText( self, wx.ID_ANY, u"Number of x ticks", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Num_X_Ticks.Wrap( -1 )
                       
        self.m_SpinCtrl_Num_X_Ticks = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=1, max=50, initial=18,  name="Num x ticks")
        
        self.m_staticText_Num_X_MinorTicks = wx.StaticText( self, wx.ID_ANY, u"Number of minor x ticks", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Num_X_MinorTicks.Wrap( -1 )
                       
        self.m_SpinCtrl_Num_X_MinorTicks = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=1, max=50, initial=18,  name="Number of minor x ticks")

        self.m_staticText_Y_Axis_LowLim = wx.StaticText( self, wx.ID_ANY, u"y low limit", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Y_Axis_LowLim.Wrap( -1 )
                       
        self.m_SpinCtrl_Y_Axis_LowLim = wx.SpinCtrlDouble(self, id=wx.ID_ANY, value="", pos=wx.DefaultPosition,
                                                     size=(100,-1), style=wx.SP_ARROW_KEYS| wx.ALIGN_LEFT ,
                                                     min=-100000, max=1E30, initial=0, inc=100, name="y axis lower limit")

        self.m_staticText_Y_Axis_HiLim = wx.StaticText( self, wx.ID_ANY, u"y high limit", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Y_Axis_HiLim.Wrap( -1 )
                       
        self.m_SpinCtrl_Y_Axis_HiLim = wx.SpinCtrlDouble(self, id=wx.ID_ANY, value="", pos=wx.DefaultPosition,
                                                     size=(100,-1), style=wx.SP_ARROW_KEYS| wx.ALIGN_LEFT,
                                                     min=-100000, max=1E30, initial=0, inc=100, name="y axis higher limit")

        self.m_staticText_Num_Y_Ticks = wx.StaticText( self, wx.ID_ANY, u"Number of y ticks", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Num_Y_Ticks.Wrap( -1 )
                       
        self.m_SpinCtrl_Num_Y_Ticks = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=1, max=50, initial=18,  name="Num y ticks")
        
        self.m_staticText_Num_Y_MinorTicks = wx.StaticText( self, wx.ID_ANY, u"Number of minor y ticks", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Num_Y_MinorTicks.Wrap( -1 )
                       
        self.m_SpinCtrl_Num_Y_MinorTicks = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=1, max=50, initial=18,  name="Number of minor y ticks")

        """Add widgets to the box and grid definitions"""
        bSizer21.Add(self.m_staticText_X_Axis_LowLim, 1, wx.ALL,5 )
        bSizer21.Add(self.m_SpinCtrl_X_Axis_LowLim , 1, wx.ALL,5 )
        bSizer21.Add(self.m_staticText_Y_Axis_LowLim, 1, wx.ALL,5 )
        bSizer21.Add(self.m_SpinCtrl_Y_Axis_LowLim , 1, wx.ALL,5 )
        gSizer20.Add( bSizer21, 1, wx.ALL,5 )
        bSizer22.Add(self.m_staticText_X_Axis_HiLim, 1, wx.ALL,5 )
        bSizer22.Add(self.m_SpinCtrl_X_Axis_HiLim , 1, wx.ALL,5 )
        bSizer22.Add(self.m_staticText_Y_Axis_HiLim, 1, wx.ALL,5 )
        bSizer22.Add(self.m_SpinCtrl_Y_Axis_HiLim , 1, wx.ALL,5 )
        gSizer20.Add( bSizer22, 1, wx.ALL,5 )
        bSizer23.Add(self.m_staticText_Num_X_Ticks, 1, wx.ALL,5 )
        bSizer23.Add(self.m_SpinCtrl_Num_X_Ticks , 1, wx.ALL,5 )
        bSizer23.Add(self.m_staticText_Num_Y_Ticks, 1, wx.ALL,5 )
        bSizer23.Add(self.m_SpinCtrl_Num_Y_Ticks , 1, wx.ALL,5 )
        gSizer20.Add( bSizer23, 1, wx.ALL,5 )
        bSizer24.Add(self.m_staticText_Num_X_MinorTicks, 1, wx.ALL,5 )
        bSizer24.Add(self.m_SpinCtrl_Num_X_MinorTicks , 1, wx.ALL,5 )
        bSizer24.Add(self.m_staticText_Num_Y_MinorTicks, 1, wx.ALL,5 )
        bSizer24.Add(self.m_SpinCtrl_Num_Y_MinorTicks , 1, wx.ALL,5 )
        gSizer20.Add( bSizer24, 1, wx.ALL,5 )
        bSizer20.Add(gSizer20, 1, wx.ALL, 5 )

        bSizer1.Add(bSizer20, 1, wx.ALL, 5 )     
        
################################################################ 
        """widget definitions"""
        self.m_staticText_PlotTextSize = wx.StaticText( self, wx.ID_ANY, u"Plot Text Size", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_PlotTextSize.Wrap( -1 )
                       
        self.m_SpinCtrl_PlotTextSize = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=1, max=50, initial=18,  name="Plot Text Size")
        
        self.m_staticText_LabelsFontSize = wx.StaticText( self, wx.ID_ANY, u"Label Text Size", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_LabelsFontSize.Wrap( -1 )
                       
        self.m_SpinCtrl_LabelsFontSize = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=1, max=50, initial=12,  name="Label Text Size")

        self.m_staticText_X_axis_Label_Pad = wx.StaticText( self, wx.ID_ANY, u"x axis label pad", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_X_axis_Label_Pad.Wrap( -1 )
                       
        self.m_SpinCtrl_X_axis_Label_Pad = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=-50, max=50, initial=5,  name="x axis label pad")

        self.m_staticText_Y_axis_Label_Pad = wx.StaticText( self, wx.ID_ANY, u"y axis label pad", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Y_axis_Label_Pad.Wrap( -1 )
                       
        self.m_SpinCtrl_Y_axis_Label_Pad = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=-50, max=50, initial=5,  name="y axis label pad")
        
        self.m_staticText_X_axis_Title_Pad = wx.StaticText( self, wx.ID_ANY, u"x axis title pad", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_X_axis_Title_Pad.Wrap( -1 )
                       
        self.m_SpinCtrl_X_axis_Title_Pad = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=-50, max=50, initial=5,  name="x axis title pad")
        
        self.m_staticText_Y_axis_Title_Pad = wx.StaticText( self, wx.ID_ANY, u"y axis title pad", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Y_axis_Title_Pad.Wrap( -1 )
                       
        self.m_SpinCtrl_Y_axis_Title_Pad = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=-50, max=50, initial=5,  name="y axis title pad")
        
        """Add widgets to the box and grid definitions"""
        bSizer31.Add(self.m_staticText_PlotTextSize, 1, wx.ALL,5 )
        bSizer31.Add(self.m_SpinCtrl_PlotTextSize, 1, wx.ALL,5 )
        gSizer30.Add( bSizer31, 1, wx.ALL,5 )
        bSizer32.Add(self.m_staticText_LabelsFontSize, 1, wx.ALL,5 )
        bSizer32.Add(self.m_SpinCtrl_LabelsFontSize, 1, wx.ALL,5 )
        gSizer30.Add( bSizer32, 1, wx.ALL,5 )
        bSizer33.Add(self.m_staticText_X_axis_Label_Pad, 1, wx.ALL,5 )
        bSizer33.Add(self.m_SpinCtrl_X_axis_Label_Pad, 1, wx.ALL,5 )
        gSizer30.Add( bSizer33, 1, wx.ALL,5 )
        bSizer34.Add(self.m_staticText_Y_axis_Label_Pad, 1, wx.ALL,5 )
        bSizer34.Add(self.m_SpinCtrl_Y_axis_Label_Pad, 1, wx.ALL,5 )
        gSizer30.Add( bSizer34, 1, wx.ALL,5 )
        bSizer35.Add(self.m_staticText_X_axis_Title_Pad, 1, wx.ALL,5 )
        bSizer35.Add(self.m_SpinCtrl_X_axis_Title_Pad, 1, wx.ALL,5 )
        gSizer30.Add( bSizer35, 1, wx.ALL,5 )
        bSizer36.Add(self.m_staticText_Y_axis_Title_Pad, 1, wx.ALL,5 )
        bSizer36.Add(self.m_SpinCtrl_Y_axis_Title_Pad, 1, wx.ALL,5 )
        gSizer30.Add( bSizer36, 1, wx.ALL,5 )
        bSizer30.Add(gSizer30, 1, wx.ALL, 5 )

        bSizer1.Add(bSizer30, 1, wx.ALL, 5 )
        
################################################################
        """widget definitions"""
        self.m_StaticText_X_AxisTitle =  wx.StaticText( self, wx.ID_ANY, u"x axis title (accepts LaTex syntax)--> Hit Enter", wx.DefaultPosition, wx.DefaultSize, 0 )
        
        self.m_textCtrl_X_AxisTitle = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString , wx.DefaultPosition, (200,-1), 0 | wx.TE_PROCESS_ENTER   )
        
        self.m_StaticText_Y_AxisTitle =  wx.StaticText( self, wx.ID_ANY, u"y axis title (accepts LaTex syntax)--> Hit Enter", wx.DefaultPosition, wx.DefaultSize, 0 )
        
        self.m_textCtrl_Y_AxisTitle = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString , wx.DefaultPosition, (200,-1), 0 | wx.TE_PROCESS_ENTER   )

        """Add widgets to the box and grid definitions"""
        bSizer41.Add(self.m_StaticText_X_AxisTitle, 1, wx.ALL,5 )
        bSizer41.Add(self.m_textCtrl_X_AxisTitle, 1, wx.ALL,5 )
        gSizer40.Add( bSizer41, 1, wx.ALL,5 )
        bSizer42.Add(self.m_StaticText_Y_AxisTitle, 1, wx.ALL,5 )
        bSizer42.Add(self.m_textCtrl_Y_AxisTitle, 1, wx.ALL,5 )
        gSizer40.Add( bSizer42, 1, wx.ALL,5 )
        bSizer40.Add(gSizer40, 1, wx.ALL, 5 )
        
        bSizer1.Add(bSizer40, 1, wx.ALL, 5 )
        
################################################################

        self.SetSizer( bSizer1 )
        self.Layout()
        self.Centre( wx.BOTH )
        
        """Bind event handlers and widgets to virtual functions"""
        self.Bind( wx.EVT_CLOSE, self.GenPlotOptionsQuit)
        self.m_CHKBox_BoxPlotOption.Bind(wx.EVT_CHECKBOX, self.On_CHKBox_BoxPlotOption )
        self.m_CHKBox_LegendFrameOption.Bind(wx.EVT_CHECKBOX, self.On_CHKBox_LegendFrameOption )
        self.m_CHKBox_ShowLegendOption.Bind(wx.EVT_CHECKBOX, self.On_CHKBox_ShowLegendOption )
        self.m_CHKBox_YAxisTickLabelsOption.Bind(wx.EVT_CHECKBOX, self.On_CHKBox_YAxisTickLabelsOption)
        self.m_CHKBox_YAxisExponentialOption.Bind(wx.EVT_CHECKBOX, self.On_CHKBox_YAxisExponentialOption)
        self.m_CHKBox_YAxisTicksOption.Bind(wx.EVT_CHECKBOX, self.On_CHKBox_YAxisTicksOption)
        self.m_CHKBox_MultiPlot_shareyOption.Bind(wx.EVT_CHECKBOX, self.On_CHKBox_shareyOption)
        self.m_CHKBox_MultiPlot_sharexOption.Bind(wx.EVT_CHECKBOX, self.On_CHKBox_sharexOption)
        
        self.m_CHKBox_OverrideXAxisOption.Bind(wx.EVT_CHECKBOX, self.On_CHKBox_OverrideXAxisOption)
        self.m_CHKBox_OverrideYAxisOption.Bind(wx.EVT_CHECKBOX, self.On_CHKBox_OverrideYAxisOption)
        
        self.m_CHKBox_MajorXgridlinesOption.Bind(wx.EVT_CHECKBOX, self.On_CHKBox_MajorXgridlinesOption)
        self.m_CHKBox_MajorYgridlinesOption.Bind(wx.EVT_CHECKBOX, self.On_CHKBox_MajorYgridlinesOption)
        self.m_CHKBox_MinorXgridlinesOption.Bind(wx.EVT_CHECKBOX, self.On_CHKBox_MinorXgridlinesOption)
        self.m_CHKBox_MinorYgridlinesOption.Bind(wx.EVT_CHECKBOX, self.On_CHKBox_MinorYgridlinesOption)
     
        self.m_SpinCtrl_FigWidth.Bind( wx.EVT_SPINCTRLDOUBLE, self.OnSpinCtrl_FigWidth )
        self.m_SpinCtrl_FigHeight.Bind( wx.EVT_SPINCTRLDOUBLE, self.OnSpinCtrl_FigHeight )
        
        self.m_SpinCtrl_X_Axis_LowLim.Bind( wx.EVT_SPINCTRLDOUBLE, self.OnSpinCtrl_X_Axis_LowLim )
        self.m_SpinCtrl_X_Axis_HiLim.Bind( wx.EVT_SPINCTRLDOUBLE, self.OnSpinCtrl_X_Axis_HiLim )
        self.m_SpinCtrl_Num_X_Ticks.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_Num_X_Ticks )
        self.m_SpinCtrl_Num_X_Ticks.Bind( wx.EVT_TEXT_ENTER, self.OnSpinCtrl_Num_X_Ticks )
        self.m_SpinCtrl_Num_X_MinorTicks.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_Num_X_MinorTicks )
        self.m_SpinCtrl_Num_X_MinorTicks.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_Num_X_MinorTicks )
        
        self.m_SpinCtrl_Y_Axis_LowLim.Bind( wx.EVT_SPINCTRLDOUBLE, self.OnSpinCtrl_Y_Axis_LowLim )
        self.m_SpinCtrl_Y_Axis_HiLim.Bind( wx.EVT_SPINCTRLDOUBLE, self.OnSpinCtrl_Y_Axis_HiLim )
        self.m_SpinCtrl_Num_Y_Ticks.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_Num_Y_Ticks )
        self.m_SpinCtrl_Num_Y_Ticks.Bind( wx.EVT_TEXT_ENTER, self.OnSpinCtrl_Num_Y_Ticks )
        self.m_SpinCtrl_Num_Y_MinorTicks.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_Num_Y_MinorTicks )
        self.m_SpinCtrl_Num_Y_MinorTicks.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_Num_Y_MinorTicks )
        
        self.m_SpinCtrl_PlotTextSize.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_PlotTextSize )
        self.m_SpinCtrl_PlotTextSize.Bind(wx.EVT_TEXT_ENTER, self.OnSpinCtrl_PlotTextSize )
        self.m_SpinCtrl_LabelsFontSize.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_LabelsFontSize )
        self.m_SpinCtrl_LabelsFontSize.Bind(wx.EVT_TEXT_ENTER, self.OnSpinCtrl_LabelsFontSize )
        
        self.m_SpinCtrl_X_axis_Label_Pad.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_X_axis_Label_Pad )
        self.m_SpinCtrl_X_axis_Label_Pad.Bind(wx.EVT_TEXT_ENTER, self.OnSpinCtrl_X_axis_Label_Pad )
        self.m_SpinCtrl_Y_axis_Label_Pad.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_Y_axis_Label_Pad )
        self.m_SpinCtrl_Y_axis_Label_Pad.Bind(wx.EVT_TEXT_ENTER, self.OnSpinCtrl_Y_axis_Label_Pad )
        self.m_SpinCtrl_X_axis_Title_Pad.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_X_axis_Title_Pad )
        self.m_SpinCtrl_X_axis_Title_Pad.Bind(wx.EVT_TEXT_ENTER, self.OnSpinCtrl_X_axis_Title_Pad )
        self.m_SpinCtrl_Y_axis_Title_Pad.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_Y_axis_Title_Pad )
        self.m_SpinCtrl_Y_axis_Title_Pad.Bind(wx.EVT_TEXT_ENTER, self.OnSpinCtrl_Y_axis_Title_Pad )
        self.m_textCtrl_X_AxisTitle.Bind(wx.EVT_TEXT_ENTER, self.OnTextChange_X_AxisTitle)
        self.m_textCtrl_Y_AxisTitle.Bind(wx.EVT_TEXT_ENTER, self.OnTextChange_Y_AxisTitle)
        
        self.m_ComboBox_Legend_loc.Bind(wx.EVT_COMBOBOX, self.OnComboBoxSelect_Legend_loc)
        self.m_ComboBox_MajorGridColour.Bind(wx.EVT_COMBOBOX, self.OnComboBoxSelect_MajorGridColour)
        self.m_ComboBox_MinorGridColour.Bind(wx.EVT_COMBOBOX, self.OnComboBoxSelect_MinorGridColour)

        self.Show()

###############################################################################
        """virtual event handler functions - overridden in child class"""
    def On_CHKBox_MajorXgridlinesOption (self, event):
        event.Skip() 

    def On_CHKBox_MajorYgridlinesOption (self, event):
        event.Skip() 

    def On_CHKBox_MinorXgridlinesOption (self, event):
        event.Skip() 

    def On_CHKBox_MinorYgridlinesOption (self, event):
        event.Skip() 
        
    def OnComboBoxSelect_MajorGridColour (self, event):
        event.Skip()         

    def OnComboBoxSelect_MinorGridColour (self, event):
        event.Skip()  
        
    def On_CHKBox_OverrideYAxisOption (self, event):
        event.Skip()  
        
    def On_CHKBox_OverrideXAxisOption (self, event):
        event.Skip()   
 
    def OnSpinCtrl_Num_Y_MinorTicks (self, event):
        event.Skip()  
        
    def OnSpinCtrl_Num_Y_Ticks (self, event):
        event.Skip()   
        
    def OnSpinCtrl_Y_Axis_LowLim (self, event):
        event.Skip()   

    def OnSpinCtrl_Y_Axis_HiLim (self, event):
        event.Skip()   

    def OnSpinCtrl_Num_X_MinorTicks (self, event):
        event.Skip()  
        
    def OnSpinCtrl_Num_X_Ticks (self, event):
        event.Skip()   
        
    def OnSpinCtrl_X_Axis_LowLim (self, event):
        event.Skip()   

    def OnSpinCtrl_X_Axis_HiLim (self, event):
        event.Skip()   

    def OnSpinCtrl_FigWidth(self, event):
        event.Skip()   

    def OnSpinCtrl_FigHeight(self, event):
        event.Skip()   
        
    def OnTextChange_X_AxisTitle(self, event):
        event.Skip()   
        
    def OnTextChange_Y_AxisTitle(self, event):
        event.Skip()   
        
    def OnComboBoxSelect_Legend_loc(self, event):
        event.Skip()   
        
    def GenPlotOptionsQuit(self, event):
        event.Skip()     
        
    def On_CHKBox_BoxPlotOption(self, event):
        event.Skip()   
        
    def On_CHKBox_LegendFrameOption(self, event):
        event.Skip() 

    def On_CHKBox_ShowLegendOption(self, event):
        event.Skip() 
        
    def On_CHKBox_YAxisTickLabelsOption(self, event):
        event.Skip() 
        
    def On_CHKBox_YAxisExponentialOption(self, event):
        event.Skip() 
        
    def On_CHKBox_YAxisTicksOption(self, event):
        event.Skip() 
        
    def On_CHKBox_shareyOption(self, event):
        event.Skip() 
        
    def On_CHKBox_sharexOption(self, event):
        event.Skip() 
        
    def OnSpinCtrl_PlotTextSize(self, event):
        event.Skip() 
        
    def OnSpinCtrl_LabelsFontSize(self, event):
        event.Skip()
        
    def OnSpinCtrl_X_axis_Label_Pad(self, event):
        event.Skip()
        
    def OnSpinCtrl_Y_axis_Label_Pad(self, event):
        event.Skip()
        
    def OnSpinCtrl_X_axis_Title_Pad(self, event):
        event.Skip()
        
    def OnSpinCtrl_Y_axis_Title_Pad(self, event):
        event.Skip()