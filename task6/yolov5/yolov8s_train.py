from ultralytics import YOLO


if __name__ == "__main__":
    # 加载模型
    model = YOLO("C:/Users/skw/Desktop/yolov5/weights/yolov5/yolov8s.pt")  # 替换为你的权重文件路径

    # 训练模型
    model.train(data="split_dataset\data.yaml",
                epochs=200,
                batch=32,
                workers=4,
                )
