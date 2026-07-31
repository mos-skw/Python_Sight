import cv2
import numpy as np

def detect_shapes(image_path):
    # 1. 读取图片
    img = cv2.imread(image_path)
    if img is None:
        print("❌ 读取失败！请检查图片路径是否正确")
        return

    # 2. 灰度 + 二值化
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

    # 3. 找轮廓
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 100:
            continue

        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.04 * peri, True)
        x, y, w, h = cv2.boundingRect(approx)

        shape_name = ""
        if len(approx) == 3:
            shape_name = "Triangle"
        elif len(approx) == 4:
            shape_name = "Rectangle"
        elif len(approx) >= 5:
            shape_name = "Circle"

        # 画框 + 写字
        cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(img, shape_name, (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)

    # 保存到桌面
    save_path = r"C:\Users\skw\Desktop\PythonProject\task3.6\result_shapes.jpg"
    cv2.imwrite(save_path, img)
    print(f"✅ 识别完成！结果已保存到：{save_path}")

    cv2.imshow("Result", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# ===================== 你只需要改这里 =====================
if __name__ == "__main__":
    print("几何图形识别程序")
    print("请输入你的图片完整路径：")
    img_path = input().strip()  # 在这里粘贴你的图片路径
    detect_shapes(img_path)