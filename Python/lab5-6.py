# lab5-6.py

# 示例输入 [cite: 91]
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

# 使用 zip() 函数将两个列表配对并转为字典 [cite: 90]
dict2 = dict(zip(list1, list2))

print(f"Key 列表: {list1}")
print(f"Value 列表: {list2}")
print(f"生成的字典: {dict2}")