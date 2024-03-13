from tkinter import *

BASE_BACKGROUND = "#24587A"
BASE_FONT = ('Arial Bold', 10)
BASE_FONT_1 = ('Arial Bold', 15)
BASE_COLOR = 'white'


def avg_interface():
    """ Отрисовка интерфейса для нахождения среднего арифметического значения чисел """
    global txt_d_v
    global btn_d_v_1
    btn_1.destroy()
    btn_2.destroy()
    btn_3.destroy()
    lbl_d_v = Label()
    lbl_d_v.place(x = 60, y = 0)
    lbl_d_v.configure(text = 'Введите все числа', font = BASE_FONT_1, bg = BASE_BACKGROUND, fg = BASE_COLOR)
    txt_d_v = Entry(window, width = 30)
    txt_d_v.place(x = 57, y = 40)
    btn_d_v_1 = Button(window, text = "Расчитать", command = avg, font = BASE_FONT)
    btn_d_v_1.place(x = 113, y = 70)
    btn_d_v_2 = Button(window, text = "Выйти", command = quiting, font = BASE_FONT)
    btn_d_v_2.place(x = 125, y = 200)

def is_prime_interface():
    """ Отрисовка интерфейса для проверки числа на простоту """
    global txt_prost_v_1
    global btn_prost_v_1
    btn_1.destroy()
    btn_2.destroy()
    btn_3.destroy()
    lbl = Label()
    lbl.place(x = 80, y = 0)
    lbl.configure(text = 'Введите число', font = BASE_FONT_1, bg = BASE_BACKGROUND, fg = BASE_COLOR)
    txt_prost_v_1 = Entry(window, width = 30)
    txt_prost_v_1.place(x = 57, y = 40)
    btn_prost_v_1 = Button(window, text = "Расчитать", command = is_prime, font = BASE_FONT)
    btn_prost_v_1.place(x = 113, y = 70)
    btn_prost_v_2 = Button(window, text = "Выйти", command = quiting, font = BASE_FONT)
    btn_prost_v_2.place(x = 125, y = 200)


def is_prime():
    """ Проверки числа на простоту """
    btn_prost_v_1.destroy()
    flag = True
    num = txt_prost_v_1.get()
    try:
        num = int(num)
        for i in range(2, num):
            if num%i==0 and flag == True:
                lbl_prost_1 = Label()
                lbl_prost_1.place(x = 65, y = 120)
                lbl_prost_1.configure(text = 'Число не простое.', font = BASE_FONT_1, bg = BASE_BACKGROUND, fg = BASE_COLOR)
                flag = False
        if flag == True:
            lbl_prost_2 = Label()
            lbl_prost_2.place(x = 80, y = 120)
            lbl_prost_2.configure(text = 'Число простое.', font = BASE_FONT_1, bg = BASE_BACKGROUND, fg = BASE_COLOR)
    except ValueError:
        lbl_prost_2 = Label()
        lbl_prost_2.place(x = 15, y = 120)
        lbl_prost_2.configure(text = 'Неправильный ввод данных.', font = BASE_FONT_1, bg = BASE_BACKGROUND, fg = BASE_COLOR)

        
def avg():
    """ Нахождения среднего арифметического значения чисел """
    btn_d_v_1.destroy()
    lst=[]
    num = txt_d_v.get()
    if ',' in num:
        num=num.replace(',', ' ')
    num = num.split()
    for i in range(len(num)):
        count=0
        for j in range(len(num[i])):
            if num[i][j].isalpha() == False:
                count+=1
                if count == len(num[i]):
                    lst.append(int(num[i]))
    if lst:
        l = sum(lst) / len(lst)
        lbl_d_1 = Label(window, text = 'Среднее число:', font = BASE_FONT_1, bg = BASE_BACKGROUND, fg = BASE_COLOR)
        lbl_d_1.place(x = 55, y = 130)
        lbl_d_2 = Label(window, text = l, font = BASE_FONT_1, bg = BASE_BACKGROUND, fg = BASE_COLOR)
        lbl_d_2.place(x = 200, y = 130)

def quiting():#Выход
    window.destroy()
    start()

def quiting_window():#Окончательный выход
    window.destroy()

def start():
    """ Начальное окно"""
    global window
    global btn_1
    global btn_2
    global btn_3
    window = Tk()
    window.title('Файл от компании ANTONENTERTAINMENT')
    window.geometry('300x250+800+350')
    window.resizable(width=False, height=False)
    window["bg"] = "#24587A"
    btn_1 = Button(window, text = " Посчитать среднее арифметическое чисел", command = avg_interface, font = BASE_FONT)
    btn_1.place(x = 15, y = 10)
    btn_2 = Button(window, text = " Проверить является ли число простым", command = is_prime_interface, font = BASE_FONT)
    btn_2.place(x = 25, y = 50)
    btn_3 = Button(window, text = "Выйти", command = quiting_window, font = BASE_FONT)
    btn_3.place(x = 120, y = 220)
    window.mainloop()
    
start()



