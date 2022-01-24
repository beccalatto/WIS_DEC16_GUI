# Dayplot viewer

Use this tool to visualise the seismicity from Whillans Ice Stream, West Antarctica for a day in the 2010 summer deployment (December 16th, 2010).

<img src="https://github.com/beccalatto/WIS_DEC16_GUI/blob/main/images/BB_RESET.png" width="300" height="300">

Visualise December 16th seismicity, with options of:
- Single station or multiple stations as a composite
- Component (Z, N, E)
- Filter (None, Lowpass 1 Hz, Highpass 1 Hz)
- Pre-processing (Detrended, detrended + frequency normalised)
- Vertical axis limits (Default = central station median at local noon; options for 50%, 100%, 250%, 500%)

Download instructions:
- Download this repository and unzip
- Open a Python compiler (GUI constructed in Spyder)
- Set local directory to repository
- Run gui.py

Python dependencies:
- Python 3 (Untested for Python 2)
- Required packages:
  - pillow
  - PySimpleGUI
  - opencv-python

Troubleshoot:
If GUI will not close, try window.close() in console. 
If GUI will not close but remains active, test CTRL+C in console. Else, reset console and re-run.
Other questions can be directed to RL2797 [@] columbia [.edu]

References:
Latto, R., Turner, R. J., Reading, A. M., Winberry, J. P., “Event detection for cryoseismology.” The Cryosphere, in prep.
