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

import MyCustomLibraries.Export_GUI as export_gui
# Import the export gui frame design

from MyCustomLibraries.SpectraDA_Func_Def import (Save_File, 
                                                  path_leaf)
# Import the custom functions required

class ExportFrame(wx.Frame):
    """Member functions for the export frame gui"""
    
    def __init__(self, parent=None):
        """Initialise the wx frame design"""
        export_gui.ExportFrame.__init__(self, parent)
                
    def OnButtonClick_ExportFile( self, event ):
        """Function for saving the figure to user defined location and name
        Preferences are saved on export"""
        n = self.m_ComboBox_Format.GetCurrentSelection()
        Format = self.m_ComboBox_Format.GetString(n)
        n = self.m_ComboBox_Resolution.GetCurrentSelection()
        Resolution = int(self.m_ComboBox_Resolution.GetString(n))
        Initital_directory = self.m_textCtrl_DIR.GetValue()# I want to remove this
        SaveFileName_Head_Tail = Save_File (Initital_directory)
        SaveFileName_NameOnly = path_leaf(SaveFileName_Head_Tail)
        SaveFileName = Initital_directory + '/' + SaveFileName_NameOnly + '.' + Format
        print('SaveFileName :', SaveFileName)
        self.FullSpectrumGroup.fig.savefig( SaveFileName , 
                                               dpi=Resolution, 
                                               format = Format,
                                               bbox_inches='tight')
            
        self.FullSpectrumGroup.save_General_prefs()
        self.FullSpectrumGroup.save_Spectra_prefs()
        print('Export Complete')
        
        
    def ExportGuiQuit( self, event ):
        """Virtual event handler for closing the frame - overridden in child class"""
        event.Skip()      
        
    def OnComboBox_ExportFormat( self, event ):
        """Virtual event handler for selecting the export file format - no action required"""
        event.Skip()      

    def OnComboBox_ExportResolution( self, event ):
        """Virtual event handler for selecting the export file resolution - no action required"""
        event.Skip()
