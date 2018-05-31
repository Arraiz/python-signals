from .LoadFileDialog import Ui_LoadFile
from PyQt5 import QtWidgets
from scipy.io import wavfile
from pyqtgraph import mkPen
from numpy import arange, sin, pi, linspace


class LoadFileDialogLogic(Ui_LoadFile):

    def __init__(self, LoadFileDialogLogic):
        Ui_LoadFile.__init__(self)

    def setupBinds(self):
        self.pushButton.clicked.connect(self.openFileDialog)
        self.lineEdit.setText("Enter File Direction")
        self.plot.plotItem.vb.setBackgroundColor("w")

    def openFileDialog(self):
        self._audio_file = None
        qfd = QtWidgets.QFileDialog()
        filter = "wav(*.wav)"
        self._audio_file = QtWidgets.QFileDialog.getOpenFileName(
            qfd, "Select a file", "", filter)[0]
        print(str(self._audio_file))

        if(len(str(self._audio_file)) > 4):
            # check if file is not empty
            self.lineEdit.setText(str(self._audio_file))
            # open file
            fs, data = wavfile.read(str(self._audio_file))
            self.x = linspace(0, len(data), fs)
            print(len(data))
            print(str(fs))
            print(len(self.x))
            # self.plot.plot(self.x, data, pen=mkPen('b', width=1))
