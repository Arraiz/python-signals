from PyQt5 import QtCore, QtGui, QtWidgets
from plot.GraphicWidgetLogic import GraphicWidgetLogic
from .HarmonicSynthesisWidget import Ui_FreeHarmSynthWidget
from numpy import sin,pi,arange,cos
from pyqtgraph import mkPen

class FreeHarmonicSynthesisWidgetLogic(Ui_FreeHarmSynthWidget):
    def __init__(self,FreeHarmonicSynthesisWidgetLogic):
        Ui_FreeHarmSynthWidget.__init__(self)
        self.FS:float = 48000
        self.x=[]
        self.y=[]
        self.plot=0
        self.freqBias:float = 0.01
    
        


    def Logic(self):
        self.bind()
        self.PlotPreview.setBackground(background="w")
        self.plot = self.PlotPreview.plotItem
        self.x = arange(0,1,1/self.FS)

        
    # bidnea los scrolls a las amplitudes y y frecuancias de los senos
    def bind(self):
        self.FreqVSlider.valueChanged.connect(self.update)
        self.FreqSpinBox.valueChanged.connect(self.update)

        self.FreqVSlider_2.valueChanged.connect(self.update)
        self.FreqSpinBox_2.valueChanged.connect(self.update)

        self.FreqVSlider_3.valueChanged.connect(self.update)
        self.FreqSpinBox_3.valueChanged.connect(self.update)

        self.FreqVSlider_4.valueChanged.connect(self.update)
        self.FreqSpinBox_4.valueChanged.connect(self.update)

        self.FreqVSlider_5.valueChanged.connect(self.update)
        self.FreqSpinBox_5.valueChanged.connect(self.update)

        self.FreqVSlider_6.valueChanged.connect(self.update)
        self.FreqSpinBox_6.valueChanged.connect(self.update)

        self.FreqVSlider_7.valueChanged.connect(self.update)
        self.FreqSpinBox_7.valueChanged.connect(self.update)


        self.FreqVSlider_8.valueChanged.connect(self.update)
        self.FreqSpinBox_8.valueChanged.connect(self.update)

        self.FreqVSlider_9.valueChanged.connect(self.update)
        self.FreqSpinBox_9.valueChanged.connect(self.update)

        self.FreqVSlider_10.valueChanged.connect(self.update)
        self.FreqSpinBox_10.valueChanged.connect(self.update)


        self.pushButtonPlot.clicked.connect(self.GeneratePlot)


    def update(self):
        self.plot.clear()
        self.y=(self.freqBias*self.FreqVSlider.value()*cos(2*pi*self.x*self.FreqSpinBox.value()))+(self.freqBias*self.FreqVSlider_2.value()*sin(2*pi*self.x*self.FreqSpinBox_2.value()))+(self.freqBias*self.FreqVSlider_3.value()*sin(2*pi*self.x*self.FreqSpinBox_3.value()))+(self.freqBias*self.FreqVSlider_4.value()*sin(2*pi*self.x*self.FreqSpinBox_4.value()))+(self.freqBias*self.FreqVSlider_5.value()*sin(2*pi*self.x*self.FreqSpinBox_5.value()))+(self.freqBias*self.FreqVSlider_6.value()*sin(2*pi*self.x*self.FreqSpinBox_6.value()))+(self.freqBias*self.FreqVSlider_7.value()*sin(2*pi*self.x*self.FreqSpinBox_7.value()))+(self.freqBias*self.FreqVSlider_8.value()*sin(2*pi*self.x*self.FreqSpinBox_8.value()))+(self.freqBias*self.FreqVSlider_9.value()*sin(2*pi*self.x*self.FreqSpinBox_9.value()))+(self.freqBias*self.FreqVSlider_10.value()*sin(2*pi*self.x*self.FreqSpinBox_10.value()))
        self.plot.plot(self.x,self.y,pen=mkPen('r', width=1))


    def GeneratePlot(self):
        self.PlotWindow = QtWidgets.QWidget()
        self.ui = GraphicWidgetLogic(self)
        self.ui.setupUi(self.PlotWindow)
        self.ui.initializeBinds()
        self.ui.plotHarmonic(self.x,self.y)
        return self.PlotWindow  

