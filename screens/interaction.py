from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import numpy as np
from pyqtgraph import PlotWidget
import pyqtgraph as pg
from embedder.embedder import Embedder
from utils.worker import Worker
from PyQt5.QtCore import QThread
from utils import shared

class InteractionWindow(QMainWindow):
    def __init__(self):
        super(InteractionWindow, self).__init__()
        loadUi("Polyglot/screens/NEW_interaction.ui", self)
        self.back_b.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_b.clicked.connect(self.onBack)
        self.analyse_b.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.analyse_b.clicked.connect(self.analyse)
        self.graphWidget.setBackground('white')
        self.graphWidget.setXRange(-1, 1, padding=0)
        self.graphWidget.setYRange(-1, 1, padding=0)

        font=QtGui.QFont()
        font.setPixelSize(20)

        plot = self.graphWidget.getPlotItem()
        plot.getAxis("bottom").setStyle(tickTextOffset = 20, tickFont = font)
        plot.getAxis("left").setStyle(tickTextOffset = 20, tickFont = font)
        plot.getAxis('left').setPen(size=20, color="black")
        plot.getAxis('bottom').setPen(size=20, color="black")

        self.embeddings = None
        self.sentences = {}

    def onBack(self):
        this_widget = shared.stack_w.currentWidget()
        shared.stack_w.removeWidget(this_widget)
        this_widget.deleteLater()

    def prepareSentences(self):
        en_text = self.english_edit.toPlainText().splitlines()
        hi_text = self.hindi_edit.toPlainText().splitlines()
        self.sentences['en'] = en_text
        self.sentences['hi'] = hi_text

    def analyse(self):
        self.thread = QThread()
        self.worker = Worker()
        self.prepareSentences()
        self.worker.setInputSentences(self.sentences)
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.thread.finished.connect(self.thread.deleteLater)

        self.worker.processed.connect(self.onAnalysingDone)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)

        self.thread.start()
        self.analyse_b.setEnabled(False)
        self.analyse_b.setText("Processing...")

    def onAnalysingDone(self, embeddings):
        self.embeddings = embeddings
        self.analyse_b.setEnabled(True)
        self.analyse_b.setText("Analyse")
        self.plot()
        print(self.embeddings)

    def plot(self):
        self.graphWidget.clear()
        self.graphWidget.addLegend()
        plotItem = self.graphWidget.getPlotItem()
        en_scatter = pg.ScatterPlotItem(size=20)
        hi_scatter = pg.ScatterPlotItem(size=20)
        n = len(self.embeddings['en'])
        en_spots = [{'pos': self.embeddings['en'][i], 'data': 1, 'brush':pg.intColor(i, n), 'symbol':'o'} for i in range(n)]
        hi_spots = [{'pos': self.embeddings['hi'][i], 'data': 1, 'brush':pg.intColor(i, n), 'symbol':'t'} for i in range(n)]
        en_scatter.addPoints(en_spots, name = "English", symbol = 'o')
        hi_scatter.addPoints(hi_spots, name = "Hindi", symbol = 't')
        plotItem.addItem(en_scatter)
        plotItem.addItem(hi_scatter)