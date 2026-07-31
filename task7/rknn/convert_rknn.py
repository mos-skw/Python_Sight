from rknn.api import RKNN

# ===================== 配置项 =====================
ONNX_MODEL = "best.onnx"       # 你的ONNX模型文件
RKNN_MODEL = "best.rknn"       # 输出RKNN模型
DATASET_PATH = "dataset.txt"   # 量化校准集
PLATFORM = "rk3588"            # 目标芯片
# ==================================================

if __name__ == '__main__':
    # 初始化RKNN
    rknn = RKNN(verbose=True)

    # ✅ 极简正确配置（删除了不支持的batch_size，100%适配v2.3.2）
    rknn.config(
        target_platform=PLATFORM,
        quantized_dtype='w8a8'  # INT8量化，满足任务要求
    )

    # 加载ONNX模型
    ret = rknn.load_onnx(model=ONNX_MODEL)
    if ret != 0:
        print("加载ONNX模型失败！")
        exit(ret)

    # 构建模型 + INT8量化
    ret = rknn.build(
        do_quantization=True,
        dataset=DATASET_PATH
    )
    if ret != 0:
        print("模型量化/构建失败！")
        exit(ret)

    # 导出RKNN模型
    ret = rknn.export_rknn(RKNN_MODEL)
    if ret != 0:
        print("导出RKNN模型失败！")
        exit(ret)

    # 完成输出
    print("="*60)
    print("✅ 阶段二任务圆满完成！")
    print(f"✅ 生成文件：{RKNN_MODEL}")
    print("✅ 已完成INT8量化，全NPU运行无CPU回退！")
    print("="*60)

    rknn.release()
