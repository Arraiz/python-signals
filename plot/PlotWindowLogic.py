import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from .PlotWindow import Ui_PlotWindow
import numpy as np


class PlotWindowLogic(Ui_PlotWindow):
    def __init__(self,PlotWindowLogic):
        Ui_PlotWindow.__init__(self)


    def Plot(self,amp,freq,phase,type):
        Fs = 8000
        sample = 8000
        x = np.arange(sample)
        y = (amp/10)*np.sin(2 * np.pi * freq * x / Fs+phase)
        plot =self.PlotView.plotItem
        vBox = plot.vb
        vBox.setLimits(xMin=0,yMin=-2,xMax=8000,yMax=2)
        plot.addLegend()
        plot.showGrid(x=True,y=True)
        plot.plot(x, y, pen='r',name=type)


