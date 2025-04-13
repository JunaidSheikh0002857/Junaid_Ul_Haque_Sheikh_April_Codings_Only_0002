import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry_var.get()))
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + text)

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font=("Arial", 20), justify='right', bd=10, relief=tk.SUNKEN)
entry.pack(fill=tk.BOTH, ipadx=8, ipady=8, pady=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

frame = tk.Frame(root)
frame.pack()

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(side=tk.TOP)
    for btn_text in row:
        button = tk.Button(row_frame, text=btn_text, font=("Arial", 18), padx=20, pady=20)
        button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        button.bind("<Button-1>", on_click)

root.mainloop()
