from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
import pyqtgraph as pg
from utils.sentenceWorker import SentenceWorker
from PyQt5.QtCore import QThread
from utils import shared


class SentenceWindow(QMainWindow):
    def __init__(self):
        super(SentenceWindow, self).__init__()
        loadUi("Polyglot/screens/sentence.ui", self)
        self.back_b.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_b.clicked.connect(self.onBack)

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

        self.graphWidget.setBackground("white")
        self.graphWidget.setXRange(-1, 1, padding=0)
        self.graphWidget.setYRange(-1, 1, padding=0)

        font = QtGui.QFont()
        font.setPixelSize(20)

        plot = self.graphWidget.getPlotItem()
        plot.getAxis("bottom").setStyle(tickTextOffset=20, tickFont=font)
        plot.getAxis("left").setStyle(tickTextOffset=20, tickFont=font)
        plot.getAxis("left").setPen(size=20, color="black")
        plot.getAxis("bottom").setPen(size=20, color="black")

        self.embeddings = None
        self.sentences = {}

    def onBack(self):
        this_widget = shared.stack_w.currentWidget()
        shared.stack_w.removeWidget(this_widget)
        this_widget.deleteLater()

    def prepareSentences(self):
        en_text = self.english_edit.toPlainText().splitlines()
        hi_text = self.hindi_edit.toPlainText().splitlines()
        nep_text = self.nepali_edit.toPlainText().splitlines()
        self.sentences["en"] = en_text
        self.sentences["hi"] = hi_text
        self.sentences["nep"] = nep_text

    def analyse(self, model):
        self.thread = QThread()
        self.prepareSentences()

        self.worker = SentenceWorker()
        self.worker.setInputSentences(self.sentences)
        self.worker.setModel(model)
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.thread.finished.connect(self.thread.deleteLater)

        self.worker.processed.connect(self.onAnalysingDone)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)

        self.thread.start()
        self.setAllButtonStatus(False)

    def setAllButtonStatus(self, value):
        self.analyse_b_xlmr.setEnabled(value)
        self.analyse_b_labse.setEnabled(value)
        self.analyse_b_mpnet.setEnabled(value)

    def onAnalysingDone(self, embeddings):
        self.embeddings = embeddings
        self.setAllButtonStatus(True)
        self.plot()

    def plot(self):
        self.graphWidget.clear()
        self.graphWidget.addLegend()
        plotItem = self.graphWidget.getPlotItem()

        n = len(self.embeddings["en"])

        en_scatter = pg.ScatterPlotItem(size=20)
        hi_scatter = pg.ScatterPlotItem(size=20)
        nep_scatter = pg.ScatterPlotItem(size=20)

        en_spots = [
            {
                "pos": self.embeddings["en"][i][0],
                "data": 1,
                "brush": pg.intColor(i, n),
                "symbol": "o",
            }
            for i in range(n)
        ]
        hi_spots = [
            {
                "pos": self.embeddings["hi"][i][0],
                "data": 1,
                "brush": pg.intColor(i, n),
                "symbol": "t",
            }
            for i in range(n)
        ]
        nep_spots = [
            {
                "pos": self.embeddings["nep"][i][0],
                "data": 1,
                "brush": pg.intColor(i, n),
                "symbol": "s",
            }
            for i in range(n)
        ]

        en_scatter.addPoints(en_spots, name="English", symbol="o")
        hi_scatter.addPoints(hi_spots, name="Hindi", symbol="t")
        nep_scatter.addPoints(nep_spots, name="Nepali", symbol="s")

        plotItem.addItem(en_scatter)
        plotItem.addItem(hi_scatter)
        plotItem.addItem(nep_scatter)
