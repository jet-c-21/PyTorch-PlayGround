import torch


x = torch.randn(3, requires_grad=True)
x


y = x + 2
y


z = y * y * 2
z


z = z.mean()
z


z.backward() # dz / dx


x.grad



