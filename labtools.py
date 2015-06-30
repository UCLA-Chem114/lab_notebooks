%matplotlib qt
from pylab import *
from scipy.optimize import curve_fit
import pandas as pd

def choose_file():
    from PyQt4 import QtGui
    app = QtGui.QApplication([dir])
    fname = QtGui.QFileDialog.getOpenFileName(None, "Select a file...", '.', filter="All files (*)")
    return str(fname)

