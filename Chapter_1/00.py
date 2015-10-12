#!/usr/bin/python
# -*- coding: utf-8 -*-

# 00. 文字列の逆順
# 文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．

string_value = "stressed"
string_list = list(string_value)
string_list.reverse()

print("".join(string_list))
#print("\n") ## This is not required, as pring() method adds '\n'

