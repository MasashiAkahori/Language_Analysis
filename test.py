#-*- encoding: utf-8 -*-
from pyknp import Jumanpp
from pyknp import KNP
# import ginza
import spacy
from spacy import displacy
import sys
import codecs
# sys.stdin = codecs.getreader('utf_8')(sys.stdin)
# sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
# JUMAN++をsubprocessモードで使用
text = "下鴨神社の参道は暗かった。"
jumanpp = Jumanpp()
result = jumanpp.analysis(text)
for mrph in result.mrph_list():
    print("\tID:%d, 見出し:%s, 読み:%s, 原形:%s, 品詞:%s, 品詞細分類:%s, 活用型:%s, 活用形:%s, 意味情報:%s, 代表表記:%s" \
            % (mrph.mrph_id, mrph.midasi, mrph.yomi, mrph.genkei, mrph.hinsi, mrph.bunrui, mrph.katuyou1, mrph.katuyou2, mrph.imis, mrph.repname))


nlp = spacy.load('ja_ginza')
doc = nlp('銀座でランチをご一緒しましょう。')

# 単語間の係り受け解析
for sent in doc.sents:
    for token in sent:
        print(token.text+' ← '+token.head.text+', '+token.dep_)

# グラフ表示
displacy.render(doc, style='dep', jupyter=True, options={'compact':True, 'distance': 90})