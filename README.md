# Spectra-Plot
This program will plot spectra organised into a folder in two column text files.

It is specficially designed for specra data exported from Renishaw WiRE into text format.

I have a seperate script for converting the specrum data exported from lumerical. 
See "Lumerical-Spectra-Data-Sort" 

The program includes some normalisation options, inset plot options, truncate spectra,
multi plot and offset plot options, etc...
---------------------
Known Troubleshoot:

If error occurs (ValueError: not enough values to unpack). 
Delete the prefs.pickle file. it's is with the main.py file
Or: press "Restore Default Prefs"
---------------------
To get this working on a fresh python install:

Install packages needed do:

--> pip install -U matplotlib

--> pip install -U wxPython
---------------------

1) Ensure you have the libraries listed above installed in your python distribtion 
	by running the above commands in the python console  
2) Export your spectra into seperate text files from WiRE and group them into folders
3) From your python editor or IDE, run the "main.py" file.
4) click the "select directory" button and navigate to a folder containing the 
	spectra text files
5) Click "Import Data", observe the plot in the plot window. In Spyder (Anaconda), this is 
	integrated into the IDE. 
6) Select plot options as desired
7) Save prefs buttons create two prefs.pickle files which you can copy to the other 
	folders for consistent plot settings
8) Click Export to save the plot in a chosen file format

