import numpy as np
from indicnlp.tokenize import sentence_tokenize
import os
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, BisectingKMeans, AgglomerativeClustering, SpectralClustering, DBSCAN
from sklearn.metrics.cluster import adjusted_mutual_info_score, adjusted_rand_score
from sentence_transformers import SentenceTransformer

langs = ["English/", "Nepali/", "Hindi/"]

class Article:
    emb = None
    pca_emb = None

    def __init__(self, text, lang, cat, fname):
        self.text = text
        self.lang = lang
        self.cat = cat
        self.fname = fname

    def sen_split(self):
        self.text = sentence_tokenize.sentence_split(self.text, lang=self.lang)


class DocumentEmbedder:
    def __init__(self):
        pass
    
    def embed(self, path, model):
        articles = []

        for lang in langs:
            categories = [f for f in os.listdir(path + lang) if os.path.isdir(os.path.join(path + lang, f))]
            for category in categories:
                for filename in os.listdir(path + lang + category):
                    if filename[:-4] != "metadata":
                        with open(os.path.join(path + lang + category, filename), 'r', encoding="utf8") as file:
                            articles.append(Article(file.read(), lang[:3].lower(), category.lower(), filename.lower()))

        model = SentenceTransformer(model, device = 'cuda')
        # model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-mpnet-base-v2', device='cuda')
        # model = SentenceTransformer('LaBSE', device='cuda')
        # model = SentenceTransformer('sentence-transformers/paraphrase-xlm-r-multilingual-v1', device='cuda')

        for article in articles:
            article.sen_split()
            article.emb = np.mean(model.encode(article.text), axis=0)

        embedding_space = []

        for article in articles:
            embedding_space.append(article.emb)

        embedding_space = np.array(embedding_space)
        pca = PCA(n_components=2)
        pca.fit(embedding_space)
        for article in articles:
            article.pca_emb = pca.transform(article.emb.reshape(1, -1))

        emb_by_cat = {}

        for article in articles:
            category = article.cat
            if category not in emb_by_cat:
                emb_by_cat[category] = []
            emb_by_cat[category].append(article.pca_emb)


        scores = {}
        real = []
        cats = {"entertainment": 0,
                "sports": 1,
                "politics": 2,
                "crime": 3,
                "economics": 4}
        for a in articles:
            real.append(cats[a.cat])
        real = np.array(real)

        kmeans = KMeans(n_clusters=5)
        labels = kmeans.fit_predict(embedding_space)

        scores['KMeans'] = [adjusted_mutual_info_score(list(labels), list(real)), 
                                adjusted_rand_score(list(labels), list(real))]

        bisect_means = BisectingKMeans(n_clusters=5)
        labels = bisect_means.fit_predict(embedding_space)
        scores['BisectingKMeans'] = [adjusted_mutual_info_score(list(labels), list(real)), 
                                adjusted_rand_score(list(labels), list(real))]

        agg = AgglomerativeClustering(n_clusters=5)
        labels = agg.fit_predict(embedding_space)
        scores['Agglomerative'] = [adjusted_mutual_info_score(list(labels), list(real)), 
                                adjusted_rand_score(list(labels), list(real))]

        spec = SpectralClustering(n_clusters=5)
        labels = spec.fit_predict(embedding_space)
        scores['Spectral'] = [adjusted_mutual_info_score(list(labels), list(real)), 
                                adjusted_rand_score(list(labels), list(real))]

        for key, val in scores.items():
            for i in range(len(val)):
                scores[key][i] = round(scores[key][i], 3)

        return {'embeddings':emb_by_cat, "scores":scores}
