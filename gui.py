# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'giu.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(415, 102)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 415, 22))
        self.menubar.setObjectName("menubar")
        self.menuSignal_Visualizer = QtWidgets.QMenu(self.menubar)
        self.menuSignal_Visualizer.setObjectName("menuSignal_Visualizer")
        self.menuGenerate = QtWidgets.QMenu(self.menubar)
        self.menuGenerate.setObjectName("menuGenerate")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSine = QtWidgets.QAction(MainWindow)
        self.actionSine.setObjectName("actionSine")
        self.actionCosine = QtWidgets.QAction(MainWindow)
        self.actionCosine.setObjectName("actionCosine")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionPure_Signal = QtWidgets.QAction(MainWindow)
        self.actionPure_Signal.setObjectName("actionPure_Signal")
        self.menuSignal_Visualizer.addSeparator()
        self.menuSignal_Visualizer.addAction(self.actionExit)
        self.menuGenerate.addAction(self.actionPure_Signal)
        self.menuGenerate.addSeparator()
        self.menubar.addAction(self.menuSignal_Visualizer.menuAction())
        self.menubar.addAction(self.menuGenerate.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuSignal_Visualizer.setTitle(_translate("MainWindow", "Signal Visualizer"))
        self.menuGenerate.setTitle(_translate("MainWindow", "Generate"))
        self.actionSine.setText(_translate("MainWindow", "Sine"))
        self.actionCosine.setText(_translate("MainWindow", "Cosine"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionPure_Signal.setText(_translate("MainWindow", "Pure Signal"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

