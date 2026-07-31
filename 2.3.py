import numpy as np

# 创建数组a和b
a = np.array([[1, 5], [9, 4]])
b = np.array([[2, 6], [4, 8]])

print("数组a：")
print(a)
print("\n数组b：")
print(b)

# (1) 垂直方向连接
c = np.vstack((a, b))
print("\n(1) 垂直连接后的数组c：")
print(c)

# (2) 水平方向分割
d, e = np.hsplit(c, 2)
print("\n(2) 分割后的数组d（前两列）：")
print(d)
print("\n分割后的数组e（后两列）：")
print(e)

# (3) 展平并排序
f = c.flatten()
print("\n(3) 展平后的数组f：")
print(f)

# 二叉树排序（使用快速排序）
sorted_f = np.sort(f)
print("\n排序后的数组f：")
print(sorted_f)