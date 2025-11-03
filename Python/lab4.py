# 导入 functools 模块中的 reduce 函数
from functools import reduce

# --------------------------------------------------
# 1. fliter, reduce 求素数及其和 [cite: 24]
# --------------------------------------------------
print("--- 1. 求100以内素数及其和 ---")

# 辅助函数：判断是否为素数
def is_prime(n):
    if n < 2:
        return False
    # 仅需检查到 n 的平方根
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 使用 filter 方法求出100以内的素数 [cite: 25]
# 范围是从 0 到 100
primes_iterator = filter(is_prime, range(101))
primes_list = list(primes_iterator)
print(f"100以内的素数: {primes_list}")

# 使用 reduce 方法计算这些素数的和 [cite: 26]
# 按照要求尽可能使用 lambda 表达式 [cite: 23]
sum_of_primes = reduce(lambda x, y: x + y, primes_list)
print(f"素数之和: {sum_of_primes}")
print("\n")


# --------------------------------------------------
# 2. map 规范姓名 [cite: 27]
# --------------------------------------------------
print("--- 2. 规范姓名 ---")
# 按照文档要求，使用程序定义输入 [cite: 29, 30]
input_names = ['lisa', 'JACK', 'Adam']
print(f"输入: {input_names}")

# 使用 map() 函数和 lambda 表达式 [cite: 23, 28]
# str.capitalize() 函数可以将字符串首字母大写，其他字母小写
normalized_names = list(map(lambda s: s.capitalize(), input_names))
print(f"输出: {normalized_names}")
print("\n")


# --------------------------------------------------
# 3. sorted 按照排名对 list 进行排序 [cite: 31]
# --------------------------------------------------
print("--- 3. 按排名排序 ---")
# 按照文档要求，使用程序定义输入 [cite: 29, 34]
input_list = [(1, 'byd'), (3, 'xiaopeng'), (2, 'tesla'), (4, 'weilai')]
print(f"输入: {input_list}")

# 使用 sorted 函数和 lambda 表达式 [cite: 33]
# key=lambda t: t[0] 表示按照元组 (tuple) 的第一个元素（索引为0）进行排序
sorted_list = sorted(input_list, key=lambda t: t[0])
print(f"输出: {sorted_list}")
print("\n")


# --------------------------------------------------
# 4. 使用闭包实现步数记录 [cite: 35]
# --------------------------------------------------
print("--- 4. 闭包实现步数记录 ---")

# 补全下方代码 [cite: 36, 37]
def count_steps(original_step=0):
    # original_step 是外部函数的变量，被内部函数 wrapper 引用
    def wrapper(new_steps):
        # 声明 original_step 不是局部变量，而是来自外部（非局部）作用域
        nonlocal original_step
        # 累加步数
        original_step += new_steps
        # 返回当前的总步数
        return original_step
    return wrapper

# --- 执行语句 --- [cite: 37]
# 1. 创建闭包实例，初始步数为 10
count_steps_instance = count_steps(10)

# 2. 第一次调用，增加 5 步
# (内部 original_step 变为 10 + 5 = 15)
print(count_steps_instance(5))

# 3. 第二次调用，再增加 5 步
# (内部 original_step 变为 15 + 5 = 20)
print(count_steps_instance(5))

# 4. 第三次调用，再增加 8 步
# (内部 original_step 变为 20 + 8 = 28)
print(count_steps_instance(8))