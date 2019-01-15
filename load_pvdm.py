# -*- coding:utf-8 -*-
from gensim.models.doc2vec import  Doc2Vec
import gensim
import smart_open
from gensim.models.doc2vec import TaggedDocument, Doc2Vec

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
model_loaded = Doc2Vec.load('web_1.doc2vec')


sims = model_loaded.most_similar(positive=["长春"], topn=10)
for s in sims:
    print(s[0])

doc_id = 36
inferred_vector = model_loaded.infer_vector(['【', '长春', '巢谷', '商旅', '酒店', '团购', '】', '长春', '巢谷', '商旅', '酒店', '百度', '糯米'])
# inferred_vector = model_loaded.infer_vector(train_data[doc_id].words)
sims = model_loaded.docvecs.most_similar([inferred_vector], topn=len(model_loaded.docvecs))

print('Document ({}): «{}»\n'.format(doc_id, ' '.join(train_data[doc_id].words)))
print(u'SIMILAR/DISSIMILAR DOCS PER MODEL %s:\n' % model_loaded)
for label, index in [('MOST', 0), ("SECOND", 1), ('MEDIAN', len(sims) // 2), ('LEAST', len(sims) - 1)]:
    print(sims[index][1])
    print(u'%s %s: «%s»\n' % (label, sims[index], ' '.join(train_data[sims[index][0]].words)))
# # print model.docvecs[[299]]