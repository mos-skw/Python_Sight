import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# ===================== 【GPU 自动配置】 =====================
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"✅ 运行设备: {device}")

# ===================== 超参数 =====================
batch_size = 64    # 批次大小
lr = 0.001         # 学习率
epochs = 5         # 训练轮数

# ===================== 数据预处理与加载 =====================
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

# 下载训练集 & 测试集
train_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
test_dataset = datasets.MNIST(root='./data', train=False, transform=transform)

train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

# ===================== 搭建 CNN 模型（LeNet） =====================
class LeNet(nn.Module):
    def __init__(self):
        super(LeNet, self).__init__()
        # 卷积层 + 池化层（提取图像特征）
        self.conv_layer = nn.Sequential(
            nn.Conv2d(1, 16, 3),  # 卷积
            nn.ReLU(),            # 激活
            nn.MaxPool2d(2),      # 池化

            nn.Conv2d(16, 32, 3),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )

        # 全连接层（分类）
        self.fc_layer = nn.Sequential(
            nn.Linear(32 * 5 * 5, 128),
            nn.ReLU(),
            nn.Linear(128, 10)
        )

    def forward(self, x):
        x = self.conv_layer(x)
        x = torch.flatten(x, 1)
        x = self.fc_layer(x)
        return x

# ===================== 模型、损失函数、优化器 =====================
model = LeNet().to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=lr)

# ===================== 测试函数（计算测试集准确率） =====================
def test_model():
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            _, pred = torch.max(output, 1)
            correct += (pred == target).sum().item()
            total += target.size(0)
    acc = 100 * correct / total
    return acc

# ===================== 训练函数（实时打印信息） =====================
print("\n======= 开始训练 =======")
for epoch in range(epochs):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)

        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()

        # 实时打印：Epoch | Step | Loss
        if batch_idx % 100 == 0:
            print(f"Epoch: {epoch+1:2d} | Step: {batch_idx:3d} | Loss: {loss.item():.4f}")

    # 每个 Epoch 结束后输出测试集准确率
    test_acc = test_model()
    print(f"\n=== Epoch {epoch+1} 结束 ===")
    print(f"✅ 测试集准确率: {test_acc:.2f}%\n")

print("======= 训练完成 =======")