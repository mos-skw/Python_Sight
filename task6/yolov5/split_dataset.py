import os      # 导入os库，用于文件路径操作、目录创建等
import shutil  # 导入shutil库，用于文件复制
import random  # 导入random库，用于随机打乱文件顺序

# ---------------------- 路径配置 ----------------------
# 原始数据读取位置：图片和标签的根目录
original_images_dir = "dataset/images"  # 原始图片存放文件夹（读取位置）
original_labels_dir = "dataset/labels"  # 原始标签存放文件夹（读取位置）

# 输出数据保存位置：划分后的训练/验证/测试集根目录
output_dir = "split_dataset"
# 训练集图片/标签保存位置
train_images_dir = os.path.join(output_dir, "images/train")  # 训练集图片保存路径
val_images_dir = os.path.join(output_dir, "images/val")      # 验证集图片保存路径
test_images_dir = os.path.join(output_dir, "images/test")    # 测试集图片保存路径
# 验证集图片/标签保存位置
train_labels_dir = os.path.join(output_dir, "labels/train")  # 训练集标签保存路径
val_labels_dir = os.path.join(output_dir, "labels/val")      # 验证集标签保存路径
test_labels_dir = os.path.join(output_dir, "labels/test")    # 测试集标签保存路径

# ---------------------- 目录创建 ----------------------
# 循环创建所有输出目录（若目录已存在则跳过，避免报错）
for dir_path in [
    train_images_dir, val_images_dir, test_images_dir,
    train_labels_dir, val_labels_dir, test_labels_dir
]:
    os.makedirs(dir_path, exist_ok=True)  # 创建目录，exist_ok=True表示目录存在时不报错

# ---------------------- 文件列表获取与打乱 ----------------------
# 从 original_images_dir（读取位置） 获取所有 .jpg 图片文件名
image_files = [f for f in os.listdir(original_images_dir) if f.endswith(".jpg")]
random.shuffle(image_files)  # 随机打乱图片文件名顺序，保证划分的随机性

# ---------------------- 数据集比例划分（8:1:1） ----------------------
total = len(image_files)                # 统计图片总数量
train_end = int(total * 0.8)            # 训练集结束索引（前80%）
val_end = train_end + int(total * 0.1)  # 验证集结束索引（中间10%）
train_files = image_files[:train_end]   # 训练集文件列表（切片：0到train_end）
val_files = image_files[train_end:val_end]  # 验证集文件列表（切片：train_end到val_end）
test_files = image_files[val_end:]      # 测试集文件列表（切片：val_end到末尾）

# ---------------------- 文件复制函数 ----------------------
# ---------------------- 文件复制函数 ----------------------
def copy_files(file_list, src_img, src_lbl, dst_img, dst_lbl):
    """
    批量复制图片和对应的标签文件
    参数说明：
    - file_list: 待复制的文件名列表
    - src_img: 图片源文件夹（读取位置）
    - src_lbl: 标签源文件夹（读取位置）
    - dst_img: 图片目标文件夹（保存位置）
    - dst_lbl: 标签目标文件夹（保存位置）
    """
    for file in file_list:
        # ==================== 新增：安全检查开始 ====================
        # 1. 构造当前图片和对应标签的完整路径
        current_img_path = os.path.join(src_img, file)
        label_file = os.path.splitext(file)[0] + ".txt"
        current_lbl_path = os.path.join(src_lbl, label_file)

        # 2. 检查文件是否都存在
        img_exists = os.path.exists(current_img_path)
        lbl_exists = os.path.exists(current_lbl_path)

        # 3. 如果任意文件缺失，打印提示并跳过本轮循环（不执行后面的原代码）
        if not img_exists:
            print(f"[Warning] 图片未找到，已跳过: {file}")
            continue
        if not lbl_exists:
            print(f"[Info] 图片无标签（可能是背景图），已跳过: {file}")
            continue
        # ==================== 新增：安全检查结束 ====================
        # 复制图片：从 src_img（读取位置） 到 dst_img（保存位置）
        shutil.copy(os.path.join(src_img, file), dst_img)
        # 生成对应的标签文件名（将.jpg后缀替换为.txt）
        label_file = os.path.splitext(file)[0] + ".txt"
        # 复制标签：从 src_lbl（读取位置） 到 dst_lbl（保存位置）
        shutil.copy(os.path.join(src_lbl, label_file), dst_lbl)

# ---------------------- 执行数据集划分 ----------------------
# 复制训练集：从原始路径 到 训练集保存路径
copy_files(train_files, original_images_dir, original_labels_dir, train_images_dir, train_labels_dir)
# 复制验证集：从原始路径 到 验证集保存路径
copy_files(val_files, original_images_dir, original_labels_dir, val_images_dir, val_labels_dir)
# 复制测试集：从原始路径 到 测试集保存路径
copy_files(test_files, original_images_dir, original_labels_dir, test_images_dir, test_labels_dir)

# ---------------------- 结果输出 ----------------------
print(f"划分完成：\n训练集 {len(train_files)}，验证集 {len(val_files)}，测试集 {len(test_files)}")