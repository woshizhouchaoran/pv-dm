from gensim.models.doc2vec import  Doc2Vec
import jieba
import re

model = Doc2Vec.load('web_1.doc2vec')
string = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+ ", "",'【长春巢谷商旅酒店团购】长春巢谷商旅酒店百度糯米')
cut = jieba.cut(string)

list = [i for i in cut]

print(list)

sims = model.docvecs.most_similar([model.infer_vector(list)], topn=10)
for s in sims:
    print(s[0])
model.infer_vector(list)
# print(model.infer_vector(list))
#寻找与某个文档最相似的文档
print(model.docvecs.most_similar(3328))
print(model.docvecs.similarity(3326,3327))