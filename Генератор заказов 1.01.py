#!/usr/bin/env python 
# -- coding: utf-8 --

from tkinter import *
from re import search
import datetime
import pyperclip



root = Tk()


root.wm_title("Форма заказа")


############

# 
# def copy(event):
#     print('copy')
# 
# def paste(event):
#     print('paste')
# 
# def cut(event):
#     print('paste')
# 
# def test(event):    
#     print('event.char:', event.char)
#     print('event.keycode:', event.keycode)
#     print('event.keysym:', event.keysym)
#     print('---')
# 
# 
# root.bind('<Control-c>', copy)
# root.bind('<Control-v>', paste)
# root.bind('<Control-ntilde>', copy)
# root.bind('<Control-igrave>', paste)
# root.bind('<Control-x>', cut)
# root.bind('<Control-division>', cut)
# root.bind('<Control-Cyrillic_em>', paste)
# 
#         
##################



def getForm():
    answers=[]
    extra=False
    wtext=''
    labelWarning.config(text='', bg=None)

    for a in range(0,17): #собрал answers
        if (a==6) or (a==8) or (a==16):
            answers.append((Elist[a].get('1.0', END)).replace("\n",""))
        else:
            answers.append((Elist[a].get().replace("\n","")))
    
    for x in answers[:8]:
        if x=='':
            wtext=' часть обязательных полей не заполнена!'
            labelWarning.config(text=wtext, bg='red')
    
    for x in answers[9:15]:
        if x!='':
            extra=True
            for y in answers[9:14]:
                if y=='': 
                    wtext=' часть обязательных полей не заполнена!'
                    labelWarning.config(text=wtext, bg='red')
    
    if wtext=='':
            
        if extra==False:
            if not dateformat(answers[0]):
                wtext+=' неверный формат даты!'
                labelWarning.config(text=wtext, bg='red')
            if not numformat(answers[7]):
                wtext+=' неверный формат числовых данных!'
                labelWarning.config(text=wtext, bg='red')
        else:
            if not (dateformat(answers[0]) and dateformat(answers[9])):
                wtext+=' неверный формат даты!'
                labelWarning.config(text=wtext, bg='red')
            if not (all((numformat(answers[7]), numformat(answers[12]), numformat(answers[13]), numformate(answers[15])))):
                wtext+=' неверный формат количества или суммы!'
                labelWarning.config(text=wtext, bg='red')
        if not emailformat(answers[2]):
                wtext+=' неверный формат e-mail!'
                labelWarning.config(text=wtext, bg='red')

    if wtext=='':
        filename=str(answers[1])+' - ' + ''.join(filter(lambda x: x.isdigit(), str(datetime.datetime.now())))+'.cardboardia'
        labelWarning.config(text='''Спасибо, информация сформирована и сохранена в файл '''+filename+'''!
        Вы можете использовать эту же форму для создания новых заказов.''', bg='green')
        f=open(filename, 'w')
        for x in answers:
            f.write(x+'\n')
        f.close()



def emailformat(text):
    match=search(r"^\w[\w.]+@[\w.]+\w$",text)
    if match:
        return True
    return False

def numformat(text):
    match=search(r'^[\d.]+$',text)
    if match:
        return True
    return False
    
def numformate(text):
    match=search(r'^[\d.]+$',text)
    if (match) or (text==''):
        return True
    return False    


def dateformat(text):
    match=search(r'^[0123]\d\.[01]\d\.20\d\d$',text)
    if match:
        return True
    return False

'''дальше - интерфейс'''

Label(root, text='     ').grid(column=3)
Label(root, text='     ').grid(column=6)

labelWarning = Label(root, text='')
labelWarning.grid(row=0, column=0, columnspan=6)
label0 = Label(root, text="ЗАКАЗ:", font=('Arial',15)).grid(column=0, row=1, columnspan=3)

label1 = Label(root, text=" Дата заказа (ДД.ММ.ГГГГ):*").grid(column=0, row=3)
E1 = Entry(root, bd=3,width=9)
E1.grid(column=1, row=3)

label2 = Label(root, text="Кто заказывает:*").grid(column=0, row=4)
E2 = Entry(root, bd=3, width=30)
E2.grid(column=1, row=4)

label3 = Label(root, text="E-mail:*").grid(column=0, row=5)
E3 = Entry(root, bd=3, width=30)
E3.grid(column=1, row=5)

label4 = Label(root, text="Должность:*").grid(column=0, row=6)
E4 = Entry(root, bd=3, width=30)
E4.grid(column=1, row=6)

label5 = Label(root, text=" Ответственный менеджер:*").grid(column=0, row=7)
E5 = Entry(root, bd=3, width=30)
E5.grid(column=1, row=7)

label6 = Label(root, text="Проект:*").grid(column=0, row=8)
E6 = Entry(root, bd=3, width=30)
E6.grid(column=1, row=8)

label7 = Label(root, text="Что нужно и единицы измерения (шт./кг./л.):*").grid(column=0, row=9)
E7 = Text(root, bd=3, height=5, width=23)
E7.grid(column=1, row=9, rowspan=5)

label8 = Label(root, text="Сколько (только цифра):*").grid(column=0, row=15)
E8 = Entry(root, bd=3, width=30)
E8.grid(column=1, row=15)

label9 = Label(root, text="Комментарий к заказу:").grid(column=0, row=16)
E9 = Text(root, bd=3, height=4, width=23)
E9.grid(column=1, row=16, rowspan=4)

label10 = Label(root, text="ЭТА ЧАСТЬ ЗАПОЛНЯЕТСЯ, ТОЛЬКО ЕСЛИ УЖЕ КУПИЛ:", font=('Arial',15)).grid(column=4, columnspan=3, row=1)

label11 = Label(root, text=" Дата покупки (ДД.ММ.ГГГГ):**").grid(column=4, row=3)
E11 = Entry(root, bd=3,width=9)
E11.grid(column=5, row=3)

label12 = Label(root, text="Кто купил:**").grid(column=4, row=4)
E12= Entry(root, bd=3, width=30)
E12.grid(column=5, row=4)

label13 = Label(root, text="Магазин/поставщик**").grid(column=4, row=5)
E13 = Entry(root, bd=3, width=30)
E13.grid(column=5, row=5)

label14 = Label(root, text="Цена за единицу измерения (руб):**").grid(column=4, row=6)
E14 = Entry(root, bd=3, width=30)
E14.grid(column=5, row=6)

label15 = Label(root, text="Количество (только цифра):**").grid(column=4, row=7)
E15 = Entry(root, bd=3, width=30)
E15.grid(column=5, row=7)

label16 = Label(root, text="Дополнительные траты - на что:").grid(column=4, row=8)
E16 = Entry(root, bd=3, width=30)
E16.grid(column=5, row=8)

label17 = Label(root, text="Дополнительные траты - сумма (руб.):").grid(column=4, row=9)
E17 = Entry(root, bd=3, width=30)
E17.grid(column=5, row=9)

label18 = Label(root, text="Комментарий к покупке:").grid(column=4, row=10)
E18 = Text(root, bd=3, height=4, width=23)
E18.grid(column=5, row=10, rowspan=4)

Label(root).grid(column=0)


label19 = Label(root, text=r''' Для копирования и вставки используйте Ctrl+C и Ctrl+V. Поля отмеченные * обязательны к заполнению. 
 Поля отмеченные ** обязательны к заполнению, если Вы заполняете 2-ю часть формы. 
 Сформированные документы необходимо высылать на oksana.sinkevich@gmail.com .''').grid(column=4, row=15, columnspan=3, rowspan=3)

Elist=(E1,E2,E3,E4,E5,E6,E7,E8,E9,E11,E12,E13,E14,E15,E16,E17,E18)

submit = Button(root, text ="Сформировать", command = getForm)
submit.grid(column=4, row=18, columnspan=3, rowspan=2)


root.mainloop()

