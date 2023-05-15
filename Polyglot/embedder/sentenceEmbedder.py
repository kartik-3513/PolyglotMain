import numpy as np
from sklearn.decomposition import PCA
from sentence_transformers import SentenceTransformer
import torch

class Sentence:
    emb = None
    pca_emb = None

    def __init__(self, text, lang):
        self.text = text
        self.lang = lang

class SentenceEmbedder:
    def __init__(self):
        pass

    def embed(self, inputSentences, model):

        if torch.cuda.is_available():
            model = SentenceTransformer(model, device = 'cuda')
        else:
            model = SentenceTransformer(model)

        sentences = []

        for lang, sen_list in inputSentences.items():
            for sentence in sen_list:
                sentences.append(Sentence(sentence, lang))

        embedding_space = []
        for sentence in sentences:
            sentence.emb = model.encode(sentence.text)
            embedding_space.append(sentence.emb)

        embedding_space = np.array(embedding_space)
        pca = PCA(n_components=2)
        pca.fit(embedding_space)

        for sentence in sentences:
            sentence.pca_emb = pca.transform(sentence.emb.reshape(1, -1))

        emb_by_lang = {}

        for sentence in sentences:
            lang = sentence.lang
            if lang not in emb_by_lang:
                emb_by_lang[lang] = []
            emb_by_lang[lang].append(sentence.pca_emb)

        return emb_by_lang
