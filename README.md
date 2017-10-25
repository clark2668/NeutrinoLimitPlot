# NeutrinoLimitPlot
Python code to make a plot of the leading neutrino limits. The y-axis is Flux and the x-axis is Energy.

## plotting_program
- This contains the code to actually make the plot.
- It is a python program that can be called by running `python make_plot.py`.
- It's output is a single image file (currently .pdf) called `leading_limits_plot.pdf`.
- The python script is completely self-contained (no dependencies) except Python.
- You will need a few pieces of software installed for Python (but these are not very unusual)
  - Numpy
  - Matplotlib
- Currently, the program also requires a functioning latex distribution to make the plot look extra pretty. Uncomment those lines if you do not have this.

## source_info
- This file contains the original PDF source files, the PNG screen captures of the digitized plots, and the CSV files that are the results of digitization.
- The plots were all digitized out of their original publications by [WebPlotDigitizer](http://arohatgi.info/WebPlotDigitizer/).

## latex_document
- This contains a compilable Latex document with the figure included.
- In particular, it includes appropriately formated Bibtex entries for use in other Latex papers.

## Acknowledgements and Other Notes
- Many thanks to Ming-Yuan Lu for the projection of the ARA sensitivity
- Please feel free to use this code, but please acknowledge the source
- If you find a mistake in my digitization or plotting, please file an "Issue", I'm happy to fix it!

