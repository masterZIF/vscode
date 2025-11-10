# lab5-2.py

# 示例输入
my_list = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 1]

# --- 方案一：使用 set --- [cite: 80]
def dedupe_with_set(data):
    return list(set(data))

# --- 方案二：使用循环 ---
def dedupe_with_loop(data):
    result_list = []
    for item in data:
        if item not in result_list:
            result_list.append(item)
    return result_list

# (额外方案) 方案三：使用字典
def dedupe_with_dict(data):
    return list(dict.fromkeys(data).keys())


print(f"原始列表: {my_list}")
print(f"方案一 (set) 去重: {dedupe_with_set(my_list)}")
print(f"方案二 (loop) 去重: {dedupe_with_loop(my_list)}")