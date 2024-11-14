import tkinter as tk 
from tkinter import messagebox
def submit_form():
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    if not name or not age or not email:
        messagebox.showwarning("Input Error", "All fields are required")
        return
    
    messagebox.showinfo("Form Submitted", f"name: {name}\nAge: {age}\nEmail: {email}")

root = tk.Tk()
root.title("Entry Form")

tk.Label(root, text = "Name:").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text = "Age:").grid(row=1, column=0, padx=10, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text = "Email:").grid(row=2, column=0, padx=10, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, padx=10, pady=5)

submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=3, column=2, padx=10)

root.mainloop()