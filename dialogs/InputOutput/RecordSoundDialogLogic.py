from .RecordSoundDialog import Ui_RecordSoundDialog
import pyaudio
from PyQt5 import QtWidgets
from pyqtgraph import mkPen
import wave
import numpy as np
import sounddevice as sd


class RecordSoundDialogLogic(Ui_RecordSoundDialog):
    def __init__(self, RecordSoundDialogLogic):
        Ui_RecordSoundDialog.__init__(self)
        # Default settings
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 48000
        self.RECORD_SECONDS = 2
        self.WAVE_OUTPUT_FILENAME = "record.wav"
        self.x = []
        self.y = []
        self.frames = []
        self.p = 0
        self.amplitude = []

    def setupBinds(self):
        self.graphicsView.setBackground(background="w")
        self.pushButtonRecord.clicked.connect(self.record)
        self.pushButtonPlay.clicked.connect(self.play)
        self.pushButtonSave.clicked.connect(self.saveFile)

    def record(self):

        self.LabelStatus.setText(
            "Recording: "+str(self.RECORD_SECONDS)+" at "+str(self.RATE))

        self.p = pyaudio.PyAudio()

        # valores de grabacion del usuario
        self.RATE = int(self.doubleSpinBoxFrequency.value())
        self.RECORD_SECONDS = int(self.doubleSpinBoxDuration.value())

        print(str(self.RATE)+" "+str(self.RECORD_SECONDS))
        self.frames = []
        self.data = []
        self.amplitude = []
        self.y = []
        stream = self.p.open(format=self.FORMAT,
                             channels=self.CHANNELS,
                             rate=self.RATE,
                             input=True,
                             frames_per_buffer=self.CHUNK)

        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = stream.read(self.CHUNK)
            self.frames.append(data)

        self.LabelStatus.setText("Record Finished")

        stream.stop_stream()
        stream.close()
        self.p.terminate()

        self.frames = b''.join(self.frames)

        self.amplitude = np.fromstring(self.frames, np.int16)
        self.y = self.amplitude
        duration = len(self.y)/self.RATE

        self.x = np.arange(0, duration, 1/self.RATE)

        self.graphicsView.plotItem.clear()
        self.graphicsView.plot(self.x, self.amplitude, pen=mkPen('b', width=1))
        # self.graphicsView.plotItem.plot(self.x, self.amplitude)

    def play(self):
        sd.play(self.y, self.RATE, blocking=True)

    def saveFile(self):
        qfd = QtWidgets.QFileDialog()
        fileName = QtWidgets.QFileDialog.getSaveFileName(qfd, "Save File")

        # print("ruta"+str(fileName))
        # devuelve un array con 2 elementos el primero es la ruta
        wf = wave.open(str(fileName[0]), 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(self.frames)
        wf.close()
        self.LabelStatus.setText("Saved OK.")
    

    
