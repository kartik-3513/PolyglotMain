from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QPixmap
from . import upload 
from . import sentence
from utils import shared

class MainPage(QMainWindow):
    def __init__(self):
        super(MainPage, self).__init__()
        loadUi("Polyglot/screens/intro.ui", self)
        pixmap = QPixmap("Polyglot/screens/word-cloudedited.png")
        self.title_l.setPixmap(pixmap)
        self.start_sentence_b.clicked.connect(self.onClickStartSentenceButton)
        self.start_sentence_b.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_upload_b.clicked.connect(self.onClickStartUploadButton)
        self.start_upload_b.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def onClickStartSentenceButton(self):
        shared.stack_w.addWidget(sentence.SentenceWindow())
        shared.stack_w.setCurrentIndex(shared.stack_w.currentIndex() + 1)

    def onClickStartUploadButton(self):
        shared.stack_w.addWidget(upload.UploadWindow())
        shared.stack_w.setCurrentIndex(shared.stack_w.currentIndex() + 1)
