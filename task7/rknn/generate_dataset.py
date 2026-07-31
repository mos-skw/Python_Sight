import os

# ===================== 配置项（不用改） =====================
IMAGE_FOLDER = "calib_data"  # 图片文件夹名称
TXT_FILE = "dataset.txt"     # 输出的校准列表文件
# 支持的图片格式（常见格式全包含）
IMG_FORMATS = (".jpg", ".jpeg", ".png", ".bmp", ".JPG", ".JPEG", ".PNG", ".BMP")

# ============================================================

def generate_dataset_txt():
    # 检查图片文件夹是否存在
    if not os.path.exists(IMAGE_FOLDER):
        print(f"❌ 错误：文件夹 {IMAGE_FOLDER} 不存在！")
        print(f"请先创建 {IMAGE_FOLDER} 文件夹，并放入50~100张图片")
        return

    # 获取所有图片路径
    img_paths = []
    for filename in os.listdir(IMAGE_FOLDER):
        if filename.endswith(IMG_FORMATS):
            # 生成相对路径（RKNN工具要求的格式）
            img_path = os.path.join(IMAGE_FOLDER, filename)
            img_paths.append(img_path)

    # 检查是否找到图片
    if len(img_paths) == 0:
        print(f"❌ 错误：{IMAGE_FOLDER} 文件夹中没有找到任何图片！")
        return

    # 写入 dataset.txt
    with open(TXT_FILE, "w", encoding="utf-8") as f:
        for path in img_paths:
            f.write(path + "\n")

    # 打印结果
    print("="*50)
    print(f"✅ 成功生成 {TXT_FILE}！")
    print(f"✅ 共扫描到 {len(img_paths)} 张图片")
    print(f"✅ 路径已自动写入文件，可直接用于RKNN量化！")
    print("="*50)

if __name__ == "__main__":
    generate_dataset_txt()
