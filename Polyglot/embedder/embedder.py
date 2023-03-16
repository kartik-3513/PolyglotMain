from laserembeddings import Laser
import pickle as pk

class Embedder:
    def __init__(self, pca_1_file, pca_2_file):
        self.laser = Laser()
        self.pca_1 = pk.load(open(pca_1_file,'rb'))
        self.pca_2 = pk.load(open(pca_2_file,'rb'))
    
    def embed(self, sentences):
        sen_1, sen_2 = sentences[0], sentences[1]
        embedding_1 = self.laser.embed_sentences([sen_1], lang=['en'])
        embedding_2 = self.laser.embed_sentences([sen_2], lang=['hi'])
        point_1 = self.pca_1.transform(embedding_1).squeeze()
        point_2 = self.pca_2.transform(embedding_2).squeeze()
        return [point_1, point_2]