import cv2
import numpy as np

# 读取图片
img = cv2.imread("4-1.png")
if img is None:
    print("图片没读到！")
    exit()

output = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二值化（保证前景是白色）
_, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)

# 找轮廓
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 过滤太小的噪点
contours = [c for c in contours if cv2.contourArea(c) > 100]

# ========== 1. 找面积最大轮廓 ==========
max_cnt = max(contours, key=cv2.contourArea)
max_area = cv2.contourArea(max_cnt)

# ========== 2. 找最不规则（凸包缺陷法） ==========
def irregular_score(cnt):
    hull = cv2.convexHull(cnt)
    hull_area = cv2.contourArea(hull)
    if hull_area == 0:
        return 0
    return 1 - (cv2.contourArea(cnt) / hull_area)  # 越大越不规则

most_irregular_cnt = max(contours, key=irregular_score)
irreg_area = cv2.contourArea(most_irregular_cnt)

# ========== 绘制 ==========
# 最大面积：红框
x, y, w, h = cv2.boundingRect(max_cnt)
cv2.rectangle(output, (x, y), (x+w, y+h), (0, 0, 255), 2)
cv2.putText(output, f"Max Area: {max_area:.0f}", (x, y-5),
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

# 最不规则：绿框
x2, y2, w2, h2 = cv2.boundingRect(most_irregular_cnt)
cv2.rectangle(output, (x2, y2), (x2+w2, y2+h2), (0, 255, 0), 2)
cv2.putText(output, f"Irregular: {irreg_area:.0f}", (x2, y2-5),
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

# 打印
print("面积最大形状面积：", max_area)
print("最不规则形状面积：", irreg_area)

# 显示
cv2.imshow("Original", img)
cv2.imshow("Result", output)
cv2.waitKey(0)
cv2.destroyAllWindows()