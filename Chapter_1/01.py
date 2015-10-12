#!/usr/bin/python
# -*- coding: utf-8 -*-

# 01. 「パタトクカシーー」
# 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．

input_string = u"パタトクカシーー"
input_list = list(input_string)

#output_string1 = input_list[0] + input_list[2] + input_list[4] + input_list[6] 

# not sure if it works..
output_string1 = ""
output_string2 = ""
for i in input_list:
    output_string1 = output_string1 + input_list.pop(0)
    output_string2 = output_string2 + input_list.pop(0)
output_string1 = output_string1 + input_list.pop(0)
output_string2 = output_string2 + input_list.pop(0)

print(output_string1)

