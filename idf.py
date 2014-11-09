#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import codecs
import vital
import math
import mecabutil

# 日本語を標準出力できるように
sys.stdout = codecs.getwriter("utf_8")(sys.stdout)

def get_idf(directory_path):
    files = vital.get_abs_path(directory_path)   

    df = {}
    idf = {}
    df_default = 0

    for file in files:
        contents = vital.file_read(file)

        # 形態素解析し，結果をWordクラスの配列に格納
        words = mecabutil.get_words(contents)
        
        # 形態素解析結果から，名詞の単語の表層のみを抽出
        nouns = [word.surface for word in words if word.pos == u"名詞"]

        # 文書中の名詞を集合(重複なしの要素の集まり)とし，存在する名詞のdf値をインクリメント
        for key in set(nouns):
            df[key] = df.get(key, df_default) + 1

        for k,v in df.items():
            idf[k] = math.log10( 1.0 + (len(files) / v) )


    return idf

if __name__ == '__main__':
    directory_path = "/home/sia/Develop/WebRetrieve/output/"

    idf = get_idf(directory_path)
    for k,v in idf.items():
        print(k),
        print(v)
