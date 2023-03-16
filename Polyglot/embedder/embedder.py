from laserembeddings import Laser
import pickle as pk

class Embedder:
    def __init__(self, pca_1_file, pca_2_file):
        self.laser = Laser()
        self.pca_1 = pk.load(open(pca_1_file,'rb'))
        self.pca_2 = pk.load(open(pca_2_file,'rb'))
    
    def embed(self, sentences):
        print(sentences)
        # en_embs, hi_embs = [], []
        en_emb = self.laser.embed_sentences(sentences['en'], lang='en')
        hi_emb = self.laser.embed_sentences(sentences['hi'], lang='hi')
        # for i in range(len(sentences['en'])):
            # en_embs.append(en_emb)
            # hi_embs.append(hi_emb)
        # print(len(en_embs), len(en_embs[0]))
        en_points = self.pca_1.transform(en_emb).squeeze()
        hi_points = self.pca_2.transform(hi_emb).squeeze()
        return {'en':en_points, 'hi':hi_points}