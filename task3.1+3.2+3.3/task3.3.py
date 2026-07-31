import cv2
import numpy as np

# 读取图片
img = cv2.imread("test.png")
if img is None:
    print("图片读取失败！")
    exit()

# ===================== 安全添加椒盐噪声 =====================
def add_salt_pepper_noise(img, prob=0.02):
    output = img.copy()
    h, w = output.shape[:2]
    noise_pixels = int(h * w * prob)

    # 随机加白点（盐）
    for i in range(noise_pixels):
        y = np.random.randint(0, h)
        x = np.random.randint(0, w)
        output[y, x] = 255

    # 随机加黑点（胡椒）
    for i in range(noise_pixels):
        y = np.random.randint(0, h)
        x = np.random.randint(0, w)
        output[y, x] = 0

    return output

# 添加噪声
img_noise = add_salt_pepper_noise(img, prob=0.03)

# 保存
cv2.imwrite("noise_salt_pepper.jpg", img_noise)

# ===================== 显示（不会黑图） =====================
cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Salt Pepper Noise", cv2.WINDOW_NORMAL)

cv2.imshow("Original", img)
cv2.imshow("Salt Pepper Noise", img_noise)

cv2.waitKey(0)
cv2.destroyAllWindows()