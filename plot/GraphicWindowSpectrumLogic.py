from .GraphicWindowSpectrum import Ui_GraphicWindowSpectrum
from pyqtgraph import SignalProxy, LinearRegionItem, InfiniteLine
from pyqtgraph.Point import Point
from numpy import sin, cos, fft, arange, pi, savetxt,linspace
from scipy import signal
from scipy.signal import square, sawtooth, gausspulse
from pyqtgraph import mkPen,setConfigOption

from PyQt5 import QtCore   



class GraphicWidgetLogicSpectrumLogic (Ui_GraphicWindowSpectrum):
    def __init__(self,GraphicWidgetLogic):
        Ui_GraphicWindowSpectrum.__init__(self)
        self.FS = 48000
        self.x=0
        self.y=0



    # se inicializa el sistema de visualizado avanzado
    def initializeBinds(self):
        # añadir plots


        
        setConfigOption('leftButtonPan', False)
        self.x=0
        self.y=0

        self.zoomedPlot = self.graphicsView.addPlot(row=1, col=0)
        self.fullPlot = self.graphicsView.addPlot(row=2, col=0)  
        
        self.zoomedPlot.vb.setBackgroundColor("w")
        self.fullPlot.vb.setBackgroundColor("w")
        self.penB=mkPen('b') 
        self.penR=mkPen('r') 
        self.region = LinearRegionItem()
        self.region.setZValue(10)

        self.vb = self.zoomedPlot.vb
        self.region.setRegion([1000, 2000])

        self.fullPlot.addItem(self.region, ignoreBounds=True)  
        #pg.dbg()
        self.zoomedPlot.setAutoVisible(y=True)

        self.vLine = InfiniteLine(angle=90, movable=False)
        self.hLine = InfiniteLine(angle=0, movable=False)
        self.zoomedPlot.addItem(self.vLine, ignoreBounds=True)
        self.zoomedPlot.addItem(self.hLine, ignoreBounds=True)

        # signal para capturar evento de raton
        # proxy = SignalProxy(self.zoomedPlot.scene().sigMouseMoved, rateLimit=60, slot=self.mouseMoved)
        
        self.zoomedPlot.scene().sigMouseMoved.connect(self.mouseMoved)
        self.region.sigRegionChanged.connect(self.update)
        
        self.zoomedPlot.sigRangeChanged.connect(self.updateRegion)





    def updateRegion(self,window, viewRange):
        rgn = viewRange[0]
        self.region.setRegion(rgn)


    def update(self):
        self.region.setZValue(10)
        minX, maxX = self.region.getRegion()
        self.zoomedPlot.setXRange(minX, maxX, padding=0)    
  
    def mouseMoved(self,evt):
        pos = Point(evt.x(),evt.y())
        if self.zoomedPlot.sceneBoundingRect().contains(pos):
          mousePoint = self.vb.mapSceneToView(pos)
          index = float(evt.x())
        #   if index > 0 :
            # self.dataLabel.setText("<span style='font-size: 12pt'>x=%0.1f,   <span style='color: red'>y1=%0.1f</span>,   <span style='color: green'>y2=%0.1f</span>" % int(index), self.x[index], self.y[index])
          self.vLine.setPos(mousePoint.x())
          self.hLine.setPos(mousePoint.y())



    def PlotFFT(self,Xarray,Yarray):
        self.x = Xarray
        self.y = Yarray
        self.X = linspace(0,((self.FS)/2),(self.FS)/2)
        self.Y = abs(fft.rfft(self.y,self.FS-1))/len(self.X)/2
        #x = linspace(0, 1, 500, endpoint=False)
        #y = sin(2 * pi * 5 * x)+sin(2 * pi * 15 * x)+sin(2 * pi * 25 * x)
        #Y = abs(fft.rfft(y,500-1))/(500-1)
        #X = linspace(0,(500-1)/2,500/2)

        self.fullPlot.plot(self.X,self.Y,pen=self.penR)
        self.zoomedPlot.plot(self.X,self.Y,pen=self.penB)
