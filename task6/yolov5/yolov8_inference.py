from ultralytics import YOLO
import cv2
import os

# 获取当前脚本所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 拼接权重文件的绝对路径
model_path = os.path.join(current_dir, "yolov8n.pt")

# 加载模型（传入绝对路径）
model = YOLO(model_path)

# 推理图片（同样建议使用绝对路径）
img_path = os.path.join(current_dir, "data/images/bus.jpg")
results = model(img_path)

# 可视化并保存结果
for r in results:
    annotated_frame = r.plot()
    cv2.imshow("YOLOv8 Inference", annotated_frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    output_path = os.path.join(current_dir, "yolov8_bus_result.jpg")
    cv2.imwrite(output_path, annotated_frame)