import cv2
import numpy as np


def detect_cube_color(image_path):
    # 读取图片
    img = cv2.imread(image_path)
    if img is None:
        return "❌ 图片读取失败，请检查路径是否正确"

    # 转 HSV 颜色空间（最适合颜色识别）
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # ---------- 定义红、黄、绿 颜色范围 ----------
    # 红色
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    # 黄色
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])

    # 绿色
    lower_green = np.array([35, 100, 100])
    upper_green = np.array([77, 255, 255])

    # ---------- 生成颜色掩码 ----------
    mask_red = cv2.inRange(hsv, lower_red1, upper_red1) + cv2.inRange(hsv, lower_red2, upper_red2)
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    # ---------- 计算颜色像素数量 ----------
    count_red = cv2.countNonZero(mask_red)
    count_yellow = cv2.countNonZero(mask_yellow)
    count_green = cv2.countNonZero(mask_green)

    # ---------- 判断最多的颜色 ----------
    max_count = max(count_red, count_yellow, count_green)

    if max_count == count_red:
        return "红色方块"
    elif max_count == count_yellow:
        return "黄色方块"
    else:
        return "绿色方块"


# ===================== 主程序：你输入路径，自动输出结果 =====================
if __name__ == "__main__":
    print("=" * 50)
    print("        方块颜色识别程序（输入路径 → 输出类别）")
    print("=" * 50)

    # 让你输入图片路径
    img_path = input("请输入图片完整路径：")

    # 识别并输出结果
    result = detect_cube_color(img_path)
    print("\n👉 识别结果：", result)