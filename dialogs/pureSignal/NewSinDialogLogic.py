from PyQt5 import QtCore, QtGui, QtWidgets
from .NewSinDialog import Ui_NewSinDialog
from plot.PlotWindowLogic import PlotWindowLogic

class Ui_NewSinDialogLogic(Ui_NewSinDialog):
    def __init__(self, NewSignalDialogLogic):
        Ui_NewSinDialog.__init__(self)

    def GeneratePlot(self):
        self.PlotWindow = QtWidgets.QWidget()
        self.ui = PlotWindowLogic(self)
        self.ui.setupUi(self.PlotWindow)
        self.ui.initBindings()
        self.ui.PlotSin(self.doubleSpinBoxAmplitude.value(),self.doubleSpinBoxFrecuency.value(),self.doubleSpinBoxPhase.value())
        return self.PlotWindow
        
