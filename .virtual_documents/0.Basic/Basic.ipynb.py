import torch


x = torch.empty(2, 3)  # 2 row, 3 column
x


y = torch.empty(3, 2, 3)
y, y.size()


rand_tensor = torch.rand(2, 2)
rand_tensor


zeros_tensor = torch.zeros(2, 2)
zeros_tensor, zeros_tensor.size()


ones_tensor = torch.ones(2, 2)
print(ones_tensor.type())
print(ones_tensor.dtype)


x = torch.tensor([1, 2])
y = torch.tensor([3, 4])
z = y.add(x)
print(f"y={y} z={z}")


y.add_(x)
print(f"y={y}")


x = torch.rand(5,3)


x


x[:, 0] # to get only first column


x[1, :] # row 1 with all columns


x[3, 1] # row 3 col 1


x[3, 1].item() # to get the actual value


x = torch.rand(4,4)


x


y = x.view(16)


y


y = x.view(-1, 8)
y


y.size()


import numpy as np


a = torch.ones(5)
a


b = a.numpy()
b, type(b)


a.add_(1)
a


b


a = np.ones(5)
a


b = torch.from_numpy(a)
b





a += 1
a


b


if torch.cuda.is_available():
    device = torch.device('cuda')


x = torch.ones(5, device=device)


y = torch.ones(5)


x


y


y = y.to(device)


y


z = x+y


z.numpy()


z = z.to('cpu')


z



