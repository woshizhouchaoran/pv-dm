from xlrd import open_workbook
import jieba
import re

xl = open_workbook('/Users/mccat/PycharmProjects/PlaceDatasetCollectionTools/二次过滤模块/CPData1.0000.xls')
# 通过sheet_by_index()获取的sheet没有write()方法
rs = xl.sheet_by_index(0)

txtNames = ["web_doc1.txt","web_doc2.txt","web_doc3.txt","web_doc4.txt","web_doc5.txt"]

# file_handle1 = open(txtNames[0],mode='w')
file_handle2 = open(txtNames[1],mode='w')
file_handle3 = open(txtNames[2],mode='w')
file_handle4 = open(txtNames[3],mode='w')
file_handle5 = open(txtNames[4],mode='w')

def get_tex(file_handle,n,l):
    for i in range(1,n):
        string = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+ ", "",str(rs.cell(i, l).value))
        texts = jieba.cut(string)
        text = [j for j in texts]
        tex = ''
        for t in text:
            tex = tex+' '+t
        file_handle.write(tex+'\n')
    file_handle.close()

get_tex(file_handle2,rs.nrows,2)
get_tex(file_handle3,rs.nrows,4)
get_tex(file_handle4,rs.nrows,5)
get_tex(file_handle5,rs.nrows,6)
# get_tex(file_handle1,rs.nrows,1)