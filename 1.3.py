# 任务1.3：Python之禅字符统计（简洁版）
import this
from collections import Counter

# 获取Python之禅
zen = this.s

# 统计字符频率
freq = Counter(zen)

# 按频率排序
sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

# 打印结果
print("字符\t出现次数")
print("-" * 20)
for char, count in sorted_items:
    display = char if char not in '\n ' else ('\\n' if char == '\n' else '空格')
    print(f"{display}\t{count}")

# 输出字符序列
print("\n字符序列：", ''.join(char for char, _ in sorted_items))