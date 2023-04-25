from PyQt5.QtCore import QObject, pyqtSignal
from embedder import document_embedder_object

class DocumentWorker(QObject):    
    processed = pyqtSignal(dict)
    finished = pyqtSignal()
    
    def setPath(self, path):
        self.path = path
    
    def setModel(self, model):
        self.model = model

    def run(self):
        """Long-running task."""
        res = document_embedder_object.embed(self.path, self.model)
        self.processed.emit(res)
        self.finished.emit()