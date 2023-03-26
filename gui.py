#! /usr/bin/env python3


import tkinter as tk

bg_color = "#3d6466"


def gui():
    root = tk.Tk()
    root.title("Cercles de Mohr")
    root.eval("tk::PlaceWindow . center")
    frame = tk.Frame(root, width=800, height=600, bg=bg_color)
    frame.grid(row=0, column=0)
    frame.pack_propagate(False)

    tk.Label(frame, text="Enter a file", bg=bg_color, fg="white").pack()


    root.mainloop()
