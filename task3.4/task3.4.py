import cv2
import numpy as np

# 1. 读取带椒盐噪声的图片（替换为你的图片路径）
img_noise = cv2.imread("1.jpg", cv2.IMREAD_GRAYSCALE)  # 读成灰度图更方便处理

if img_noise is None:
    print("图片读取失败！")
    exit()

# 2. 均值滤波（卷积核大小 ）
img_mean = cv2.blur(img_noise, (9, 9))

# 3. 高斯滤波（卷积核大小 ，标准差自动计算）
img_gauss = cv2.GaussianBlur(img_noise, (9, 9), 0)

# 4. 保存结果
cv2.imwrite("result_mean_filter.jpg", img_mean)
cv2.imwrite("result_gauss_filter.jpg", img_gauss)

# 5. 显示对比
cv2.namedWindow("Noisy Image", cv2.WINDOW_NORMAL)
cv2.namedWindow("Mean Filter", cv2.WINDOW_NORMAL)
cv2.namedWindow("Gaussian Filter", cv2.WINDOW_NORMAL)

cv2.imshow("Noisy Image", img_noise)
cv2.imshow("Mean Filter", img_mean)
cv2.imshow("Gaussian Filter", img_gauss)

cv2.waitKey(0)
cv2.destroyAllWindows()