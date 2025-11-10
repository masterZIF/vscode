# lab5-8.py
from collections import Counter

def can_construct(ransomNote: str, magazine: str) -> bool:
    
    # 统计 magazine 中每个字符的出现次数 [cite: 107]
    mag_counts = Counter(magazine)
    
    # 遍历 ransomNote
    for char in ransomNote:
        # 检查 magazine 是否有足够的字符
        if mag_counts[char] > 0:
            # magazine 中的每个字符只能在 ransomNote 中使用一次 [cite: 103]
            mag_counts[char] -= 1
        else:
            return False
            
    return True

# 示例 1 [cite: 104]
ransomNote1 = "a"
magazine1 = "b"
print(f"输入: ransomNote = '{ransomNote1}', magazine = '{magazine1}'")
print(f"输出: {can_construct(ransomNote1, magazine1)}")

# 示例 2 [cite: 104]
ransomNote2 = "aa"
magazine2 = "ab"
print(f"\n输入: ransomNote = '{ransomNote2}', magazine = '{magazine2}'")
print(f"输出: {can_construct(ransomNote2, magazine2)}")

# 示例 3 [cite: 104]
ransomNote3 = "aa"
magazine3 = "aab"
print(f"\n输入: ransomNote = '{ransomNote3}', magazine = '{magazine3}'")
print(f"输出: {can_construct(ransomNote3, magazine3)}")