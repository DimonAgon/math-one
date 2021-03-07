# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


G=4
N=25
M="ІО"
print("Моя група: ", M+"-0"+str(G))
print("Мій номер у групі:",N)
if M=="ІО": N+=2
print("Мій варіант:", (N+G%60)%30+1)




from tkinter import *
from tkinter.messagebox import *
import funcs
from random import randint


# ----------------------------------------------------------------------------------------------------------------------
# ВТОРОЕ ОКНО
# ----------------------------------------------------------------------------------------------------------------------

def openWin2():
    i = 1
    res_set = ""
    expression = ""
    def save_D_fnc(event):
        data = funcs.makeFormatedSet(funcs.culcFirstExpression(funcs.set_A, funcs.set_B, funcs.set_C))
        file = open("logs_2.txt", "r")
        data_from_file = file.read()
        if data in data_from_file:
            file.close()
        else:
            file.close()
            file = open("logs_2.txt", "w")
            file.write(data)
            file.close()

    def next_shg(event):
        nonlocal i
        nonlocal expression
        nonlocal res_set
        nonlocal L1
        left_set = ""
        right_set = ""
        operator = ""
        L1.grid_forget()
        L2.grid_forget()
        shg_btn["text"] = "Наступний крок"

        if i == 1:
            left_set = "⌜"
            operator = f"({funcs.makeFormatedSet(funcs.set_B)})"
            right_set = ""
            res_set = funcs.getNotSet(funcs.set_B)

        elif i == 2:
            left_set = f"({str(funcs.makeFormatedSet(funcs.set_A))})\n"
            operator = " ∩\n "
            right_set = f"({str(funcs.makeFormatedSet(res_set))})"
            res_set = set(funcs.set_A) & set(res_set)

        elif i == 3:
            left_set = f"({funcs.makeFormatedSet(list(res_set))})\n"
            operator = " ∪ \n"
            right_set = f"({funcs.makeFormatedSet(funcs.set_B)})"
            res_set = set(funcs.set_B) | set(res_set)

        elif i == 4:
            left_set = f"({funcs.makeFormatedSet(list(res_set))})\n"
            operator = " \ \n"
            right_set = f"{funcs.makeFormatedSet(funcs.set_A)}"
            res_set = set(res_set) - set(funcs.set_A)

        elif i == 5:
            left_set = f"({funcs.makeFormatedSet(list(res_set))})\n"
            operator = " ∪ \n"
            right_set = f"{funcs.makeFormatedSet(funcs.set_C)}"
            res_set = set(res_set) | set(funcs.set_C)
            shg_btn["text"] = "Розпочати ще раз"
            i = 0
        i += 1
        expression = left_set + operator + right_set
        L1["text"] = expression
        L2["text"] = f"Множина результат:\n{funcs.makeFormatedSet(list(res_set))}"
        L1.grid(row=4, column=1, columnspan=40)
        L2.grid(row=5, column=1, columnspan=40)




    win2 = Toplevel()
    win2.title("Вікно 2")
    L1 = Label(master=win2)
    L2 = Label(master=win2)
    if funcs.set_A == [] or funcs.set_B == [] or funcs.set_C == []:
        txt = "Сгенеруйте множини у головному вікні"
    else:
        txt = f"Множина А: \n({funcs.makeFormatedSet(funcs.set_A)})\n\n" \
              f"Множина B: \n({funcs.makeFormatedSet(funcs.set_B)})\n\n" \
              f"Множина С: \n({funcs.makeFormatedSet(funcs.set_C)})"
        shg_btn = Button(master=win2, text="Покрокове виконання")
        shg_btn.bind("<Button-1>", next_shg)
        shg_btn.grid(row=3, column=1, columnspan=40)
        Label(master=win2, text="Початковий вираз: ((A ∩ (⌜B)) ∪ B) \ A) ∪ C").grid(row=1, column=1, columnspan=40)
        L3 = Label(master=win2, text=f"Множина D:\n{funcs.makeFormatedSet(funcs.culcFirstExpression(funcs.set_A, funcs.set_B, funcs.set_C))}")
        L3.grid(row=6, column=1, columnspan=40)
        save_D = Button(master=win2, text="Зберігти у файл")
        save_D.grid(row=7, column=1, columnspan=40)
        save_D.bind("<Button-1>", save_D_fnc)


    sets_l = Label(master=win2, text=txt, justify=LEFT)
    sets_l.grid(row=2, column=1, columnspan=40, sticky=W)



# ----------------------------------------------------------------------------------------------------------------------
# ОКНО 3
# ----------------------------------------------------------------------------------------------------------------------

def openWin3():
    win3 = Toplevel()
    win3.title("Вікно 3")
    L1 = Label(master=win3)
    L2 = Label(master=win3)
    i = 1
    res_set = ""
    expression = ""
    def save_D_fnc(event):
        data = funcs.makeFormatedSet(funcs.culcFirstExpression(funcs.set_A, funcs.set_B, funcs.set_C))
        file = open("logs_3.txt", "r")
        data_from_file = file.read()
        if data in data_from_file:
            file.close()
        else:
            file.close()
            file = open("logs_3.txt", "w")
            file.write(data)
            file.close()
    def next_shg(event):
        nonlocal i
        nonlocal expression
        nonlocal res_set
        nonlocal L1
        left_set = ""
        right_set = ""
        operator = ""
        L1.grid_forget()
        L2.grid_forget()
        shg_btn["text"] = "Наступний крок"

        if i == 1:
            left_set = f"{funcs.makeFormatedSet(funcs.set_B)}\n"
            operator = f"\\ \n"
            right_set = f"{funcs.makeFormatedSet(funcs.set_A)}"
            res_set = set(funcs.set_B).difference(set(funcs.set_A))

        elif i == 2:
            left_set = f"({funcs.makeFormatedSet(list(res_set))})\n"
            operator = " ∪ \n"
            right_set = f"{funcs.makeFormatedSet(funcs.set_C)}"
            res_set = set(res_set) | set(funcs.set_C)
            shg_btn["text"] = "Розпочати ще раз"
            i = 0
        i += 1
        expression = left_set + operator + right_set
        L1["text"] = expression
        L2["text"] = f"Множина результат:\n{funcs.makeFormatedSet(list(res_set))}"
        L1.grid(row=4, column=1, columnspan=40)
        L2.grid(row=5, column=1, columnspan=40)

    if funcs.set_A == [] or funcs.set_B == [] or funcs.set_C == []:
        txt = "Сгенеруйте множини у головному вікні"
    else:
        txt = f"Множина А: \n({funcs.makeFormatedSet(funcs.set_A)})\n\n" \
              f"Множина B: \n({funcs.makeFormatedSet(funcs.set_B)})\n\n" \
              f"Множина С: \n({funcs.makeFormatedSet(funcs.set_C)})"
        shg_btn = Button(master=win3, text="Покрокове виконання")
        shg_btn.bind("<Button-1>", next_shg)
        shg_btn.grid(row=3, column=1, columnspan=40)
        Label(master=win3, text="Початковий вираз: (B \ A) ∪ C").grid(row=1, column=1, columnspan=40)
        L3 = Label(master=win3,
                   text=f"Множина D:\n{funcs.makeFormatedSet(funcs.culcFirstExpression(funcs.set_A, funcs.set_B, funcs.set_C))}")
        L3.grid(row=6, column=1, columnspan=40)
        save_D = Button(master=win3, text="Зберігти у файл")
        save_D.grid(row=7, column=1, columnspan=40)
        save_D.bind("<Button-1>", save_D_fnc)

    sets_l = Label(master=win3, text=txt, justify=LEFT)
    sets_l.grid(row=2, column=1, columnspan=40, sticky=W)

# ----------------------------------------------------------------------------------------------------------------------
# ОКНО 4
# ----------------------------------------------------------------------------------------------------------------------
def openWin4():
    win4 = Toplevel()
    win4.title("Вікно 4")

    def save_D_fnc(event):
        data = funcs.makeFormatedSet(funcs.culcSecondExp(funcs.set_X, funcs.set_Y))
        file = open("logs_4.txt", "r")
        data_from_file = file.read()
        if data in data_from_file:
            file.close()
        else:
            file.close()
            file = open("logs_4.txt", "w")
            file.write(data)
            file.close()

    if funcs.set_X == [] or funcs.set_Y == []:
        txt = "Сгенеруйте множини у головному вікні"
    else:
        txt = f"Множина X: \n({funcs.makeFormatedSet(funcs.set_X)})\n\n" \
              f"Множина Y: \n({funcs.makeFormatedSet(funcs.set_Y)})"
        Label(master=win4, text="Початковий вираз: X △ Y").grid(row=1, column=1, columnspan=40)
        L3 = Label(master=win4,
                   text=f"Множина Z:\n{funcs.makeFormatedSet(funcs.culcSecondExp(funcs.set_X, funcs.set_Y))}")
        L3.grid(row=3, column=1, columnspan=40)
        save_D = Button(master=win4, text="Зберігти у файл")
        save_D.grid(row=4, column=1, columnspan=40)
        save_D.bind("<Button-1>", save_D_fnc)

    sets_l = Label(master=win4, text=txt, justify=LEFT)
    sets_l.grid(row=2, column=1, columnspan=40, sticky=W)

# ----------------------------------------------------------------------------------------------------------------------
# ОКНО 5
# ----------------------------------------------------------------------------------------------------------------------
def openWin5():
    win5 = Toplevel()
    win5.title("Вікно 5")

    def check_sets(value_of_r_btns=1):
        if value_of_r_btns == 1:
            nonlocal l_first_exp_set_txt
            nonlocal l_s_first_exp_set_txt
            if "Збережіть множину" in l_first_exp_set_txt or "Збережіть множину" in l_s_first_exp_set_txt:
                showerror("Помилка", "Для перевірки спершу збережіть множини в вікнах 2-3")
            else:
                if funcs.getOriginSet(l_first_exp_set_txt) == funcs.getOriginSet(l_s_first_exp_set_txt):
                    showinfo("Інфо", "Множина-результат початкового та спрощенного виразу рівні")
                else:
                    showerror("Помилка", "Множина-результат початкового та спрощенного виразу не рівні")
        else:
            nonlocal l_second_exp_set_txt
            nonlocal l_s_second_exp_set_txt
            if "Збережіть множину" in l_second_exp_set_txt:
                showerror("Помилка", "Для перевірки спершу збережіть множину з вікна 4")
            else:
                if funcs.getOriginSet(l_second_exp_set_txt) == funcs.getOriginSet(l_s_second_exp_set_txt):
                    showinfo("Інфо", "Множина-результат другого виразу, обчисленного за допомогою функції з модуля "
                                     "funcs та за допомогою вбудованого оператора Python рівні")
                else:
                    showerror("Помилка", "Множина-результат другого виразу, обчисленного за допомогою функції з модуля"
                                     "funcs та за допомогою вбудованого оператора Python не рівні")

    files = {"logs_2.txt":None, "logs_3.txt":None, "logs_4.txt":None}
    for file in files:
        f = open(file, "r")
        data = f.read()
        if data:
            files[file] = data
        f.close()

    l_first_exp = Label(master=win5, text="Множина-результат першого виразу:")
    if files["logs_2.txt"] is None:
        l_first_exp_set_txt = "Збережіть множину з вікна2 у файл"
    else:
        l_first_exp_set_txt = files["logs_2.txt"] + "\n\n"
    l_first_exp_set = Label(master=win5, text =l_first_exp_set_txt )
    l_first_exp.grid(row=1, column=1)
    l_first_exp_set.grid(row=2,column=1)

    l_s_fisrt_exp = Label(master=win5, text="Множина-результат спрощеного першого виразу:")
    if files["logs_3.txt"] is None:
        l_s_first_exp_set_txt = "Збережіть множину з вікна3 у файл"
    else:
        l_s_first_exp_set_txt = files["logs_3.txt"] + "\n\n"
    l_s_fisrt_exp_set = Label(master=win5, text=l_s_first_exp_set_txt)
    l_s_fisrt_exp.grid(row=1, column=3)
    l_s_fisrt_exp_set.grid(row=2, column=3)

    l_second_exp = Label(master=win5, text="Множина-результат другого виразу:")
    if files["logs_4.txt"] is None:
        l_second_exp_set_txt = "Збережіть множину з вікна4 у файл"
    else:
        l_second_exp_set_txt = files["logs_4.txt"]
    l_second_exp_set = Label(master=win5, text=l_second_exp_set_txt)
    l_second_exp.grid(row=3, column=1)
    l_second_exp_set.grid(row=4, column=1)

    l_s_second_exp = Label(master=win5, text="Множина-результат другого виразу обчисленого функциею Python:")
    if funcs.set_X and funcs.set_Y:
        l_s_second_exp_set_txt = funcs.makeFormatedSet(list(set(funcs.set_X) ^ set(funcs.set_Y)))
    else:
        l_s_second_exp_set_txt = "Згенеруйте множини у головному вікні"

    l_s_second_exp_set = Label(master=win5, text=l_s_second_exp_set_txt)
    l_s_second_exp.grid(row=3,column=3)
    l_s_second_exp_set.grid(row=4, column=3)

    checking_var = IntVar()
    checking_var.set(1)
    l_checking = Label(master=win5, text="Перевірка рівності множин")
    checking_r_btn_1 = Radiobutton(master=win5, text="Перший вираз", variable=checking_var, value=1)
    checking_r_btn_2 = Radiobutton(master=win5, text="Другий вираз", variable=checking_var, value=2)
    checking_btn_check = Button(master=win5, text="Перевірити", command = lambda: check_sets(checking_var.get()))
    l_checking.grid(row=5, column=1, columnspan=3)
    checking_r_btn_1.grid(row=6, column=1, columnspan=3)
    checking_r_btn_2.grid(row=7, column=1, columnspan=3)
    checking_btn_check.grid(row=8, column=1, columnspan=3)



# ----------------------------------------------------------------------------------------------------------------------
# Функции главного окна
# ----------------------------------------------------------------------------------------------------------------------

def getSets(event):
    # Функция которая получает/генерирует множества и передаёт их в funcs
    a_set = []
    b_set = []
    c_set = []
    u_set = []
    error = False

    # УНИВЕРСАЛЬНОЕ МНОЖЕСТВО
    try:
        if universum_max.get() == "" and universum_min.get() == "":
            u_set_max = 255
            u_set_min = 0
        elif universum_max.get() == "":
            u_set_max = 255
            u_set_min = int(universum_min.get())
        elif universum_min.get() == "":
            u_set_min = 0
            u_set_max = int(universum_max.get())
        else:
            u_set_min = int(universum_min.get())
            u_set_max = int(universum_max.get())
    except ValueError:
        error = True
        showerror("Помилка!", "Введіть корректное значення при виборі універсальної множини ")
    else:
        if u_set_max < u_set_min:
            error = True
            showerror("Помилка!", "Максимум множини меньше мінімума ")
        elif u_set_max > 255 or u_set_min < 0:
            error = True
            showerror("Помилка!", "Числа повинні належати діапазону від 0 до 255")
        elif u_set_max == u_set_min:
            error = True
            showerror("Помилка!", "Максимум множини не може дорівнювати мінімуму")
        else:
            for el in range(u_set_min, (u_set_max)+1):
                u_set.append(el)
            try:
                if isARandom.get():
                    mod_A = rnd_mod_A.get()
                    if int(mod_A) <= 0 or int(mod_A) > u_set_max:
                        error = True
                        showerror("Помилка!", "Потужність множини А повинна бути більше нуля і меньше "
                                              "максимума універсальної множини")
                    for el in range(0, int(mod_A)):
                        rand_num = randint(u_set_min, u_set_max)
                        while (rand_num in a_set) and not error:
                            rand_num = randint(u_set_min, u_set_max)
                        else:
                            a_set.append(rand_num)
                else:
                    users_A = userSetA.get()
                    users_A = users_A.split(",")
                    for i in users_A:
                        a_set.append(int(i))

                if isBRandom.get():
                    mod_B = rnd_mod_B.get()
                    if int(mod_B) <= 0 or int(mod_B) > u_set_max:
                        error = True
                        showerror("Помилка!", "Потужність множини В повинна бути більше нуля і меньше "
                                              "максимума універсальної множини")
                    for el in range(0, int(mod_B)):
                        rand_num = randint(u_set_min, u_set_max)
                        while (rand_num in b_set) and not error:
                            rand_num = randint(u_set_min, u_set_max)
                        else:
                            b_set.append(rand_num)
                else:
                    users_B = userSetB.get()
                    users_B = users_B.split(",")
                    for i in users_B:
                        b_set.append(int(i))

                if isCRandom.get():
                    mod_C = rnd_mod_C.get()
                    if int(mod_C) <= 0 or int(mod_C) > u_set_max:
                        error = True
                        showerror("Помилка!", "Потужність множини С повинна бути більше нуля і меньше "
                                              "максимума універсальної множини")
                    for el in range(0, int(mod_C)):
                        rand_num = randint(u_set_min, u_set_max)
                        while (rand_num in c_set) and not error:
                            rand_num = randint(u_set_min, u_set_max)
                        else:
                            c_set.append(rand_num)

                else:
                    users_C = userSetC.get()
                    users_C = users_C.split(",")
                    for i in users_C:
                        c_set.append(int(i))
            except ValueError:
                error = True
                showerror("Помилка!", "Введіть корректне значення параметрів  множин ")
            for el in a_set:
                if el > u_set_max or el < u_set_min:
                    error = True
                    showerror("Помилка!",
                              "Введенна множина А включає елементы, які не входять в універсальну мн-ну")
            for el in b_set:
                if el > u_set_max or el < u_set_min:
                    error = True
                    showerror("Помилка!",
                              "Введенна множина А включає елементы, які не входять в універсальну мн-ну")
            for el in c_set:
                if el > u_set_max or el < u_set_min:
                    error = True
                    showerror("Помилка!",
                              "Введенна множина А включає елементы, які не входять в універсальну мн-ну")
            if error:
                error = False
            else:
                funcs.set_A = a_set
                funcs.set_B = b_set
                funcs.set_C = c_set
                funcs.universum = u_set
                funcs.set_X = funcs.getNotSet(funcs.set_B)
                funcs.set_Y = funcs.set_A




def checkRndButtns():
    # Функция, которая открывает и скрывает виджеты для ручного ввода множеств
    if not isARandom.get():
        userSetA_L.grid(row=4, column=1, columnspan=4, sticky=W)
        userSetA.grid(row=4, column=5, columnspan=8, sticky=W)
    else:
        userSetA_L.grid_forget()
        userSetA.grid_forget()
    if not isBRandom.get():
        userSetB_L.grid(row=4, column=13, columnspan=4, sticky=W)
        userSetB.grid(row=4, column=17, columnspan=8, sticky=W)
    else:
        userSetB_L.grid_forget()
        userSetB.grid_forget()
    if not isCRandom.get():
        userSetC_L.grid(row=4, column=25, columnspan=4, sticky=W)
        userSetC.grid(row=4, column=29,columnspan=8, sticky=W)
    else:
        userSetC_L.grid_forget()
        userSetC.grid_forget()

def clear_files():
    files = ["logs_2.txt", "logs_3.txt", "logs_4.txt"]
    for file in files:
        f = open(file, "w")
        f.close()

# ----------------------------------------------------------------------------------------------------------------------
# Главное окно
# ----------------------------------------------------------------------------------------------------------------------

root = Tk()
root.title("ДМ Лаб1")
mainmenu = Menu(root)
root.config(menu=mainmenu)
moremenu = Menu(mainmenu, tearoff=0)
moremenu.add_command(label="Вікно 2", command=openWin2)
moremenu.add_command(label="Вікно 3", command=openWin3)
moremenu.add_command(label="Вікно 4", command=openWin4)
moremenu.add_command(label="Вікно 5", command=openWin5)
mainmenu.add_cascade(label="Більше", menu=moremenu)
clear_files()


# ФИО, группа, вариант
Label(text=(f"ПІБ: Дзюба Олег Глібович\n"
                    f"Група: {funcs.getMyInfo()[0]}\n"
                    f"Номер у списку: {funcs.getMyInfo()[1]}\n"
                    f"Варіант: {funcs.getMyInfo()[2]}"), justify=CENTER).grid(row=1, column=1, columnspan=36)

# Формирование множеств

# А
isARandom = BooleanVar()
isARandom.set(True)
Label(text = "Потужність множини А:").grid(row=2, column=1, columnspan=8)
rnd_mod_A = Spinbox(from_=1, to=99999, width=5)
rnd_mod_A.grid(row=2, column=9, columnspan=4)
cbA = Checkbutton(text="Визначити множину A власноруч", variable=isARandom,onvalue=0, offvalue=1, command=checkRndButtns)
cbA.grid(row=3, column=1, columnspan=12, sticky=W)


# В
isBRandom = BooleanVar()
isBRandom.set(True)
Label(text = "Потужність множини В:").grid(row=2, column=13, columnspan=8)
rnd_mod_B = Spinbox(from_=1, to=99999, width=5)
rnd_mod_B.grid(row=2, column=21, columnspan=4)
cbB = Checkbutton(text="Визначити множину B власноруч", variable=isBRandom, onvalue=0, offvalue=1, command=checkRndButtns)
cbB.grid(row=3, column=13, columnspan=12, sticky=W)

# C
isCRandom = BooleanVar()
isCRandom.set(True)
Label(text="Потужність множини C:").grid(row=2, column=25, columnspan=8)
rnd_mod_C = Spinbox(from_=1, to=99999, width=5)
rnd_mod_C.grid(row=2, column=33, columnspan=4)
cbC = Checkbutton(text="Визначити множину С власноруч", variable=isCRandom, onvalue=0, offvalue=1, command=checkRndButtns)
cbC.grid(row=3, column=25, columnspan=12, sticky=W)

userSetA_L = Label(text = "Множина А:")
userSetA = Entry(width=20)

userSetB_L = Label(text = "Множина B:")
userSetB = Entry(width=20)

userSetC_L = Label(text = "Множина C:")
userSetC = Entry(width=20)

Label(text="Діапазон універсальної множини", justify=CENTER).grid(row=5, column=1, columnspan=36)

Label(text="Від", justify=RIGHT).grid(row=6, column=9, columnspan=4, sticky=E)
universum_min = Entry(width=10)
universum_min.grid(row=6, column=13,columnspan=4, sticky=W)

Label(text="До", justify=RIGHT).grid(row=6, column=17, columnspan=4,sticky=E)
universum_max = Entry(width=10)
universum_max.grid(row=6, column=21, columnspan=4,  sticky=W)

get_sets_btb = Button(text="Згенерувати множини")
get_sets_btb.grid(row=7, column=1, columnspan=36)
get_sets_btb.bind("<Button-1>", getSets)


root.mainloop()






