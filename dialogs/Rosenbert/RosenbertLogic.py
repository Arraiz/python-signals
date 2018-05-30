from numpy import pi,zeros,concatenate,cos,round,arange
from scipy import signal
from .Rosenbert import Ui_RosenbertDialog
from pyqtgraph import mkPen


class RosenbertDialogLogic(Ui_RosenbertDialog):
    def __init__(self, Ui_NewPureSignalDialogLogic):
        Ui_RosenbertDialog.__init__(self)
        self.FS=0
        self.x=0
        self.y=0
        self.a1=0.25
        self.a2=0.35
        self.period=100
        self.alpha1=0
        self.alpha2=0
        self.plot=0
        self.alpha1=0
        self.alpha2=0

    def update(self):
    
    
        # generamos el pulso glotal
        self.alpha1=int(self.doubleSpinBoxAlpha1.value())
        self.alpha2=int(self.doubleSpinBoxAlpha2.value())
        self.period=int(self.doubleSpinBoxFrequency.value())

        
        self.x=arange(0,1,1/self.period)
        z=zeros((self.period-(self.alpha1+self.alpha2))*self.period)
        n1=round(self.period*self.alpha1)
        n2=round(self.period*self.alpha2)
        g=[]
        x1=arange(0,n1)
        self.g=0.5*(1-cos(pi*x1/n1))
        x2=arange(1,n2)
        self.g = concatenate((self.g,cos(pi*x2/(2*n2))))
        self.g=concatenate((self.g,z))
        self.y=g
        self.plot.clear()
        self.plot.plot(self.x,self.y,pen=mkPen('b', width=1))




    def setupBinds(self):
        self.doubleSpinBoxFrequency.valueChanged.connect(self.update)
        self.doubleSpinBoxAlpha1.valueChanged.connect(self.update)
        self.doubleSpinBoxAlpha2.valueChanged.connect(self.update)
        self.plot = self.PreviewPlot.plotItem
        self.plot.vb.setBackgroundColor("w")


    def defaultPlot(self):


        x=arange(0,1,1/self.period)
        alpha1=int(self.period*self.a1)
        alpha2=int(self.period*self.a2)
        z=zeros((self.period-(alpha1+alpha2)))
        n1=round(alpha1)
        n2=round(alpha2)
        g=[]
        x1=arange(0,n1)
        g=0.5*(1-cos(pi*x1/n1))
        x2=arange(0,n2)
        g = concatenate((g,cos(pi*x2/(2*n2))))
        g=concatenate((g,z))
        self.plot.plot(x,g,pen=mkPen('b', width=1))


