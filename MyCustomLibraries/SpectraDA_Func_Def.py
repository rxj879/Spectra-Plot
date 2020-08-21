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

from tkinter import filedialog
from tkinter import Tk
# Import ask save / open file and directory dialogue box library

import os
# Import os library for removing files

from pathlib import Path
# import the library for handling windows paths

import math
import numpy as np
# Import the mathematical libraries

import matplotlib.pyplot as plt
# Import the plotting libraries

def path_leaf(path):
    """ Function for splitting the file path"""
    head= Path(path).stem
    return head
    
def PickleResortDataDICT(Dict_Index):
    """Dictionary for switching the normalisation used on loading prefs"""
    switcher = {
    0 : 'Data',
    1 : 'Raman_Shift',
    2 : 'Raman_Intensity',
    3 : 'Vec_Norm_Intensity',
    4 : 'std_var_Norm_Intensity',
    5 : 'Zero_to_One_Intensity',
    6 : 'Series_FileName'
    }
    return switcher.get(Dict_Index, 'Data')

def InsetLineColourArray():
    """Inset line colour array"""
    Colour = [
        'Black',
        'Dark Grey',
        'Grey',
        'Light Grey',
        'White'
        ]
    return Colour
    
def FuncInsetLineColour(argument):
    """Dictionary for switching colour arguements"""
    switcher = {
    'Black' : 'k',
    'Dark Grey' : 'dimgrey',
    'Grey' : 'darkgrey',
    'Light Grey' : 'lightgrey',
    'White' : 'white'
    }
    return switcher.get(argument, 'k')

def InsetLineColourRev(argument):
    """Reverse dictionary for switching colour argurments"""
    switcher = {
    'k' : 'Black',
    'dimgrey' : 'Dark Grey',
    'darkgrey' : 'Grey',
    'lightgrey' : 'Light Grey',
    'white' : 'White'
    }
    return switcher.get(argument, 'k')

def Legend_PositionOptionsArray():
    """Generic legend position options array"""
    Array = ['best',
             'upper right'	,
             'upper left',
             'lower left',
             'lower right'	,
             'right'	,
             'center left'	,
             'center right'	,
             'lower center'	,
             'upper center'	,
             'center',
             'None']
    return Array

def Radio2NormOption_Y_Variable(argument):
    """Dictionary for switching the normalisation options in the radio box"""
    switcher = {
    0: 'Raman_Intensity',
    1: 'Vec_Norm_Intensity',
    2: 'std_var_Norm_Intensity',
    3: 'Zero_to_One_Intensity'
    }
    return switcher.get(argument, 'k-')

def Share_Axis_Set(X_Option, Y_Option, sub_Plot_Num , ax1):
    """Take an axis and share attributes according to the options"""
    if X_Option and Y_Option:
        ax_i = plt.subplot(sub_Plot_Num, sharex=ax1, sharey =ax1)
            
    elif Y_Option:
        ax_i = plt.subplot(sub_Plot_Num, sharey =ax1)
        
    elif X_Option:
        ax_i = plt.subplot(sub_Plot_Num, sharex=ax1)
        
    else: 
        ax_i = plt.subplot(sub_Plot_Num)
        
    return ax_i

def format_exponent(ax, axis='y'):
    """Set axis label format to exponent"""
    ax.ticklabel_format(axis=axis, style='sci', scilimits=(0, 0))

    if axis == 'y':
        ax_axis = ax.yaxis
        x_pos = 0.0
        y_pos = 1.0
        horizontalalignment='left'
        verticalalignment='bottom'
        
    else:
        ax_axis = ax.xaxis
        x_pos = 1.0
        y_pos = -0.05
        horizontalalignment='right'
        verticalalignment='top'

    plt.tight_layout()
    offset = ax_axis.get_offset_text().get_text()

    if len(offset) > 0:
        minus_sign = u'\u2212'
        expo = np.float(offset.replace(minus_sign, '-').split('e')[-1])
        offset_text = r'x$\mathregular{10^{%d}}$' %expo
        ax_axis.offsetText.set_visible(False)
        ax.text(x_pos, y_pos, offset_text, transform=ax.transAxes,
               horizontalalignment=horizontalalignment,
               verticalalignment=verticalalignment)
        
    return ax

def FindMax(Axis_Arrays):
    """Find the maximum value from arrays which dont share the same dimensions"""
    Max = np.max(Axis_Arrays[0])
    if len(Axis_Arrays) > 1:
        for i in range(1,len(Axis_Arrays)):
            Max_new = np.max(Axis_Arrays[i])
        
            if Max > Max_new:
                Max = Max_new
        
    return Max

def FindMin(Axis_Arrays):
    """Find the minimum value from arrays which dont share the same dimensions"""
    Min = np.max(Axis_Arrays[0])
    if len(Axis_Arrays) > 1:
        for i in range(1,len(Axis_Arrays)):
            Min_new = np.min(Axis_Arrays[i])
        
            if Min > Min_new:
                Min = Min_new
                
    return Min

def Compute_Scaled_Move(Move_Coeff , Axis_Arrays):
    """Compute a scaled move of the plot labels"""
    Scaled_Move = Move_Coeff*abs(FindMax(Axis_Arrays)-FindMin(Axis_Arrays))
    return Scaled_Move

def ComputeLabelX(Array):
    """Compute label x coordinate"""
    X = min(Array)+ (max(Array)-min(Array))/2
    return X

def ComputeLabelY(Array):
    """Compute label y coordinate"""
    Y = min(Array)+ (max(Array)-min(Array))/2
    return Y
    
def LineStyle(argument):
    """Dictionary for switching the line style argument"""
    switcher = {
    'Line': '-',
    'Dash': '--',
    'DashDot': '-.',
    'Dotted': ':'
    }
    return switcher.get(argument, 'k-')

def LineStyleRev(argument):
    """Dictionary for reverse switching the line style arguement"""
    switcher = {
    '-' : 'Line',
    '--':'Dash',
    '-.' : 'DashDot',
    ':' : 'Dotted'
    }
    return switcher.get(argument, 'Line')

def LineStyleArray():
    """Line style array"""
    Style = [
        'Line',
        'Dash',
        'DashDot',
        'Dotted'
        ]
    return Style

def LineColour(argument):
    """Dictionary for switching line colours where appropriate"""
    switcher = {
    'Black': 'k',
    'Red': 'r',
    'Green': 'g',
    'Blue': 'b'
    }
    return switcher.get(argument, argument)

def LineColourRev(argument):
    """Dictionary for reverse switching line colours where appropriate"""
    switcher = {
    'k' : 'Black',
    'r' : 'Red',
    'g' : 'Green',
    'b' : 'Blue',
    'crimson' :'crimson' 
    }
    return switcher.get(argument, argument)

def LineColourArray():
    """Line colour options array"""
    Colour = [
        'Black',
        'dimgrey',
        'darkgrey',
        'silver',
        'lightgrey',

        'maroon',
        'darkred',
        'firebrick',
        'red',
        'orangered',
        'darkorange',
        'orange',
        
        'saddlebrown',
        'darkgoldenrod',
        'goldenrod',
        'gold',

        'darkolivegreen',
        'olivedrab',
        'olive',
        'y',
        'darkkhaki',
        'khaki',
        
        'darkgreen',
        'Green',
        'limegreen',
        'lime',
        'mediumspringgreen',
        'palegreen',
        'greenyellow',
        
        'midnightblue',
        'navy',
        'darkblue',
        'mediumblue',
        'blue',
        'slateblue',
        
        'indigo',
        'purple',
        'darkmagenta',
        'darkorchid',
        'mediumorchid',
        'orchid',
        'plum',
        
        'crimson',
        'deeppink',
        'magenta',
        'hotpink',
        'pink'   ]
    return Colour

def swap(list, n, m):
    """Function for swapping two list elements"""
    list[n] , list[m] = list[m], list[n]
    return list

def Get_Dir (Idir):
    "This uses tkinter to ask for the directory where the data is in text files"
    root = Tk();
    root.directory =  filedialog.askdirectory(initialdir = Idir, title = "Select directory/folder with the text data. Then hit import!");
    root.withdraw();
    return root.directory;

def ExportResolutionList():
    "Provides the list of resolutions for export"
    ResolutionList = [
                  '150',
                  '200',
                  '300',
                  '400',
                  '500',
                  '600'
                  ]
    return ResolutionList

def ExportFormatList():
    "Provides the list of file formats for export"
    FormatList = [
                  'png',
                  'eps',
                  'svg',
                  'pdf'
                  ]
    return FormatList

def Save_File (Idir=None):
    "This uses tkinter to ask for the data file"
    root = Tk();
    files = [('All Files', '*.*'), 
             ('PNG Files', '*.png'),
             ('eps Files', '*.eps'), 
             ('svg Files', '*.svg'), 
             ('pdf Files', '*.pdf')]
    root.file =  filedialog.asksaveasfile(filetypes = files, initialdir = Idir, title = "Save as");
    root.withdraw();
    print(root.file.name)
    return root.file.name;

def vec_norm (Spectrum):
    """Compute normalisation coefficient for vector normalisation"""
    norm_squared =0
    for i in range(len(Spectrum)):
        norm_squared = norm_squared + math.pow(Spectrum[i],2);
    norm = math.sqrt(norm_squared)
    if norm == 0:
        norm = 1;
    return norm

def std_var_mean (Spectrum):
    """Compute mean for standard normal variate"""
    mean = sum(Spectrum)/len(Spectrum)
    
    return mean

def std_var_norm (Spectrum , mean):
    """Compute normalisation coefficient for intensity normalisation"""
    norm=0
    for i in range(len(Spectrum)):
        norm = norm + pow((Spectrum[i]-mean),2); 
    norm = pow(norm, 0.5)/(len(Spectrum)-1)
    if norm == 0:
        norm = 1;
    return norm

def TakeValuesBetweenTwoLimits(Array, LowerLimit, UperLimit):
    """Create a truth array for values in a list which lie between two values"""
    Truthindex = (Array>LowerLimit) & (Array<UperLimit)
    return Array[Truthindex], Truthindex

def Create_Directory(dirName):
    """Check and create a directory"""
    try:
        # Create target Directory
        os.mkdir(dirName)
        
    except FileExistsError:
        pass     
    
    if not os.path.exists(dirName):
        os.mkdir(dirName)

    else:    
        pass

def GenerateTwoColumnData(Column1, Column2):
    
    Data = []
    for i in range(len(Column1)):
        Data.append([Column1[i], Column2[i]])
    return Data