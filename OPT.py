import cvxpy
import numpy as np
def OPT_method(value,weight):

    x =cvxpy.Variable(len(value), boolean = True)

    utility = sum(cvxpy.multiply(value, x))
    objective =cvxpy.Maximize(utility)

    constraints = cvxpy.multiply(weight, x) <= 1

    problem = cvxpy.Problem(objective,[constraints])
    problem.solve(solver = cvxpy.GLPK_MI)

    return problem.value

def OPT_method_TwoDimensional(value,weight_x,weight_y):

    x =cvxpy.Variable(len(value), boolean = True)

    utility = sum(cvxpy.multiply(value, x))
    objective =cvxpy.Maximize(utility)

    constraints_1 = cvxpy.multiply(weight_x, x) <= 1
    constraints_2 = cvxpy.multiply(weight_y, x) <= 1

    problem = cvxpy.Problem(objective,[constraints_1,constraints_2])
    problem.solve(solver = cvxpy.GLPK_MI)

    return problem.value