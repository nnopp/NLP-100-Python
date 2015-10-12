#!/usr/bin/python
# -*- coding: utf-8 -*-

# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

input_string1 = u"パトカー"
input_list1 = list(input_string1)
input_string2 = u"タクシー"
input_list2 = list(input_string2)

output_list = list()

while(True):
    try:
        output_list.append(input_list1.pop(0))
        output_list.append(input_list2.pop(0))
    except:
        break

output_string = "".join(output_list)
print(output_string)
# For some reason, following does not work..
#print("".join(output_list))


