#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import codecs
import nltk
import pprint

# 日本語を標準出力できるように
sys.stdout = codecs.getwriter("utf_8")(sys.stdout)

docs = [
        [u"明日" , u"の" , u"天気" , u"は" , u"晴れ"],
        [u"明日" , u"の" , u"天気" , u"は" , u"曇り"],
        [u"今日" , u"の" , u"天気" , u"は" , u"晴れ"]]


collection = nltk.TextCollection(docs)
uniqTerms = list(set(collection))

for doc in docs:
    for term in uniqTerms:
        print("%s : %f" % (term, collection.tf_idf(term, doc)))
