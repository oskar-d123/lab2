from matrix import *
import matplotlib.pyplot as plt
import sys

def main(filename):
    data = loadtxt(filename)
    X, Y = transpose(data)
    
    Xp = powers(X, 0, 1)
    Yp = powers(Y, 1, 1)
    Xpt = transpose(Xp)

    [[b], [m]] = matmul(invert(matmul(Xpt, Xp)), matmul(Xpt, Yp))

    # Predict values
    Y_predicted = [b[0] + m[0] * x for x in X]

    # Plotting
    plt.plot(X, Y, 'ro', label='Data points')
    plt.plot(X, Y_predicted, label='Regression line')
    plt.xlabel('Temperature')
    plt.ylabel('Chirps per minute')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main(sys.argv[1])
