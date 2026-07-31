import torch
print(torch.cuda.is_available())  # True
print(torch.version.cuda)        # 12.8
print("RTX5060 正常使用GPU！")