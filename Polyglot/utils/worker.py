from PyQt5.QtCore import QObject, pyqtSignal
from embedder import embedder_object
class Worker(QObject):
    
    processed = pyqtSignal(list)
    finished = pyqtSignal()
    
    def setInputSentences(self, sentences):
        self.sentences = sentences

    def run(self):
        """Long-running task."""
        res = embedder_object.embed(self.sentences)
        self.processed.emit(res)
        self.finished.emit()