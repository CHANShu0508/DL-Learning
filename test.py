import torch

x = torch.tensor([2, 3], requires_grad=True)
y = x ** 2

y.backward
