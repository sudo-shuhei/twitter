# from PrepareChain import *
# from PrepareChain import *
import pandas as pd
from tqdm import tqdm
import sys
from collections import defaultdict
from janome.tokenizer import Tokenizer

def make_triplet_freqs(text, triplet_freqs):
    u"""
    形態素解析から3つ組の出現回数まで
    @return 3つ組とその出現回数の辞書 key: 3つ組（タプル） val: 出現回数
    """
    sentences = text
    # print(sentences)

    # 形態素解析
    morphemes = _morphological_analysis(sentences)
    # 3つ組をつくる
    triplets = _make_triplet(morphemes)
    # 出現回数を加算
    for (triplet, n) in triplets.items():
        triplet_freqs[triplet] += n

    return triplet_freqs

def _morphological_analysis(sentence):
    u"""
    一文を形態素解析する
    @param sentence 一文
    @return 形態素で分割された配列
    """
    morphemes = []
    t = Tokenizer()
    node = t.tokenize(sentence)
    result = []
    for token in t.tokenize(sentence):
        # print(token.surface)
        result.append(token.surface)
    return result

def _make_triplet(morphemes):
    u"""
    形態素解析で分割された配列を、形態素毎に3つ組にしてその出現回数を数える
    @param morphemes 形態素配列
    @return 3つ組とその出現回数の辞書 key: 3つ組（タプル） val: 出現回数
    """
    # print(morphemes)
    # 3つ組をつくれない場合は終える
    if len(morphemes) < 3:
        return {}

    # 出現回数の辞書
    triplet_freqs = defaultdict(int)

    # 繰り返し
    for i in range(len(morphemes)-2):
        # print(morphemes[i])
        triplet = tuple(morphemes[i:i+3])
        triplet_freqs[triplet] += 1

        #beginを追加
        triplet = ("begin", morphemes[0], morphemes[1])
        triplet_freqs[triplet] = 1

        #endを追加
        triplet = (morphemes[-2], morphemes[-1], "end")
        triplet_freqs[triplet] = 1

    return triplet_freqs


def storeTweetstoDB():

    if len(sys.argv) > 2:
        df = pd.read_csv(sys.argv[1])
    else:
        csvfilepath = 'processedtweets.csv'
        df = pd.read_csv(csvfilepath)


    tweets = df['text']

    # print(len(tweets))
    triplet_freqs = defaultdict(int)

    for i in tqdm(range(len(tweets))):
        triplet_freqs = make_triplet_freqs(tweets[i],triplet_freqs)

    print(triplet_freqs)

    with open("dict.txt", mode = "w") as f:
        f.write(str(triplet_freqs))


if __name__ == '__main__':
    storeTweetstoDB()
