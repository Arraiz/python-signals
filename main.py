import sys
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
# importamos la interfaz grafica
from gui import Ui_MainWindow
from dialogs.NewSignalDialogLogic import NewSignalDialogLogic


# creamos la clase que hereda de nuestra IU para añadir la Logica

class UI_Logic(Ui_MainWindow):
    # constructor
    def __init__(self, MainWindow):
        # constructor padre
        Ui_MainWindow.__init__(self)
        self.setupUi(MainWindow)
        self.setupMenu()
        
    def openNewPlotDialog(self):
        self.window = QtWidgets.QWidget()
        self.ui = NewSignalDialogLogic(self)
        self.ui.setupUi(self.window)
        self.ui.pushButtonPlot.clicked.connect(self.ui.newPlot)
        self.ui.pushButtonCancel.clicked.connect(self.window.close)
        self.window.show()
        self.window.activateWindow()
        self.window.raise_()

    ##################################

    def setupMenu(self):
        self.actionPure_Signal.triggered.connect(self.openNewPlotDialog)


    
      

if __name__ == '__main__':
    # entry point
    app = QtWidgets.QApplication(sys.argv)
    mainW = QtWidgets.QMainWindow()
    prog = UI_Logic(mainW)
    mainW.show()
    sys.exit(app.exec_())
