from datetime import datetime
import random
from matplotlib import pyplot as plt
from numba import jit

@jit
def calculate_pi_using_monte_carlo(n):
    """
    Calculates pi using monte carlo method.
    """
    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []
    inside_circle = 0
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)

    pi = 4 * inside_circle / n
    return pi, x_inside, y_inside, x_outside, y_outside

n = 100000000
start_date = datetime.now()
pi, x_inside, y_inside, x_outside, y_outside = calculate_pi_using_monte_carlo(n)
print(pi)
print(datetime.now() - start_date)
# plt.plot(x_inside, y_inside, '.', color = 'red')
# plt.plot(x_outside, y_outside, '.', color = 'blue')
# plt.show()


