import cv2

img = cv2.imread("test.png")
if img is not None:
    # 自动缩放到适合屏幕
    cv2.namedWindow("My Image", cv2.WINDOW_NORMAL)
    cv2.imshow("My Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()