# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/HarmonicSynthesisWidget.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FreeHarmSynthWidget(object):
    def setupUi(self, FreeHarmSynthWidget):
        FreeHarmSynthWidget.setObjectName("FreeHarmSynthWidget")
        FreeHarmSynthWidget.resize(953, 619)
        self.layoutWidget = QtWidgets.QWidget(FreeHarmSynthWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(-5, 1, 971, 611))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButtonPlot = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonPlot.setObjectName("pushButtonPlot")
        self.horizontalLayout_2.addWidget(self.pushButtonPlot)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.PlotPreview = PlotWidget(self.layoutWidget)
        self.PlotPreview.setObjectName("PlotPreview")
        self.verticalLayout_2.addWidget(self.PlotPreview)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.FreqSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.FreqSpinBox.setMaximum(20000.0)
        self.FreqSpinBox.setObjectName("FreqSpinBox")
        self.verticalLayout.addWidget(self.FreqSpinBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.FreqVSlider = QtWidgets.QSlider(self.layoutWidget)
        self.FreqVSlider.setMouseTracking(False)
        self.FreqVSlider.setMaximum(100)
        self.FreqVSlider.setOrientation(QtCore.Qt.Vertical)
        self.FreqVSlider.setObjectName("FreqVSlider")
        self.horizontalLayout.addWidget(self.FreqVSlider)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_23.addLayout(self.verticalLayout)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.FreqSpinBox_2 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.FreqSpinBox_2.setMaximum(20000.0)
        self.FreqSpinBox_2.setObjectName("FreqSpinBox_2")
        self.verticalLayout_12.addWidget(self.FreqSpinBox_2)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.FreqVSlider_2 = QtWidgets.QSlider(self.layoutWidget)
        self.FreqVSlider_2.setMaximum(100)
        self.FreqVSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.FreqVSlider_2.setObjectName("FreqVSlider_2")
        self.horizontalLayout_12.addWidget(self.FreqVSlider_2)
        self.verticalLayout_12.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_23.addLayout(self.verticalLayout_12)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.FreqSpinBox_3 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.FreqSpinBox_3.setMaximum(20000.0)
        self.FreqSpinBox_3.setObjectName("FreqSpinBox_3")
        self.verticalLayout_13.addWidget(self.FreqSpinBox_3)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.FreqVSlider_3 = QtWidgets.QSlider(self.layoutWidget)
        self.FreqVSlider_3.setMaximum(100)
        self.FreqVSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.FreqVSlider_3.setObjectName("FreqVSlider_3")
        self.horizontalLayout_14.addWidget(self.FreqVSlider_3)
        self.verticalLayout_13.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_23.addLayout(self.verticalLayout_13)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.FreqSpinBox_4 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.FreqSpinBox_4.setMaximum(20000.0)
        self.FreqSpinBox_4.setObjectName("FreqSpinBox_4")
        self.verticalLayout_14.addWidget(self.FreqSpinBox_4)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.FreqVSlider_4 = QtWidgets.QSlider(self.layoutWidget)
        self.FreqVSlider_4.setMaximum(100)
        self.FreqVSlider_4.setOrientation(QtCore.Qt.Vertical)
        self.FreqVSlider_4.setObjectName("FreqVSlider_4")
        self.horizontalLayout_15.addWidget(self.FreqVSlider_4)
        self.verticalLayout_14.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_23.addLayout(self.verticalLayout_14)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.FreqSpinBox_5 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.FreqSpinBox_5.setMaximum(20000.0)
        self.FreqSpinBox_5.setObjectName("FreqSpinBox_5")
        self.verticalLayout_15.addWidget(self.FreqSpinBox_5)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.FreqVSlider_5 = QtWidgets.QSlider(self.layoutWidget)
        self.FreqVSlider_5.setMaximum(100)
        self.FreqVSlider_5.setOrientation(QtCore.Qt.Vertical)
        self.FreqVSlider_5.setObjectName("FreqVSlider_5")
        self.horizontalLayout_16.addWidget(self.FreqVSlider_5)
        self.verticalLayout_15.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_23.addLayout(self.verticalLayout_15)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.FreqSpinBox_6 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.FreqSpinBox_6.setMaximum(20000.0)
        self.FreqSpinBox_6.setObjectName("FreqSpinBox_6")
        self.verticalLayout_18.addWidget(self.FreqSpinBox_6)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.FreqVSlider_6 = QtWidgets.QSlider(self.layoutWidget)
        self.FreqVSlider_6.setMaximum(100)
        self.FreqVSlider_6.setOrientation(QtCore.Qt.Vertical)
        self.FreqVSlider_6.setObjectName("FreqVSlider_6")
        self.horizontalLayout_19.addWidget(self.FreqVSlider_6)
        self.verticalLayout_18.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_23.addLayout(self.verticalLayout_18)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.FreqSpinBox_7 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.FreqSpinBox_7.setMaximum(20000.0)
        self.FreqSpinBox_7.setObjectName("FreqSpinBox_7")
        self.verticalLayout_17.addWidget(self.FreqSpinBox_7)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.FreqVSlider_7 = QtWidgets.QSlider(self.layoutWidget)
        self.FreqVSlider_7.setMaximum(100)
        self.FreqVSlider_7.setOrientation(QtCore.Qt.Vertical)
        self.FreqVSlider_7.setObjectName("FreqVSlider_7")
        self.horizontalLayout_17.addWidget(self.FreqVSlider_7)
        self.verticalLayout_17.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_23.addLayout(self.verticalLayout_17)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.FreqSpinBox_8 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.FreqSpinBox_8.setMaximum(20000.0)
        self.FreqSpinBox_8.setObjectName("FreqSpinBox_8")
        self.verticalLayout_19.addWidget(self.FreqSpinBox_8)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.FreqVSlider_8 = QtWidgets.QSlider(self.layoutWidget)
        self.FreqVSlider_8.setMaximum(100)
        self.FreqVSlider_8.setOrientation(QtCore.Qt.Vertical)
        self.FreqVSlider_8.setObjectName("FreqVSlider_8")
        self.horizontalLayout_20.addWidget(self.FreqVSlider_8)
        self.verticalLayout_19.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_23.addLayout(self.verticalLayout_19)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.FreqSpinBox_9 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.FreqSpinBox_9.setMaximum(20000.0)
        self.FreqSpinBox_9.setObjectName("FreqSpinBox_9")
        self.verticalLayout_20.addWidget(self.FreqSpinBox_9)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.FreqVSlider_9 = QtWidgets.QSlider(self.layoutWidget)
        self.FreqVSlider_9.setMaximum(100)
        self.FreqVSlider_9.setOrientation(QtCore.Qt.Vertical)
        self.FreqVSlider_9.setObjectName("FreqVSlider_9")
        self.horizontalLayout_21.addWidget(self.FreqVSlider_9)
        self.verticalLayout_20.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_23.addLayout(self.verticalLayout_20)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.FreqSpinBox_10 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.FreqSpinBox_10.setMaximum(20000.0)
        self.FreqSpinBox_10.setObjectName("FreqSpinBox_10")
        self.verticalLayout_21.addWidget(self.FreqSpinBox_10)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.FreqVSlider_10 = QtWidgets.QSlider(self.layoutWidget)
        self.FreqVSlider_10.setMaximum(100)
        self.FreqVSlider_10.setOrientation(QtCore.Qt.Vertical)
        self.FreqVSlider_10.setObjectName("FreqVSlider_10")
        self.horizontalLayout_22.addWidget(self.FreqVSlider_10)
        self.verticalLayout_21.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_23.addLayout(self.verticalLayout_21)
        self.verticalLayout_2.addLayout(self.horizontalLayout_23)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(FreeHarmSynthWidget)
        QtCore.QMetaObject.connectSlotsByName(FreeHarmSynthWidget)

    def retranslateUi(self, FreeHarmSynthWidget):
        _translate = QtCore.QCoreApplication.translate
        FreeHarmSynthWidget.setWindowTitle(_translate("FreeHarmSynthWidget", "Harmonic Synthesis"))
        self.pushButtonPlot.setText(_translate("FreeHarmSynthWidget", "View Plot"))

from pyqtgraph import PlotWidget
