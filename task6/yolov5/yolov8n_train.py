from ultralytics import YOLO


if __name__ == "__main__":
    # 加载模型
    model = YOLO("D:\\1aworkplace\\python vscode cv\\project6\\yolov5\\weights\\yolov8\\yolov8n.pt")  # 替换为你的权重文件路径

    # 训练模型
    model.train(data="split_dataset\data.yaml",
                epochs=100,
                batch=64,
                workers=4,
                )