import pickle
from tkinter import *
from datetime import date, datetime

window = Tk()
window.title("Assistant")
window.geometry('600x600')
window.resizable(False,False)

# Словарь для хранения задач по дням
tasks_dict = {}


def load_tasks():
    global tasks_dict
    try:
        with open('tasks.pkl', 'rb') as f:
            tasks_dict = pickle.load(f)
            if not isinstance(tasks_dict, dict):  # Убедимся, что это словарь
                tasks_dict = {}
    except (FileNotFoundError, EOFError):
        tasks_dict = {}  # Если файл не найден или пуст, начинаем с пустого словаря


def save_tasks():
    with open('tasks.pkl', 'wb') as f:
        pickle.dump(tasks_dict, f)


def addtask(inp, label_tasks, day):
    taskname = inp.get()
    if taskname:  # Проверяем, что задача не пустая
        if day not in tasks_dict:
            tasks_dict[day] = []  # Создаем новый список задач для дня, если его нет
        tasks_dict[day].append(taskname)  # Добавляем задачу в список
        inp.delete(0, END)  # Очищаем строку ввода
        update_task_display(label_tasks, day)  # Обновляем отображение задач


def clear_tasks(label_tasks, day):
    global tasks_dict
    if day in tasks_dict:
        tasks_dict[day].clear()  # Очищаем задачи для выбранного дня
        update_task_display(label_tasks, day)  # Обновляем отображение задач


def accepttask(inp_number, label_tasks, day):
    try:
        task_index = int(inp_number.get()) - 1  # Получение порядкового номера задачи
        if day in tasks_dict and 0 <= task_index < len(tasks_dict[day]):
            label = label_tasks.grid_slaves(row=task_index + 1, column=1)[0]  # Получаем подходящую метку
            label.config(bg="green")  # Окрашиваем задачу в зеленый цвет
        inp_number.delete(0, END)  # Очищаем входное поле
    except (ValueError, IndexError):
        pass  # Игнорируем ошибки преобразования или индекса


def declinetask(inp_number, label_tasks, day):
    try:
        task_index = int(inp_number.get()) - 1  # Получение порядкового номера задачи
        if day in tasks_dict and 0 <= task_index < len(tasks_dict[day]):
            label = label_tasks.grid_slaves(row=task_index + 1, column=1)[0]  # Получаем подходящую метку
            label.config(bg="red")  # Окрашиваем задачу в красный цвет
        inp_number.delete(0, END)  # Очищаем входное поле
    except (ValueError, IndexError):
        pass  # Игнорируем ошибки преобразования или индекса


def update_task_display(label_tasks, day):
    # Очищаем метки для обновления
    for widget in label_tasks.grid_slaves():
        widget.destroy()

    tasks_list = tasks_dict.get(day, [])
    for idx, task in enumerate(tasks_list):
        task_label = Label(label_tasks, text=task, font=("Galiver Sans", 20))
        task_label.grid(row=idx, column=1)  # Установка метки на соответствующую строку и колонку


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


def tasknum(day):
    wt = Toplevel(window)
    wt.title(f"Day {day}")
    wt.geometry("750x600")

    fr = Frame(wt, padx=5, pady=2)
    fr.pack(side="left", anchor="nw")

    toftask = Label(fr, text=f"Your tasks for day {day}:", font=("Galiver Sans", 25))
    toftask.grid(row=0, column=1)

    inp = Entry(fr, width=40)
    inp.grid(row=1, column=1)

    label_tasks = Frame(fr)
    label_tasks.grid(row=2, column=1)

    hbut = Button(fr, text="Add Task", command=lambda: addtask(inp, label_tasks, day))
    hbut.grid(row=1, column=2)

    clearbut = Button(fr, text="Clear Tasks", command=lambda: clear_tasks(label_tasks, day))
    clearbut.grid(row=1, column=3)

    accepttasken = Entry(fr, width=5)
    accepttasken.grid(row=1, column=4)

    accepttaskbut = Button(fr, text="Accept", command=lambda: accepttask(accepttasken, label_tasks, day))
    accepttaskbut.grid(row=1, column=5)

    declinetasken = Entry(fr, width=5)
    declinetasken.grid(row=2, column=4)

    declinetaskbut = Button(fr, text="Decline", command=lambda: declinetask(declinetasken, label_tasks, day))
    declinetaskbut.grid(row=2, column=5)

    update_task_display(label_tasks, day)  # Отображаем уже сохраненные задачи для данного дня


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
