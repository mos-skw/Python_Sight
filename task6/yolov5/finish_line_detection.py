# 导入Ultralytics YOLO库：用于加载训练好的模型，实现目标检测推理
from ultralytics import YOLO
# 导入OpenCV库：用于读取图片、绘制检测框/终点线、保存结果图片
import cv2
# 导入操作系统库：用于遍历文件夹、创建输出目录、处理文件路径
import os
# 关闭SSL验证，彻底解决联网报错
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# ===================== 核心函数：终点线检测与判定 =====================
# 函数功能：加载训练好的模型，对测试图片批量推理，判定目标是否越过终点线
# 参数说明：
# model_path：训练好的模型权重路径（best.pt）
# test_image_dir：测试图片所在的文件夹路径
# output_dir：处理后的结果图片保存路径
def detect_finish_line(model_path, test_image_dir, output_dir):
    # 1. 加载本地训练完成的YOLO模型（禁止联网下载）
    model = YOLO(model_path, task='detect')

    # 2. 创建输出文件夹（如果文件夹不存在则自动创建，存在则不报错）
    os.makedirs(output_dir, exist_ok=True)

    # 3. 遍历测试文件夹中的所有文件
    for img_name in os.listdir(test_image_dir):
        # 过滤文件：只处理 jpg/png 格式的图片，跳过其他文件
        if not img_name.endswith((".jpg", ".png")):
            continue
        
        # 拼接图片的完整路径（文件夹路径 + 图片名称）
        img_path = os.path.join(test_image_dir, img_name)
        # 用OpenCV读取图片
        img = cv2.imread(img_path)
        # 如果图片读取失败（损坏/路径错误），跳过该图片
        if img is None:
            continue
        
        # ===================== 终点线位置设置 =====================
        # 获取图片的 高度h 和 宽度w
        h, w = img.shape[:2]
        # 定义终点线的纵坐标：图片高度的 75% 位置（3/4处）
        finish_line_y = int(h * 0.75)

        # ===================== YOLO模型推理（核心检测） =====================
        results = model(img, verbose=False)  # verbose=False 关闭冗余日志

        # ===================== 绘制红色终点线 =====================
        cv2.line(img, (0, finish_line_y), (w, finish_line_y), (0, 0, 255), 2)

        # 初始化全局终点标志
        finish_flag = False

        # ===================== 遍历模型检测到的所有目标 =====================
        for r in results:
            boxes = r.boxes
            for box in boxes:
                # 提取检测框坐标并转为整数
                x1, y1, x2, y2 = box.xyxy[0].int().tolist()
                # 获取置信度
                conf = box.conf[0].item()

                # 绘制绿色检测框
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

                # ===================== 文字绘制在【框内】（核心修改） =====================
                # 文字位置：框内左上角（x1+5, y1+20），完全在绿色框内部
                text = f"green_sign {conf:.2f}"
                cv2.putText(
                    img, text, 
                    (x1 + 5, y1 + 20),  # 框内坐标
                    cv2.FONT_HERSHEY_SIMPLEX, 
                    0.5, 
                    (0, 255, 0),  # 绿色文字
                    1
                )

                # 判定当前目标是否越过终点线
                current_box_finish = False
                if y2 >= finish_line_y:
                    current_box_finish = True
                    finish_flag = True

                # ===================== 终点标志显示在【框内】 =====================
                if current_box_finish:
                    # 在框内第二行显示 FINISH 标志
                    cv2.putText(
                        img, "FINISH", 
                        (x1 + 5, y1 + 40),  # 置信度文字下方
                        cv2.FONT_HERSHEY_SIMPLEX, 
                        0.5, 
                        (0, 0, 255),  # 红色文字
                        1
                    )

        # ===================== 全局终点提示 =====================
        if finish_flag:
            cv2.putText(img, "Finish", (w//2 - 150, h//2), 
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        # 保存结果图片
        output_path = os.path.join(output_dir, img_name)
        cv2.imwrite(output_path, img)
        print(f"处理完成：{output_path}")

# ===================== 主函数入口 =====================
if __name__ == "__main__":
    trained_model_path = "runs/detect/train3/weights/best.pt"  # 模型路径
    test_images_dir = "split_dataset/images/test"           # 测试集路径
    output_result_dir = "finish_line_results"                  # 输出文件夹

    # 执行检测
    detect_finish_line(trained_model_path, test_images_dir, output_result_dir)