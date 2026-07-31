# 任务1.4：9x9二维数组操作

# 步骤1：创建左上角递增的数组
n = 9
arr = [[0] * n for _ in range(n)]

# 遍历修改，实现左上角向右下递增
for i in range(n):
    for j in range(n):
        arr[i][j] = max(i, j)
        # 修正，使其符合示例
        arr[i][j] = max(i, j)

# 但示例的模式是取对角线的最大值
arr = [[max(i, j) for j in range(n)] for i in range(n)]

print("步骤1结果：")
for row in arr:
    print(row)

# 步骤2：用9画菱形
# 找到中心点
center = n // 2

# 遍历修改，在菱形区域放9
for i in range(n):
    for j in range(n):
        # 菱形条件：曼哈顿距离 <= 4
        if abs(i - center) + abs(j - center) <= 4:
            arr[i][j] = 9

print("\n步骤2结果：")
for row in arr:
    print(row)
print()