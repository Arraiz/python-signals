# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlotWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PlotWindow(object):
    def setupUi(self, PlotWindow):
        PlotWindow.setObjectName("PlotWindow")
        PlotWindow.resize(849, 530)
        self.gridLayout = QtWidgets.QGridLayout(PlotWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.PlotView = PlotWidget(PlotWindow)
        self.PlotView.setObjectName("PlotView")
        self.verticalLayout.addWidget(self.PlotView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonAddSignal = QtWidgets.QPushButton(PlotWindow)
        self.pushButtonAddSignal.setObjectName("pushButtonAddSignal")
        self.horizontalLayout.addWidget(self.pushButtonAddSignal)
        self.pushButtonPlotNewSignal = QtWidgets.QPushButton(PlotWindow)
        self.pushButtonPlotNewSignal.setObjectName("pushButtonPlotNewSignal")
        self.horizontalLayout.addWidget(self.pushButtonPlotNewSignal)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(PlotWindow)
        QtCore.QMetaObject.connectSlotsByName(PlotWindow)

    def retranslateUi(self, PlotWindow):
        _translate = QtCore.QCoreApplication.translate
        PlotWindow.setWindowTitle(_translate("PlotWindow", "Form"))
        self.pushButtonAddSignal.setText(_translate("PlotWindow", "Add Signal"))
        self.pushButtonPlotNewSignal.setText(_translate("PlotWindow", "Plot Signal"))

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PlotWindow = QtWidgets.QWidget()
    ui = Ui_PlotWindow()
    ui.setupUi(PlotWindow)
    PlotWindow.show()
    sys.exit(app.exec_())

