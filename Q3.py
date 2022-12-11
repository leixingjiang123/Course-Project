import numpy as np
from OPT import OPT_method_TwoDimensional
from ThresholdAlgorithm import TwodimensionalThresholdAlgorithm
from DataGenerator import generate_twodimensional

def main():
    p_min = [1,2]
    p_max = [5,4]

    n_experiment = 100

    input_size = 1000

    temp =[]

    for i in range(n_experiment):
        value, weight_x, weight_y = generate_twodimensional(p_min,p_max,input_size)

        ALG = TwodimensionalThresholdAlgorithm(value,weight_x,weight_y,p_min,p_max)

        OPT = OPT_method_TwoDimensional(value,weight_x,weight_y)

        #print(ALG)
        #print(OPT)
        ratio = OPT/ALG

        temp.append(ratio)

    ratios = np.array(temp)
    ratio = ratios.mean()


    print("Average OPT/ALG with 100 experiments is " + str(ratio))


if __name__ == '__main__':
    main()
