import numpy as np
from numpy.core.fromnumeric import transpose

def sub(b, ax):
    r = []
    for i in range(len(b)):
        r.append((abs(b[i] - ax[i])))
    return r

def multiply(a, x):
    ax = []
    for i in range(len(a)):
        sum = 0
        for j in range(len(a)):
            sum += a[i][j] * x[j]
        ax.append(sum)
    return ax

def check(x_new, x_old, epsilon):
    for i in range(len(x_new)):
        if abs(x_new[i] - x_old[i]) > epsilon:
            return False
    return True

def main():
    a = [
        [3.81, 0.25, 1.28, 0.75],
        [2.25, 1.32, 4.58, 0.49],
        [5.31, 6.28, 0.98, 1.04],
        [9.39, 2.45, 3.35, 2.28]
    ]
    b = [4.21, 6.47, 2.38, 10.48]
    a_new = np.array(a)
    b_new = np.array(b)
    a_new, b_new = transpose(a_new)@a_new, transpose(a_new)@b_new
    a = a_new.tolist()
    b = b_new.tolist()
    epsilon = pow(10, -5)
    c = []
    d = []
    for i in range(len(a)):
        line = []
        for j in range(len(a[i])):
            if  i == j:
                line.append(0)
            else:
                line.append(-a[i][j] / a[i][i])
            c.append(line)
            d.append(b[i] / a[i][i])
        x_old = [0, 0, 0, 0]
        x_new = [0, 0, 0, 0]
        k = 1
        while True:
            k += 1
            for i in range(len(x_old)):
                for j in range(len(x_old)):
                    if i > j:
                        x_new[i] += c[i][j] * x_new[j]
                    else:
                        x_new[i] += c[i][j] * x_old[j]
                x_new[i] += d[i]
            ax = multiply(a, x_new)
            if (k % 100) == 0:
                print('Iteration -- ', k)
                print('x: ', x_new)
                r = sub(b, ax)
                print('r: ', r)
            if (check(x_new, x_old, epsilon)):
                print('Iteration -- ', k)
                print('x: ', x_new)
                r = sub(b, ax)
                print('r: ', r)
                break
            x_old = x_new.copy()
            x_new = [0, 0, 0, 0]

if __name__ == '__main__':
    main()