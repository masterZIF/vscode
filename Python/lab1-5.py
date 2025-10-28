# lab1-5.py

# --- 配置参数 ---
DAYS_IN_YEAR = 365
INITIAL_LEVEL = 1.0

# ------------------------------------
#               问题 1
# ------------------------------------

def progress_daily(rate):
    """
    计算一年中每天以固定速率进步或退步后的水平。
    rate: 每天进步或退步的百分比（如 0.01 代表进步 1%）
    """
    level = INITIAL_LEVEL
    for _ in range(DAYS_IN_YEAR):
        # 每天的水平 = 当前水平 * (1 + 变化率)
        level *= (1 + rate)
    return level

# 1. 每天进步 1% (rate = 0.01)
progress_rate_1 = 0.01
final_level_1 = progress_daily(progress_rate_1)

# 2. 每天退步 1% (rate = -0.01)
retreat_rate_1 = -0.01
final_level_2 = progress_daily(retreat_rate_1)

# 3. 将前面两问的数值改为 5‰ 和 1‰ (5‰ = 0.005, 1‰ = 0.001)

# 进步 5‰
progress_rate_3 = 0.005
final_level_3 = progress_daily(progress_rate_3)

# 退步 1‰ (注意：题目可能指每天以 1‰ 退步，或者指与进步 5‰ 对应)
# 假设是每天进步 5‰，每天退步 1‰
retreat_rate_3 = -0.001
final_level_4 = progress_daily(retreat_rate_3)


print("=" * 40)
print("             问题 1 结果")
print("=" * 40)
print(f"1. 每天进步 1% (0.01) 后的水平：{final_level_1:.2f}")
print(f"2. 每天退步 1% (-0.01) 后的水平：{final_level_2:.2f}")
print(f"3. 每天进步 5‰ (0.005) 后的水平：{final_level_3:.2f}")
print(f"3. 每天退步 1‰ (-0.001) 后的水平：{final_level_4:.2f}")
print("-" * 40)


# ------------------------------------
#               问题 2
# ------------------------------------

# 一周 7 天，5 个工作日进步 1% (0.01)，2 个休息日退步 1% (-0.01)
WORKDAY_RATE = 0.01
RESTDAY_RATE = -0.01
WORKDAYS = 5
RESTDAYS = 2

def progress_work_rest_cycle():
    """计算按工作日/休息日周期变化后的水平。"""
    level = INITIAL_LEVEL
    day_of_week = 0  # 0代表周一（第一个工作日）

    for _ in range(DAYS_IN_YEAR):
        # 模拟一周七天循环
        if day_of_week < WORKDAYS:
            # 工作日：每天进步 1%
            level *= (1 + WORKDAY_RATE)
        else:
            # 休息日：每天退步 1%
            level *= (1 + RESTDAY_RATE)

        # 切换到下一天，并确保在 0-6 之间循环
        day_of_week = (day_of_week + 1) % 7
    return level

final_level_q2 = progress_work_rest_cycle()

print("\n" + "=" * 40)
print("             问题 2 结果")
print("=" * 40)
print(f"工作日进步 1%，休息日退步 1% 后的水平：{final_level_q2:.2f}")
print("-" * 40)


# ------------------------------------
#               问题 3
# ------------------------------------

# A君：每天进步 1% (0.01)，不间歇。其结果就是 final_level_1 (问题1的第一个结果)
LEVEL_A = final_level_1 

# 寻找 B 君 (每周 5 天工作，2 天休息，休息日退步 1%) 需要的进步系数 (x)，
# 使 LEVEL_B >= LEVEL_A

def find_required_progress(target_level):
    """通过二分法查找所需的进步系数。"""
    
    # 查找范围：进步系数 x 最小为 0 (不进步)，最大假设为 0.1 (10%)
    low = 0.0
    high = 0.1
    epsilon = 0.0000001 # 精度要求
    
    # B君的退步率是固定的
    B_RESTDAY_RATE = -0.01
    
    # 迭代查找
    while (high - low) > epsilon:
        B_WORKDAY_RATE = (low + high) / 2
        level_b = INITIAL_LEVEL
        day_of_week = 0
        
        for _ in range(DAYS_IN_YEAR):
            if day_of_week < WORKDAYS:
                level_b *= (1 + B_WORKDAY_RATE)
            else:
                level_b *= (1 + B_RESTDAY_RATE)
            day_of_week = (day_of_week + 1) % 7
        
        # 判断 B 君的水平是否达到 A 君的目标
        if level_b < target_level:
            # 如果 B 水平太低，说明进步系数 B_WORKDAY_RATE 太小，需要提高 low
            low = B_WORKDAY_RATE
        else:
            # 如果 B 水平足够或太高，说明进步系数 B_WORKDAY_RATE 太大，需要降低 high
            high = B_WORKDAY_RATE
            
    return high * 100 # 返回百分比

# 查找 B 君工作日的进步系数 x
required_progress_percent = find_required_progress(LEVEL_A)

print("\n" + "=" * 40)
print("             问题 3 结果")
print("=" * 40)
print(f"A 君的最终水平（每天进步 1%）：{LEVEL_A:.2f}")
print(f"B 君需要的工作日进步系数：{required_progress_percent:.4f}%")
print(f"B 君需要每天进步：{required_progress_percent/100:.6f}")
print("-" * 40)