import tkinter as tk
from tkinter import ttk, messagebox

def submit_form():
    name = name_var.get()
    email = email_var.get()
    phone = phone_var.get()
    address = address_var.get()
    
    if not name or not email or not phone or not address:
        messagebox.showerror("Error", "All fields are required!")
        return
    
    messagebox.showinfo("Success", f"Data Submitted:\nName: {name}\nEmail: {email}\nPhone: {phone}\nAddress: {address}")
    
    name_var.set("")
    email_var.set("")
    phone_var.set("")
    address_var.set("")

root = tk.Tk()
root.title("Responsive Data Entry Form")
root.geometry("400x300")
root.resizable(True, True)

name_var = tk.StringVar()
email_var = tk.StringVar()
phone_var = tk.StringVar()
address_var = tk.StringVar()

frame = ttk.Frame(root, padding=20)
frame.grid(row=0, column=0, sticky="nsew")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Name
ttk.Label(frame, text="Name:").grid(row=0, column=0, sticky="w", pady=5)
name_entry = ttk.Entry(frame, textvariable=name_var, width=30)
name_entry.grid(row=0, column=1, pady=5, sticky="ew")

# Email
ttk.Label(frame, text="Email:").grid(row=1, column=0, sticky="w", pady=5)
email_entry = ttk.Entry(frame, textvariable=email_var, width=30)
email_entry.grid(row=1, column=1, pady=5, sticky="ew")

# Phone
ttk.Label(frame, text="Phone:").grid(row=2, column=0, sticky="w", pady=5)
phone_entry = ttk.Entry(frame, textvariable=phone_var, width=30)
phone_entry.grid(row=2, column=1, pady=5, sticky="ew")

# Address
ttk.Label(frame, text="Address:").grid(row=3, column=0, sticky="w", pady=5)
address_entry = ttk.Entry(frame, textvariable=address_var, width=30)
address_entry.grid(row=3, column=1, pady=5, sticky="ew")

# Submit Button
submit_btn = ttk.Button(frame, text="Submit", command=submit_form)
submit_btn.grid(row=4, column=0, columnspan=2, pady=10)

frame.columnconfigure(1, weight=1)

root.mainloop()
