# lab1-7.py

import math

def calculate_gcd(a, b):
    """
    计算两个正整数的最大公约数 (GCD)。
    使用欧几里得算法 (辗转相除法)
    """
    while b:
        a, b = b, a % b
    return a

def calculate_lcm(a, b):
    """
    计算两个正整数的最小公倍数 (LCM)。
    公式: LCM(a, b) = (|a * b|) / GCD(a, b)
    """
    if a == 0 or b == 0:
        return 0
    
    # 确保使用绝对值，尽管题目要求是正整数
    a_abs = abs(a)
    b_abs = abs(b)
    
    # 1. 计算最大公约数 (GCD)
    # Python 3.9 及以上可以直接使用 math.gcd(a_abs, b_abs)
    # 为了兼容性，这里使用自定义函数，或者导入 math 模块
    
    # 如果环境支持，直接用内置函数更简洁：
    # common_divisor = math.gcd(a_abs, b_abs)
    
    # 使用自定义的 GCD 函数
    common_divisor = calculate_gcd(a_abs, b_abs)
    
    # 2. 计算最小公倍数 (LCM)
    # 注意：先除以 GCD 再相乘，可以防止乘法溢出（虽然对于小整数不会）
    lcm = (a_abs * b_abs) // common_divisor
    
    return lcm

# --- 运行示例（接收用户输入） ---

if __name__ == "__main__":
    print("请输入两个正整数 (例如: 4,6)：")
    try:
        # 接收一行输入，并按逗号分割，然后将每个部分转换为整数
        input_str = input()
        num1, num2 = map(int, input_str.split(','))
        
        if num1 <= 0 or num2 <= 0:
            print("错误：请输入两个正整数。")
        else:
            # 计算最小公倍数
            result = calculate_lcm(num1, num2)
            
            # 输出结果
            print("-" * 20)
            print(f"输入：{num1},{num2}")
            print(f"输出：{result}")
            print("-" * 20)

    except ValueError:
        print("输入格式错误，请确保只输入两个由逗号分隔的正整数。")