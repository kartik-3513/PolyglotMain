from PyQt5.QtCore import QObject, pyqtSignal
from embedder import sentence_embedder_object

class SentenceWorker(QObject):    
    processed = pyqtSignal(dict)
    finished = pyqtSignal()
    
    def setInputSentences(self, sentences):
        self.sentences = sentences

    def setModel(self, model):
        self.model = model

    def run(self):
        """Long-running task."""
        res = sentence_embedder_object.embed(self.sentences, self.model)
        self.processed.emit(res)
        self.finished.emit()