import requests,re
from bs4 import BeautifulSoup
import gensim, logging
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
import numpy as np
import re
import pandas as pd


model = gensim.models.Word2Vec.load("teste_corpus_maior")

vocab = list(model.wv.vocab)
X = model[vocab]


tsne = TSNE(n_components=2)
X_tsne = tsne.fit_transform(X)



df = pd.concat([pd.DataFrame(X_tsne),
                pd.Series(vocab)],
               axis=1)

df.columns = ['x', 'y', 'word']


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.scatter(df['x'], df['y'])


for i, txt in enumerate(df['word']):
    ax.annotate(txt, (df['x'].iloc[i], df['y'].iloc[i]))

plt.show()