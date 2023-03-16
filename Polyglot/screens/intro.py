from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QPixmap
from . import interaction
from utils import shared

class MainPage(QMainWindow):
    def __init__(self):
        super(MainPage, self).__init__()
        loadUi("Polyglot/screens/intro.ui", self)
        pixmap = QPixmap("Polyglot/screens/word-cloudedited.png")
        self.title_l.setPixmap(pixmap)
        self.start_b.clicked.connect(self.onClickMainVideo)
        self.start_b.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def onClickMainVideo(self):
        shared.stack_w.addWidget(interaction.InteractionWindow())
        shared.stack_w.setCurrentIndex(shared.stack_w.currentIndex() + 1)
