import gensim.models

cn_model = gensim.models.KeyedVectors.load_word2vec_format('/Users/mccat/PycharmProjects/自然语言处理/Chinese-Word-Vectors-master/sgns.zhihu.bigram',binary=False)
gensim.models.doc2vec.TaggedLineDocument('/Users/mccat/PycharmProjects/Text-Model/PVDM/1')
with open('/Users/mccat/PycharmProjects/Text-Model/PVDM/1','r') as infile:
    doc = infile.readlines()
# model = gensim.models.Doc2Vec(doc,dm=0,alpha=0.1,size=20,min_alpha=0.025)

