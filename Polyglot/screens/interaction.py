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
        loadUi("Polyglot/screens/interaction.ui", self)
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
        self.sentences = []

    def onBack(self):
        this_widget = shared.stack_w.currentWidget()
        shared.stack_w.removeWidget(this_widget)
        this_widget.deleteLater()

    def prepareSentences(self):
        en_text = self.english_edit.toPlainText()
        print(en_text)
        self.sentences.append(en_text)
        self.sentences.append(self.hindi_edit.toPlainText())

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
        brushes = [pg.mkBrush(30, 255, 35, 255)]
        en_spots = [{'pos': self.embeddings[0], 'data': 1, 'brush':brushes[0], 'symbol':'o'}]
        hi_spots = [{'pos': self.embeddings[1], 'data': 1, 'brush':brushes[0], 'symbol':'t'}]
        en_scatter.addPoints(en_spots, name = "English", symbol = 'o')
        hi_scatter.addPoints(hi_spots, name = "Hindi", symbol = 't')
        plotItem.addItem(en_scatter)
        plotItem.addItem(hi_scatter)
        # plotItem.autoRange()
        # self.graphWidget.plot(hour, temperature, pen=pen)
        # styles = {'color':'white', 'font-size':'10px', 'padding':'200px'}
        # self.graphWidget.setLabel('left', 'Temperature (°C)', **styles)
        # self.graphWidget.setLabel('bottom', 'Hour (H)', **styles)
        # self.graphWidget.plot(hour, temperature, name = "Sensor 1",  pen = pen, symbol='+', symbolSize=30, symbolBrush=('b'))
        # pen = pg.mkPen(color=(255, 255, 255))
        # self.graphWidget.setTitle("Your Title Here")
        # getting random position
 
        # adding points to the scatter plot
        # self.graphWidget.plot(scatter)
        # add item to plot window
        # adding scatter plot item to the plot window
        # self.graphWidget.setStyleSheet("border: 5px solid white; padding : 5px;")


# from pathlib import Path
# from PyQt5 import QtCore, QtGui
# from PyQt5.QtCore import QUrl
# from PyQt5.QtCore import QThread
# from widgets.analyzeWorker import Worker
# import shared
# import multiprocessing

# class Player(QMainWindow):
#     def __init__(self):
#         super(Player, self).__init__()
#         loadUi("screens/player.ui", self)
#         self.reset()
#         self.back_b.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
#         self.back_b.clicked.connect(self.onBack)
#         self.analyse_b.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
#         self.analyse_b.clicked.connect(self.analyze)

#         # self.fname = None
#         self.onSelectVideoDialog()  # anti pattern but works

#     def reset(self):
#         self.label.setText("Open a video and start analyzing.")
#         self.labels = None
#         try:
#             self.mediaPlayer.positionChanged.disconnect()
#         except:
#             pass

#     def onBack(self):
#         this_widget = shared.stack_w.currentWidget()
#         shared.stack_w.removeWidget(this_widget)
#         this_widget.deleteLater()

#     def onSelectVideoDialog(self):
#         home_dir = str(Path.home())
#         new_fname = QFileDialog.getOpenFileName(self, "Open file", home_dir)
#         if new_fname[0] == "":
#             return

#         self.fname = new_fname
#         self.reset()
#         self.playlist = QMediaPlaylist()
#         self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(self.fname[0])))
#         self.playlist.setCurrentIndex(1)
#         self.playlist.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)

#         self.mediaPlayer.setPlaylist(self.playlist)
#         self.mediaPlayer.play()

#     def analyze(self):
#         self.thread = QThread()
#         self.worker = Worker()
#         self.worker.setFileSource(self.fname[0])
#         self.worker.moveToThread(self.thread)

#         self.thread.started.connect(self.worker.run)
#         self.thread.finished.connect(self.thread.deleteLater)

#         self.worker.processed.connect(self.onAnalyzingDone)
#         self.worker.finished.connect(self.thread.quit)
#         self.worker.finished.connect(self.worker.deleteLater)

#         self.thread.start()
#         self.analyse_b.setEnabled(False)
#         self.label.setText("Processing...")

#     def output(self):
#         self.i = 0
#         self.mediaPlayer.stop()
#         self.mediaPlayer.positionChanged.connect(self.onPositionChanged)
#         self.mediaPlayer.setNotifyInterval(int(1000 / shared.model.frames_per_second))
#         self.mediaPlayer.play()

#     def onPositionChanged(self):
#         self.label.setText(self.labels[self.i])
#         self.i = min(self.i + 1, len(self.labels) - 1)

#     def onAnalyzingDone(self, labelList):
#         self.labels = labelList
#         self.output()
#         self.analyse_b.setEnabled(True)

# def plot(self):
#         self.graphWidget.clear()
#         plotItem = self.graphWidget.getPlotItem()
#         self.graphWidget.setBackground('white')
#         pen = pg.mkPen(color='r')
#         self.graphWidget.setXRange(-1, 1, padding=0)
#         self.graphWidget.setYRange(-1, 1, padding=0)

#         scatter = pg.ScatterPlotItem(size=20)
#         n = 300
#         pos = np.random.normal(size=(2, n), scale=1e-5)
#         spots = [{'pos': pos[:, i], 'data': i}
#                  for i in range(n)] + [{'pos': [0, 0], 'data': 10000}]
        
#         self.graphWidget.addLegend()
#         scatter.addPoints(spots, name = "abcde")

#         plotItem.addItem(scatter)
#         plotItem.autoRange(padding=0)