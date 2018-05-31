from .RecordSoundDialog import Ui_RecordSoundDialog
import pyaudio
from PyQt5 import QtWidgets
import wave
import numpy as np
import sounddevice as sd


class RecordSoundDialogLogic(Ui_RecordSoundDialog):
    def __init__(self, RecordSoundDialogLogic):
        Ui_RecordSoundDialog.__init__(self)
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

    def setupBinds(self):
        self.pushButtonRecord.clicked.connect(self.record)
        self.pushButtonPlay.clicked.connect(self.play)
        self.pushButtonSave.clicked.connect(self.saveFile)

    def record(self):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 48000
        RECORD_SECONDS = 2
        WAVE_OUTPUT_FILENAME = "salida.wav"

        self.LabelStatus.setText(
            "Recording: "+str(RECORD_SECONDS)+" at "+str(RATE))

        self.p = pyaudio.PyAudio()

        stream = self.p.open(format=FORMAT,
                             channels=CHANNELS,
                             rate=RATE,
                             input=True,
                             frames_per_buffer=CHUNK)

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        self.LabelStatus.setText("Record Finished")

        stream.stop_stream()
        stream.close()
        self.p.terminate()

        frames = b''.join(frames)

        amplitude = np.fromstring(frames, np.int16)
        self.y = amplitude
        duration = len(self.y)/RATE

        self.x = np.arange(0, duration, 1/RATE)

        self.graphicsView.plotItem.plot(self.x, amplitude)

    def play(self):
        sd.play(self.y, self.RATE, blocking=True)

    def saveFile(self):

        fileName, _ = QtWidgets.QFileDialog.getSaveFileUrl(self)

        print(fileName)

        # wf = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
        # wf.setnchannels(self.CHANNELS)
        # wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        # wf.setframerate(self.RATE)
        # wf.writeframes(b''.join(self.frames))
        # wf.close()
        # self.LabelStatus.setText("Saved OK.")
