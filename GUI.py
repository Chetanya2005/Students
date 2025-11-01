import tkinter as tk
from tkinter import messagebox

def save_student():
    name = name_entry.get()
    roll = roll_entry.get()
    age = age_entry.get()

    if name.strip() == "" or roll.strip() == "" or age.strip() == "":
        messagebox.showerror("Error", "Please fill all fields")
        return

    # Save student data to file
    with open("students.txt", "a") as f:
        f.write(f"Name: {name}, Roll: {roll}, Age: {age}\n")

    # Clear entries after save
    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)

    messagebox.showinfo("Success", "Student saved successfully!")

# GUI window
root = tk.Tk()
root.title("Student Management System")
root.geometry("350x250")

# Name
tk.Label(root, text="Student Name:").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

# Roll Number
tk.Label(root, text="Roll Number:").pack(pady=5)
roll_entry = tk.Entry(root)
roll_entry.pack(pady=5)

# Age
tk.Label(root, text="Age:").pack(pady=5)
age_entry = tk.Entry(root)
age_entry.pack(pady=5)

# Save Button
tk.Button(root, text="Save Student", command=save_student).pack(pady=15)

root.mainloop()
