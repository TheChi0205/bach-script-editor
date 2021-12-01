import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import subprocess
import string
import os
letters = string.ascii_lowercase

def convert_string(x):
  new_string = ""
  for z in x:
    try:
      letters.index(z)
    except ValueError:
      new_string += z
    else:
      index_of_letter = letters.index(z)
      new_string += letters[index_of_letter + 1]
  return(new_string)

def reset_string(x):
  new_string = ""
  for z in x:
    try:
      letters.index(z)
    except ValueError:
      new_string += z
    else:
      index_of_letter = letters.index(z)
      new_string+= letters[index_of_letter - 1]
  return new_string

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.thechi"), ("All Files", "*.*")],
        initialdir="files/text/",
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, reset_string(text))

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="thechi",
        filetypes=[("Text Files", "*.thechi"), ("All Files", "*.*")],
        initialdir="files/text/",
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(convert_string(text))

def convert_file():

        filepath = asksaveasfilename(
            defaultextension="bat",
            filetypes=[("Text Files", "*.bat"), ("All Files", "*.*")],
            initialdir = "files/bat/",
        )
        if not filepath:
            return

        with open(filepath, "w") as output_file:
            text = txt_edit.get(1.0, tk.END)
            output_file.write(text)

def quicksave():
    with open('files/quicksave.thechi', "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(convert_string(text))

def quickload():
    txt_edit.delete(1.0, tk.END)
    with open('files/quicksave.thechi', "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, reset_string(text))

def run():
    with open("quick.bat", "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    os.system('start cmd /K quick.bat')


window = tk.Tk()
window.title(".bat editor")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)


fr_buttons = tk.Frame(window)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)
btn_convert = tk.Button(fr_buttons, text="Convert", command=convert_file)
btn_quicksave = tk.Button(fr_buttons, text="Quicksave", command=quicksave)
btn_quickload = tk.Button(fr_buttons, text="Quick load", command=quickload)
btn_run = tk.Button(fr_buttons,text="Run", command=run)

txt_edit = tk.Text(window)
txt_edit.configure(background='black', fg="white", insertbackground="white", font="Arial")
fr_buttons.configure(background="#06001a")

btn_open.configure(background="#30698a", fg="#c2fffd",font="Arial 12")
btn_save.configure(background="#30698a", fg="#c2fffd",font="Arial 12")
btn_convert.configure(background="#30698a", fg="#c2fffd",font="Arial 12")
btn_quicksave.configure(background="#30698a", fg="#c2fffd",font="Arial 12")
btn_quickload.configure(background="#30698a", fg="#c2fffd",font="Arial 12")
btn_run.configure(background="#15800f", fg="#c2fffd",font="Arial 12")

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
btn_convert.grid(row=2, column=0, sticky="ew", padx=5,pady=5)
btn_quicksave.grid(row=3,column=0, sticky="ew", padx=5)
btn_quickload.grid(row=4,column=0, sticky="ew", padx=5)
btn_run.grid(row=5,column=0, sticky="ew", padx=5,pady=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()
