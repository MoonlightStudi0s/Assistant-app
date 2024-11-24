'''import pickle
import datetime
from datetime import datetime, date
import os
import sys
import customtkinter as ctk

# Определение пути к файлу
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

tasks_file_path = os.path.join(base_path, 'tasks.pkl')

# Список для хранения задач
tasks_list = []


def load_tasks():
    global tasks_list
    try:
        with open('tasks.pkl', 'rb') as f:
            tasks_list = pickle.load(f)
    except (FileNotFoundError, EOFError):
        tasks_list = []


def save_tasks():
    with open('tasks.pkl', 'wb') as f:
        pickle.dump(tasks_list, f)


def addtask(inp, label_tasks):
    taskname = inp.get()
    if taskname:
        tasks_list.append(taskname)
        inp.delete(0, ctk.END)
        update_task_display(label_tasks)


def update_task_display(label_tasks):
    label_tasks.configure(text="\n".join(tasks_list))


def d_upd(label_date):
    bb = date.today()
    label_date.configure(text=f"Today: {bb}")


def t_upd(label_time):
    now = datetime.now()
    label_time.configure(text=f"Now: {now.strftime('%H:%M:%S')}")
    label_time.after(1000, t_upd, label_time)


def wtime():
    win = ctk.CTkToplevel(window)
    win.title("DateTime")
    win.geometry('600x600')

    frame = ctk.CTkFrame(win)
    frame.pack(padx=10, pady=10)

    label_time = ctk.CTkLabel(frame, font=("Galiver Sans", 46))
    label_time.grid(row=1, column=1)
    t_upd(label_time)

    label_date = ctk.CTkLabel(frame, font=("Galiver Sans", 46))
    label_date.grid(row=2, column=1)
    d_upd(label_date)


def tasknum(day):
    global a
    a = day
    wt = ctk.CTkToplevel(window)
    wt.title(f"Day {day}")
    wt.geometry("600x600")

    frame = ctk.CTkFrame(wt)
    frame.pack(padx=10, pady=10)

    label_title = ctk.CTkLabel(frame, text="Your tasks for this day:", font=("Galiver Sans", 25))
    label_title.grid(row=0, column=1)

    inp = ctk.CTkEntry(frame, width=40)
    inp.grid(row=1, column=1)

    label_tasks = ctk.CTkLabel(frame, font=("Galiver Sans", 20))
    label_tasks.grid(row=2, column=1)

    hbut = ctk.CTkButton(frame, text="Add Task", command=lambda: addtask(inp, label_tasks))
    hbut.grid(row=1, column=2)

    update_task_display(label_tasks)


def task_calendar():
    windoww = ctk.CTkToplevel(window)
    windoww.title("Tasks")
    windoww.geometry('600x600')

    frame = ctk.CTkFrame(windoww)
    frame.pack(padx=10, pady=10)

    day_labels = ["M", "T", "Th", "S", "F", "S", "W"]
    for i, day in enumerate(day_labels):
        label = ctk.CTkLabel(frame, text=day, font=("Galiver Sans", 20))
        label.grid(row=0, column=i + 1)

    buttons = {}
    for i in range(30):
        btn_name = f"btn{i + 1}"
        buttons[btn_name] = ctk.CTkButton(frame, text=f"{i + 1}", width=6, height=3, command=lambda i=i: tasknum(i + 1))
        row = (i // 7) + 1
        column = (i % 7) + 1
        buttons[btn_name].grid(row=row, column=column)


# Загружаем задачи при старте
load_tasks()

# Основное окно
ctk.set_appearance_mode("System")  # Options: "Light", "Dark", "System"
ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue", "dark-gray"

window = ctk.CTk()
window.title("Assistant")
window.geometry('600x600')

# Меню
frame = ctk.CTkFrame(window)
frame.pack(expand=True, padx=10, pady=10)

btn_datetime = ctk.CTkButton(frame, text="DateTime", command=wtime, width=6, height=3)
btn_datetime.grid(row=2, column=1)

btn_tasks = ctk.CTkButton(frame, text="Tasks", command=task_calendar, width=6, height=3)
btn_tasks.grid(row=3, column=1)

# Сохраняем задачи при закрытии программы
window.protocol("WM_DELETE_WINDOW", lambda: [save_tasks(), window.destroy()])

window.mainloop()
'''

#предпоследняя версия кода с апдейтом на удаление задач и фиксом задач для дня

'''import pickle
from tkinter import *
from datetime import date, datetime

window = Tk()
window.title("Assistant")
window.geometry('600x600')

# Список для хранения задач
tasks_list = []


def cleartask(aa,label_tasks):
    global tasks_list
    #if aa in label_tasks:
    tasks_list.clear()
    update_task_display(label_tasks)


def load_tasks():
    global tasks_list
    try:
        with open('tasks.pkl', 'rb') as f:
            tasks_list = pickle.load(f)
    except (FileNotFoundError, EOFError):
        tasks_list = []  # Если файл не найден или пуст, начинаем с пустого списка


def save_tasks():
    with open('tasks.pkl', 'wb') as f:
        pickle.dump(tasks_list, f)


def addtask(inp, label_tasks):
    taskname = inp.get()
    if taskname:  # Проверяем, что задача не пустая
        tasks_list.append(str(taskname))  # Убедитесь, что задача — это строка
        inp.delete(0, END)  # Очищаем строку ввода
        update_task_display(label_tasks)  # Обновляем отображение задач


def update_task_display(label_tasks):
    # Преобразуем все элементы в строки, если они не являются таковыми
    str_tasks_list = [str(task) for task in tasks_list]
    label_tasks.config(text="\n".join(str_tasks_list))  # Обновляем текст выше всех задач


def d_upd(lableee):
    bb = date.today()
    lableee.config(text=f"Today: {bb.year}-{bb.month}-{bb.day}")


def t_upd(lablee):
    b = datetime.now()
    lablee.config(text=f"Now: {b.hour}:{b.minute}:{b.second}")
    lablee.after(1000, t_upd, lablee)


def wtime():
    win = Toplevel(window)
    win.title("DateTime")
    win.geometry('600x600')

    ff = Frame(win, pady=1, padx=1)
    ff.pack()
    lablee = Label(ff, font=("Galiver Sans", 46))
    lablee.grid(row=1, column=1)
    t_upd(lablee)
    lableee = Label(ff, font=("Galiver Sans", 46))
    lableee.grid(row=2, column=1)
    d_upd(lableee)


def tasknum(aa):
    wt = Toplevel(window)
    wt.title(f"Day {aa}")
    wt.geometry("600x600")

    fr = Frame(wt, padx=5, pady=2)
    fr.pack(side="left", anchor="nw")

    toftask = Label(fr, text="Your tasks for this day:", font=("Galiver Sans", 25))
    toftask.grid(row=0, column=1)

    inp = Entry(fr, width=40)
    inp.grid(row=1, column=1)

    label_tasks = Label(fr, font=("Galiver Sans", 20))
    label_tasks.grid(row=2, column=1)

    hbut = Button(fr, text="Add Task", command=lambda: addtask(inp, label_tasks))
    hbut.grid(row=1, column=2)

    clearbut = Button(fr, text="clear tasks", command=lambda: cleartask(aa,label_tasks))
    clearbut.grid(row=1,column=3)


    update_task_display(label_tasks)  # Отображаем уже сохраненные задачи


def task_calendar():
    windoww = Toplevel(window)
    windoww.title("Tasks")
    windoww.geometry('600x600')

    frame = Frame(windoww, padx=60, pady=20)
    frame.pack(side="left", anchor="nw")

    days = ["M", "T", "Th", "S", "F", "S", "W"]
    for i, day in enumerate(days):
        Label(frame, text=day, font=("Galiver Sans", 20)).grid(row=0, column=i + 1)

    for i in range(30):
        Button(frame, text=f"{i + 1}", width=6, height=3, command=lambda i=i: tasknum(f"{i + 1}")).grid(
            row=(i // 7) + 1, column=(i % 7) + 1)


# Загружаем задачи при старте
load_tasks()

# Главное меню
frame = Frame(window, padx=2, pady=2)
frame.pack(expand=True)

Button(frame, text="DateTime", command=wtime, width=6, height=3).grid(row=2, column=1)
Button(frame, text="Tasks", command=task_calendar, width=6, height=3).grid(row=3, column=1)

# Сохраняем задачи при закрытии программы
window.protocol("WM_DELETE_WINDOW", lambda: [save_tasks(), window.destroy()])

window.mainloop()
'''

import pickle
from tkinter import *
from datetime import datetime, date
import os
import sys

# Определение пути к файлу
if getattr(sys, 'frozen', False):
    # Если программа запущена как .exe
    base_path = sys._MEIPASS
else:
    # Если программа запускается из источника
    base_path = os.path.dirname(os.path.abspath(__file__))

# Полный путь к файлу tasks.pkl
tasks_file_path = os.path.join(base_path, 'tasks.pkl')

window = Tk()
window.title("Assistant")
window.geometry('600x600')

# Словарь для хранения задач по дням
tasks_dict = {}


def load_tasks():
    global tasks_dict
    try:
        with open(tasks_file_path, 'rb') as f:
            tasks_dict = pickle.load(f)

            if not isinstance(tasks_dict, dict):  # Проверяем, что загруженные данные - это словарь
                tasks_dict = {}
    except (FileNotFoundError, EOFError):
        tasks_dict = {}  # Если файл не найден или пуст, начинаем с пустого словаря

def save_tasks():
    with open(tasks_file_path, 'wb') as f:
        pickle.dump(tasks_dict, f)

def addtask(inp, label_tasks):
    taskname = inp.get().strip()  # Убираем лишние пробелы
    if taskname:  # Проверяем, что задача не пустая
        day = a  # Используем глобальную переменную дня
        if day not in tasks_dict:
            tasks_dict[day] = []  # Инициализируем список задач, если его нет
        tasks_dict[day].append(taskname)  # Добавляем задачу в список задач для этого дня
        inp.delete(0, END)  # Очищаем строку ввода
        update_task_display(label_tasks)  # Обновляем отображение задач

def update_task_display(label_tasks):
    day = a  # Используем глобальную переменную дня
    tasks_for_today = tasks_dict.get(day, [])  # Получаем задачи для текущего дня
    label_tasks.config(text="\n".join(tasks_for_today))  # Обновляем текст задач

def d_upd(lableee):
    bb = date.today()
    lableee.config(text=f"Today: {bb}")

def t_upd(lablee):
    now = datetime.now()
    lablee.config(text=f"Now: {now.strftime('%H:%M:%S')}")
    lablee.after(1000, t_upd, lablee)

def wtime():
    win = Toplevel(window)
    win.title("DateTime")
    win.geometry('600x600')

    ff = Frame(win, pady=1, padx=1)
    ff.pack()
    lablee = Label(ff, font=("Galiver Sans", 46))
    lablee.grid(row=1, column=1)
    t_upd(lablee)
    lableee = Label(ff, font=("Galiver Sans", 46))
    lableee.grid(row=2, column=1)
    d_upd(lableee)

def tasknum(day):
    global a
    a = day
    wt = Toplevel(window)
    wt.title(f"Tasks for Day {day}")
    wt.geometry("600x600")

    fr = Frame(wt, padx=5, pady=2)
    fr.pack(side="left", anchor="nw")

    toftask = Label(fr, text="Your tasks for this day:", font=("Galiver Sans", 25))
    toftask.grid(row=0, column=1)

    inp = Entry(fr, width=40)
    inp.grid(row=1, column=1)

    label_tasks = Label(fr, font=("Galiver Sans", 20))
    label_tasks.grid(row=2, column=1)

    hbut = Button(fr, text="Add Task", command=lambda: addtask(inp, label_tasks))
    hbut.grid(row=1, column=2)





    update_task_display(label_tasks)  # Отображаем уже сохраненные задачи для текущего дня

def task_calendar():
    windoww = Toplevel(window)
    windoww.title("Tasks")
    windoww.geometry('600x600')

    frame = Frame(windoww, padx=60, pady=20)
    frame.pack(side="left", anchor="nw")

    # Создаем кнопки для дней
    for i in range(30):
        day = i + 1
        Button(frame, text=f"{day}", width=6, height=3, command=lambda day=day: tasknum(day)).grid(row=(i // 7) + 1, column=(i % 7) + 1)

# Загружаем задачи при старте
load_tasks()

# Главное меню
frame = Frame(window, padx=2, pady=2)
frame.pack(expand=True)

but = Button(frame, text="DateTime", command=wtime, width=6, height=3)
but.grid(row=2, column=1)
taskbut = Button(frame, text="Tasks", command=task_calendar, width=6, height=3)
taskbut.grid(row=3, column=1)

# Сохраняем задачи при закрытии программы
window.protocol("WM_DELETE_WINDOW", lambda: [save_tasks(), window.destroy()])

window.mainloop()



