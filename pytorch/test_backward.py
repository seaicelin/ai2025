import torch



def test():
    x = torch.tensor(3.0, requires_grad=True)
    y = x**2
    y.backward()
    print(x.grad)

def test2():
    a = torch.tensor(1.0, requires_grad=True)
    b = torch.tensor(2.0, requires_grad=True)
    y = a * 2 + b * 3
    y.backward()
    print(a.grad)
    print(b.grad)

if __name__ == "__main__":
    test2()