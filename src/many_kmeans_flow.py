from metaflow import FlowSpec, step 
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

class ManyKmeansFlow(FlowSpec):

    @step
    def start(self):
        """Membaca data dan preprocessing."""
        self.data = pd.read_csv('D:/IPSD/WhatsApp-Group-Analysis-with-Clustering/data/clean_data_group.txt', names=['text'])
        self.next(self.vectorize)

    @step
    def vectorize(self):
        """Mengubah teks menjadi vektor menggunakan TF-IDF."""
        vectorizer = TfidfVectorizer(max_features=100)
        self.vectors = vectorizer.fit_transform(self.data['text']).toarray()
        self.features = vectorizer.get_feature_names_out()
        self.next(self.kmeans_3, self.kmeans_4, self.kmeans_5)

    @step
    def kmeans_3(self):
        """Clustering dengan 3 cluster."""
        self.kmeans = KMeans(n_clusters=3, random_state=42).fit(self.vectors)
        self.clusters = self.get_top_words(self.kmeans)
        self.next(self.join)

    @step
    def kmeans_4(self):
        """Clustering dengan 4 cluster."""
        self.kmeans = KMeans(n_clusters=4, random_state=42).fit(self.vectors)
        self.clusters = self.get_top_words(self.kmeans)
        self.next(self.join)

    @step
    def kmeans_5(self):
        """Clustering dengan 5 cluster."""
        self.kmeans = KMeans(n_clusters=5, random_state=42).fit(self.vectors)
        self.clusters = self.get_top_words(self.kmeans)
        self.next(self.join)

    def get_top_words(self, model):
        """Mengambil 3 kata teratas untuk setiap cluster."""
        top_words = []
        for i in range(model.n_clusters):
            cluster_center = model.cluster_centers_[i]
            top_indices = cluster_center.argsort()[-3:][::-1]
            top_words.append([self.features[idx] for idx in top_indices])
        return top_words

    @step
    def join(self, inputs):
        """Menggabungkan hasil."""
        self.results = {
            "k3": inputs.kmeans_3.clusters,
            "k4": inputs.kmeans_4.clusters,
            "k5": inputs.kmeans_5.clusters,
        }
        self.next(self.end)

    @step
    def end(self):
        """Akhir alur."""
        print("Clustering selesai.")
        print("Hasil:", self.results)
