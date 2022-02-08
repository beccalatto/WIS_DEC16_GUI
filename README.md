# Dayplot viewer

Use this tool to visualise the seismicity from Whillans Ice Stream, West Antarctica for a day in the 2010 summer deployment (December 16th, 2010). We chose this day as a representative example of typical seismicity following a manual reconnaisance of several weeks of data, as well as utilizing available knowledge of global catalogue events (teleseisms) and a Pratt, 2014 stick-slip.

<img src="https://github.com/beccalatto/WIS_DEC16_GUI/blob/main/images/BB_RESET.png" width="300" height="300">

Visualise December 16th seismicity, with options of:
- Single station or multiple stations as a composite
- Component (Z, N, E)
- Filter (None, Lowpass 1 Hz, Highpass 1 Hz)
- Pre-processing (Detrended, detrended + frequency normalised)
- Vertical axis limits (Default = central station median at local noon; options for 50%, 100%, 250%, 500%)
- Horizontal axis limits (Default = 0 min to 60 min; options for 0-15min, 15-30min, 30-45min, and 45-60min)

Visualise MULTI-STA/LTA event detection outputs for this day (https://github.com/rossjturner/seismic_attributes):
- Show event detection from the October 2021 prototype catalogue (before frequency normalisation was enabled as a pre-processing step).
- Show event detection with frequency normalisation enabled as a pre-processing step. The following parameters can be toggled:
1. EVENT JOIN: The maximum duration of gaps between triggered events before those events are considered separate.
   - OPTIONS: 15, 30, 60, 120
3. THRESHOLD ON: Threshold for switching single seismometer trigger on.
   - OPTIONS: 3, 4, 5
5. THRESHOLD OFF: Threshold for switching single seismometer trigger off.
   - OPTIONS: 1, 1.5, 2
7. COINCIDENCE SUM: The number of seismometers, n, on which an event must be detected for that event to be included in the (reference) event catalogue.
   - OPTIONS: 3, 4, 5, 6


Download instructions:
- Download this repository and Extract folder. Requires 853 MB.
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
WORKFLOW: Latto, R., Turner, R. J., Reading, A. M., Winberry, J. P., “Event detection for cryoseismology.” The Cryosphere, in prep.

DATASET: Paul Winberry, Sridhar Anandakrishnan, & Douglas Wiens. (2010). Geophysical Study of Ice Stream Stick-slip dynamics. International Federation of Digital Seismograph Networks. https://doi.org/10.7914/SN/2C_2010

SOFTWARE: Turner, R. J., Latto, R. B., & Reading, A. M. (2021). An ObsPy Library for Event Detection and Seismic Attribute Calculation: Preparing Waveforms for Automated Analysis. Journal of Open Research Software, 9(1), 29. DOI: http://doi.org/10.5334/jors.365
