"""""
Python入门习题第100练: 中文文本人名提取与频率统计
需求: 从鹿鼎记.txt文件中提取所有人名, 并统计这些人名出现的频率, 打印出现频率最高的前20个人名。
"""""
import jieba.posseg as posseg
# 导入jieba.posseg模块,用于分词和词性标注
# 导入pandas模块,用于数据处理
import pandas as pd

with open("鹿鼎记.txt", encoding="utf-8") as f:
    # 定义变量保存读取到的所有数据
    content = ""
# 持续读取,直到为"为止
    while True:
        # 以行的方式读取
        text = f.readline()
        # 如果读取到的内容为空字符
        if text == "":
            # 退出循环
            break
        # 将读取到的内容拼接到content中
        content = content + text
        # 定义列表保存提取到的人名
        words = []
        # 对文本进行分词和词性标注
        for word, flag in posseg.cut(content):
            if flag == "nr":
                # 将人名添加到到表
            words.append(word)
        print(pd.Series(words).value_counts()[:20])
