# lab5-3.py

# --- 1. 创建元组，进行索引、长度计算、切片 [cite: 82] ---
print("--- 任务1 ---")
my_tuple = (10, 20, 30, 'python', 40.5)

print(f"索引[0]: {my_tuple[0]}")
print(f"索引[-1]: {my_tuple[-1]}")
print(f"元组长度: {len(my_tuple)}")
print(f"切片[1:3]: {my_tuple[1:3]}")

# --- 2. 元组添加元素 [cite: 82, 83] ---
print("\n--- 任务2 (添加元素) ---")
print(f"原始元组: {my_tuple}")
# 元组不可变，通过创建新元组实现“添加”
new_tuple = my_tuple + (50, 'new_element')
print(f"添加后: {new_tuple}")

# --- 3. 两个元组连接 [cite: 84] ---
print("\n--- 任务3 (元组连接) ---")
tuple_a = (1, 2, 3)
tuple_b = ('a', 'b', 'c')
connected_tuple = tuple_a + tuple_b
print(f"{tuple_a} + {tuple_b} = {connected_tuple}")

# --- 4. 列表和元组连接 [cite: 85] ---
print("\n--- 任务4 (列表和元组连接) ---")
my_list = [100, 200, 300]
my_tuple_b = (400, 500)
connected_list_tuple = tuple(my_list) + my_tuple_b
print(f"列表 {my_list} 和元组 {my_tuple_b} 连接: {connected_list_tuple}")