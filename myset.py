from tkinter import *
from tkinter import messagebox
from random import sample
from tkinter import END


def count_var(event):
    n = 4
    g = 23
    n += 2
    num = (n + g % 60) % 30 + 1
    return var.config(text=('Варіант - '+str(num)+ "\t\t\t")), var_but.config(state=DISABLED)

def power_func(event):
    power_a = (entr_pow_A.get()).split(' ')
    power_b = (entr_pow_B.get()).split(' ')
    power_c = (entr_pow_C.get()).split(' ')
    if power_a[0].isdigit() and power_b[0].isdigit() and power_c[0].isdigit():
        power.append(power_a[0])
        power.append(power_b[0])
        power.append(power_c[0])
        but_pow.config(state=DISABLED)
        entr_pow_A.config(state=DISABLED)
        entr_pow_B.config(state=DISABLED)
        entr_pow_C.config(state=DISABLED)
        uni_but.config(state=NORMAL)
    else:
        messagebox.showinfo('Error', 'Ви ввели не чисельне значення.')


def create_uni(event):
    # TODO decoment
    start = ['0'] #(entry_start.get()).split(' ')
    end = ['255'] #(entry_end.get()).split(' ')
    if start[0].isdigit() and end[0].isdigit() and int(start[0]) >= 0 and int(end[0]) <= 255:
        uni_range.append(start[0])
        uni_range.append(end[0])
        uni_but.config(state=DISABLED)
        entry_start.config(state=DISABLED)
        entry_end.config(state=DISABLED)
        but_hand_A.config(state=NORMAL)
        but_hand_B.config(state=NORMAL)
        but_hand_C.config(state=NORMAL)
    else:
        messagebox.showinfo('Error', 'Спробуйте ще раз. \n Допустимий діапазон від 0 до 255.')


def generate_a():
    generate(0, entr_hand_A)
    cast_str_to_list(entr_hand_A, set_a)


def generate_b():
    generate(1, entr_hand_B)
    cast_str_to_list(entr_hand_B, set_b)


def generate_c():
    generate(2, entr_hand_C)
    cast_str_to_list(entr_hand_C, set_c)


def cast_str_to_list(entr_hand, my_set_ref):
    p = ((entr_hand.get()).split(','))
    for i in p:
        my_set_ref.append(int(i))


def generate(power_index, entr_hand_myset):
    generate_from = int(uni_range[0])
    generate_to = int(uni_range[1])
    power_set = int(power[power_index])
    entr_hand_myset.insert(END, str(sample(range(generate_from, generate_to), power_set)).strip('[]'))

def save_gen_sets():
    entr_hand_A.config(state=DISABLED)
    entr_hand_B.config(state=DISABLED)
    entr_hand_C.config(state=DISABLED)
    but_hand_A.config(state=DISABLED)
    but_hand_B.config(state=DISABLED)
    but_hand_C.config(state=DISABLED)
    windows_menu.entryconfig(windows_menu.index('Window 2'), state=NORMAL)
    windows_menu.entryconfig(windows_menu.index('Window 3'), state=NORMAL)
    windows_menu.entryconfig(windows_menu.index('Window 4'), state=NORMAL)
    windows_menu.entryconfig(windows_menu.index('Window 5'), state=NORMAL)
    to = int(uni_range[1]) + 1
    frm = int(uni_range[0])
    for i in range(frm, to, 1):
        empty.append(i)

    cast_str_to_list(entr_hand_A, set_a)
    cast_str_to_list(entr_hand_B, set_b)
    cast_str_to_list(entr_hand_B, set_c)


def u():
    if len(empty) > 10:
        # 0, 1, 2, 3, 4... 5
        return ((str(empty)).strip('[]'))[0:40].rpartition(',')[0] + '...' + \
               ((str(empty)).strip('[]')).rpartition(',')[2]
    else:
        return (str(empty)).strip('[]')


def write_to_file(result):
    with open('result.txt', 'a') as f:
        f.write(str(result))
        f.write('\n')


# ----------------------------------------------------------------------------------------------------------------------
power = []
uni_range = []
set_a = []
set_b = []
set_c = []
a = set(set_a)
b = set(set_b)
c = set(set_c)
r = []
e = []
p = []
empty = []
count = 0
iterator = 0
step = 0

# ----------------------------------------------------------------------------------------------------------------------
# Візитка
root = Tk()
root.title("Лабораторна робота №1")
root.geometry('890x420')

fr_name = Frame(root, bg="#856ff8", bd=10)
fr_name.grid(row=0, sticky='w')
name = Label(fr_name, text="Федорко Андрій Петрович\nГрупа ІО-04\nНомер у списку - 23", bg='#856ff8',
             font=('Arial', 18))
name.pack()

var_but = Button(fr_name, text="Порахувати\nваріант", bg='#956fff', command=count_var, font=('Garamond', 12))
var_but.bind('<Button-1>', count_var)
var_but.pack()
var = Label(fr_name, text='Варіант - ?\t\t\t', bg='#856ff8', font=('Arial', 18))
var.pack()

# ----------------------------------------------------------------------------------------------------------------------
fr_power = Frame(root, bg='#8499B1', bd=31)
fr_power.place(x=399, y=0)
power_lab = Label(fr_power, bg='#8499B1', font=('Century Schoolbook', 18),
                  text='Input cardinality for А, В, С.\t   ')
power_lab.grid(row=0, columnspan=3)
pow_A = Label(fr_power, bg='#8499B1', font=('Century Schoolbook', 15), text='A:')
pow_A.grid(row=1, sticky=W)
pow_B = Label(fr_power, bg='#8499B1', font=('Century Schoolbook', 15), text='B:')
pow_B.grid(row=2, sticky=W)
pow_C = Label(fr_power, bg='#8499B1', font=('Century Schoolbook', 15), text='C:')
pow_C.grid(row=3, sticky=W)
entr_pow_A = Entry(fr_power, width=7, font=('Century Schoolbook', 15))
entr_pow_A.grid(row=1, column=1, sticky=W)
entr_pow_B = Entry(fr_power, width=7, font=('Century Schoolbook', 15))
entr_pow_B.grid(row=2, column=1, sticky=W)
entr_pow_C = Entry(fr_power, width=7, font=('Century Schoolbook', 15))
entr_pow_C.grid(row=3, column=1, sticky=W)
but_pow = Button(fr_power, width=7, text='Задати', font=('Garamond', 13), bg='#8499B1', height=5, command=power_func)
but_pow.bind('<Button-1>', power_func)
but_pow.grid(row=1, column=2, rowspan=3, sticky=W)

# ----------------------------------------------------------------------------------------------------------------------
fr_hand = Frame(root, bg='#84DCC6', bd=42)
fr_hand.place(x=0, y=190)
hand_lab = Label(fr_hand, bg='#84DCC6', text='Enter sets', font=('Century Schoolbook', 18))
hand_lab.grid(row=0, columnspan=3)
hand_A = Label(fr_hand, bg='#84DCC6', text='Set A = ', font=('Century Schoolbook', 15))
hand_A.grid(row=1, column=0)
hand_B = Label(fr_hand, bg='#84DCC6', text='Set B = ', font=('Century Schoolbook', 15))
hand_B.grid(row=2, column=0)
hand_C = Label(fr_hand, bg='#84DCC6', text='Set C = ', font=('Century Schoolbook', 15))
hand_C.grid(row=3, column=0)
entr_hand_A = Entry(fr_hand, width=20, font=('Century Schoolbook', 15))
entr_hand_A.grid(row=1, column=1, sticky=W)
entr_hand_B = Entry(fr_hand, width=20, font=('Century Schoolbook', 15))
entr_hand_B.grid(row=2, column=1, sticky=W)
entr_hand_C = Entry(fr_hand, width=20, font=('Century Schoolbook', 15))
entr_hand_C.grid(row=3, column=1, sticky=W)
but_hand_A = Button(fr_hand, width=10, text='Generate', font=('Garamond', 13), bg='#70D3B9', state=DISABLED,
                    command=generate_a)
but_hand_A.grid(row=1, column=2, sticky=W)
but_hand_B = Button(fr_hand, width=10, text='Generate', font=('Garamond', 13), bg='#70D3B9', state=DISABLED,
                    command=generate_b)
but_hand_B.grid(row=2, column=2, sticky=W)
but_hand_C = Button(fr_hand, width=10, text='Generate', font=('Garamond', 13), bg='#70D3B9', state=DISABLED,
                    command=generate_c)
but_hand_C.grid(row=3, column=2, sticky=W)
but_hand = Button(fr_hand, width=7, text='Save', font=('Garamond', 13), bg='#70D3B9', height=5, command=save_gen_sets)
but_hand.grid(row=1, column=3, rowspan=3, sticky=W)

# ----------------------------------------------------------------------------------------------------------------------

fr_universal = Frame(root, bg='plum3', bd=66)
fr_universal.place(x=523, y=190)
#r_universal.pack(expand=True)
#fr_universal.place(relx=.5, rely=.5, anchor="c")

lab_uni = Label(fr_universal, text='Set range for the universal set', font=('Century Schoolbook', 15),
                bg='plum3')
lab_uni.grid(row=0, columnspan=2)
entry_start = Entry(fr_universal, width=7, font=('Century Schoolbook', 15))
entry_start.grid(row=1, column=1)
lab_start = Label(fr_universal, text="Begin:", bg='plum3', font=('Century Schoolbook', 15))
lab_start.grid(row=1, column=0)
entry_end = Entry(fr_universal, width=7, font=('Century Schoolbook', 15))
entry_end.grid(row=2, column=1)
lab_end = Label(fr_universal, text="End:", bg='plum3', font=('Century Schoolbook', 15))
lab_end.grid(row=2, column=0)
uni_but = Button(fr_universal, text='Задати', font=('Garamond', 13), bg='thistle1', command=create_uni, state=DISABLED)
uni_but.bind('<Button-1>', create_uni)
uni_but.grid(row=3, columnspan=3)


# ----------------------------------------------------------------------------------------------------------------------
def create_win2():
    root2 = Toplevel(root)
    root2.title('Window 2 (ful formula)')
    root2.geometry('488x455')

    frame = Frame(root2, bg='spring green', bd=20)
    frame.pack()

    A = set(set_a)
    B = set(set_b)
    C = set(set_c)
    not_c = set(empty) - set(set_c)
    not_a = set(empty) - set(set_a)
    a_diff_c = set(set_a) - not_c
    not_c_intersection_a_diff_c = not_c & a_diff_c
    b_diff_c = set(set_b) - set(set_c)
    intersect2 = not_c_intersection_a_diff_c & b_diff_c
    not_c_union_b = not_c | set(set_b)
    final_intersection = intersect2 & not_c_union_b

    def result():
        global count
        count += 1
        change = {
            1: '¬C =',
            2: 'A\\C =',
            3: '¬C ∩ (A\\C) =',
            4: 'B\\C =',
            5: '¬C ∩ (A\\C) ∩ (B\\C) =',
            6: '¬C ∪ B =',
            7: '¬C ∩ (A\\C) ∩ (B\\C) ∩ (¬C ∪ B) =',
        }
        calc = {
            1: not_c,
            2: a_diff_c,
            3: not_c_intersection_a_diff_c,
            4: b_diff_c,
            5: intersect2,
            6: not_c_union_b,
            7: final_intersection,
        }
        assert len(change) == len(calc)
        index_within_array = count <= len(change)
        if index_within_array:
            res_txt.insert(END, str(change[count]) + set_to_str(calc[count]) + '\n')
        should_disable_increment = count == len(change)
        if should_disable_increment:
            step_but.config(state=DISABLED)
            if len(final_intersection) > 10:
                return label_d.config(text=('D1=', get_shorten_sequence_as_str(final_intersection)))
            else:
                return label_d.config(text=('D1=', str(final_intersection).strip('{}')))


    label_a = Label(frame, text=('A=', (str(set_a)).strip('[[]]')), bg='spring green', font=('Century Schoolbook', 14))
    label_a.grid(row=0, column=0, sticky='w')
    label_b = Label(frame, text=('B=', (str(set_b)).strip('[[]]')), bg='spring green', font=('Century Schoolbook', 14))
    label_b.grid(row=1, column=0, sticky='w')
    label_c = Label(frame, text=('C=', (str(set_c)).strip('[[]]')), bg='spring green', font=('Century Schoolbook', 14))
    label_c.grid(row=2, column=0, sticky='w')
    label_u = Label(frame, text=('U=', u()), bg='spring green', font=('Century Schoolbook', 14))
    label_u.grid(row=3, column=0, sticky='w')

    step_but = Button(frame, text='Крок', font=('Garamond', 14), bg='light sea green', command=result)
    step_but.grid(row=4, columnspan=3)

    res_txt = Text(frame, font=('Century Schoolbook', 14), width=40, height=9, bd=2, bg='light yellow')
    res_txt.grid(row=5, columnspan=4, rowspan=4)

    label_d = Label(frame, bg='spring green', font=('Century Schoolbook', 14), text='D1=')
    label_d.grid(row=10, column=0, sticky='w')

    save_but = Button(frame, text='Зберегти', font=('Garamond', 14), bg='light sea green',
                      command=write_to_file(final_intersection))
    save_but.grid(row=11, columnspan=3)

def get_shorten_sequence_as_str(sequence):
    if len(sequence) != 0:
        return ((str(sequence)).strip('{}'))[0:40].rpartition(',')[0] + '...' + \
               ((str(sequence)).strip('{}')).rpartition(',')[2]
    else:
        return '∅'

def set_to_str(myset):
    return str(myset) if len(myset) != 0 else "∅"

# ---------------------------------------------------------------------------------------------------------------------



def create_win3():
    root3 = Toplevel(root)
    root3.title('Window 3')
    root3.geometry('488x450')

    frame = Frame(root3, bg='brown1', bd=20)
    frame.pack()

    b_diff_c = set(set_b) - set(set_c)
    a_intersect_b_diff_c = set(set_a) & b_diff_c
    union2 = a_intersect_b_diff_c

    def res():
        global iterator
        iterator += 1
        switch = {
            1: 'B\\C = ',
            2: 'A ∩ (B\\C) = ',
        }
        do = {
            1: b_diff_c,
            2: a_intersect_b_diff_c,
        }
        if iterator <= len(switch):
            res_txt.insert(END, str(switch[iterator]) + set_to_str(do[iterator]) + '\n')
        if iterator == len(switch):
            step_but.config(state=DISABLED)
            if len(union2) > 10:
                return label_d.config(text=('D2=', get_shorten_sequence_as_str(a_intersect_b_diff_c)))
            else:
                return label_d.config(text=('D2=', str(a_intersect_b_diff_c).strip('{}')))

    label_a = Label(frame, text=('A=', (str(set_a)).strip('[[]]')), bg='brown1', font=('Century Schoolbook', 14))
    label_a.grid(row=0, column=0, sticky='w')
    label_b = Label(frame, text=('B=', (str(set_b)).strip('[[]]')), bg='brown1', font=('Century Schoolbook', 14))
    label_b.grid(row=1, column=0, sticky='w')
    label_c = Label(frame, text=('C=', (str(set_c)).strip('[[]]')), bg='brown1', font=('Century Schoolbook', 14))
    label_c.grid(row=2, column=0, sticky='w')
    label_u = Label(frame, text=('U=', u()), bg='brown1', font=('Century Schoolbook', 14))
    label_u.grid(row=3, column=0, sticky='w')

    step_but = Button(frame, text='Крок', font=('Garamond', 14), bg='tan1', command=res)
    step_but.grid(row=4, columnspan=4)

    res_txt = Text(frame, font=('Century Schoolbook', 14), width=40, height=8, bd=2, bg='light yellow')
    res_txt.grid(row=5, columnspan=4, rowspan=4)

    label_d = Label(frame, bg='brown1', font=('Century Schoolbook', 14), text='D2=')
    label_d.grid(row=10, column=0, sticky='w')

    save_but = Button(frame, text='Зберегти', font=('Garamond', 14), bg='tan1', command=write_to_file(union2))
    save_but.grid(row=11, columnspan=4)


# ----------------------------------------------------------------------------------------------------------------------
def create_win4():
    root4 = Toplevel(root)
    root4.title("Window 4")
    root4.geometry('488x400')

    frame = Frame(root4, bg='SkyBlue1', bd=20)
    frame.pack()
    x, y = set(set_c), set(set_b)
    z = set(set_c) & set(set_b)


    def calculate():
        global step
        step += 1
        text = {
            1: 'X ∩ Y ='
        }
        get = {
            1: z
        }
        if step < 2:
            res_txt.insert(END, str(text[step]) + set_to_str(get[step]) + '\n')
        if step == 1:
            step_but.config(state=DISABLED)
            if len(z) > 10:
                return label_z.config(text=('Z1=', get_shorten_sequence_as_str(z)))
            else:
                return label_z.config(text=('Z1=', str(z).strip('{}')))

        if len(x) > 20:
            return label_x.config(text=('X=', get_shorten_sequence_as_str(set(set_c))))
        else:
            return label_x.config(text=('X=', str((set_c)).strip('[]')))

    label_x = Label(frame, text=('X=', (str((set_c))).strip('[]')), bg='SkyBlue1', font=('Century Schoolbook', 14))
    label_x.grid(row=0, column=0, sticky='w')
    label_y = Label(frame, text=('Y=', (str((set_c))).strip('[]')), bg='SkyBlue1', font=('Century Schoolbook', 14))
    label_y.grid(row=1, column=0, sticky='w')

    step_but = Button(frame, text='Compute', font=('Garamond', 14), bg='MediumOrchid1', command=calculate)
    step_but.grid(row=2, columnspan=4)

    res_txt = Text(frame, font=('Century Schoolbook', 14), width=40, height=9, bd=2, bg='light yellow')
    res_txt.grid(row=3, columnspan=4, rowspan=4)

    label_z = Label(frame, text='Z1=', bg='SkyBlue1', font=('Century Schoolbook', 14))
    label_z.grid(row=8, column=0, sticky='w')

    save_but = Button(frame, text='Зберегти', font=('Garamond', 14), bg='MediumOrchid1',
                      command=(write_to_file(z)))
    save_but.grid(row=9, columnspan=4)

    if len(y) > 10:
        label_y.config(text=('Y=', get_shorten_sequence_as_str(y)))
    else:
        label_y.config(text=('Y=', str(y).strip('{}')))

    if len(x) > 10:
        label_x.config(text=('X=', get_shorten_sequence_as_str(x)))
    else:
        label_x.config(text=('X=', str(x).strip('{}')))


# ----------------------------------------------------------------------------------------------------------------------
def create_win5():
    root5 = Toplevel(root)
    root5.title('Window 5')
    root5.geometry('488x192')
    frame = Frame(root5, bg='LightPink1', bd=25)
    frame.grid()
    list_res = []
    x = set(set_c)
    y = set(set_b)
    z = set(x) & set(y)

    write_to_file(z)

    with open("result.txt", 'r+') as f:
        result = f.readlines()

    for i in result:
        list_res.append(i.strip('{}').split("\n"))

    def compare_d():
        if list_res[0] == list_res[1]:
            messagebox.showinfo('Congratulation', 'Множина D1 дорівнює D2')
        else:
            messagebox.showinfo('Error', 'Множина D1 не дорівнює D2 ')

    def compare_z():
        if list_res[2] == list_res[3]:
            messagebox.showinfo('Congratulation', 'Множина Z1 дорівнює Z2')
        else:
            messagebox.showinfo('Error', 'Множина Z1 не дорівнює Z2 ')

    label_d1 = Label(frame, text='D1=', bg='LightPink1',
                     font=('Century Schoolbook', 14))
    label_d1.grid(row=0, columnspan=4, sticky='w')
    label_d2 = Label(frame, text=('D2=', ), bg='LightPink1',
                     font=('Century Schoolbook', 14))
    label_d2.grid(row=1, columnspan=4, sticky='w')
    label_z1 = Label(frame, text=('Z1=', ), bg='LightPink1',
                     font=('Century Schoolbook', 14))
    label_z1.grid(row=2, columnspan=4, sticky='w')
    label_z2 = Label(frame, text=('Z2=', (str(list_res[3][0])).strip('[[}]')), bg='LightPink1',
                     font=('Century Schoolbook', 14))
    label_z2.grid(row=3, columnspan=4, sticky='w')

    button_d = Button(frame, text='Порівняти D1 і D2', font=('Garamond', 14), bg='RosyBrown1', width=20,
                      command=compare_d)
    button_d.grid(row=4, column=0, sticky='w')

    button_z = Button(frame, text='Порівняти Z1 і Z2', font=('Garamond', 14), bg='RosyBrown1', width=20,
                      command=compare_z)
    button_z.grid(row=4, column=2)

    if len(z) > 15:
        label_z2.config(text=('Z2=', ((str(z)).strip('{}'))[0:40].rpartition(',')[0] + '...' +
                              ((str(x)).strip('{}')).rpartition(',')[2]))
    else:
        label_z2.config(text=('Z2=', ((str(z)).strip('{}'))))

    if len(str(list_res[0][0]).strip('[[}]')) > 15:
        label_d1.config(text=('D1=', (str(list_res[0][0]).strip('[[}]'))[0:45].rpartition(',')[0] + '...' +
                              (str(list_res[0][0]).strip('[[}]')).rpartition(',')[2]))
    else:
        label_d1.config(text=('D1=', str(list_res[0][0]).strip('[[}]')))

    if len(str(list_res[1][0]).strip('[[}]')) > 15:
        label_d2.config(text=('D2=', (str(list_res[1][0]).strip('[[}]'))[0:45].rpartition(',')[0] + '...' +
                              (str(list_res[1][0]).strip('[[}]')).rpartition(',')[2]))
    else:
        label_d2.config(text=('D2=', str(list_res[1][0]).strip('[[}]')))

    if len(str(list_res[2][0]).strip('[[}]')) > 15:
        label_z1.config(text=('Z1=', (str(list_res[2][0]).strip('[[}]'))[0:45].rpartition(',')[0] + '...' +
                              (str(list_res[2][0]).strip('[[}]')).rpartition(',')[2]))
    else:
        label_z1.config(text=('Z2=', str(list_res[2][0]).strip('[[}]')))


# ----------------------------------------------------------------------------------------------------------------------

menu_bar = Menu(root, bg='Red')
root.config(menu=menu_bar)

windows_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Windows', menu=windows_menu)
windows_menu.add_command(label='Window 2', command=create_win2, state=DISABLED)
windows_menu.add_command(label='Window 3', command=create_win3, state=DISABLED)
windows_menu.add_command(label='Window 4', command=create_win4, state=DISABLED)
windows_menu.add_command(label='Window 5', command=create_win5, state=DISABLED)

root.mainloop()
