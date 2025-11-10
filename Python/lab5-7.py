# lab5-7.py
import string
from collections import Counter # 用于词频统计

# 1. 定义要剔除的特殊符号 [cite: 97]
punctuations = r"""!"#$%&()*+,-./:;<=>?@[\]^_‘{|}~"""

# 2. 读取文件
try:
    with open('hamlet.txt', 'r', encoding='utf-8') as file:
        text = file.read()
except FileNotFoundError:
    print("错误：hamlet.txt 文件未找到。")
    print("请确保 hamlet.txt 与本脚本在同一目录下。")
    exit()

# 3. 文本清理
text = text.lower() # (1) 单词不区分大小写 [cite: 96, 100]

# (2) 剔除特殊符号 [cite: 97]
translation_table = str.maketrans(punctuations, ' ' * len(punctuations))
cleaned_text = text.translate(translation_table)

# (3) 分割单词 (split() 默认处理所有空白，包括换行符 [cite: 98])
words = cleaned_text.split()

# 4. 词频统计
word_counts = Counter(words)

# 5. 输出出现最多的10个单词 [cite: 95, 99]
print("--- hamlet.txt 词频统计 Top 10 ---")
top_10 = word_counts.most_common(10)

for word, count in top_10:
    print(f"{word}: {count}")