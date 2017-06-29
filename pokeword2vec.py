import requests,re
from bs4 import BeautifulSoup
# import modules & set up logging
import gensim, logging
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.datasets import fetch_20newsgroups

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def clean(text):
    """Remove posting header, split by sentences and words, keep only letters"""
    lines = re.split('[?!.:]\s', re.sub('^.*Lines: \d+', '', re.sub('\n', ' ', text)))
    return [re.sub('[^a-zA-Z]', ' ', line).lower().split() for line in lines]



import os

corpus = []

for filename in os.listdir('pokeCorpus'):

    with open('pokeCorpus/' + filename, "r") as text_file:

      corpus = corpus + clean(text_file.read())

     

model = gensim.models.Word2Vec(corpus,size=100, window=5, min_count=5, workers=4)  # default value is 5
model.save("teste_corpus_maior")
