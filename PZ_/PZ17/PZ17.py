import tkinter as tk
from tkinter import messagebox

def on_ok_click():
    messagebox.showinfo("Успех", "Регистрация завершена (данные не отправлены)")

def on_cancel_click():
    root.destroy()

# Создание основного окна с бежевым фоном
root = tk.Tk()
root.title("Регистрация в электронной библиотеке")
root.geometry("600x700")
root.configure(bg='#F5F5DC')  # Бежевый фон

# Функция для создания строки с меткой и полем ввода
def create_label_entry(parent, text, show=None):
    frame = tk.Frame(parent, bg='#F5F5DC')
    frame.pack(fill=tk.X, pady=5)
    
    label = tk.Label(frame, text=text, width=25, anchor='e', bg='#F5F5DC')
    label.pack(side=tk.LEFT, padx=5)
    
    if show:
        entry = tk.Entry(frame, show=show, width=30)
    else:
        entry = tk.Entry(frame, width=30)
    entry.pack(side=tk.LEFT)
    
    return entry

# Заголовок
title_label = tk.Label(
    root,
    text="Заполнив анкету, вы сможете пользоваться нашей электронной библиотекой",
    wraplength=500,
    font=("Arial", 12),
    bg='#F5F5DC'
)
title_label.pack(pady=15)

# Поля для ввода
name_entry = create_label_entry(root, "Введите регистрационное имя:")
password_entry = create_label_entry(root, "Введите пароль:", "*")
confirm_password_entry = create_label_entry(root, "Подтвердите пароль:", "*")

# Возраст
age_frame = tk.Frame(root, bg='#F5F5DC')
age_frame.pack(fill=tk.X, pady=5)

age_label = tk.Label(age_frame, text="Ваш возраст:", width=25, anchor='e', bg='#F5F5DC')
age_label.pack(side=tk.LEFT, padx=5)

age_var = tk.StringVar(value="20-30")
age_options_frame = tk.Frame(age_frame, bg='#F5F5DC')
age_options_frame.pack(side=tk.LEFT)

ages = ["До 20", "20-30", "30-50", "Старше 50"]
for age in ages:
    tk.Radiobutton(
        age_options_frame,
        text=age,
        variable=age_var,
        value=age,
        bg='#F5F5DC'
    ).pack(side=tk.LEFT, padx=5)

# Языки
lang_frame = tk.Frame(root, bg='#F5F5DC')
lang_frame.pack(fill=tk.X, pady=5)

lang_label = tk.Label(lang_frame, text="На каких языках читаете:", width=25, anchor='e', bg='#F5F5DC')
lang_label.pack(side=tk.LEFT, padx=5)

lang_vars = []
languages = ["Русский", "Английский", "Французский", "Немецкий"]
for lang in languages:
    var = tk.IntVar()
    cb = tk.Checkbutton(
        lang_frame,
        text=lang,
        variable=var,
        bg='#F5F5DC'
    )
    cb.pack(side=tk.LEFT, padx=5)
    lang_vars.append((lang, var))

# Формат данных
format_frame = tk.Frame(root, bg='#F5F5DC')
format_frame.pack(fill=tk.X, pady=5)

format_label = tk.Label(format_frame, text="Предпочтительный формат данных:", width=25, anchor='e', bg='#F5F5DC')
format_label.pack(side=tk.LEFT, padx=5)

format_var = tk.StringVar(value="HTML")
tk.Radiobutton(
    format_frame,
    text="HTML",
    variable=format_var,
    value="HTML",
    bg='#F5F5DC'
).pack(side=tk.LEFT, padx=5)
tk.Radiobutton(
    format_frame,
    text="Plain text",
    variable=format_var,
    value="Plain text",
    bg='#F5F5DC'
).pack(side=tk.LEFT, padx=5)

# Любимые авторы
authors_frame = tk.Frame(root, bg='#F5F5DC')
authors_frame.pack(fill=tk.X, pady=5)

authors_label = tk.Label(authors_frame, text="Ваши любимые авторы:", width=25, anchor='e', bg='#F5F5DC')
authors_label.pack(side=tk.LEFT, padx=5)

authors_entry = tk.Entry(authors_frame, width=30)
authors_entry.pack(side=tk.LEFT)

# Кнопки
button_frame = tk.Frame(root, bg='#F5F5DC')
button_frame.pack(pady=20)
tk.Button(
    button_frame,
    text="OK",
    command=on_ok_click,
    width=15
).pack(side=tk.LEFT, padx=20)
tk.Button(
    button_frame,
    text="Отменить",
    command=on_cancel_click,
    width=15
).pack(side=tk.LEFT, padx=20)

# Нижний текст
bottom_text = """Проверка PHP Лабораторные по базам данных

Лабораторные по базам данных

Сегодня замечательный день
Я сделал свою первую интернет страничку
и буду богатым и свободным человеком!"""

tk.Label(
    root,
    text=bottom_text,
    justify=tk.LEFT,
    bg='#F5F5DC'
).pack(pady=20)

root.mainloop()