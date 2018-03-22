import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from .FFTWindow import Ui_PlotWindowFFT


from numpy import fft,linspace
from scipy import signal


class FFTWindowLogic(Ui_PlotWindowFFT):
    def __init__(self,Ui_PlotWindowFFT,yArray,Fs):
        Ui_PlotWindowFFT.__init__(self)
        self.y = yArray
        self.Fs = Fs
    
    def PlotFFT(self):
        self.Y = abs(fft.rfft(self.y,self.Fs-1))
        self.X = linspace(0,(self.Fs/2),self.Fs/2)
        self.plot = self.FFTplotView.plotItem
        self.plot.plot(self.X,self.Y)

