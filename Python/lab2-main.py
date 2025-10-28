# lab2-main.py - 第二次实验所有题目整合，带统一入口

import math

# --- 工具函数 ---

def get_positive_integer(prompt):
    """通用的获取正整数输入函数，用于错误处理"""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("错误：请输入非负整数。")
                continue
            return value
        except ValueError:
            print("输入无效，请输入一个整数。")

def is_prime(n):
    """判断一个数是否是素数（质数），用于任务 6 和 7"""
    if n < 2:
        return False
    # 只需要检查到 sqrt(n)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# ----------------------------------------------------
#               实验内容 (9个任务)
# ----------------------------------------------------

# 任务 1: 华氏温度转换成摄氏温度
def task1_fahrenheit_to_celsius():
    """计算华氏度到摄氏度的转换"""
    print("\n--- 任务 1: 华氏温度转换成摄氏温度 ---")
    
    while True:
        try:
            f = float(input("请输入华氏温度 (℉): "))
            break
        except ValueError:
            print("输入无效，请输入一个数字。")

    # 摄氏度(℃) = (华氏度(℉) - 32) ÷ 1.8
    c = (f - 32) / 1.8
    
    print(f"输入: {f}")
    # 结果保留 2 位小数
    print(f"输出: {c:.2f}℃")


# 任务 2: 输入年份判断是否是闰年
def task2_is_leap_year():
    """判断输入的年份是否为闰年"""
    print("\n--- 任务 2: 判断是否是闰年 ---")
    year = get_positive_integer("请输入年份: ")
    
    is_leap = False
    
    # 闰年规则:
    # 1. 公元年分非4的倍数，为平年。
    # 2. 公元年分为4的倍数但非100的倍数，为闰年。
    # 3. 公元年分为100的倍数但非400的倍数，为平年。
    # 4. 公元年分为400的倍数为闰年。
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        is_leap = True
        
    result = "是闰年" if is_leap else "不是闰年"
    print(f"输入: {year}")
    print(f"输出: {year}{result}")


# 任务 3: 体脂率的判断实验 (包含容错和优化输出)
def task3_body_fat_rate():
    """计算体脂率并判断是否正常，包含容错处理"""
    print("\n--- 任务 3: 体脂率的判断实验 ---")
    
    # 1. 输入和容错处理
    while True:
        try:
            sex = int(input("请输入性别 (男:1, 女:0): "))
            if sex not in [0, 1]:
                print("错误：性别项输入有误，请检查后再次输入 (男:1, 女:0)。") #
                continue
            age = int(input("请输入年龄 (0 < age < 150): "))
            if not (0 < age < 150):
                print("错误：年龄范围输入有误 (0 < age < 150)。")
                continue
            height = float(input("请输入身高 (米, 0 < height < 3): "))
            if not (0 < height < 3):
                # 示例 31 提示检查身高输入
                print("错误：疑似输入身高有误，请检查后再次输入 (0 < height < 3 米)。") 
                continue
            weight = float(input("请输入体重 (公斤, 0 < weight < 300): "))
            if not (0 < weight < 300):
                print("错误：体重范围输入有误 (0 < weight < 300 kg)。")
                continue
            break
        except ValueError:
            print("输入无效，请确保输入格式正确。")

    # 2. 数据处理与计算
    
    # BMI = 体重(kg) / (身高* 身高) 米
    bmi = weight / (height ** 2)
    
    # 体脂率 = 1.2 * BMI + 0.23 * 年龄 - 5.4 - 10.8 * 性别 (男 : 1 女 : 0)
    bfr = 1.2 * bmi + 0.23 * age - 5.4 - 10.8 * sex
    
    # 正常体脂率范围
    MALE_NORMAL = (0.15, 0.18)
    FEMALE_NORMAL = (0.25, 0.28)
    
    if sex == 1:
        # 男性 15%～18%
        gender_str = "先生"
        normal_range = MALE_NORMAL
        gender_prefix = "男性"
    else:
        # 女性 25%～28%
        gender_str = "女士"
        normal_range = FEMALE_NORMAL
        gender_prefix = "女性"
        
    # 3. 结果判断和优化输出
    
    bfr_percent = bfr * 100
    
    if normal_range[0] * 100 <= bfr_percent <= normal_range[1] * 100:
        advice = "身体非常健康，请继续保持。"
        status = "正常"
    elif bfr_percent < normal_range[0] * 100:
        advice = "请注意，您的身体偏瘦。"
        status = "偏瘦"
    else:
        advice = "请注意，您的身体偏胖。"
        status = "偏胖"
        
    # 4. 输出
    print("-" * 30)
    print(f"输入: 性别={sex}, 年龄={age}, 身高={height:.2f}m, 体重={weight:.2f}kg")
    print(f"体脂率: {bfr_percent:.2f}%") # 结果保留 2 位小数
    print(f"{gender_str}你好，恭喜你，{advice}") # 优化提示
    print(f"({gender_prefix}正常体脂率范围：{normal_range[0]*100}% ~ {normal_range[1]*100}%)")
    print("-" * 30)


# 任务 4: 1~100求和
def task4_sum_1_to_100():
    """计算 1 到 100 的和"""
    print("\n--- 任务 4: 1~100求和 ---")
    
    # 使用高斯求和公式： n * (n + 1) / 2
    n = 100
    total_sum = n * (n + 1) // 2
    
    # 或者使用内置的 sum 和 range
    # total_sum = sum(range(1, 101))
    
    print("输入：无") #
    print(f"输出：{total_sum}") #


# 任务 5: 打印九九乘法表
def task5_multiplication_table():
    """打印九九乘法表"""
    print("\n--- 任务 5: 打印九九乘法表 ---")
    print("输入：无")
    print("输出：")
    
    # 使用嵌套循环打印乘法表
    for i in range(1, 10):
        # j 从 1 循环到 i
        for j in range(1, i + 1):
            # 格式化输出：例如 "1x1=1"
            # end='\t' 用于在每个乘式后添加制表符，使格式整齐
            print(f"{j}x{i}={i*j}", end='\t')
        # 打印完一行后换行
        print()


# 任务 6: 判断素数 (使用 is_prime 辅助函数)
def task6_prime_number():
    """判断输入的数是否为素数"""
    print("\n--- 任务 6: 判断素数 ---")
    num = get_positive_integer("请输入一个大于 1 的自然数: ")
    
    result = "是素数" if is_prime(num) else "不是素数"
    
    print(f"输入: {num}")
    print(f"输出: {num}{result}")


# 任务 7: 偶数分解 (戈德巴赫猜想)
def task7_even_decomposition():
    """输入一个大于 2 的偶数，分解为两个素数之和"""
    print("\n--- 任务 7: 偶数分解 ---")
    
    while True:
        num = get_positive_integer("请输入一个大于 2 的偶数: ")
        if num > 2 and num % 2 == 0:
            break
        print("输入无效，请重新输入一个大于 2 的偶数。")
        
    print(f"输入: {num}")
    print("输出:")
    
    # 较小的素数放在前面
    for i in range(2, num // 2 + 1):
        # 检查 i 是否是素数
        if is_prime(i):
            # 检查 num - i 是否是素数
            j = num - i
            if is_prime(j):
                # 列出所有的分解方式，每种方式占一行
                print(f"{num}={i}+{j}")


# 任务 8: 组成最大数
def task8_largest_number_from_digits():
    """输入一个正整数，输出由它的各位数字组成的最大数"""
    print("\n--- 任务 8: 组成最大数 ---")
    
    num = get_positive_integer("请输入一个正整数: ")
    
    # 1. 将整数转换为字符串，得到各位数字
    num_str = str(num)
    
    # 2. 将字符串转换为列表，并按降序排序
    # Python 的 sorted() 默认是升序，这里使用 reverse=True
    digits = sorted(list(num_str), reverse=True)
    
    # 3. 将排序后的数字列表重新连接成一个字符串
    largest_number_str = "".join(digits)
    
    print(f"输入: {num}")
    print(f"输出: {largest_number_str}")


# 任务 9: 汉诺塔
def task9_hanoi_tower():
    """递归解决汉诺塔问题"""
    print("\n--- 任务 9: 汉诺塔 ---")
    
    num_disks = get_positive_integer("请输入盘子数量 n (例如: 3): ")
    print(f"输入: {num_disks}")
    print("输出:")
    
    def hanoi(n, source, auxiliary, destination):
        """
        n: 盘子数量
        source: 源柱 (A)
        auxiliary: 辅助柱 (B)
        destination: 目标柱 (C)
        """
        if n == 1:
            # 只有一个盘子时，直接从源柱移到目标柱
            print(f"{source} --> {destination}")
            return
        
        # 1. 将 n-1 个盘子从源柱移到辅助柱 (目标柱是暂存区)
        hanoi(n - 1, source, destination, auxiliary)
        
        # 2. 将第 n 个盘子（最大的那个）从源柱移到目标柱
        print(f"{source} --> {destination}")
        
        # 3. 将 n-1 个盘子从辅助柱移到目标柱 (源柱是暂存区)
        hanoi(n - 1, auxiliary, source, destination)

    # 初始调用：n个盘子从 A 移到 C，B 为辅助柱
    hanoi(num_disks, 'A', 'B', 'C')


# ----------------------------------------------------
#               统一入口 (Main Function)
# ----------------------------------------------------

def main():
    """统一入口：显示菜单并根据用户选择运行对应任务"""
    tasks = {
        '1': task1_fahrenheit_to_celsius,
        '2': task2_is_leap_year,
        '3': task3_body_fat_rate,
        '4': task4_sum_1_to_100,
        '5': task5_multiplication_table,
        '6': task6_prime_number,
        '7': task7_even_decomposition,
        '8': task8_largest_number_from_digits,
        '9': task9_hanoi_tower
    }
    
    print("=" * 40)
    print("      第二次实验：编程练习合集")
    print("=" * 40)

    while True:
        print("\n请选择要运行的实验任务：")
        print("1. 华氏度转摄氏度 (Lab 2-1)")
        print("2. 判断是否是闰年 (Lab 2-2)")
        print("3. 体脂率判断实验 (Lab 2-3) **含容错**")
        print("4. 1~100求和 (Lab 2-4)")
        print("5. 打印九九乘法表 (Lab 2-5)")
        print("6. 判断素数 (Lab 2-6)")
        print("7. 偶数分解 (Lab 2-7)")
        print("8. 组成最大数 (Lab 2-8)")
        print("9. 汉诺塔 (Lab 2-9)")
        print("0. 退出程序")
        
        choice = input("\n请输入编号 (0-9): ").strip()
        
        if choice == '0':
            print("\n程序已退出。再见！")
            break
        
        if choice in tasks:
            # 调用用户选择的任务函数
            tasks[choice]()
        else:
            print("\n!!! 输入无效，请重新输入 0 到 9 之间的数字。 !!!")

# 程序的执行起点
if __name__ == "__main__":
    main()