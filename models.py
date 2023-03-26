#! /usr/bin/env python3
# coding: utf-8

import os
import numpy as np


def get_data(file_path="Triax_11bb25.txt"):
    if file_path == '':
        return None
    file_path = file_path.replace("'", "")
    dico = {}
    # s22
    dico["np_deviateur"] = np.loadtxt(file_path)[:, 6]
    dico["deviateur_max"] = max(dico["np_deviateur"])
    # e22
    dico["np_variation_h"] = np.loadtxt(file_path)[:, 1]

    return dico
