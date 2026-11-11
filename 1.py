import tkinter as tk

root = tk.Tk()
root.title("Моё первое окно")
root.geometry("300x200")

def say_hello():
    print("Привет!")

button = tk.Button(
    root,
    text="Привет",
    command=say_hello, 
    font=("Arial", 14),
    padx=20,
    pady=10
)

button.pack(expand=True)

root.mainloop()
