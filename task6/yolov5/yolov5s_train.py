from ultralytics import YOLO


if __name__ == "__main__":
    # 加载模型
    model = YOLO("C:/Users/skw/Desktop/yolov5/weights/yolov5/yolov5s.pt")  # 替换为你的权重文件路径

    # 训练模型
    model.train(data="split_dataset/data.yaml",
                epochs=100,
                batch=32,
                workers=4,
                )
    


'''
#续训代码示例：
from ultralytics import YOLO

if __name__ == "__main__":
    # 加载【中断前保存的 last.pt】,直接续训!
    model = YOLO("runs/detect/train3/weights/last.pt")

    # 继续训练（参数完全不用改，框架会自动接着上次的轮数训）
    model.train(
        data="split_dataset/data.yaml",
        epochs=100,    # 依然写总轮数100,比如训到20轮退出,会从21轮开始训到100
        batch=8,
        workers=2,
        device=0,
        resume=True  # 关键：开启续训模式
    )
'''