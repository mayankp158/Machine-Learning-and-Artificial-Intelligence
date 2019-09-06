import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x , y):
    #nuber of observations/points
    n = np.size(x)

    #mean of x and y vector
    m_x = np.mean(x)
    m_y = np.mean(y)

    #calc cross dev and deviation abt x
    SS_xy = np.sum(x * y) - n * m_x * m_y
    SS_xx = np.sum(x * x) - n * m_x * m_x

    #calculating regression coff
    m = SS_xy / SS_xx
    c = m_y - m * m_x
    return [m,c]

def plot_regression_line(x, y, b):

    #plotting actual pt as scatter plot
    plt.scatter(x, y, color="m",marker="o",s=30)

    #predicted response vector
    y_pred = b[1] * x + b[0]

    #plotting regression line
    plt.scatter(x, y_pred, color="g")
    plt.plot(x,y_pred,color="b")

    plt.xlabel('x')
    plt.ylabel('y')

    plt.show()

def main():

    #observations
    x = np.array([0,1,2,3,4,5,6,7,8,9])
    y = np.array([1,3,2,5,7,8,8,9,10,12])

    #estimating coff
    m , c = estimate_coef(x,y)
    print("Estimated coefficient:\n")
    print("slope m = ", m)
    print("y-intercept c =",  c)

    #plotting regression line
    plot_regression_line(x, y, [c,m])

if __name__ == "__main__":
    main()


