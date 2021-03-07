from tkinter import DISABLED

from myset import var, var_but


def count_var(event):
    n = 4
    g = 23
    n += 2
    num = (n + g % 60) % 30 + 1
    return var.config(text=('Варіант', num)), var_but.config(state=DISABLED)