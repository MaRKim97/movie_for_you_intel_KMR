# TFIDF: Text Frequency(한 문장 안에서 특정 단어가 몇번 등장하느냐) I Document Frequency(한 문서 안에 특정 단어가 몇개의 문장에 등장하느냐)
# 가중치 계산법: TF * (1/DF)

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.io import mmwrite, mmread
import pickle

df_reviews = pd.read_csv('./cleaned_one_review.csv')
df_reviews.info()

Tfidf = TfidfVectorizer(sublinear_tf=True)
Tfidf_matrix = Tfidf.fit_transform(df_reviews['reviews'])
print(Tfidf_matrix.shape)

with open('./models/tfidf.pickle', 'wb') as f:
    pickle.dump(Tfidf, f)

mmwrite('./models/Tfidf_movie_review.mtx', Tfidf_matrix)
# cos 값을 통해서 상관도를 예측할 수 있다(-1: 상반, 0: 상관없음, 1: 상관)