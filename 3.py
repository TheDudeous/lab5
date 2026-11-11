import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Программа со вкладками")
root.geometry("500x350")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Привет")

ttk.Label(tab1, text="Введите имя:", font=("Arial", 12)).pack(pady=10)

name_entry = ttk.Entry(tab1, font=("Arial", 12))
name_entry.pack(pady=5)

greeting = ttk.Label(tab1, text="", font=("Arial", 14, "bold"))
greeting.pack(pady=10)

def say_hello():
    name = name_entry.get().strip() or "друг"
    greeting.config(text=f"Привет, {name}!")

ttk.Button(tab1, text="Поздороваться", command=say_hello).pack(pady=5)

tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Калькулятор")

calc_entry = ttk.Entry(tab2, font=("Arial", 16), justify="right")
calc_entry.pack(fill="x", padx=10, pady=10)

def press(key):
    if key == "C":
        calc_entry.delete(0, tk.END)
    elif key == "=":
        try:
            calc_entry.delete(0, tk.END)
            calc_entry.insert(0, str(eval(calc_entry.get())))
        except Exception:
            calc_entry.delete(0, tk.END)
            calc_entry.insert(0, "Ошибка")
    else:
        calc_entry.insert(tk.END, key)

calc_frame = ttk.Frame(tab2)
calc_frame.pack(padx=10, pady=10)

calc_buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+",
]
for i, text in enumerate(calc_buttons):
    ttk.Button(
        calc_frame, text=text, width=5,
        command=lambda t=text: press(t)
    ).grid(row=i // 4, column=i % 4, padx=2, pady=2)

tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Заметки")

text = tk.Text(tab3, wrap="word", font=("Consolas", 11))
text.pack(fill="both", expand=True, padx=10, pady=10)
text.insert("1.0", "Здесь можно писать заметки...\n")

tab4 = ttk.Frame(notebook)
notebook.add(tab4, text="О программе")

about = (
    "Программа со вкладками\n\n"
    "Демонстрирует виджет ttk.Notebook —\n"
    "контейнер, который переключает\n"
    "содержимое по вкладкам.\n\n"
    "Вкладки:\n"
    " • Привет — ввод имени и приветствие\n"
    " • Калькулятор — простая арифметика\n"
    " • Заметки — многострочное поле\n"
    " • О программе — эта справка"
)
ttk.Label(tab4, text=about, justify="left",
          font=("Arial", 11)).pack(padx=20, pady=20, anchor="w")

root.mainloop()
