import numpy as np

def euler_method(t0, x0, h, tk):
    n = int((tk - t0) / h)
    x = np.zeros((n+1, 2))
    x[0] = x0
    for i in range(n):
        x1 = x[i, 0]
        x2 = x[i, 1]
        x[i+1, 0] = x1 + h * (-501 * x1 + 499 * x2 + 1)
        x[i+1, 1] = x2 + h * (500 * x1 - 500 * x2)
    return x


t0 = 0
x0 = np.array([0, 0])
h = 0.05
tk = 1.0


x_euler = euler_method(t0, x0, h, tk)


print("Метод Эйлера:")
print("t\tx1\tx2")
for i in range(0, len(x_euler), 2):
    print("{:.1f}\t{:.4f}\t{:.4f}".format(i*h, x_euler[i, 0], x_euler[i, 1]))



print("Аналитическое решение:")
print("t\tx1\tx2")
for i in range(0, int(tk / h) + 1):
        t = i * h
        x1 = 0.5 + 0.5 * np.exp(-t) - 1000 * t
        x2 = 0.5 - 0.5 * np.exp(-t)
        print("{:.1f}\t{:.4f}\t{:.4f}".format(t, x1, x2))