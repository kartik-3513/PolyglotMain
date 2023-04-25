from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import numpy as np
from pyqtgraph import PlotWidget
import pyqtgraph as pg
from embedder.documentEmbedder import DocumentEmbedder
from utils.documentWorker import DocumentWorker
from PyQt5.QtCore import QThread
from utils import shared


class UploadWindow(QMainWindow):
    def __init__(self):
        super(UploadWindow, self).__init__()
        loadUi("Polyglot/screens/upload.ui", self)
        self.back_b.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_b.clicked.connect(self.onBack)

        self.graphWidget.setXRange(-1, 1, padding=0)
        self.graphWidget.setYRange(-1, 1, padding=0)
        self.graphWidget.setBackground("white")

        font = QtGui.QFont()
        font.setPixelSize(20)

        plot = self.graphWidget.getPlotItem()
        plot.getAxis("bottom").setStyle(tickTextOffset=20, tickFont=font)
        plot.getAxis("left").setStyle(tickTextOffset=20, tickFont=font)
        plot.getAxis("left").setPen(size=20, color="black")
        plot.getAxis("bottom").setPen(size=20, color="black")

        self.upload_b.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.upload_b.clicked.connect(self.onUploadButtonClick)
        self.analyse_b_xlmr.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.analyse_b_xlmr.clicked.connect(
            lambda: self.analyse(
                "sentence-transformers/paraphrase-xlm-r-multilingual-v1"
            )
        )
        self.analyse_b_labse.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.analyse_b_labse.clicked.connect(lambda: self.analyse("LaBSE"))
        self.analyse_b_mpnet.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.analyse_b_mpnet.clicked.connect(
            lambda: self.analyse(
                "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"
            )
        )

        self.score_table.setColumnCount(3)
        header = self.score_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        self.score_table.setHorizontalHeaderLabels(
            ["Clustering Method", "Mutual Info.", "Rand Index"]
        )
        self.score_table.setRowCount(4)

    def reset(self):
        self.embeddings = None
        self.score = None
        self.path = None
        self.setAllButtonStatus(True)
        self.score_table.setRowCount(0)

    def updateTable(self):
        self.score_table.setRowCount(4)
        row = 0
        for key, value in self.scores.items():
            self.score_table.setItem(row, 0, QTableWidgetItem(key))
            self.score_table.setItem(row, 1, QTableWidgetItem(str(value[0])))
            self.score_table.setItem(row, 2, QTableWidgetItem(str(value[1])))
            row += 1
        self.score_table.show()

    def onBack(self):
        this_widget = shared.stack_w.currentWidget()
        shared.stack_w.removeWidget(this_widget)
        this_widget.deleteLater()

    def onUploadButtonClick(self):
        self.reset()
        self.path = QFileDialog.getExistingDirectory(self, "Select Folder") + "/"
        self.path_l.setText(self.path)

    def analyse(self, model):
        self.thread = QThread()
        self.worker = DocumentWorker()
        self.worker.setPath(self.path)
        self.worker.setModel(model)
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.thread.finished.connect(self.thread.deleteLater)

        self.worker.processed.connect(self.onAnalysingDone)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)

        self.thread.start()
        self.setAllButtonStatus(False)
        # self.analyse_b.setText("Processing...")

    def onAnalysingDone(self, result):
        self.embeddings = result["embeddings"]
        self.scores = result["scores"]
        self.setAllButtonStatus(True)
        # self.analyse_b.setText("Analyse")
        self.updateTable()
        self.plot()

    def setAllButtonStatus(self, value):
        self.analyse_b_xlmr.setEnabled(value)
        self.analyse_b_labse.setEnabled(value)
        self.analyse_b_mpnet.setEnabled(value)

    def plot(self):
        self.graphWidget.clear()
        self.graphWidget.addLegend()
        plotItem = self.graphWidget.getPlotItem()
        # add description for each point in the scatter plot to the legend item

        i = 0
        n_of_categ = len(self.embeddings.items())
        symbols = ["o", "s", "t", "d", "+"]
        for key, val in self.embeddings.items():
            color = pg.intColor(i, n_of_categ)
            scatter = pg.ScatterPlotItem(size=15)
            n = len(val)
            spots = [
                {
                    "pos": val[j][0],
                    "data": 1,
                    "pen": color,
                    "brush": color,
                }
                for j in range(n)
            ]
            scatter.addPoints(spots, name=key, symbol=symbols[i])
            plotItem.addItem(scatter)
            i += 1
        return

        # en_scatter = pg.ScatterPlotItem(size=20)
        # hi_scatter = pg.ScatterPlotItem(size=20)
        # n = len(self.embeddings['en'])
        # en_spots = [{'pos': self.embeddings['en'][i], 'data': 1, 'brush':pg.intColor(i, n), 'symbol':'o'} for i in range(n)]
        # hi_spots = [{'pos': self.embeddings['hi'][i], 'data': 1, 'brush':pg.intColor(i, n), 'symbol':'t'} for i in range(n)]
        # en_scatter.addPoints(en_spots, name = "English", symbol = 'o')
        # hi_scatter.addPoints(hi_spots, name = "Hindi", symbol = 't')
        # plotItem.addItem(en_scatter)
        # plotItem.addItem(hi_scatter)
