from PyQt5 import QtCore, QtGui, QtWidgets
from .NewCosDialog import Ui_NewCosDialog
from plot.PlotWindowLogic import PlotWindowLogic

class Ui_NewCosDialogLogic(Ui_NewCosDialog):
    def __init__(self, NewSignalDialogLogic):
        Ui_NewCosDialog.__init__(self)

    def GeneratePlot(self):
        self.PlotWindow = QtWidgets.QWidget()
        self.ui = PlotWindowLogic(self)
        self.ui.setupUi(self.PlotWindow)
        self.ui.initBindings()
        self.ui.PlotCos(self.doubleSpinBoxAmplitude.value(),self.doubleSpinBoxFrecuency.value(),self.doubleSpinBoxPhase.value())
        return self.PlotWindow
        
