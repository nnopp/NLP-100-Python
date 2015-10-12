#!/usr/bin/python
# -*- coding: utf-8 -*-

# 04. 元素記号
# "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

input_string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

input_list = input_string.split(' ')
output_list = list()

for i, v in enumerate(input_list):
    if(i == 0 or i == 4 or i == 5 or i == 6 or i == 7 or \
            i == 8 or i == 14 or i == 15 or i == 18):
        output_list.append(str(v[0:2]))
        # this would cause "index out of range error..
        #output_list[i] = str(v[0:2])
    else:
        output_list.append(str(v[0:1]))
        #output_list[i] = v[0:1]
        # this would cause "index out of range error..

print(output_list)


