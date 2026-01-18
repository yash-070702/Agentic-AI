import numpy as np
from scipy import linalg

# A = np.array([[2, 1],
#               [1, 3]])
# B=np.array([5,6])

# solve=linalg.solve(A,B)
# print("Solution of the linear equations:", solve)


# A = np.array([[1, 2],
#               [3, 4]])

# A_inv = linalg.inv(A)
# print(A_inv)


# print(A @ A_inv)

#####################################################

# from scipy.optimize import minimize

# def loss(x):
#     return (x - 9)**2

# result = minimize(loss, x0=0)
# print(result.x)

#####################################################

# from scipy import stats

# data = [10, 12, 13, 12, 11, 14, 15]

# mean = stats.gmean(data)
# std = stats.tstd(data)

# print(mean, std)

######################################################

# from scipy.optimize import fsolve

# def equations(vars):
#     x, y = vars
#     return [x + y - 10, x - y - 2]

# solution = fsolve(equations, [0, 0])
# print(solution)

#######################################################

# from scipy.integrate import quad

# def reward_rate(t):
#     return t**2

# result, error = quad(reward_rate, 0, 3)

# print(result)
# print("Estimated error:", error)


from scipy.integrate import dblquad

def cost(y, x):
    return x * y

result, error = dblquad(cost, 0, 2, lambda x: 0, lambda x: 1)
print(result)



