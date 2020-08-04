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

import glob, os
# glob is used for listing files in a directory, os for removing files

import numpy as np
# import the mathematical library numpy

import matplotlib.pyplot as plt
# import plotting library

import pickle
# Import pickle for saving prefs

from mpl_toolkits.axes_grid1.inset_locator import (InsetPosition,
                                                  mark_inset)
# Import special libraries for inset plotting

from MyCustomLibraries.SpectraDA_Func_Def import  (LineStyle, 
                                                   LineColour, 
                                                   swap, 
                                                   vec_norm, 
                                                   intensity_norm, 
                                                   ComputeLabelX, 
                                                   ComputeLabelY,
                                                   format_exponent,
                                                   Share_Axis_Set,
                                                   TakeValuesBetweenTwoLimits,
                                                   FindMax,
                                                   FindMin,
                                                   FuncInsetLineColour,
                                                   PickleResortDataDICT,
                                                   Compute_Scaled_Move)
# Import custom functions required

class DataClass_Spectra:
    """Class for multiple spectra"""
    
    def __init__(self):
        """initialise with required variables"""
        self.Data = []
        
        self.Raman_Shift = []
        self.Raman_Intensity = []
        self.Vec_Norm_Intensity = []
        self.Intensity_Norm_Intensity = []
        self.Zero_to_One_Intensity = []

        self.Series_FileName = []
        self.Series_Label = []
        self.Series_order =[]
        
        self.Series_Colour = []
        self.Series_LineSty = []
        
        self.Series_Label_X = []
        self.Series_Label_Y = []
        self.Series_Label_X_MOVE = []
        self.Series_Label_Y_MOVE = []
        
        self.Series_UpperBoundX = []
        self.Series_LowerBoundX = []
        self.Series_UpperBoundXOriginal = []
        
        self.IncludeSelectedSpectrum = []
        self.Series_InsetShow = []
        
        self.Directory = '';
        
        self.fig = plt.figure()
        
        self.NumOfSpectra = 0

        self.MoveXLabelCoeff = 0.005
        self.MoveYLabelCoeff = 0.01
        self.MoveLabelFaster_Coeff = 5.0  
        
        self.MoveBoundXCoeff = 10.0
        self.MoveBoundXFaster_Coeff = 10.0
        
#########################
        """Here are the general plot style options to add to the GUI"""
        self.OverrideXAxisOption = False
        self.OverrideYAxisOption = False
        
        self.X_Axis_LowLim = float
        self.X_Axis_HiLim = float
        
        self.Y_Axis_LowLim = float
        self.Y_Axis_HiLim = float

        self.X_Axis_LowLim_Override = float
        self.X_Axis_LowLim_Override = float
        
        self.Y_Axis_LowLim_Override = float
        self.Y_Axis_LowLim_Override = float
        
        self.Num_X_Ticks = 5
        self.Num_X_MinorTicks = 4
        self.Num_Y_Ticks = 5
        self.Num_Y_MinorTicks = 4
        self.Inset_XAxis_MinorNumInc =  4
        self.Inset_YAxis_NumInc = 4
        self.FigWidth = 2.5
        self.FigHeight = 1.8
        self.Legend_X_MOVE = 0.0
        self.Legend_Y_MOVE = 0.0
        
        self.BoxPlotOption = False
        self.LegendFrameOption = False
        self.ShowLegendOption = True
        self.YAxisTickLabelsOption = True
        self.YAxisExponentialOption = False
        self.YAxisTicksOption = False
        self.MajorXgridlinesOption = False
        self.MinorXgridlinesOption = False
        self.MajorYgridlinesOption = False
        self.MinorYgridlinesOption = False
        
        self.MajorGridColour = 'Grey'
        self.MinorGridColour = 'Light Grey'
        
        self.PlotTextSize = 10
        self.LabelsFontSize = 8
        self.Y_AxisTitle = 'Intensity (arb. units)'
        self.X_AxisTitle = 'Raman shift (cm$^{-1}$)'
        self.Legend_loc= 'upper left' 
        self.Y_axis_Label_Pad = 5.0
        self.X_axis_Label_Pad = 5.0
        self.Y_axis_Title_Pad = 5.0
        self.X_axis_Title_Pad = 5.0
        
        """MultiPlot Options"""
        self.MultiPlot_shareyOption = False
        self.MultiPlot_sharexOption = True

#########################
        """Here are the inset plot style options to add to the GUI"""        
        self.InsetPlotOption = False

        self.InsetLabelBackgroundWhite = True
        self.YInsetAxisTicksOption = False
        self.InsetLabelsTextSize = 10
        self.X_insetaxis_Label_Pad = 0.0      
        self.RShift_inset_Max = 4000
        self.RShift_inset_Min = 0
        self.Inset_XAxis_NumInc = 5
        self.Inset_LowerLeftX = 0.5
        self.Inset_LowerLeftY = 0.5
        self.Inset_Width = 0.5
        self.Inset_Height = 0.5
        self.InsetSizeIncrement = 0.01
        self.InsetLineColour = 'k'
        self.InsetLineJoin = [2,4]
        
################################################################
        """Redundant inset plot options"""
        self.YInsetAxisTickLabelsOption = True
        self.YInsetAxisExponentialOption = True
        self.Y_insetaxis_Label_Pad = 0.0

    def save_General_prefs(self):
        """Save general plot preferences"""
        print("Saving general preferences...")
        File = self.Directory+"\General_prefs.pickle"
        pickle.dump([self.OverrideXAxisOption,
                     self.OverrideYAxisOption,
                     self.X_Axis_LowLim,
                     self.X_Axis_HiLim,
                     self.Y_Axis_LowLim,
                     self.Y_Axis_HiLim,
                     self.X_Axis_LowLim_Override,
                     self.X_Axis_LowLim_Override,
                     self.Y_Axis_LowLim_Override,
                     self.Num_X_Ticks,
                     self.Num_X_MinorTicks,
                     self.Num_Y_Ticks,
                     self.Num_Y_MinorTicks,
                     self.Inset_XAxis_MinorNumInc,
                     self.Inset_YAxis_NumInc,
                     self.FigWidth,
                     self.FigHeight,
                     self.Legend_X_MOVE, 
                     self.Legend_Y_MOVE,
                     self.BoxPlotOption, 
                     self.LegendFrameOption, 
                     self.ShowLegendOption, 
                     self.YAxisTickLabelsOption,  
                     self.YAxisExponentialOption,
                     self.YAxisTicksOption,
                     self.MajorXgridlinesOption,
                     self.MinorXgridlinesOption,
                     self.MajorYgridlinesOption,
                     self.MinorYgridlinesOption,
                     self.MajorGridColour,
                     self.MinorGridColour,
                     self.PlotTextSize,
                     self.LabelsFontSize,
                     self.Y_AxisTitle,
                     self.X_AxisTitle,
                     self.Legend_loc,
                     self.Y_axis_Label_Pad,
                     self.X_axis_Label_Pad,
                     self.Y_axis_Title_Pad,
                     self.X_axis_Title_Pad,
                     self.MultiPlot_shareyOption,
                     self.MultiPlot_sharexOption,
                     self.InsetPlotOption,
                     self.InsetLabelBackgroundWhite,
                     self.YInsetAxisTicksOption,
                     self.InsetLabelsTextSize,
                     self.X_insetaxis_Label_Pad, 
                     self.RShift_inset_Max,
                     self.RShift_inset_Min,    
                     self.Inset_XAxis_NumInc,
                     self.Inset_LowerLeftX,
                     self.Inset_LowerLeftY, 
                     self.Inset_Width ,
                     self.Inset_Height ,
                     self.InsetSizeIncrement,
                     self.InsetLineColour,
                     self.InsetLineJoin ,
                     self.YInsetAxisTickLabelsOption ,
                     self.YInsetAxisExponentialOption,
                     self.Y_insetaxis_Label_Pad ], open(File, "wb"))

        print("General preferences saved.")

    def load_General_prefs(self):
        """Load general plot preferences"""
        print("Loading preferences...")
        File = self.Directory+"\General_prefs.pickle"
        (self.OverrideXAxisOption,
         self.OverrideYAxisOption,
         self.X_Axis_LowLim,
         self.X_Axis_HiLim,
         self.Y_Axis_LowLim,
         self.Y_Axis_HiLim,
         self.X_Axis_LowLim_Override,
         self.X_Axis_LowLim_Override,
         self.Y_Axis_LowLim_Override,
         self.Num_X_Ticks,
         self.Num_X_MinorTicks,
         self.Num_Y_Ticks,
         self.Num_Y_MinorTicks,
         self.Inset_XAxis_MinorNumInc,
         self.Inset_YAxis_NumInc,
         self.FigWidth,
         self.FigHeight,
         self.Legend_X_MOVE, 
         self.Legend_Y_MOVE,
         self.BoxPlotOption, 
         self.LegendFrameOption, 
         self.ShowLegendOption, 
         self.YAxisTickLabelsOption,  
         self.YAxisExponentialOption,
         self.YAxisTicksOption,
         self.MajorXgridlinesOption,
         self.MinorXgridlinesOption,
         self.MajorYgridlinesOption,
         self.MinorYgridlinesOption,
         self.MajorGridColour,
         self.MinorGridColour,
         self.PlotTextSize,
         self.LabelsFontSize,
         self.Y_AxisTitle,
         self.X_AxisTitle,
         self.Legend_loc,
         self.Y_axis_Label_Pad,
         self.X_axis_Label_Pad,
         self.Y_axis_Title_Pad,
         self.X_axis_Title_Pad,
         self.MultiPlot_shareyOption,
         self.MultiPlot_sharexOption,
         self.InsetPlotOption,
         self.InsetLabelBackgroundWhite,
         self.YInsetAxisTicksOption,
         self.InsetLabelsTextSize,
         self.X_insetaxis_Label_Pad, 
         self.RShift_inset_Max,
         self.RShift_inset_Min,    
         self.Inset_XAxis_NumInc,
         self.Inset_LowerLeftX,
         self.Inset_LowerLeftY, 
         self.Inset_Width ,
         self.Inset_Height ,
         self.InsetSizeIncrement,
         self.InsetLineColour,
         self.InsetLineJoin ,
         self.YInsetAxisTickLabelsOption ,
         self.YInsetAxisExponentialOption,
         self.Y_insetaxis_Label_Pad )= pickle.load(open(File, "rb"))
        
    def save_Spectra_prefs(self):
        """Save spectra specific plot preferences"""
        print("Saving Spectra specific preferences...")
        File = self.Directory+"\Spectra_prefs.pickle"
        pickle.dump([self.Series_Label,
                     self.Series_order ,
                     self.Series_Colour,
                     self.Series_LineSty,
                     self.Series_Label_X,
                     self.Series_Label_Y ,
                     self.Series_Label_X_MOVE ,
                     self.Series_Label_Y_MOVE ,
                     self.Series_UpperBoundX ,
                     self.Series_LowerBoundX ,
                     self.Series_UpperBoundXOriginal ,
                     self.IncludeSelectedSpectrum,
                     self.Series_InsetShow  ], open(File, "wb"))

        print("Spectra specific preferences saved.")
                
    def load_Spectra_prefs(self):
        """Load spectra specific plot preferneces"""
        print("Loading preferences...")
        File = self.Directory+"\Spectra_prefs.pickle"
        (self.Series_Label,
         self.Series_order ,
         self.Series_Colour,
         self.Series_LineSty,
         self.Series_Label_X,
         self.Series_Label_Y ,
         self.Series_Label_X_MOVE ,
         self.Series_Label_Y_MOVE ,
         self.Series_UpperBoundX ,
         self.Series_LowerBoundX ,
         self.Series_UpperBoundXOriginal ,
         self.IncludeSelectedSpectrum,
         self.Series_InsetShow)= pickle.load(open(File, "rb"))

    def Delete_General_Prefs(self):
        """Delete general plot preferences file"""
        File = self.Directory+"\General_prefs.pickle"
        os.remove(File)

    def Delete_Spectra_Prefs(self):
        """Delete spectra specific plot preferences"""
        File = self.Directory+"\Spectra_prefs.pickle"
        os.remove(File)
        
    def CheckandLoad_Spectra_Prefs(self):
        """Check and load spectra specific plot preferences"""
        try:
            print("Loading preferences...")
            self.load_Spectra_prefs()
        except (OSError, IOError):
            print("No preferences file found. Creating one...")
            self.save_Spectra_prefs()

    def CheckandLoad_General_Prefs(self):
        """Check and load general plot preferences"""
        try:
            print("Loading preferences...")
            self.load_General_prefs()
        except (OSError, IOError):
            print("No preferences file found. Creating one...")
            self.save_General_prefs()
    
    def Sort_Arrays_PostPickleLoad(self):
        """Sort the spectra according to loaded sort order"""
        for i in range(0, 7):
            if len(self.__dict__[PickleResortDataDICT(i)])!=0:
                Temp_Sorted_Data = [self.__dict__[PickleResortDataDICT(i)][j] for j in self.Series_order]
                self.__dict__[PickleResortDataDICT(i)] = Temp_Sorted_Data

    def ChangeInsetSize_Pos(self, Dimension, Value):
        """Change inset size and position"""
        self.__dict__['Inset_' + Dimension] =  Value*self.InsetSizeIncrement
        
    def ReturnInsetSize_Pos(self, Dimension):
        """Compute and return inset size and positions"""
        Value = self.__dict__['Inset_' + Dimension]/self.InsetSizeIncrement
        return Value

    def Import_Data(self, Text_Data_Directory):
        """Import the data and create class attributes"""
        self.Directory = Text_Data_Directory
        os.chdir(Text_Data_Directory)
        self.NumOfSpectra = np.size(glob.glob("*.txt"))
        self.Series_order = list(range(0,self.NumOfSpectra))
        i=1
        
        for file in glob.glob("*.txt"):
            Data=np.genfromtxt(file); # , delimiter = '\t'
            self.Data.append(Data)
            self.Raman_Shift.append(Data[:,][:,0])
            self.Raman_Intensity.append(Data[:,][:,1])
            self.Series_FileName.append(file)
            self.Series_Colour.append('k')
            self.Series_LineSty.append('-')
            self.Series_Label.append('Series ' + str(i))
            i+=1
            self.Series_Label_X.append(ComputeLabelX(self.Raman_Shift[-1]))
            self.Series_Label_Y.append(ComputeLabelY(self.Raman_Intensity[-1]))
            self.Series_Label_X_MOVE.append(0.0)
            self.Series_Label_Y_MOVE.append(0.0)
            self.Series_UpperBoundX.append(max(self.Raman_Shift[-1]))
            self.Series_LowerBoundX.append(0.0)
            self.IncludeSelectedSpectrum.append(True)
            self.Series_InsetShow.append(True)
            
        self.Series_UpperBoundXOriginal = self.Series_UpperBoundX
        self.RShift_inset_Max = ((FindMax(self.Raman_Shift) - 
                                 FindMin(self.Raman_Shift))*0.6+
                                    FindMin(self.Raman_Shift))
        self.RShift_inset_Min = ((FindMax(self.Raman_Shift) - 
                                 FindMin(self.Raman_Shift))*0.4+
                                    FindMin(self.Raman_Shift))
        
        self.CheckandLoad_General_Prefs()
        self.CheckandLoad_Spectra_Prefs()
        self.Sort_Arrays_PostPickleLoad()

    def Plot_Spectra(self, Y_Variable):
        """Plot standard spectra plot"""
        plt.rcParams.update({'font.size': self.PlotTextSize})     
        self.fig , ax = plt.subplots(figsize = (self.FigWidth,self.FigHeight), dpi = 300)

        for i in range(self.NumOfSpectra):
            if self.IncludeSelectedSpectrum[i]:
                plt.plot(self.Raman_Shift[i], self.__dict__[Y_Variable][i], 
                         color = self.Series_Colour[i], linestyle= self.Series_LineSty[i] ,linewidth=1)
        
        if self.ShowLegendOption:
            self.Add_TheLegend_ToPosition()

        plt.xlabel(self.X_AxisTitle, labelpad=self.X_axis_Title_Pad)
        plt.ylabel(self.Y_AxisTitle, labelpad=self.Y_axis_Title_Pad)
        self.Apply_TickLabelOptions(ax)
        
        if self.InsetPlotOption:
            self.Insert_Inset_Plot( ax, Y_Variable)

        plt.show()

    def Plot_OFFSET_Spectra(self, Y_Variable):
        """Plot spectra offset from one another"""
        plt.rcParams.update({'font.size': self.PlotTextSize})  
        self.fig , ax = plt.subplots(figsize = (self.FigWidth,self.FigHeight), dpi = 300)
        Offset =  0.0;
        
        for i in range(self.NumOfSpectra):
            if self.IncludeSelectedSpectrum[i]:
                plt.plot(self.Raman_Shift[i], self.__dict__[Y_Variable][i] + Offset , 
                         color = self.Series_Colour[i], linestyle= self.Series_LineSty[i], linewidth=1)
                Offset = self.AddSeriesLabel_ReturnNewOffset( i, Y_Variable, 
                                                             Offset, AddLabel=self.ShowLegendOption)
        
        plt.xlabel(self.X_AxisTitle, labelpad=self.X_axis_Title_Pad)
        plt.ylabel(self.Y_AxisTitle, labelpad=self.Y_axis_Title_Pad)
        self.Apply_TickLabelOptions(ax)
        
        if self.InsetPlotOption:
            self.Insert_OffsetInset_Plot( ax, Y_Variable)
        
        plt.show()

    def SUB_Plot_Spectra(self, Y_Variable):
        """Plot spectra in a multi sub plot"""
        plt.rcParams.update({'font.size': self.PlotTextSize})  
        NumOfSpectra = sum(self.IncludeSelectedSpectrum)
        self.fig, ax = plt.subplots(nrows=NumOfSpectra, ncols=1,
                                    figsize = (self.FigWidth,self.FigHeight), dpi = 300)
        BoolList = self.IncludeSelectedSpectrum
        Raman_Shift_toShow = [i for indx,i in enumerate(self.Raman_Shift) if BoolList[indx] == True]
        Intensity_Y_Var_toShow = [i for indx,i in enumerate(self.__dict__[Y_Variable]) if BoolList[indx] == True]
        line_Col_toShow = [i for indx,i in enumerate(self.Series_Colour) if BoolList[indx] == True]
        line_Sty_toShow = [i for indx,i in enumerate(self.Series_LineSty) if BoolList[indx] == True]
        sub_Plot_Num = self.ReturnSubPlotNum(0)
        ax1 = plt.subplot(sub_Plot_Num)
        plt.plot(Raman_Shift_toShow[0], Intensity_Y_Var_toShow[0], 
                 color = line_Col_toShow[0], linestyle= line_Sty_toShow[0], linewidth=1)
        n_th = [y for y in enumerate(BoolList) if y[1]==True][0][0]
        self.AddSeriesLabel_ReturnNewOffset( n_th , Y_Variable, 0, AddLabel=self.ShowLegendOption)
        plt.xlabel(self.X_AxisTitle, fontsize=int(self.PlotTextSize *1.5), 
                   labelpad=self.X_axis_Title_Pad)
        ax = self.fig.gca()
        self.Apply_TickLabelOptions(ax)

        for i in range(1, NumOfSpectra):
            sub_Plot_Num = self.ReturnSubPlotNum(i)
            ax_i = Share_Axis_Set(self.MultiPlot_sharexOption, 
                                  self.MultiPlot_shareyOption, 
                                  sub_Plot_Num , ax1)
            plt.plot(Raman_Shift_toShow[i], Intensity_Y_Var_toShow[i],
                     color = line_Col_toShow[i], linestyle= line_Sty_toShow[i], linewidth=1)
            n_th = [y for y in enumerate(BoolList) if y[1]==True][i][0]
            self.AddSeriesLabel_ReturnNewOffset( n_th, Y_Variable, 0, AddLabel=self.ShowLegendOption)
            
            if self.MultiPlot_sharexOption:
                plt.setp(ax_i.get_xticklabels(), visible=False)
            
            ax = self.fig.gca()
            self.Apply_TickLabelOptions(ax_i)

        self.fig.text(-0.001*self.Y_axis_Title_Pad, 0.5, self.Y_AxisTitle, 
                      fontsize=int(self.PlotTextSize*1.5),
                      va='center', rotation='vertical')
        
        plt.show()

    def Insert_Inset_Plot(self, ax, Y_Variable):
        """Add inset plot"""
        ax_inset = self.SetupInset(ax)

        for Series in range(self.NumOfSpectra):
            if self.Series_InsetShow[Series]:
                RShift_in_Limits, ArrayElements_in_Limits = TakeValuesBetweenTwoLimits(self.Raman_Shift[Series], 
                                                                               self.RShift_inset_Min,
                                                                               self.RShift_inset_Max)
                Y_Variable_in_Limits = self.__dict__[Y_Variable][Series][ArrayElements_in_Limits]
                ax_inset.plot(RShift_in_Limits , Y_Variable_in_Limits, 
                              color = self.Series_Colour[Series], linestyle= self.Series_LineSty[Series],
                              label=self.Series_Label[Series])

        self.Apply_INSET_TickLabelOptions( ax_inset)

    def SetupInset(self, ax):
        """Setup inset parameters"""
        ax_inset = plt.axes([0,0,1,1])
        inset_pos = InsetPosition(ax, [self.Inset_LowerLeftX,
                                       self.Inset_LowerLeftY,
                                       self.Inset_Width,
                                       self.Inset_Height])
        ax_inset.set_axes_locator(inset_pos)
        mark_inset(ax, ax_inset, loc1=self.InsetLineJoin[0], loc2=self.InsetLineJoin[1],
                   fc="none", ec=self.InsetLineColour)
        return ax_inset

    def InsetLineJoin_Switch(self):
        """Switch inset line connectors"""
        if self.InsetLineJoin == [1,3]:
            self.InsetLineJoin[0] = 2
            self.InsetLineJoin[1] = 4
            
        elif self.InsetLineJoin == [2,4]:
            self.InsetLineJoin[0] = 1
            self.InsetLineJoin[1] = 2

        elif self.InsetLineJoin == [1,2]:
            self.InsetLineJoin[0] = 3
            self.InsetLineJoin[1] = 4
            
        elif self.InsetLineJoin == [3,4]:
            self.InsetLineJoin[0] = 1
            self.InsetLineJoin[1] = 3

        else:
            self.InsetLineJoin[0] = 2
            self.InsetLineJoin[1] = 4
            
    def Apply_INSET_TickLabelOptions(self, ax_inset):
        """Apply inset tick label options"""
        minor_X_Ticks = (self.Inset_XAxis_NumInc-1)*(self.Inset_XAxis_MinorNumInc+1) + 1
        ax_inset.set_xticks(np.linspace(int(self.RShift_inset_Min), int(self.RShift_inset_Max), self.Inset_XAxis_NumInc))
        ax_inset.set_xticks(np.linspace(int(self.RShift_inset_Min), int(self.RShift_inset_Max), minor_X_Ticks), minor=True)
        ax_inset.set_xlim(int(self.RShift_inset_Min), int(self.RShift_inset_Max))
        ylim = ax_inset.get_ylim()
        ylim_Range = ylim[1] - ylim[0]
        ax_inset.set_ylim((ylim[0]-0.03*ylim_Range), (ylim[1]+0.03*ylim_Range))
        ylim = ax_inset.get_ylim()
        ax_inset.set_yticks(np.linspace(ylim[0], ylim[1], self.Inset_YAxis_NumInc))
        
        if self.MajorXgridlinesOption:
            grid_Colour = FuncInsetLineColour( self.MajorGridColour)
            plt.grid(b=self.MajorXgridlinesOption, 
                        which='major', axis='x', color=grid_Colour, linestyle='--', linewidth=0.8)
            
        if self.MajorYgridlinesOption:
            grid_Colour = FuncInsetLineColour( self.MajorGridColour)
            plt.grid(b=self.MajorYgridlinesOption, 
                        which='major', axis='y', color=grid_Colour, linestyle='--', linewidth=0.8)
        
        if self.MinorXgridlinesOption:
            grid_Colour = FuncInsetLineColour( self.MinorGridColour)
            plt.grid(b=self.MinorXgridlinesOption, 
                        which='minor', axis='x', color=grid_Colour, linestyle='--', linewidth= 0.6 )
        
        if self.MinorYgridlinesOption:
            grid_Colour = FuncInsetLineColour( self.MinorGridColour)
            plt.grid(b=self.MinorYgridlinesOption, 
                        which='minor', axis='y', color=grid_Colour, linestyle='--', linewidth= 0.6 )
        
        if self.InsetLabelBackgroundWhite:
            ax_inset.set_xticklabels(ax_inset.get_xticks(), backgroundcolor='w')
        
        ax_inset.tick_params(axis='x', which='major',
                             labelsize = self.InsetLabelsTextSize,
                             pad=self.X_insetaxis_Label_Pad)
            
        if self.YInsetAxisTickLabelsOption:
            ax_inset.axes.yaxis.set_ticklabels([])
        
        if self.YInsetAxisExponentialOption and self.YInsetAxisTickLabelsOption == False:
            ax_inset = format_exponent(ax_inset, axis='y')
            ax_inset.tick_params(axis='y', which='major', pad=self.Y_insetaxis_Label_Pad)
            
        if self.YInsetAxisTicksOption:
            plt.yticks([])

    def Insert_OffsetInset_Plot(self, ax, Y_Variable):
        """Insert inset plot for the offset spectra plot"""
        ax_inset = self.SetupInset(ax)
        Offset =  0.0;

        for Series in range(self.NumOfSpectra):
            if self.Series_InsetShow[Series]:
                RShift_in_Limits, ArrayElements_in_Limits = TakeValuesBetweenTwoLimits(self.Raman_Shift[Series], 
                                                                                   self.RShift_inset_Min,
                                                                                   self.RShift_inset_Max)
                Y_Variable_in_Limits = self.__dict__[Y_Variable][Series][ArrayElements_in_Limits]
                ax_inset.plot(RShift_in_Limits , Y_Variable_in_Limits + Offset, 
                              color = self.Series_Colour[Series], linestyle= self.Series_LineSty[Series])
                Offset = self.AddSeriesLabel_ReturnNewOffset( Series, Y_Variable, Offset,  AddLabel=False)

        self.Apply_INSET_TickLabelOptions( ax_inset)


    def ComputeMoveLabel_XandY(self, i , Y_Variable):
        """Compute new label coordinates"""        
        MoveLabel_Y = Compute_Scaled_Move(self.Series_Label_Y_MOVE[i] , self.__dict__[Y_Variable])
        MoveLabel_X = Compute_Scaled_Move(self.Series_Label_X_MOVE[i] , self.Raman_Shift)
        return MoveLabel_X, MoveLabel_Y

    def ReturnSubPlotNum(self,i):
        """compute multi plot sub plot index"""
        NumOfSpectra = sum(self.IncludeSelectedSpectrum)
        SubPlotNum =  int(str(NumOfSpectra) +str(1)+ str(NumOfSpectra - i))
        return SubPlotNum

    def AddSeriesLabel_ReturnNewOffset(self, i, Y_Variable, Offset, AddLabel = True):
        """Add series label and return new offset"""        
        MoveLabel_X, MoveLabel_Y = self.ComputeMoveLabel_XandY( i , Y_Variable)
        
        if AddLabel:
            plt.text(self.Series_Label_X[i]+MoveLabel_X, 
                     self.Series_Label_Y[i]+Offset+MoveLabel_Y, 
                     self.Series_Label[i], 
                     fontsize=self.LabelsFontSize)
            
        Offset = max(self.__dict__[Y_Variable][i]) + Offset
        return Offset

    def Apply_TickLabelOptions(self, ax):
        """Apply tick and label options"""
        ax.tick_params(axis='x', which='major', pad=self.X_axis_Label_Pad)
        xlim  = ax.get_xticks()
        self.X_Axis_LowLim_Override = xlim[0]
        self.X_Axis_HiLim_Override = xlim[-1]
        
        if self.MajorXgridlinesOption:
            grid_Colour = FuncInsetLineColour( self.MajorGridColour)
            plt.grid(b=self.MajorXgridlinesOption, 
                        which='major', axis='x', color=grid_Colour, linestyle='--', linewidth=0.8)
            
        if self.MajorYgridlinesOption:
            grid_Colour = FuncInsetLineColour( self.MajorGridColour)
            plt.grid(b=self.MajorYgridlinesOption, 
                        which='major', axis='y', color=grid_Colour, linestyle='--', linewidth=0.8)
        
        if self.MinorXgridlinesOption:
            grid_Colour = FuncInsetLineColour( self.MinorGridColour)
            plt.grid(b=self.MinorXgridlinesOption, 
                        which='minor', axis='x', color=grid_Colour, linestyle='--', linewidth= 0.6 )
        
        if self.MinorYgridlinesOption:
            grid_Colour = FuncInsetLineColour( self.MinorGridColour)
            plt.grid(b=self.MinorYgridlinesOption, 
                        which='minor', axis='y', color=grid_Colour, linestyle='--', linewidth= 0.6 )
        
        if self.OverrideXAxisOption == False: 
            self.X_Axis_LowLim = self.X_Axis_LowLim_Override
            self.X_Axis_HiLim = self.X_Axis_HiLim_Override 
            self.Num_X_Ticks = len(xlim )

        else:
            ax.set_xticks(np.linspace(self.X_Axis_LowLim,self.X_Axis_HiLim,self.Num_X_Ticks))
            TotalMinorTicks = (self.Num_X_Ticks-1)*(self.Num_X_MinorTicks+1)+1
            ax.set_xticks(np.linspace(self.X_Axis_LowLim,self.X_Axis_HiLim,TotalMinorTicks ), minor=True)
            ax.set_xlim(self.X_Axis_LowLim, self.X_Axis_HiLim)
        
        ylim  = ax.get_yticks()
        self.Y_Axis_LowLim_Override = ylim[0]
        self.Y_Axis_HiLim_Override = ylim[-1]
        
        if self.OverrideYAxisOption == False: 
            self.Y_Axis_LowLim = self.Y_Axis_LowLim_Override
            self.Y_Axis_HiLim = self.Y_Axis_HiLim_Override 
            self.Num_Y_Ticks = len(ylim )

        else:
            ax.set_yticks(np.linspace(self.Y_Axis_LowLim,self.Y_Axis_HiLim,self.Num_Y_Ticks))
            TotalMinorTicks = (self.Num_Y_Ticks-1)*(self.Num_Y_MinorTicks+1)+1
            ax.set_yticks(np.linspace(self.Y_Axis_LowLim,self.Y_Axis_HiLim,TotalMinorTicks ), minor=True)
            ax.set_ylim(self.Y_Axis_LowLim, self.Y_Axis_HiLim)
            
        if self.BoxPlotOption:
            ax.spines["top"].set_visible(False)
            ax.spines["right"].set_visible(False)
            ax.spines["left"].set_visible(True)
            
        if self.YAxisTickLabelsOption:
            ax.axes.yaxis.set_ticklabels([])
        
        if self.YAxisExponentialOption and self.YAxisTickLabelsOption == False:
            ax = format_exponent(ax, axis='y')
            ax.tick_params(axis='y', which='major', pad=self.Y_axis_Label_Pad)
            
        if self.YAxisTicksOption:
            plt.yticks([])

    def Add_TheLegend_ToPosition(self):
        """Add legend"""
        plt.rcParams.update({"legend.frameon": self.LegendFrameOption})
        if  self.Legend_loc == 'None':
            plt.legend(self.Series_Label, 
                       loc=(self.Legend_X_MOVE, self.Legend_Y_MOVE+0.5),
                       fontsize=self.LabelsFontSize)            
        
        else :
            plt.legend(self.Series_Label,loc = self.Legend_loc, 
                       fontsize=self.LabelsFontSize)

    def MoveBound(self, Series,  Move, Bound ):
        """Move single spectrum crop bound"""                    
        self.__dict__['Series_' + Bound + 'BoundX'][Series] =  Move*self.MoveBoundXCoeff

    def MoveALLBound(self,   Direction, Bound ):
        """Move all spectrum plot bounds"""
        for Series in range(self.NumOfSpectra):
            self.__dict__['Series_' + Bound + 'BoundX'][Series] +=  Direction*self.MoveBoundXCoeff*self.MoveBoundXFaster_Coeff

    def CropXBounds(self, Y_Variable):
        """Function for cropping the spectra"""        
        for Series in range(self.NumOfSpectra): 
            Temperary_R_Shift = self.Data[Series][:,][:,0] 
            Temperary_Intensity = self.Data[Series][:,][:,1]
            New_X = Temperary_R_Shift[Temperary_R_Shift<  self.Series_UpperBoundX[Series]]
            New_Y = Temperary_Intensity[Temperary_R_Shift <  self.Series_UpperBoundX[Series]]
            NewNew_X = New_X[New_X > self.Series_LowerBoundX[Series]]
            NewNew_Y = New_Y[New_X > self.Series_LowerBoundX[Series]]
            self.Raman_Shift[Series] = NewNew_X
            self.Raman_Intensity[Series] = NewNew_Y 

    def MoveAllLabels(self, XY = 'Y', Direction = 1.0, Plot_Option = 1):
        """Function for moving all labels"""        
        if Plot_Option == 0:
            self.__dict__['Legend_' + XY + '_MOVE'] +=  Direction*self.MoveYLabelCoeff*self.MoveLabelFaster_Coeff
         
        elif Plot_Option == 1 or 2:
            for Series in range(self.NumOfSpectra):
                self.__dict__['Series_Label_' + XY + '_MOVE'][Series] += Direction*self.MoveYLabelCoeff*self.MoveLabelFaster_Coeff

    def ReturnBoundMoveValue(self, Bound = 'Upper', Series = 0):
        """Compute the amount by which a crop bound will move"""        
        int_Bound = int(round(self.__dict__['Series_' + Bound + 'BoundX'][Series]/
                     (self.MoveBoundXCoeff)))
        return int_Bound

    def ReturnLabelMoveValue(self, XY = 'Y', Series = 0):
        """Compute the amount bu which a label will move"""
        int_XY = int(round(self.__dict__['Series_Label_' + XY + '_MOVE'][Series]/
                     (self.__dict__['Move' + XY + 'LabelCoeff'])))
        return int_XY

    def ReturnLegendMoveValue(self, XY = 'Y'):
        """Compute the amount by which the legend will move"""        
        int_XY = int(round(self.__dict__['Legend_' + XY + '_MOVE']/
                     (self.__dict__['Move' + XY + 'LabelCoeff'])))
        return int_XY

    def MoveOneLabel(self, XY = 'Y', Series = 0, Move = 0, Plot_Option = 1):
        """Move a single spectra label"""        
        if Plot_Option == 0:
            self.Legend_loc = 'None'
            self.__dict__['Legend_' + XY + '_MOVE'] =  self.__dict__['Move' +XY + 'LabelCoeff']*Move
         
        elif Plot_Option == 1 or 2:
            self.__dict__['Series_Label_' + XY + '_MOVE'][Series] = self.__dict__['Move' + XY + 'LabelCoeff']*Move

    def SetNewColour(self, Series, Colour):
        """Set a new line colour"""
        self.Series_Colour[Series] = LineColour(Colour)

    def SetNewInsetColour(self, Colour):
        """Set the inset line colour"""
        self.InsetLineColour = FuncInsetLineColour(Colour)
        
    def SetNewStyle(self, Series, Style):
        """Set new line style to a spectrum"""
        self.Series_LineSty[Series] = LineStyle(Style)

    def DoSelectedNormalisation(self, Y_Variable):
        """Choose which nomralisation to do"""
        if Y_Variable == 'Raman_Intensity':
            self.No_Normalisation()
                
        elif Y_Variable == 'Vec_Norm_Intensity':
            self.Vector_Norm()

        elif Y_Variable == 'Intensity_Norm_Intensity':
            self.Intensity_Norm()

        elif Y_Variable ==  'Zero_to_One_Intensity':
            self.Zero_to_One_Norm()
            
        else:
            print('Normalisation Option Undefined')

    def No_Normalisation(self):
        """No normalisation - do nothing"""
        pass

    def Vector_Norm(self):
        """Vector normalisation"""
        self.Vec_Norm_Intensity = []
        for i in range(self.NumOfSpectra):
            norm = vec_norm(self.Raman_Intensity[i])
            self.Vec_Norm_Intensity.append(self.Raman_Intensity[i]/norm)
            self.Series_Label_Y[i] = ComputeLabelY(self.Vec_Norm_Intensity[i])

    def Intensity_Norm(self):
        """Intensity normalisation"""
        self.Intensity_Norm_Intensity=[]
        for i in range(self.NumOfSpectra):
            norm = intensity_norm(self.Raman_Intensity[i])
            self.Intensity_Norm_Intensity.append(self.Raman_Intensity[i]/norm)
            self.Series_Label_Y[i] = ComputeLabelY(self.Intensity_Norm_Intensity[i])

    def Zero_to_One_Norm(self):
        """Normalise zero to one"""
        self.Zero_to_One_Intensity = []
        for i in range(self.NumOfSpectra):
            S_max = np.max(self.Raman_Intensity[i])
            S_min = np.min(self.Raman_Intensity[i])
            self.Zero_to_One_Intensity.append((self.Raman_Intensity[i]-S_min)/(S_max-S_min))
            self.Series_Label_Y[i] = 0.5

    def Move_Spectra_Up(self, n):
        """Resort a spectra up in the list"""
        members = [attr for attr in dir(self) if not callable(getattr(self, attr)) 
                   and not attr.startswith("__")]

        for i in range(len(members)):
            if (n>0 and type(self.__dict__[members[i]]) is list 
                and len(self.__dict__[members[i]]) != 0  and members[i] != 'InsetLineJoin'):
                self.__dict__[members[i]] = swap(self.__dict__[members[i]],n,n-1)

    def Move_Spectra_Down(self, n):
        """Resort a spectra down in the list"""
        members = [attr for attr in dir(self) if not callable(getattr(self, attr)) 
                   and not attr.startswith("__")]

        for i in range(len(members)):
            if (n != self.NumOfSpectra  and type(self.__dict__[members[i]]) is list 
                and len(self.__dict__[members[i]]) != 0 and members[i] != 'InsetLineJoin'):
                self.__dict__[members[i]] = swap(self.__dict__[members[i]],n,n+1)
         