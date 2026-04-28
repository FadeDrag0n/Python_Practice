import tkinter as tk


def show_status():
    status1 = "+" if var1.get() else "-"
    status2 = "+" if var2.get() else "-"

    report = f"flag 1: {status1}, flag 2: {status2}"

    entry.delete(0, tk.END)
    entry.insert(0, report)


root = tk.Tk()
root.title("Checkbutton ex")

var1 = tk.BooleanVar()
var2 = tk.BooleanVar()

cb1 = tk.Checkbutton(root, text="Option 1", variable=var1)
cb1.pack(pady=5)

cb2 = tk.Checkbutton(root, text="Option 2", variable=var2)
cb2.pack(pady=5)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

btn = tk.Button(root, text="Show status", command=show_status)
btn.pack(pady=10)

root.mainloop()