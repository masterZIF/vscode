# lab5-1.py
def find_pivot_element(nums):
    """
    找出列表中比它前面元素都大，比它后面元素都小的数。
    """
    n = len(nums)
    if n == 0:
        return -1

    # O(n^2) 的直接遍历解法
    for i in range(n):
        is_pivot = True
        
        # 检查左边
        for j in range(i):
            if nums[j] > nums[i]:
                is_pivot = False
                break
        if not is_pivot:
            continue
            
        # 检查右边
        for j in range(i + 1, n):
            if nums[j] < nums[i]:
                is_pivot = False
                break
        
        # 如果左右检查都通过，则返回第一个解
        if is_pivot:
            return i 

    return -1

# 示例输入1：[6, 3, 4, 9, 1] [cite: 79]
# 示例输出1：-1 [cite: 79]
# 示例输入2：[4, 3, 6, 9, 7] [cite: 79]
# 示例输出2：2 [cite: 79]
input1 = [6, 3, 4, 9, 1] 
input2 = [4, 3, 6, 9, 7] 
# 示例输入3：[1,2,3,4,5] (根据题目描述，1符合条件) [cite: 78]
input3 = [1, 2, 3, 4, 5] 

print(f"输入: {input1}, 输出: {find_pivot_element(input1)}")
print(f"输入: {input2}, 输出: {find_pivot_element(input2)}")
print(f"输入: {input3}, 输出: {find_pivot_element(input3)}")