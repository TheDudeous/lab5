import tkinter as tk

def add_digit(digit):
    """Добавляет цифру в поле ввода."""
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(digit))

def add_operation(op):
    """Добавляет знак операции в поле ввода."""
    current = entry.get()
    if current and current[-1] not in "+-*/":
        entry.delete(0, tk.END)
        entry.insert(0, current + op)

def clear():
    """Очищает поле ввода."""
    entry.delete(0, tk.END)

def calculate():
    """Вычисляет выражение и выводит результат."""
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(0, "Деление на 0!")
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")


root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x400")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 20), justify="right", bd=8)
entry.pack(fill="x", padx=10, pady=10, ipady=8)

buttons_frame = tk.Frame(root)
buttons_frame.pack(expand=True, fill="both", padx=10, pady=10)

buttons = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("0", 3, 0), ("C", 3, 1), ("=", 3, 2), ("+", 3, 3),
]

for text, row, col in buttons:
    if text.isdigit():
        cmd = lambda t=text: add_digit(t)
    elif text in "+-*/":
        cmd = lambda t=text: add_operation(t)
    elif text == "C":
        cmd = clear
    else: 
        cmd = calculate

    tk.Button(
        buttons_frame,
        text=text,
        font=("Arial", 16),
        command=cmd,
        width=4,
        height=2,
    ).grid(row=row, column=col, padx=3, pady=3, sticky="nsew")

for i in range(4):
    buttons_frame.columnconfigure(i, weight=1)
    buttons_frame.rowconfigure(i, weight=1)

root.mainloop()
