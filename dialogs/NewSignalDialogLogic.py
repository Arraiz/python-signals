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
        self.func = 'Sin'
        if(self.radioButtonCos.isChecked()==True):
            self.func='Cos'  
        elif(self.radioButtonSquare.isChecked()==True):
            self.func='Square'
        elif(self.radioButtonSawTooth.isChecked()==True):
            self.func='SawTooth'  
        self.PlotWindow = QtWidgets.QWidget()
        self.ui = PlotWindowLogic(self)
        self.ui.setupUi(self.PlotWindow)
        self.ui.initBindings()
        self.ui.Plot(self.horizontalSliderAmplitude.value(),self.horizontalSliderFrequency.value(),self.horizontalSliderPhase.value(),self.spinBoxFs.value(),self.func)
        return self.PlotWindow


        
        
        
    

    