from random import sample
from tkinter import END

from myset import uni_range, power


def cast_str_to_list(entr_hand, my_set_ref):
    p = ((entr_hand.get()).split(','))
    for i in p:
        my_set_ref.append(int(i))


def generate(power_index, entr_hand_myset):
    generate_from = int(uni_range[0])
    generate_to = int(uni_range[1])
    power_set = int(power[power_index])
    entr_hand_myset.insert(END, str(sample(range(generate_from, generate_to), power_set)).strip('[]'))