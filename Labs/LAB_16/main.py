import tkinter as tk

def on_closing():
    print("Bye! Bye!")
    root.destroy()

def simple_action():
    print("Button Pressed (command)")
    btn1.config(text="Pressed!")
    lbl.config(text="Btn1 was pressed")

def action_with_arg(text):
    print(f"Argument: {text}")
    text = entry1.get()
    entry2.delete(0, tk.END)
    entry2.insert(0, text)

def left_click(event):
    print("Left mouse button (bind)")

def right_click(event):
    print("Right mouse button (bind)")

root = tk.Tk()
root.geometry("300x600")
icon = tk.PhotoImage(file="icon.gif")
root.iconphoto(True, icon)
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", on_closing)

btn1 = tk.Button(root, text="Command", command=simple_action)
btn1.pack(pady=5)

btn2 = tk.Button(root, text="Lambda", command=lambda: action_with_arg("Hello!"))
btn2.pack(pady=5)

btn3 = tk.Button(root, text="Bind LMB")
btn3.bind("<Button-1>", left_click)
btn3.pack(pady=5)

btn4 = tk.Button(root, text="Bind RMB")
btn4.bind("<Button-3>", right_click)
btn4.pack(pady=5)

lbl = tk.Label(root, text="Waiting...")
lbl.pack(pady=5)

entry1 = tk.Entry(root, width=20)
entry2 = tk.Entry(root, width=20)
entry1.pack(pady=5)
entry2.pack(pady=5)

text_var = tk.StringVar()

entry = tk.Entry(root, textvariable=text_var)
entry.pack(pady=10)
label = tk.Label(root, textvariable=text_var)
label.pack(pady=10)
button = tk.Button(root, textvariable=text_var)
button.pack(pady=10)


root.mainloop()