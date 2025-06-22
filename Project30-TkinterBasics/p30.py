import tkinter as tk

window = tk.Tk()
window.resizable(False, False)
window.title("My first Tkinter App")
window.geometry("300x200")


def say_hello():
    name = name_entry.get()
    if name:
        greeting_label.config(text=f"Hello,{name}")
    else:
        greeting_label.config(text="Enter Name")


welcome_label = tk.Label(window, text="Welcome to the App", font=("Arial", 16))
welcome_label.pack(pady=10)

name_entry = tk.Entry(window, width=20)
name_entry.pack(pady=10)

name_button = tk.Button(window, text="Say your name",
                        font=("Arial", 16), command=say_hello)
name_button.pack(pady=10)

greeting_label = tk.Label(window, text="", font=("Arail", 16))
greeting_label.pack(pady=10)


window.mainloop()
