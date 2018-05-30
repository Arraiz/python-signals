# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/LoadFileDialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoadFile(object):
    def setupUi(self, LoadFile):
        LoadFile.setObjectName("LoadFile")
        LoadFile.resize(753, 412)
        self.layoutWidget = QtWidgets.QWidget(LoadFile)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 751, 411))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.plot = PlotWidget(self.layoutWidget)
        self.plot.setObjectName("plot")
        self.verticalLayout_2.addWidget(self.plot)
        self.buttonBox_2 = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.buttonBox_2.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_2.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_2.setObjectName("buttonBox_2")
        self.verticalLayout_2.addWidget(self.buttonBox_2)

        self.retranslateUi(LoadFile)
        self.buttonBox_2.accepted.connect(LoadFile.close)
        self.buttonBox_2.rejected.connect(LoadFile.close)
        QtCore.QMetaObject.connectSlotsByName(LoadFile)

    def retranslateUi(self, LoadFile):
        _translate = QtCore.QCoreApplication.translate
        LoadFile.setWindowTitle(_translate("LoadFile", "Load File Window"))
        self.pushButton.setText(_translate("LoadFile", "Load"))

from pyqtgraph import PlotWidget
