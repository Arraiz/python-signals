import sys
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
# importamos la interfaz grafica
from gui import Ui_MainWindow

from dialogs.PeriodicKnownSignals.NewSquareDialogLogic import Ui_NewSuareDialogLogic
from dialogs.PeriodicKnownSignals.NewSawtoothDialogLogic import Ui_NewSawtoothDialogLogic
from dialogs.HarmonicSynthesis.HarmonicSynthesisWidgetLogic import FreeHarmonicSynthesisWidgetLogic
from dialogs.pureSignal.NewPureSignalLogic import Ui_NewPureSignalDialogLogic
from dialogs.Rosenbert.RosenbertLogic import RosenbertDialogLogic

from dialogs.InputOutput.LoadFileDialogLogic import LoadFileDialogLogic
from dialogs.InputOutput.RecordSoundDialogLogic import RecordSoundDialogLogic
# ----------------------------
# # PUNTO DE ENTRADA DE LA APP
# ----------------------------

# creamos la clase que hereda de nuestra IU para añadir la Logica

class UI_Logic(Ui_MainWindow):
    # constructor
    def __init__(self, MainWindow):
        # constructor padre
        Ui_MainWindow.__init__(self)
        self.setupUi(MainWindow)
        self.setupMenu()
        # lista para soportar la multiventana
        self.windows = []
        self.plotWindows = []
        self.FS = 48000

    # dialogo señales puras
    def openPureSignalDialog(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_NewPureSignalDialogLogic(self)
        self.ui.setupUi(self.window)
        self.ui.setupBinds()
        self.ui.buttonBox.accepted.connect(self.openPlotAndCloseWindow)
        self.windows.append(self.window)
        self.windows[len(self.windows)-1].show()
        self.windows[len(self.windows)-1].activateWindow()
        self.windows[len(self.windows)-1].raise_()
        # self.window.show()
        # self.window.activateWindow()
        # self.window.raise_()

    def openNewSquarePlotDialog(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_NewSuareDialogLogic(self)
        self.ui.setupUi(self.window)
        self.ui.setupBinds()
        self.ui.buttonBox.accepted.connect(self.openPlotAndCloseWindow)
        self.windows.append(self.window)
        self.windows[len(self.windows)-1].show()
        self.windows[len(self.windows)-1].activateWindow()
        self.windows[len(self.windows)-1].raise_()
        # self.window.show()
        # self.window.activateWindow()
        # self.window.raise_()

    # def openNewSawtoothPlotDialog(self):
    #     self.window = QtWidgets.QDialog()
    #     self.ui = Ui_NewSawtoothDialogLogic(self)
    #     self.ui.setupUi(self.window)
    #     self.ui.setupBinds()
    #     self.ui.buttonBox.accepted.connect(self.openPlotAndCloseWindow)
    #     self.windows.append(self.window)
    #     self.windows[len(self.windows)-1].show()
    #     self.windows[len(self.windows)-1].activateWindow()
    #     self.windows[len(self.windows)-1].raise_()
    #     #self.window.show()
    #     #self.window.activateWindow()
    #     #self.window.raise_()

    def openNewSawtoothPlotDialog(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_NewSawtoothDialogLogic(self)
        self.ui.setupUi(self.window)
        self.ui.setupBinds()
        self.ui.buttonBox.accepted.connect(self.openPlotAndCloseWindow)
        self.windows.append(self.window)
        self.windows[len(self.windows)-1].show()
        self.windows[len(self.windows)-1].activateWindow()
        self.windows[len(self.windows)-1].raise_()
        # self.window.show()
        # self.window.activateWindow()
        # self.window.raise_()

    # abrimos el plot que se elija
    # def openPlotAndCloseWindow(self):
    #     plotWindow =  self.ui.GeneratePlot()
    #     self.plotWindows.append(plotWindow)
    #     self.plotWindows[len(self.plotWindows)-1].show()
    #     self.plotWindows[len(self.plotWindows)-1].activateWindow()
    #     self.plotWindows[len(self.plotWindows)-1].raise_()
    #     self.window.hide()

        # abrimos el plot que se elija
    def openPlotAndCloseWindow(self):
        plotWindow = self.ui.GeneratePlot()
        self.plotWindows.append(plotWindow)
        self.plotWindows[len(self.plotWindows)-1].show()
        self.plotWindows[len(self.plotWindows)-1].activateWindow()
        self.plotWindows[len(self.plotWindows)-1].raise_()
        self.window.hide()

    # ventana de sistesis harmonica
    def openHarmonicSynthesis(self):
        self.window = QtWidgets.QWidget()
        self.ui = FreeHarmonicSynthesisWidgetLogic(self)
        self.ui.setupUi(self.window)
        self.ui.Logic()
        self.ui.pushButtonPlot.clicked.connect(self.openPlotAndCloseWindow)
        self.windows.append(self.window)
        self.windows[len(self.windows)-1].show()
        self.windows[len(self.windows)-1].activateWindow()
        self.windows[len(self.windows)-1].raise_()

    def openRosenbert(self):
        self.window = QtWidgets.QDialog()
        self.ui = RosenbertDialogLogic(self)
        self.ui.setupUi(self.window)
        self.ui.setupBinds()
        self.ui.defaultPlot()
        self.ui.buttonBox.accepted.connect(self.openPlotAndCloseWindow)
        self.windows.append(self.window)
        self.windows[len(self.windows)-1].show()
        self.windows[len(self.windows)-1].activateWindow()
        self.windows[len(self.windows)-1].raise_()

    def openLoadFile(self):
        self.window = QtWidgets.QDialog()
        self.ui = LoadFileDialogLogic(self)
        self.ui.setupUi(self.window)
        self.ui.setupBinds()
        self.window.show()
        self.window.activateWindow()
        self.window.raise_()

    def openRedordSound(self):
        self.window = QtWidgets.QDialog()
        self.ui = RecordSoundDialogLogic(self)
        self.ui.setupUi(self.window)
        self.ui.setupBinds()
        self.window.show()
        self.window.activateWindow()
        self.window.raise_()
    ##################################


    ###########CONTEXT MENU
    def setupMenu(self):
        self.actionNew.triggered.connect(self.openPureSignalDialog)
        self.actionSquare.triggered.connect(self.openNewSquarePlotDialog)
        self.actionSawtooth.triggered.connect(self.openNewSawtoothPlotDialog)
        self.actionFree.triggered.connect(self.openHarmonicSynthesis)
        self.actionRosenbert.triggered.connect(self.openRosenbert)
        self.actionLoad.triggered.connect(self.openLoadFile)
        self.actionRecord.triggered.connect(self.openRedordSound)



if __name__ == '__main__':
    # entry point
    app = QtWidgets.QApplication(sys.argv)
    mainW = QtWidgets.QMainWindow()
    prog = UI_Logic(mainW)
    mainW.show()
    sys.exit(app.exec_())
