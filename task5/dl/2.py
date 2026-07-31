import numpy as np
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

# ===================== GPU 模式 =====================
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("运行设备：", device)

# 生成数据
np.random.seed(42)
x = np.linspace(-2, 2, 300).reshape(-1, 1)
y = x**2 + 0.2 * np.random.randn(*x.shape)

x_tensor = torch.tensor(x, dtype=torch.float32).to(device)
y_tensor = torch.tensor(y, dtype=torch.float32).to(device)

# 模型
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Sequential(
            nn.Linear(1, 32), nn.ReLU(),
            nn.Linear(32, 16), nn.ReLU(),
            nn.Linear(16, 1)
        )
    def forward(self, x):
        return self.fc(x)

model = Net().to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
criterion = nn.MSELoss()

# 动态绘图
plt.ion()
fig, ax = plt.subplots(figsize=(8,5))
ax.scatter(x, y, s=15, color='blue', alpha=0.6, label='真实数据')
line, = ax.plot(x, np.zeros_like(x), 'r-', linewidth=2, label='拟合曲线')
ax.legend()
ax.set_xlabel("x")
ax.set_ylabel("y")

# 训练
for epoch in range(1000):
    pred = model(x_tensor)
    loss = criterion(pred, y_tensor)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 20 == 0:
        line.set_ydata(pred.detach().cpu().numpy())
        plt.title(f'GPU训练 | Epoch {epoch} | Loss={loss.item():.3f}')
        plt.pause(0.05)

plt.ioff()
plt.show()