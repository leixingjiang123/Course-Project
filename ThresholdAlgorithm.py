import numpy as np


def phi(taken_weight,p_min,p_max):
    beta = 1/(1+np.log(p_max/p_min))
    if taken_weight < beta:
        return p_min
    else:
        return p_min*np.exp(taken_weight/beta -1)


def SingledimensionalThresholdAlgorithm(value,weight,p_min,p_max):
    input_size = len(value)
    taken_weight = 0
    utility =0

    for i in range(input_size):
        value_density = value[i]/weight[i]
        if value_density >= phi(taken_weight,p_min,p_max) and (taken_weight+weight[i]) <=1:
            utility += value[i]
            taken_weight +=weight[i]

    return utility


def TwodimensionalThresholdAlgorithm(value,weight_x,weight_y,p_min,p_max):
    input_size = len(value)
    utility = 0
    taken_weight_x = 0
    taken_weight_y = 0

    for i in range(input_size):

        value_density_x = value[i]/weight_x[i]
        value_density_y = value[i]/weight_y[i]
        if value_density_x >= phi(taken_weight_x,p_min[0],p_max[0]) and value_density_y >= phi(taken_weight_x, p_min[1], p_max[1]) and taken_weight_x + weight_x[i] <= 1 and taken_weight_y + weight_y[i] <= 1:
            utility += value[i]
            taken_weight_x += weight_x[i]
            taken_weight_y += weight_y[i]

    return utility


