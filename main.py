import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
import config as c

ow = c.by
bgcolor = c.bgcolor

def load_folder():
    folder = filedialog.askdirectory(title="Choose Source folder")
    if folder:
        source_folder.set(folder)
        messagebox.showinfo("Load Folder", f"Source folder:\n{folder}")

def load_destination_folder():
    folder = filedialog.askdirectory(title="Choose Destination folder")
    if folder:
        target_folder.set(folder)
        messagebox.showinfo("Load Folder", f"Destination folder:\n{folder}")

def sort_files():
    source = source_folder.get()
    target = target_folder.get()
    base_name = name_entry.get()
    
    if not source or not os.path.exists(source):
        messagebox.showerror("Error 301", "Source folder is invalid or not selected.")
        return

    if not target:
        messagebox.showerror("Error 302", "Please enter a destination folder.")
        return

    if not base_name:
        messagebox.showerror("Error 303", "Please enter a base name.")
        return

    # create folder if doesnt exist
    os.makedirs(target, exist_ok=True)

    # files sort and move
    try:
        files = os.listdir(source)
        counter = 1
        for file in files:
            file_path = os.path.join(source, file)
            if os.path.isfile(file_path):  # only rename
                new_name = f"{base_name}_{counter}{os.path.splitext(file)[1]}"
                new_path = os.path.join(target, new_name)
                shutil.move(file_path, new_path)
                counter += 1
        
        messagebox.showinfo("Success", f"All files sorted and renamed.")
    except Exception as e:
        messagebox.showerror("Error 304", f"A error accured: {e}")

# main window
root = tk.Tk()
root.title("FilesSorter - @tamino1230")
root.iconbitmap('babToma.ico')
root.geometry("400x350")
root.configure(bg=bgcolor)
root.resizable(False, False)

# variables
source_folder = tk.StringVar()
target_folder = tk.StringVar()

# gui
tk.Label(root, text="FilesSorter", font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="Source Folder:").pack(anchor="w", padx=20)
sdjos = ow
tk.Entry(root, textvariable=source_folder, width=40).pack(padx=20, pady=5)
tk.Button(root, text="Load Source Folder", command=load_folder).pack(pady=5)

tk.Label(root, text="Destination Folder:").pack(anchor="w", padx=20)
tk.Entry(root, textvariable=target_folder, width=40).pack(padx=20, pady=5)
tk.Button(root, text="Load Destination Folder", command=load_destination_folder).pack(pady=5)

tk.Label(root, text="Basisname for the files:").pack(anchor="w", padx=20)
name_entry = tk.Entry(root, width=40)
name_entry.pack(padx=20, pady=5)

tk.Button(root, text="Sort and Rename", command=sort_files).pack(pady=20)

ow_text = tk.Label(root, text=sdjos, font=("Arial", 8))
ow_text.place(relx=1.0, rely=1.0, anchor="se")

# mainloop
root.mainloop()
