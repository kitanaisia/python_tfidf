#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import codecs
import mecabutil
import vital

# 日本語を標準出力できるように
sys.stdout = codecs.getwriter("utf_8")(sys.stdout)
    

def get_tf(nouns):
    tf = {}

    for key in set(nouns):
        tf[key] = nouns.count(key) 

    return tf

if __name__ == '__main__':
    # 読み込むファイル指定
    file_path = "./hoge.txt"

    # ファイル読み込み
    contents = vital.file_read(file_path)

    # 形態素解析し，結果をWordクラスの配列に格納
    words = mecabutil.get_words(contents)
    
    # 形態素解析結果から，名詞の単語の表層のみを抽出
    nouns = [word.surface for word in words if word.pos == u"名詞"]
    
    # TFの計算
    tf = get_tf(nouns)
