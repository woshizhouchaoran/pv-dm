# -*- coding:utf-8 -*-

import gensim
import smart_open
from gensim.models.doc2vec import TaggedDocument, Doc2Vec

import random
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')


data_set = "web_doc1.txt"

def read_corpus(fname, tokens_only=False):
    with smart_open.smart_open(fname, encoding="utf-8") as f:
        for i, line in enumerate(f):
            if tokens_only:
                yield gensim.utils.simple_preprocess(line)
            else:
                text = line.split()
                yield TaggedDocument(text[:], [i])


train_data = list(read_corpus(data_set))
# random.shuffle(train_data)
print(len(train_data))
# model = Doc2Vec(documents, vector_size=5, window=2, min_count=1, workers=4)
model = Doc2Vec(train_data,vector_size=100, window=2, min_count=1, workers=4)
# model.build_vocab(train_data)
# # #
# model.train(train_data, total_examples=model.corpus_count, epochs=1000)
# #
# # # store the model to mmap-able files
model.save('web_1.doc2vec')
# load the model back
