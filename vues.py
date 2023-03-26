import os

import matplotlib.pyplot as plt
import numpy as np


def get_file():
    file_path = input(
        "Drag n' drop un fichier de données à traiter \n (vide pour finir) ?> "
    )
    return file_path


def get_pressure():
    pression = input("Pression de l'eau en kPa \n (vide pour auto) ?> ")
    return pression


def tracer_datas(datas):
    idx = 0
    ax_cercle = {}
    x1_cercle = {}
    x2_cercle = {}
    r_cercle = {}
    for data in datas:
        idx += 1
        pression = data["pression"]
        deviateur_max = data['deviateur_max']

        deviateur_max = deviateur_max / 1000
        theta = np.linspace(0, 2*np.pi, 100)
        r_cercle[idx] = deviateur_max / 2

        # centre
        x1_cercle[idx] = r_cercle[idx]*np.cos(theta) + (pression*2 + deviateur_max)/2
        x2_cercle[idx] = r_cercle[idx]*np.sin(theta)


    fig, ax_cercle = plt.subplots(1)

    for index in range(1, idx+1):
        ax_cercle.plot(x1_cercle[index], x2_cercle[index])
        ax_cercle.set_aspect(1)
    # plt.xlim(-1.25,1.25)
    # plt.ylim(-1.25,1.25)
    # plt.savefig("plot_circle_matplotlib_01.png", bbox_inches='tight')

    plt.grid(linestyle=':')
    plt.title("Cercle de mohr", fontsize=24)
    plt.xlabel("Contrainte normale", fontsize=18)
    plt.ylabel("Cisaillement", fontsize=18)

    plt.show()
