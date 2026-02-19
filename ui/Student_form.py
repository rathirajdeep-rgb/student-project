import tkinter as tk
from tkinter import messagebox
from services.Student_services import add_student, get_student_by_email, get_student_by_first_name

root = tk.Tk()
root.title("Student Management")
root.geometry("750x300")
tk.Label(root, text="First Name").grid(row=0, column=0, padx=100, pady=10)
tk.Label(root, text="Last Name").grid(row=1, column=0, padx=100, pady=10)
tk.Label(root, text="Date of Birth").grid(row=2, column=0, padx=100, pady=10)
tk.Label(root, text="Email Id").grid(row=3, column=0, padx=100, pady=10)

first_name_entry = tk.Entry(root)
last_name_entry = tk.Entry(root)
dob_entry = tk.Entry(root)
email_entry = tk.Entry(root)

first_name_entry.grid(row=0, column=1)
last_name_entry.grid(row=1, column=1)
dob_entry.grid(row=2, column=1)
email_entry.grid(row=3, column=1)

def add_student_ui():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    date_of_birth = dob_entry.get()
    email_id = email_entry.get()

    if not all([first_name, last_name, date_of_birth, email_id]):
        messagebox.showerror("Error", "Please enter all fields")
        return
    try:
        add_student(first_name, last_name, date_of_birth, email_id)
        messagebox.showinfo("Success", "Student added successfully")
        first_name_entry.delete(0, tk.END)
        last_name_entry.delete(0, tk.END)
        dob_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def search_student_ui():
    email_id = email_entry.get().strip()
    first_name = first_name_entry.get().strip()
    if not email_id and not first_name:
        messagebox.showerror("Error", "Please enter Email or First Name to search")
        return
    try:
        if email_id:
            student = get_student_by_email(email_id)
        else:
            student = get_student_by_first_name(first_name)
        if not student:
            messagebox.showerror("Error", "Student not found")
            return
        first_name_entry.delete(0, tk.END)
        last_name_entry.delete(0, tk.END)
        dob_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        first_name_entry.insert(0, student['first_name'])
        last_name_entry.insert(0, student['last_name'])
        dob_entry.insert(0, student['dob'])
        email_entry.insert(0, student['email'])

    except Exception as e:
        messagebox.showerror("Error", str(e))

def clear_student_ui():
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    dob_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

# Buttons
tk.Button(root, text="Add Student", width = 15, command = add_student_ui)\
          .grid(row = 4, column = 0,  pady = 15)
tk.Button(root, text="Search Student", width = 15, command = search_student_ui)\
          .grid(row = 4, column = 1, pady = 15)
tk.Button(root, text="Clear Student", width = 15, command = clear_student_ui)\
          .grid(row =5, column = 0, columnspan = 2)

#start UI loop
root.mainloop()



