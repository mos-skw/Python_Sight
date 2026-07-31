from ultralytics import YOLO

# 加载模型
model = YOLO("best.pt")

# 只保留核心参数，完全不检查依赖、不卡住
model.export(
    format="onnx",
    imgsz=640,
    batch=1,
    opset=12,
    simplify=False,  # 关闭自动简化
    device="cpu"
)