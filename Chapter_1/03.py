#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

# 03. 円周率
# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

input_string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

# STRING.split() method may not be that "official" anymore..
input_list = input_string.strip('\.\,').split(" ")

for value in input_list:
    sys.stdout.write(str(len(value)))

sys.stdout.write('\n')


