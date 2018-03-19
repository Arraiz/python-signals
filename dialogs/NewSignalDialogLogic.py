import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from .NewSignalDialog import Ui_NewSignalDialog
from plot.PlotWindowLogic import PlotWindowLogic
import numpy as np
class NewSignalDialogLogic(Ui_NewSignalDialog):
    def __init__(self,NewSignalDialogLogic):
        Ui_NewSignalDialog.__init__(self)
    

    def newPlot(self):


        #get function
        func = 'Sin'
        if(self.radioButtonSin.isChecked==True):
            func='Cos'


        self.PlotWindow = QtWidgets.QWidget()
        self.ui = PlotWindowLogic(self)
        self.ui.setupUi(self.PlotWindow)
        self.ui.Plot(self.horizontalSliderAmplitude.value(),self.horizontalSliderFrequency.value(),self.horizontalSliderPhase.value(),'sin')
        self.PlotWindow.show()
        self.PlotWindow.activateWindow()
        self.PlotWindow.raise_()
        
    

    