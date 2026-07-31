import cv2
import numpy as np

# ===================== 读取图片（务必和代码同文件夹） =====================
img = cv2.imread("test.png")
if img is None:
    print("图片读取失败！")
    exit()

# ===================== 1. 腐蚀（erode） =====================
kernel = np.ones((3, 3), np.uint8)  # 改用小核，避免变黑
img_erode = cv2.erode(img, kernel, iterations=1)

# ===================== 2. 模糊（blur） =====================
img_blur = cv2.blur(img, (5, 5))  # 小模糊，更清晰

# ===================== 3. Canny 边缘检测（关键修复！） =====================
# 第一步：转灰度（Canny必须灰度图，这是你变黑的核心原因）
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_canny = cv2.Canny(gray, 30, 100)

# ===================== 保存图片 =====================
cv2.imwrite("erode.jpg", img_erode)
cv2.imwrite("blur.jpg", img_blur)
cv2.imwrite("canny.jpg", img_canny)

# ===================== 显示（关键修复：创建可缩放窗口） =====================
cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Erode", cv2.WINDOW_NORMAL)
cv2.namedWindow("Blur", cv2.WINDOW_NORMAL)
cv2.namedWindow("Canny", cv2.WINDOW_NORMAL)

cv2.imshow("Original", img)
cv2.imshow("Erode", img_erode)
cv2.imshow("Blur", img_blur)
cv2.imshow("Canny", img_canny)

cv2.waitKey(0)
cv2.destroyAllWindows()