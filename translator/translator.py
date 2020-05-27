#仮想環境(venv)#
# https://qiita.com/fiftystorm36/items/b2fd47cf32c7694adc2e

#ファイル読み込みでCP932(Shift-JIS)はでコードできないとか怒られたときに見よう。#
# https://qiita.com/Yuu94/items/9ffdfcb2c26d6b33792e

#Google翻訳API#
# https://codechacha.com/ja/python-google-translate/

#JSONDecodeErrorが出たときはこれ見て#
# https://teratail.com/questions/185818
# 値とは、数値型、文字列型、真偽型、配列、オブジェクト(Pythonでは辞書)、nullのいずれか

#import#
from googletrans import Translator
trs = Translator()

#dict.txt#
# fileを開く
open_file = open('dict.txt', 'r', encoding="utf-8_sig")
# dataを読み込む
raw_data = open_file.read()
# fileを閉じる
open_file.close()
# dataを表示する
# print(raw_data)
# 行ごとのリストへ変換

#output.txt#
# 出力先のファイルを書き込みで開く
output_file_name = 'output.txt'
output_file = open(output_file_name, 'w', encoding="utf-8_sig")

point_data = raw_data.splitlines()
# print("\n\n\n")
# 空の辞書を準備
point_dict = {}
# keyとvalueに対して空のリストを準備
key_list = []
points_str_list = []
# 行ごとに処理する
# print("{")
for line in point_data:
    key, points_str = line.split('": "')
    # print(len(points_str))
    # 日本語からスペース二つとダブルコーテーション一つを取り除いてkeyとしてリストに追加
    key_list.append(key.strip('  "'))
print('{')
# print(point_dict)
for x in key_list:
    # 下の文、元はpoint_dict[key]=trs.translate(key.strip('  "'), src='ja', dest='pt').text
    # value:keyを日本語からポルトガル語に翻訳
    value = trs.translate(x, src='ja', dest='pt').text
    # valueを辞書に追加
    point_dict[x] = value
    print('"{}":"{}",'.format(x, point_dict[x]))
    text = '"{}":"{}"'.format(x, point_dict[x])
    output_file.write(text)

output_file.close()
print('出力完了、出力先:{}'.format(output_file_name))

# for i in key_list:
#     print(point_dict[i])
# file_name='result.txt'
# output_file=open(file_name,'w')
# for

# for i in key_list:
#    print(point_dict[i])

# 辞書を表示
# print(point_dict)
# print("}")
# d=key+':'+point_dict[key]
# print(d)
# print(key)
# if len(points_str)<=1 or len(points_str)>2:
#    print(len(points_str))
#    print(points_str)
# points_str_list.append(trs.translate(key).text)
# print(':')

# print(point_dict)
# print(key_list)
# print("\n\n\n")
# print(point_dict)
# print(len(points_str))
# print(len(points_str))
# 辞書にデータを追加
#point_dict[student_name] = points_str
#key, value = points_str
