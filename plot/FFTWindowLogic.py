import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from .FFTWindow import Ui_PlotWindowFFT

from pyqtgraph import mkPen
from numpy import fft,linspace, sin, pi
from scipy import signal


class FFTWindowLogic(Ui_PlotWindowFFT):
    def __init__(self,Ui_PlotWindowFFT,yArray,Fs):
        Ui_PlotWindowFFT.__init__(self)
        self.y = yArray
        self.Fs = Fs
        self.pen=mkPen('r',width=2)
    
    def PlotFFT(self):
   
        self.X = linspace(0,((self.Fs)/2),(self.Fs)/2)
        self.Y = abs(fft.rfft(self.y,self.Fs-1))/len(self.X)/2
        #x = linspace(0, 1, 500, endpoint=False)
        #y = sin(2 * pi * 5 * x)+sin(2 * pi * 15 * x)+sin(2 * pi * 25 * x)
        #Y = abs(fft.rfft(y,500-1))/(500-1)
        #X = linspace(0,(500-1)/2,500/2)
        self.plot = self.FFTplotView.plotItem
        self.vBox = self.plot.vb
        self.vBox.setLimits(xMin=-1.2, yMin=-2, xMax=self.Fs/2, yMax=10)
        self.plot.addLegend()
        self.plot.showGrid(x=True, y=True)
        self.plot.plot(self.X,self.Y,pen=self.pen)

