#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import json
from turtle import st
import pandas as pd

choice_excel_data = pd.read_excel('考试宝\\test2.xlsx', sheet_name='Sheet1')

data = {}
for i in choice_excel_data.index.values:
    row_data = choice_excel_data.loc[i, ['题干（必填）', '题型 （必填）', '选项 A', '选项 B', '选项 C', '选项 D', '选项E(勿删)', '选项F(勿删)', '选项G(勿删)', '选项H(勿删)', '正确答案（必填）', '解析', '章节', '难度']].to_dict()
    # print(row_data)
    new_data = {}
    for key,value in row_data.items():
        key = key.strip()
        key = key.replace('    ', ' ')
        # key = key.replace(' ', '').replace(' ', '').replace(' ', '').replace(' ', '').replace(' ', '').replace(' ', '').replace(' ', '')
        if not isinstance(value, str):
            row_data[key] = 'None'
        if isinstance(value, str):
            value = value.strip()
        new_data[key] = value
    data[new_data['题干（必填）']] = new_data


with open('test1.json', 'w', encoding='utf8') as f:
    json.dump(data, f, ensure_ascii=False, indent = 4)
    
