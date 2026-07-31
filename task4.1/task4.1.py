import cv2
import numpy as np

# 调用摄像头
cap = cv2.VideoCapture(0)

# ROI 大小
roi_w = 320
roi_h = 240

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]
    x1 = w//2 - roi_w//2
    y1 = h//2 - roi_h//2
    x2 = x1 + roi_w
    y2 = y1 + roi_h

    # 截取ROI
    roi = frame[y1:y2, x1:x2]

    # 灰度化
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    # 边缘检测
    canny = cv2.Canny(gray, 50, 150)

    # 关键：把边缘转成3通道白色线条
    canny_color = cv2.cvtColor(canny, cv2.COLOR_GRAY2BGR)

    # 把边缘叠加在原图上（不会黑）
    mask = canny != 0
    roi[mask] = canny_color[mask]

    # 画绿色框
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)

    cv2.imshow("ROI Edge", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()