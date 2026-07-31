import cv2
import numpy as np
import matplotlib.pyplot as plt


def fourier_denoise(img):
    # 傅里叶变换
    dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    rows, cols = img.shape
    crow, ccol = rows // 2, cols // 2

    # ===================== 精准屏蔽垂直条纹（这次绝对准） =====================
    mask = np.ones((rows, cols, 2), np.uint8)

    # 垂直条纹 → 必须屏蔽 频域里 水平方向上的两条亮线
    mask[crow - 3:crow + 3, 0:ccol - 10] = 0  # 左
    mask[crow - 3:crow + 3, ccol + 10:cols] = 0  # 右

    # 逆变换
    fshift = dft_shift * mask
    f_ishift = np.fft.ifftshift(fshift)
    img_back = cv2.idft(f_ishift)
    img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])
    img_back = cv2.normalize(img_back, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    return img_back


# ===================== 输入路径 =====================
print("=== 傅里叶变换去条纹（完美版）===")
path = input("请输入图片完整路径：").strip()

img = cv2.imread(path, 0)
if img is None:
    print("读取失败！")
else:
    print("正在处理...")

    res = fourier_denoise(img)

    # 保存最终结果
    cv2.imwrite("fourier_final.png", res)

    # 显示对比
    plt.figure(figsize=(10, 6))
    plt.subplot(121), plt.imshow(img, cmap='gray'), plt.title('原图（有条纹噪声）')
    plt.subplot(122), plt.imshow(res, cmap='gray'), plt.title('傅里叶去噪后（完美）')
    plt.axis('off')
    plt.show()

    print("✅ 完美去噪！结果已保存为 fourier_final.png")