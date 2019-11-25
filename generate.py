import ast
import random
from collections import defaultdict

def get_suffix(dict, prefix1, prefix2):
    tmp_dict = defaultdict(int)
    for k, v in dict.items():
        if k[0] == prefix1 and k[1] == prefix2:
            tmp_dict[k] = v
    if tmp_dict == {}:
        return "。"
    else:
        return random.choice(list(tmp_dict.keys()))[2]

def generate():
    with open("dict.txt") as f:
        dict = f.read()

    # print(type(dict))
    dict = ast.literal_eval(dict)
    # print(type(dict))

    #始まりと終わり辞書作成
    begin_dict = defaultdict(int)
    end_dict = defaultdict(int)
    for k, v in dict.items():
        if k[0] == "begin":
            begin_dict[k] = v
        elif k[2] == "end":
            end_dict[k] = v
    # print(begin_dict, end_dict)

    #ランダムで最初の単語取り出し
    begin = random.choice(list(begin_dict.keys()))
    # print(begin)

    morphems = []
    morphems.append(begin[1])
    morphems.append(begin[2])

    while True:
        prefix1 = morphems[-2]
        prefix2 = morphems[-1]
        suffix = get_suffix(dict, prefix1, prefix2)
        morphems.append(suffix)
        # print(morphems)
        # print(morphems[-1])
        if morphems[-1] == 'end' or morphems[-1] == '。':
            break

    result = "".join(morphems[:-1])

    return result




    # print(sentence)

if __name__ == "__main__":
    generate()
