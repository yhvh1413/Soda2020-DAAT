#coding=utf-8
import re
import string
import csv
import jieba
import jieba.analyse
import jieba.posseg
from collections import Counter


def dosegment_all(sentence):
    """
    带词性标注，对句子进行分词，不排除停词等
    :param sentence:输入字符
    :return:
    """
    sentenceeged = jieba.posseg.cut(sentence.strip())
    outstr = ""
    for x in sentenceeged:
        outstr += "{}/{},".format(x.word, x.flag)
    # outstr = ",".join([("%s/%s" %(x.word,x.flag)) for x in sentenceeged])
    print(outstr)

def jieba_analysis(sent):
    str_quan1 = jieba.cut(sent, cut_all=True)
    print("全模式分词：{ %d}" % len(list(str_quan1)))
    str_quan2 = jieba.cut(sent, cut_all=True)
    print("/".join(str_quan2))
    # print(str(str_1))  
    # str_1_len=len(list(str_1))

    str_jing1 = jieba.cut(sent, cut_all=False)
    print("精准模式分词：{ %d}" % len(list(str_jing1)))
    str_jing2 = jieba.cut(sent, cut_all=False)
    print("/".join(str_jing2))

    str_soso1 = jieba.cut_for_search(sent)
    print('搜索引擎分词：{ %d}' % len(list(str_soso1)))
    str_soso2 = jieba.cut_for_search(sent)
    print("/".join(str_soso2))

def jieba_count(sent):
    text = sent
    item = text.strip("\n\r").split("\t")
    tags = jieba.analyse.extract_tags(item[0])

    word_lst = []
    for t in tags:
        word_lst.append(t)

    word_dict = {}
    for item in word_lst:
        if item not in word_dict:
            word_dict[item] = 1
        else:
            word_dict[item] += 1
    print(word_dict)

def count_words(sent):
    # 统计单词出现的次数
    count = Counter(sent)
    print(count)

def jb(word):
    s = word
    sentence = re.sub("[%s]" % re.escape(
        string.punctuation), "", s).replace(" ", "")
    jieba_analysis(sentence)
    count_words(sentence)
    jieba_count(sentence)
    dosegment_all(sentence)

def removePunctuation(text):
    text = re.sub(r"[{}]+".format(punctuation), "", text)
    return text.strip().lower()

def word_cut(sent, num): 
    index = 0
    while index < len(sent):
        if index+num <= len(sent):
            letter = sent[index:index+num]
            index += 1
            # print(letter)
            for value in dict_all:
                if letter == value["name"]:
                    new.append(value.copy())
        else:
            break


word_dict = "/Users/Soda复赛daat//data/nlp_v.sql"

print('请输入你的标签和词语')
words = input("你现在想说: ")
punctuation = "!,;:?\‘。，/"
explain = removePunctuation(words)  

new = [] 
results = [] 

fr = open(word_dict, "r")
dict_all = eval(fr.read())
fr.close()

s = explain 
sentence = re.sub("[%s]" % re.escape(
    string.punctuation), "", s).replace(" ", "")

word_cut(sentence, 1)
word_cut(sentence, 2)
word_cut(sentence, 3)
word_cut(sentence, 4)
word_cut(sentence, 5)

n = sum(item["n"] for item in new)
p = sum(item["p"] for item in new)
nu1 = sum(item["nu1"] for item in new)
nu2 = sum(item["nu2"] for item in new)
nu3 = sum(item["nu3"] for item in new)
nu4 = sum(item["nu4"] for item in new)
nu5 = sum(item["nu5"] for item in new)
nu6 = sum(item["nu6"] for item in new)
f = sum(item["f"] for item in new)
m = sum(item["m"] for item in new)

new = [n, p, nu1, nu2, nu3, nu4, nu5, nu6, f, m]  # 把数值导入新csv文件
new1 = [nu1, nu2, nu3, nu4, nu5, nu6]
# print("\t%s\t%d\t%d\n\t\t%d\t%d\t%d\t%d\t%d\t%d\n\t\t%d\t%d" %
#     ("sent:", n, p,  nu1, nu2, nu3, nu4, nu5, nu6, f, m))

# jb(words)
