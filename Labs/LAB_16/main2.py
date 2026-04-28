import tkinter as tk

def move_item():
    selection = listbox1.curselection()
    if selection:
        index = selection[0]
        value = listbox1.get(index)

        listbox1.delete(index)      # видаляємо з першого
        listbox2.insert(tk.END, value)  # додаємо в другий

def change_color():
    color = color_var.get()
    root.config(bg=color)

root = tk.Tk()
root.title("Перенесення елементів")

data1 = ["Ivan", "Petro", "Oleg"]
data2 = ["Mariya", "Ann"]

var1 = tk.StringVar(value=data1)
var2 = tk.StringVar(value=data2)

listbox1 = tk.Listbox(root, listvariable=var1)
listbox1.pack(side="left", padx=10, pady=10)

listbox2 = tk.Listbox(root, listvariable=var2)
listbox2.pack(side="right", padx=10, pady=10)

btn = tk.Button(root, text=">>", command=move_item)
btn.pack(pady=20)

color_var = tk.StringVar(value="white")

rb1 = tk.Radiobutton(root, text="Red", variable=color_var, value="red", command=change_color)
rb1.pack(pady=5)

rb2 = tk.Radiobutton(root, text="Blue", variable=color_var, value="blue", command=change_color)
rb2.pack(pady=5)

root.mainloop()