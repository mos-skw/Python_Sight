import torch

# 1. 核心判断：CUDA 是否可用（最直接）
print("CUDA可用:", torch.cuda.is_available())

# 2. 查看 PyTorch 版本及编译信息
print("PyTorch版本:", torch.__version__)

# 3. 查看 PyTorch 编译时使用的 CUDA 版本（若为 CPU 版此项为空或显示 None）
print("编译CUDA版本:", torch.version.cuda)