# lab5-5.py

# 题目给定的值集合 [cite: 89]
values = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100, 110, 200, 230, 330]

# 初始化字典 [cite: 89]
result_dict = {
    'k1': [],  # 大于 66
    'k2': []   # 小于等于 66
}

# 遍历值集合
for value in values:
    if value > 66:
        result_dict['k1'].append(value)
    else: 
        result_dict['k2'].append(value)

# 打印结果
print(f"原始数据: {values}")
print(f"分类结果: {result_dict}")