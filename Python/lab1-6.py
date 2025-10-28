# lab1-6.py - 方法一：使用列表排序

def sort_three_numbers_list(x, y, z):
    """接收三个数，将它们放入列表并使用内置函数排序。"""
    
    # 1. 将三个数放入一个列表
    numbers = [x, y, z]
    
    # 2. 对列表进行排序（默认从小到大）
    numbers.sort() 
    
    # 3. 输出排序后的结果
    # 使用 *numbers 可以解包列表，使输出格式为 'x y z'
    print("排序后的结果：", end="")
    print(*numbers, sep=",")


# --- 运行示例（接收用户输入） ---

# 提示用户输入三个整数，并用逗号分隔
print("请输入三个整数 (例如: 6,5,9)：")
try:
    # 接收一行输入，并按逗号分割，然后将每个部分转换为整数
    # map(int, input().split(',')) 用于实现输入格式： 6,5,9
    input_str = input()
    x, y, z = map(int, input_str.split(','))
    
    # 调用函数并输出结果
    sort_three_numbers_list(x, y, z)

except ValueError:
    print("输入格式错误，请确保只输入三个由逗号分隔的整数。")