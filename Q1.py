import numpy as np
from OPT import OPT_method
from ThresholdAlgorithm import SingledimensionalThresholdAlgorithm
from DataGenerator import generate, generate_hard

def main():
    p_min = 1
    p_max = 5

    n_experiment = 100

    input_size = 1000

    temp =[]

    for i in range(n_experiment):
        #value, weight = generate(p_min,p_max,input_size)

        value, weight = generate_hard(p_min, input_size)

        ALG = SingledimensionalThresholdAlgorithm(value,weight,p_min,p_max)
        OPT = OPT_method(value,weight)

        ratio = OPT/ALG

        temp.append(ratio)

    ratios = np.array(temp)
    ratio = ratios.mean()


    print("Average OPT/ALG with 100 experiments is " + str(ratio))
    print("Alpha is " + str((1+np.log(p_max/p_min))))


if __name__ == '__main__':
    main()



