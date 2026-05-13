import tkinter as tk
from tkinter import messagebox
from pathlib import Path
import os

root = tk.Tk()
root.title("File Handling CRUD App")
root.geometry("500x500")

# ------------------ Functions ------------------

def create_file():

    file_name = entry_file.get()
    content = text_content.get("1.0", tk.END)

    p = Path(file_name)

    if p.exists():
        messagebox.showerror("Error", "File Already Exists")

    else:
        with open(file_name, "w") as file:
            file.write(content)

        messagebox.showinfo("Success", "File Created")


def read_file():

    file_name = entry_file.get()

    p = Path(file_name)

    if p.exists():

        with open(file_name, "r") as file:
            data = file.read()

        text_content.delete("1.0", tk.END)
        text_content.insert(tk.END, data)

    else:
        messagebox.showerror("Error", "File Not Found")


def update_file():

    file_name = entry_file.get()
    content = text_content.get("1.0", tk.END)

    p = Path(file_name)

    if p.exists():

        with open(file_name, "w") as file:
            file.write(content)

        messagebox.showinfo("Success", "File Updated")

    else:
        messagebox.showerror("Error", "File Not Found")


def delete_file():

    file_name = entry_file.get()

    p = Path(file_name)

    if p.exists():

        os.remove(p)

        messagebox.showinfo("Success", "File Deleted")

    else:
        messagebox.showerror("Error", "File Not Found")


def rename_file():

    old_name = entry_file.get()
    new_name = entry_new.get()

    p = Path(old_name)

    if p.exists():

        p.rename(new_name)

        messagebox.showinfo("Success", "File Renamed")

    else:
        messagebox.showerror("Error", "File Not Found")


def create_folder():

    folder_name = entry_file.get()

    p = Path(folder_name)

    if p.exists():
        messagebox.showerror("Error", "Folder Already Exists")

    else:
        p.mkdir()

        messagebox.showinfo("Success", "Folder Created")


def delete_folder():

    folder_name = entry_file.get()

    p = Path(folder_name)

    if p.exists():

        p.rmdir()

        messagebox.showinfo("Success", "Folder Deleted")

    else:
        messagebox.showerror("Error", "Folder Not Found")


# ------------------ UI ------------------

title = tk.Label(root, text="File Handling CRUD App", font=("Arial", 18))
title.pack(pady=10)

label1 = tk.Label(root, text="Enter File/Folder Name")
label1.pack()

entry_file = tk.Entry(root, width=40)
entry_file.pack(pady=5)

label2 = tk.Label(root, text="Enter New Name (For Rename)")
label2.pack()

entry_new = tk.Entry(root, width=40)
entry_new.pack(pady=5)

label3 = tk.Label(root, text="Content")
label3.pack()

text_content = tk.Text(root, height=10, width=50)
text_content.pack(pady=10)

# ------------------ Buttons ------------------

btn1 = tk.Button(root, text="Create File", width=20, command=create_file)
btn1.pack(pady=3)

btn2 = tk.Button(root, text="Read File", width=20, command=read_file)
btn2.pack(pady=3)

btn3 = tk.Button(root, text="Update File", width=20, command=update_file)
btn3.pack(pady=3)

btn4 = tk.Button(root, text="Delete File", width=20, command=delete_file)
btn4.pack(pady=3)

btn5 = tk.Button(root, text="Rename File", width=20, command=rename_file)
btn5.pack(pady=3)

btn6 = tk.Button(root, text="Create Folder", width=20, command=create_folder)
btn6.pack(pady=3)

btn7 = tk.Button(root, text="Delete Folder", width=20, command=delete_folder)
btn7.pack(pady=3)

root.mainloop()