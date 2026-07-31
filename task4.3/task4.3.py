import cv2
import numpy as np

# 自动排序4个点，防黑图
def order_points(pts):
    pts = np.array(pts, dtype="float32")
    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    return rect

points = []

def mouse_click(event, x, y, flags, param):
    global points
    if event == cv2.EVENT_LBUTTONDOWN and len(points) < 4:
        points.append([x, y])
        cv2.circle(img, (x, y), 8, (0, 0, 255), -1)
        cv2.imshow("image", img)

# 读取图片
img = cv2.imread("3-1.jpg")
clone = img.copy()

# 窗口
cv2.namedWindow("image")
cv2.imshow("image", img)
cv2.setMouseCallback("image", mouse_click)
print("👉 只点地面白色矩形的4个角！")
print("👉 点完按 ENTER")

while True:
    if cv2.waitKey(1) & 0xFF == 13 and len(points) ==4:
        break

cv2.destroyAllWindows()

# 变换
src = order_points(points)
w, h = 700, 500
dst = np.float32([[0,0], [w,0], [w,h], [0,h]])

M = cv2.getPerspectiveTransform(src, dst)
result = cv2.warpPerspective(clone, M, (w, h))

# 显示
cv2.imshow("原图", clone)
cv2.imshow("上帝视角（正常图，不黑）", result)
cv2.waitKey(0)
cv2.destroyAllWindows()