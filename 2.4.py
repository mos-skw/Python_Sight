import numpy as np


def image_binarization(image, threshold=128):
    """
    图像二值化处理
    """
    # 创建二值化图像的副本
    binary_image = np.zeros_like(image)

    # 二值化处理：大于阈值的设为255，小于等于阈值的设为0
    binary_image[image > threshold] = 255

    return binary_image


def count_pixel_frequency(binary_image):
    """
    统计二值化图像中像素值的频率
    """
    unique, counts = np.unique(binary_image, return_counts=True)
    frequency = dict(zip(unique, counts))
    return frequency


# 创建100×100的随机灰度图像（0-255整数）
np.random.seed(42)
gray_image = np.random.randint(0, 256, size=(100, 100))

print("原始灰度图像：")
print(f"形状：{gray_image.shape}")
print(f"数据类型：{gray_image.dtype}")
print(f"像素值范围：{np.min(gray_image)} - {np.max(gray_image)}")

# 二值化处理
binary_image = image_binarization(gray_image, threshold=128)

# 统计频率
frequency = count_pixel_frequency(binary_image)

print("\n二值化后的图像：")
print(f"形状：{binary_image.shape}")
print(f"唯一像素值：{np.unique(binary_image)}")

print("\n像素值频率统计：")
for pixel_value, count in frequency.items():
    print(f"像素值 {int(pixel_value)}: {count} 个像素 ({count / 10000 * 100:.2f}%)")

# 验证总像素数
total_pixels = sum(frequency.values())
print(f"\n总像素数：{total_pixels} (应为10000)")