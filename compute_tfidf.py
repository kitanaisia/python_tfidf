#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append('./python_lib/')
import codecs
import tfidf

if __name__ == '__main__':
# 日本語を標準出力できるように
    sys.stdout = codecs.getwriter("utf_8")(sys.stdout)

    tf_file = u"./text/自然言語処理+OR+キーワード抽出_000.txt"
    directory_path = "./text/"

    tf = tfidf.get_tf(tf_file)
    idf = tfidf.get_idf(directory_path)
    tfidf = tfidf.get_tfidf(tf, idf)

    for k,v in tfidf.items():
        print(k),
        print(v)
