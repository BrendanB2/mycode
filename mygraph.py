#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

def main():

    plt.style.use('_mpl-gallery')

    # make data
    np.random.seed(1)
    x = 4 + np.random.normal(0, 1.5, 200)

    # plot:
    fig, ax = plt.subplots()

    ax.hist(x, bins=15, linewidth=1.0, edgecolor="black")

    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
           ylim=(0, 56), yticks=np.linspace(0, 56, 9)) 

    plt.savefig("/home/student/mycode/mygraph2.png")
    plt.savefig("/home/student/static/mygraph2.png")

main()
