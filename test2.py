#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import codecs
import nkf
import MeCab
import re
import nltk

# Wordクラス定義
class Word:
    # コンストラクタ
    def __init__(self, surface = None, pos = None, pos_detail1 = None, pos_detail2 = None, pos_detail3 = None):
        self.set_field(surface, pos, pos_detail1, pos_detail2, pos_detail3)       
        
    # セッター
    def set_field(self, surface, pos, pos_detail1, pos_detail2, pos_detail3):
        self.surface = surface
        self.pos = pos
        self.pos_detail1 = pos_detail1
        self.pos_detail2 = pos_detail2
        self.pos_detail3 = pos_detail3

    # ゲッター
    def get_surface(self):
        return self.surface

    def get_pos(self):
        return self.pos

    def get_pos_detail1(self):
        return self.pos_detail1

    def get_pos_detail2(self):
        return self.pos_detail2

    def get_pos_detail3(self):
        return self.pos_detail3

# Wordクラスの情報出力関数
def print_word(word):
    print(word.get_surface())
    print(word.get_pos())
    print(word.get_pos_detail1())
    print(word.get_pos_detail2())
    print(word.get_pos_detail3())

# 日本語を標準出力できるように
sys.stdout = codecs.getwriter("utf_8")(sys.stdout)

contents = open("./hoge.txt").read()
contents = nkf.nkf("-w -d", contents)

# 形態素解析する
# 注意：MeCab解析する文字列は必ずencodeされていること．
#       結果は，decodeして使用すること．
# 参考:http://shogo82148.github.io/blog/2012/12/15/mecab-python/
result = MeCab.Tagger("")\
        .parse(contents)\
        .decode("utf-8")

# 形態素に分解して，word_arrに突っ込む
lines = result.split("\n")
pattern = r"^(.*?)\t(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?)$"
doc_arr = []
for line in lines:
    word_arr = []
    iterator = re.finditer(pattern, line)
    for match in iterator:
        surface = match.group(1)
        word_arr.append(surface)
        doc_arr.append(word_arr)

collection = nltk.TextCollection(doc_arr)
uniqTerms = list(set(collection))

for doc in doc_arr:
    for term in uniqTerms:
        print("%s : %f" % (term, collection.tf_idf(term, doc)))
