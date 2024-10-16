from numpy_regression import *
import matplotlib.pyplot as plt #bibliotek för datavisualisering, vanligtvis i form av plotter, grafer och diagram.
import sys
import matrix as mx
import numpy as np #bibliotek för matrisfunktioner

def powers(lst, start, end):
    return mx.array([[num**i for i in range(start, end + 1)] for num in lst])

def poly(a, x):
    return sum(coef * (x ** i) for i, coef in enumerate(a))

def main(filename, degree):
    data = mx.loadtxt(filename)
    X, Y = mx.transpose(data)
    
    Xp = powers(X, 0, degree)
    Yp = powers(Y, 1, 1)
    Xpt = Xp.T

    a = mx.matmul(np.linalg.inv(mx.matmul(Xpt, Xp)), mx.matmul(Xpt, Yp))
    a = a[:, 0]  # Gör om till en endimensionell matris

    # Generate smoother X values for plotting
    X2 = np.linspace(min(X), max(X), 100)
    Y2 = [poly(a, x) for x in X2]

    # Plottar
    plt.plot(X, Y, 'ro', label='Data points')
    plt.plot(X2, Y2, label='Polynomial regression')
    plt.xlabel('Temperature')
    plt.ylabel('Chirps per minute')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    degree = int(sys.argv[2])
    main(sys.argv[1], degree)
