# vector: 여기서는 의미공간 상의 좌표(의미공간->공간을 이루는 축들이 하나하나 의미를 갖고 있다)
# 비슷한 의미를 가진 단어(유의어를 말하는 것이 아닌 학습시키는 데이터 내에서의 의미를 말한다)들은 비슷한 위치를 가진다
import pandas as pd
from gensim.models import Word2Vec

df_review = pd.read_csv('./cleaned_one_review.csv')
df_review.info()

reviews = list(df_review['reviews'])
print(reviews[0])

tokens = []
for sentence in reviews:
    token = sentence.split()
    tokens.append(token)
print(tokens[0])

embedding_model = Word2Vec(tokens, vector_size=100, window=4, min_count=20, workers=4, epochs=100, sg=1)
# vector_size: 차원의 수를 줄인다(학습을 용이하게 하기 위해), window: kernel_size와 같은 역할
# min_count:최소출현빈도, 이 수를 넘겨야 학습에 포함시키겠다, workers:학습 시 cpu 어느정도 쓸지
embedding_model.save('./models/word2vec_movie_review.model')
print(list(embedding_model.wv.index_to_key))
print(len(embedding_model.wv.index_to_key))
