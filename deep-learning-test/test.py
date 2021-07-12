import MeCab
text = '今日の夜ご飯は、メロンパン100個です。'
# import CaboCha
mecab = MeCab.Tagger()
parse = mecab.parse(text)
print(text)
print(parse)
#辞書の位置：mecab-config --dicdir
#cabocha = CaboCha.
#分かち書き
mecab = MeCab.Tagger('-Owakati')
# 振り仮名オプション
mecab = MeCab.Tagger('-Oyomi')
# 茶筌システム
mecab = MeCab.Tagger('-Ochasen')
#新語に対応した辞書を利用する時
mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
#usr/local/lib/mecab/dic
#'-d usr/local/lib/mecab/dic/mecab-ipadic-neologd'
#/usr/local/lib/mecab/dic/mecab-ipadic-neologd
#######################/
#各単語の詳細情報を出力
# par = mecab.parseToNode(text)
# """ 形態素の出力 """
# print(par.surface)
# """ 品詞などの出力 """
# print(par.feature)
# """ 次の単語へ """
# par = par.next

#read file
textFile = r'textfile.txt'
with open(textFile) as F:
    F_text = F.read()
print(F_text)