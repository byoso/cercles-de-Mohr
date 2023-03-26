#! /usr/bin/env python3
# coding: utf-8

import os
from models import get_data
from vues import get_pressure, get_file, tracer_datas
from helpers import get_pressure_auto
import gui
import tkinter as tk


GUI = True


def main():
    # get the datas
    datas = []
    if GUI:
        gui.gui()
    else:
        while True:
            file_path = get_file()
            if not file_path:
                break
            data = get_data(file_path)
            pression = get_pressure()
            if pression == "":
                data['pression'] = get_pressure_auto(file_path)
            else:
                data['pression'] = int(get_pressure())
            datas.append(data)
        tracer_datas(datas)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n<Execution interompue>")
