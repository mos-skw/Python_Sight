from PIL import Image, ImageDraw
import matplotlib.pyplot as plt


def process_image_with_pil(image_path):
    """
    使用PIL处理图像
    """
    try:
        # 读取图像
        img = Image.open(image_path)
        print(f"原始图像大小：{img.size}")

        # 显示原始图像
        plt.figure(figsize=(12, 4))
        plt.subplot(1, 3, 1)
        plt.imshow(img)
        plt.title("原始图像")
        plt.axis('off')

        # 在图像上画红色框
        draw = ImageDraw.Draw(img)
        # 获取图像尺寸
        width, height = img.size
        # 画一个红色矩形框（在图像中央区域）
        box_size = min(width, height) // 3
        left = (width - box_size) // 2
        top = (height - box_size) // 2
        right = left + box_size
        bottom = top + box_size
        draw.rectangle([left, top, right, bottom], outline='red', width=5)

        # 显示画框后的图像
        plt.subplot(1, 3, 2)
        plt.imshow(img)
        plt.title("画框后的图像")
        plt.axis('off')

        # 缩放到400×400
        resized_img = img.resize((400, 400))

        # 显示缩放后的图像
        plt.subplot(1, 3, 3)
        plt.imshow(resized_img)
        plt.title(f"缩放后图像 (400×400)")
        plt.axis('off')

        plt.tight_layout()
        plt.show()

        # 保存结果
        resized_img.save('processed_image.jpg')
        print("处理后的图像已保存为 'processed_image.jpg'")

        return resized_img

    except FileNotFoundError:
        print(f"找不到图像文件：{image_path}")
        print("请确保图像文件存在，或修改路径为正确的图像文件")
        return None


# 使用示例（请将'your_image.jpg'替换为实际的图像文件路径）
# processed_img = process_image_with_pil('your_image.jpg')

# 如果没有实际图像，可以用下面的代码创建一个示例图像
def create_sample_image():
    """创建一个示例图像用于演示"""
    # 创建一个空白图像
    img = Image.new('RGB', (600, 400), color='white')
    draw = ImageDraw.Draw(img)

    # 画一些图形
    draw.rectangle([50, 50, 250, 200], outline='blue', width=3)
    draw.ellipse([300, 50, 500, 200], outline='green', width=3)
    draw.text((200, 250), "Sample Image", fill='black')

    return img


# 使用示例图像演示
sample_img = create_sample_image()
sample_img.save('sample_image.jpg')
processed_img = process_image_with_pil('sample_image.jpg')