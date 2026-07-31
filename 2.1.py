import numpy as np

# 创建5×5的随机数组
np.random.seed(42)  # 设置随机种子以便结果可重现
random_array = np.random.randint(0, 100, size=(5, 5))
print("原始随机数组：")
print(random_array)

# 创建5×1的列向量
column_vector = np.random.randint(0, 10, size=(5, 1))
print("\n列向量：")
print(column_vector)

# 利用广播机制将列向量加到数组的每一列
result_array = random_array + column_vector
print("\n广播后的数组：")
print(result_array)

# 找出每行的最大值
row_max = np.max(result_array, axis=1)
print("\n每行的最大值：")
print(row_max)

# 计算每行的标准差
row_std = np.std(result_array, axis=1)
print("\n每行的标准差：")
print(row_std)