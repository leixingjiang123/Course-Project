import os
import numpy as np
import matplotlib.pyplot as plt
from OPT import OPT_method
from ThresholdAlgorithm import SingledimensionalThresholdAlgorithm
from DataGenerator import generate

def main():
    p_min = 1
    p_max = 5
    input_size_t = 1000

    n_experiment = 100
    epsilons = [1e-3, 1e-2, 1e-1, 1]

    result = {
        "ratio":[],
        "epsilons":epsilons,
        "alpha":[]
    }

    for epsilon in epsilons:
        ratios_temp =[]
        for i in range(n_experiment):
            value, weight = generate(p_min,p_max,input_size_t,epsilon)

            ALG = SingledimensionalThresholdAlgorithm(value,weight,p_min,p_max)
            OPT = OPT_method(value,weight)
            ratio = OPT/ALG

            ratios_temp.append(ratio)

        ratios = np.array(ratios_temp)

        result["ratio"].append(ratios.mean())

        result["alpha"].append((1+np.log(p_max/p_min)))

    root = os.path.dirname(__file__)
    plt.plot(result["epsilons"],result["ratio"], label = "Experiment Result")
    plt.plot(result["epsilons"],result["alpha"], label = "(Alpha-Competitive)")
    plt.xscale("log")
    plt.xlabel("epsilons")
    plt.ylabel("Average OPT/ALG (100 experiments)")
    leg = plt.legend(loc='upper center')
    plt.savefig(os.path.join(root, "result", "ratio_vs_epsilons.png"))

if __name__ == '__main__':
    main()