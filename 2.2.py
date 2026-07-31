import numpy as np

# 给定的三维数组
data = np.array([
    [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]],
    [[7.0, 8.0], [9.0, 10.0], [11.0, 12.0]],
    [[13.0, 14.0], [15.0, 16.0], [17.0, 18.0]],
    [[19.0, 20.0], [21.0, 22.0], [23.0, 24.0]]
])

print("原始三维数组形状：", data.shape)
print("原始数组：")
print(data)

# (1) 提取第一个样本的所有特征值
first_sample = data[0, :, :]
print("\n(1) 第一个样本的所有特征值：")
print(first_sample)

# (2) 提取第二个样本的第一个特征的所有值
second_sample_first_feature = data[1, 0, :]
print("\n(2) 第二个样本的第一个特征的所有值：")
print(second_sample_first_feature)

# (3) 提取特征的前两组值（前两个特征的所有值）
first_two_features = data[:, :2, :]
print("\n(3) 前两个特征的所有值：")
print(first_two_features)

# (4) 提取所有样本的所有特征的第二个值
all_second_values = data[:, :, 1]
print("\n(4) 所有样本的所有特征的第二个值：")
print(all_second_values)

# (5) 将数组变成3×8的二维数组
reshaped_array = data.reshape(3, 8)
print("\n(5) 重塑为3×8的数组：")
print(reshaped_array)

# 计算每个最小维度内数据的和
# 原始数据的最小维度是每个特征的2个值
# 重塑后的数组，每行包含8个值
row_sums = np.sum(reshaped_array, axis=1)
print("\n每行的和：")
print(row_sums)