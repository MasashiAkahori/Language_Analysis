from pyknp import Jumanpp, KNP


def morphological_Analysis(text):
    #構文解析
    t = Jumanpp()
    text = text
    print("入力文 {}".format(text))
    print("//////////////////////////")
    for mrph in t.analysis(text).mrph_list(): # 各形態素にアクセス
        print("見出し:%s, 読み:%s, 原形:%s, 品詞:%s, 品詞細分類:%s, 活用型:%s, 活用形:%s, 意味情報:%s, 代表表記:%s" \
            % (mrph.midasi, mrph.yomi, mrph.genkei, mrph.hinsi, mrph.bunrui, mrph.katuyou1, mrph.katuyou2, mrph.imis, mrph.repname))
        print("/////////////////////////")

def phrase_Analysis(text):
    text = text
    knp = KNP()
    result = knp.parse(line)
    print("文節")
    for bnst in result.bnst_list(): # 各文節へのアクセス
        print("\tID:%d, 見出し:%s, 係り受けタイプ:%s, 親文節ID:%d, 素性:%s" \
                % (bnst.bnst_id, "".join(mrph.midasi for mrph in bnst.mrph_list()), bnst.dpndtype, bnst.parent_id, bnst.fstring))
        print("/////////////////////////")

def select_normalization_representative_notation(fstring):
    """ 正規化代表表記を抽出します
    """
    
    begin = fstring.find('正規化代表表記:')
    end = fstring.find('/', begin + 1)
    return fstring[begin + len('正規化代表表記:') : end]

def select_dependency_structure(line):
    """係り受け構造を抽出します
    """
    # KNP
    knp = KNP(option = '-tab -anaphora')
    # 解析
    result = knp.parse(line)
    # 文節リスト
    bnst_list = result.bnst_list()
    # 文節リストをidによるディクショナリ化する
    bnst_dic = dict((x.bnst_id, x) for x in bnst_list)
    tuples = []
    for bnst in bnst_list:
        if bnst.parent_id != -1:
            # (from, to)
            tuples.append((select_normalization_representative_notation(bnst.fstring), select_normalization_representative_notation(bnst_dic[bnst.parent_id].fstring)))

    return tuples

def n_best(text):
    b = Jumanpp(option= '-s 3')
    mlist = b.analysis(text)
    for mrph in mlist.mrph_list():
        print(mrph.midasi)


if __name__ == '__main__' :
    line = '今日の夜ご飯は、メロンパン100個です。'
    print('/////////形態素解析/////////////////')
    morphological_Analysis(line)
    # parsing(line)
    
    
    print('/////////構文解析(係受け構造の抽出)/////////////////')

    tuples = select_dependency_structure(line)
    for t in tuples:
        print(t[0] + ' --係受け(関係)-> ' + t[1])


    print('/////////文節分け/////////////////')
    phrase_Analysis(line)
    print('////////////N-Bestを求める')
    n_best(line)
