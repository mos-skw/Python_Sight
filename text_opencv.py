import cv2
import numpy as np

# 读取图像
img = cv2.imread('image.jpg')  # 请替换为您的图片路径

if img is None:
    print("错误：无法读取图像")
    exit()

height, width = img.shape[:2]
print(f"图像尺寸: {width}x{height}")

# 设置窗口大小
window_width = 1000
window_height = 700

# 计算缩放比例
scale = min(window_width / width, window_height / height, 1.0)
if scale < 1.0:
    display_width = int(width * scale)
    display_height = int(height * scale)
    img_display = cv2.resize(img, (display_width, display_height))
else:
    img_display = img.copy()
    display_width, display_height = width, height

print(f"显示尺寸: {display_width}x{display_height}")

# 创建窗口
cv2.namedWindow('Image Viewer', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Image Viewer', window_width, window_height)

# 显示图像
cv2.imshow('Image Viewer', img_display)

print("操作说明：")
print("- 按 'q' 退出")
print("- 按 '+' 放大")
print("- 按 '-' 缩小")
print("- 鼠标滚轮缩放")
print("- 鼠标拖拽移动图像")

current_scale = scale
offset_x, offset_y = 0, 0
dragging = False


def mouse_callback(event, x, y, flags, param):
    global offset_x, offset_y, dragging, last_x, last_y, current_scale

    if event == cv2.EVENT_LBUTTONDOWN:
        dragging = True
        last_x, last_y = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if dragging:
            dx = x - last_x
            dy = y - last_y
            offset_x = max(0, min(offset_x - dx, display_width - window_width))
            offset_y = max(0, min(offset_y - dy, display_height - window_height))
            last_x, last_y = x, y
            update_display()

    elif event == cv2.EVENT_LBUTTONUP:
        dragging = False

    elif event == cv2.EVENT_MOUSEWHEEL:
        if flags > 0:
            current_scale = min(2.0, current_scale + 0.1)
        else:
            current_scale = max(0.2, current_scale - 0.1)
        update_display()


def update_display():
    global img_display, display_width, display_height, offset_x, offset_y

    new_width = int(width * current_scale)
    new_height = int(height * current_scale)

    img_display = cv2.resize(img, (new_width, new_height))
    display_width, display_height = new_width, new_height

    offset_x = min(offset_x, max(0, display_width - window_width))
    offset_y = min(offset_y, max(0, display_height - window_height))

    show_current_view()


def show_current_view():
    view = img_display[offset_y:offset_y + window_height, offset_x:offset_x + window_width]
    cv2.imshow('Image Viewer', view)


cv2.setMouseCallback('Image Viewer', mouse_callback)

while True:
    key = cv2.waitKey(30) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('+') or key == ord('='):
        current_scale = min(2.0, current_scale + 0.1)
        update_display()
    elif key == ord('-') or key == ord('_'):
        current_scale = max(0.2, current_scale - 0.1)
        update_display()

cv2.destroyAllWindows()