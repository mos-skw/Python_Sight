import cv2
import numpy as np


# ==========================
# 【安全读取图片】自动检查，绝不黑屏
# ==========================
def safe_read(path):
    img = cv2.imread(path)
    if img is None:
        print(f"❌ 读取失败：{path}")
        # 创建一个彩色测试图，防止黑图
        img = np.zeros((480, 640, 3), dtype=np.uint8)
        img[:] = (200, 255, 200)
        cv2.putText(img, "IMAGE NOT FOUND", (50, 240),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)
    return img


# ==========================
# 直线检测（超稳）
# ==========================
def line_demo(path):
    img = safe_read(path)
    out = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150)

    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=50, minLineLength=40, maxLineGap=5)
    if lines is not None:
        for x1, y1, x2, y2 in lines[:, 0]:
            cv2.line(out, (x1, y1), (x2, y2), (0, 0, 255), 2)

    cv2.imshow("Line Result", out)


# ==========================
# 圆检测（超稳）
# ==========================
def circle_demo(path):
    img = safe_read(path)
    out = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)

    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT,
                               dp=1, minDist=30,
                               param1=50, param2=30,
                               minRadius=10, maxRadius=200)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for x, y, r in circles[0]:
            cv2.circle(out, (x, y), r, (0, 0, 255), 2)
            cv2.circle(out, (x, y), 2, (0, 255, 0), 3)

    cv2.imshow("Circle Result", out)


# ==========================
# 主程序（只改这里！）
# ==========================
if __name__ == "__main__":
    # --------------------------
    # 必须写 绝对路径！
    # --------------------------
    LINE_PATH = r"2-1.jpg"
    CIRCLE_PATH = r"2-1.jpg"

    line_demo(LINE_PATH)
    circle_demo(CIRCLE_PATH)

    cv2.waitKey(0)
    cv2.destroyAllWindows()