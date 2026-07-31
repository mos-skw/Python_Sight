import cv2
import numpy as np

# ===================== 1. 读取图片 =====================
# 请将图片命名为 track.jpg（或对应后缀），放在代码同目录
img = cv2.imread("5-1.png")
if img is None:
    print("❌ 错误：图片读取失败！请确认图片路径和名称正确")
    exit()

# 等比例缩放，方便操作（可选，不影响效果）
h, w = img.shape[:2]
scale = 0.8
img = cv2.resize(img, (int(w * scale), int(h * scale)))

# 转换为HSV颜色空间（HSV是颜色分割的标准空间）
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# ===================== 2. 创建滑动条回调函数（空函数，仅占位） =====================
def nothing(x):
    pass

# ===================== 3. 创建Control窗口 + 6个HSV滑动条 =====================
cv2.namedWindow("Control", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Control", 600, 400)

# H: 0-179（OpenCV中H范围是0-179，不是0-360）
# S: 0-255
# V: 0-255
cv2.createTrackbar("H_min", "Control", 0, 179, nothing)
cv2.createTrackbar("H_max", "Control", 179, 179, nothing)
cv2.createTrackbar("S_min", "Control", 0, 255, nothing)
cv2.createTrackbar("S_max", "Control", 255, 255, nothing)
cv2.createTrackbar("V_min", "Control", 0, 255, nothing)
cv2.createTrackbar("V_max", "Control", 255, 255, nothing)

# ===================== 4. 实时调参循环 =====================
while True:
    # 读取滑动条当前值
    h_min = cv2.getTrackbarPos("H_min", "Control")
    h_max = cv2.getTrackbarPos("H_max", "Control")
    s_min = cv2.getTrackbarPos("S_min", "Control")
    s_max = cv2.getTrackbarPos("S_max", "Control")
    v_min = cv2.getTrackbarPos("V_min", "Control")
    v_max = cv2.getTrackbarPos("V_max", "Control")

    # 定义HSV颜色范围（根据滑动条动态更新）
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    # 生成二值化Mask（掩膜）：在范围内的像素为白色(255)，否则为黑色(0)
    mask = cv2.inRange(hsv, lower, upper)

    # 用Mask抠出目标物体（只保留Mask中白色区域的原图像素）
    result = cv2.bitwise_and(img, img, mask=mask)

    # ===================== 5. 显示结果 =====================
    cv2.imshow("Original", img)          # 原图
    cv2.imshow("Mask", mask)             # 二值化掩膜
    cv2.imshow("Result", result)         # 抠出的目标物体

    # 按ESC退出
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

# ===================== 6. 退出时打印最终参数（方便后续直接使用） =====================
print("\n✅ 最终HSV参数（可直接用于代码）：")
print(f"H_min = {h_min}, H_max = {h_max}")
print(f"S_min = {s_min}, S_max = {s_max}")
print(f"V_min = {v_min}, V_max = {v_max}")

cv2.destroyAllWindows()