import numpy as np




def generate(p_min, p_max, input_size, epsilon=1e-3):

    weight = np.random.uniform(0, epsilon, size=input_size)
    value = np.random.uniform(p_min, p_max, size=input_size) * weight

    return value, weight

def generate_hard(p_min, input_size, epsilon=1e-3):

    weight = np.random.uniform(0, epsilon, size=input_size)
    value = np.random.uniform(p_min, p_min+1e-3, size=input_size) * weight

    return value, weight


def generate_twodimensional(p_min, p_max, input_size, epsilon=1e-3):

    p_max_temp = min(p_max[0],p_max[1])
    p_min_temp = max(p_min[0],p_min[1])

    weight_x = np.random.uniform(0, epsilon, size=input_size)
    weight_y = np.random.uniform(0, epsilon, size=input_size)

    value = np.random.uniform(p_min_temp,p_max_temp, size=input_size) *weight_y

    return value, weight_x, weight_y
