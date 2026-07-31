# 任务1.2
print("\n" + "=" * 50)
import random
import time

original_list = [random.randint(1, 10000) for _ in range(1200)]


def bubble_sort(arr):
    n = len(arr)
    arr_copy = arr.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
    return arr_copy


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


print("任务1.2：排序算法时间比较")
print(f"原始列表长度: {len(original_list)}")

start = time.time()
bubble_sorted = bubble_sort(original_list)
print(f"冒泡排序时间: {time.time() - start:.6f}秒")

start = time.time()
quick_sorted = quick_sort(original_list)
print(f"快速排序时间: {time.time() - start:.6f}秒")

start = time.time()
merge_sorted = merge_sort(original_list)
print(f"归并排序时间: {time.time() - start:.6f}秒")