from math import cos
from math import pi
from src.optimization import hillclimb
from src.optimization import annealingoptimize
from src.optimization import randomoptimize
from src.optimization import randomrestart
import matplotlib.pyplot as plt

fc = 100


def cost(x):
    x = x[0] / fc
    return 16001 - func(x)
    # return 16160 - func(x)


def func(x):
    if x < 5.2:
        return 10
    elif 5.2 <= x <= 20:
        return x**2
    else:
        return cos(x) + 160 * x
        # return 160 * (cos(2*pi*x) + x)


def run():
    domain = [(-100*fc, 100*fc)]
    explored_random = set()
    explored_hill = set()
    explored_annealing = set()
    ro_res = randomoptimize(domain, cost, explored_random, iterations=100)[0] / fc
    print(f"Random optimize: {ro_res}")
    hc_res = randomrestart(domain, cost, hillclimb, explored_hill, iterations=25)[0] / fc
    print(f"Hill climbing: {hc_res}")
    sa_res = randomrestart(domain, cost, annealingoptimize, explored_annealing, iterations=10, params=[10000, 0.95, 10*fc, True])[0] / fc
    print(f"Simulated annealing: {sa_res}")
    explored_random, explored_hill, explored_annealing = sorted(i/fc for i in list(explored_random)), sorted(i/fc for i in list(explored_hill)), sorted(i/fc for i in list(explored_annealing))
    domain_values = [i/fc for i in range(domain[0][0], domain[0][1]+1)]
    codomain_values, y_random, y_hill, y_annealing = [func(i) for i in domain_values], [func(i) for i in explored_random], [func(i) for i in explored_hill], [func(i) for i in explored_annealing]
    data = [(domain_values, codomain_values, "Function", 100.0, ','), (explored_random, y_random, "Random_optimize", ro_res, '.'), (explored_hill, y_hill, "Hill_climbing", hc_res, '.'), (explored_annealing, y_annealing, "Simulated_annealing", sa_res, '.')]
    for t in data:
        plt.plot(t[0], t[1], linestyle='none', marker=t[4])
        plt.axis([domain[0][0] / fc, domain[0][1] / fc, 0, 17000])
        plt.xlabel('Values explored')
        plt.ylabel('Utility of values')
        plt.title(t[2] + f", max={t[3]}")
        plt.savefig(t[2] + ".png")
        plt.show()


if __name__ == "__main__":
    run()

