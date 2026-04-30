# Military Secret Message Encoder
# This program encrypts and decrypts messages using:
# 1. Reverse text
# 2. Caesar cipher shift (+2)

import tkinter as tk
from tkinter import messagebox, filedialog
import time

SHIFT_VALUE = 2

# -------------------------------
# TEXT PROCESSING FUNCTIONS
# -------------------------------

def reverse_text(message):
    """Reverse the entire message."""
    return message[::-1]

def shift_letters_forward(message, shift):
    """Shift letters forward in the alphabet."""
    result = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                new_char = chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                new_char = chr((ord(char) - 97 + shift) % 26 + 97)
            result += new_char
        else:
            result += char
    return result

def shift_letters_backward(message, shift):
    """Shift letters backward in the alphabet."""
    result = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                new_char = chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                new_char = chr((ord(char) - 97 - shift) % 26 + 97)
            result += new_char
        else:
            result += char
    return result

# -------------------------------
# ENCRYPTION FUNCTION
# -------------------------------

def encrypt_message():
    message = input_text.get("1.0", tk.END).strip()
    if message == "":
        messagebox.showwarning("Input Error", "Please enter a message to encrypt.")
        return

    reversed_msg = reverse_text(message)
    encrypted_msg = shift_letters_forward(reversed_msg, SHIFT_VALUE)

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, encrypted_msg)

    status_var.set("Message Encrypted Successfully")

# -------------------------------
# DECRYPTION FUNCTION
# -------------------------------

def decrypt_message():
    message = input_text.get("1.0", tk.END).strip()
    if message == "":
        messagebox.showwarning("Input Error", "Please enter a message to decrypt.")
        return

    shifted_back = shift_letters_backward(message, SHIFT_VALUE)
    decrypted_msg = reverse_text(shifted_back)

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, decrypted_msg)

    status_var.set("Message Decrypted Successfully")

# -------------------------------
# CLEAR FUNCTION
# -------------------------------

def clear_fields():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)
    status_var.set("Fields Cleared")

# -------------------------------
# COPY OUTPUT
# -------------------------------

def copy_output():
    text = output_text.get("1.0", tk.END)
    root.clipboard_clear()
    root.clipboard_append(text)
    status_var.set("Output Copied to Clipboard")

# -------------------------------
# SAVE OUTPUT
# -------------------------------

def save_output():
    text = output_text.get("1.0", tk.END).strip()
    if text == "":
        messagebox.showwarning("Warning", "No output to save.")
        return

    file = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file:
        with open(file, "w") as f:
            f.write(text)
        status_var.set("File Saved Successfully")

# -------------------------------
# LIVE CLOCK
# -------------------------------

def update_clock():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text="System Time: " + current_time)
    root.after(1000, update_clock)

# -------------------------------
# GUI WINDOW SETUP
# -------------------------------

root = tk.Tk()
root.title("Military Secret Message Encoder")
root.geometry("750x600")
root.configure(bg="#2f4f2f")
root.eval('tk::PlaceWindow . center')

# -------------------------------
# TITLE
# -------------------------------

title_label = tk.Label(
    root,
    text="🔐 Military Secret Message Encoder",
    font=("Arial", 20, "bold"),
    bg="#2f4f2f",
    fg="white"
)
title_label.pack(pady=10)

# -------------------------------
# CLOCK
# -------------------------------

clock_label = tk.Label(
    root,
    font=("Arial", 10),
    bg="#2f4f2f",
    fg="lightgreen"
)
clock_label.pack()

update_clock()

# -------------------------------
# INPUT
# -------------------------------

input_label = tk.Label(
    root,
    text="Enter Message:",
    font=("Arial", 12),
    bg="#2f4f2f",
    fg="white"
)
input_label.pack()

input_frame = tk.Frame(root)
input_frame.pack()

input_text = tk.Text(
    input_frame,
    height=6,
    width=70,
    font=("Arial", 11)
)

input_scroll = tk.Scrollbar(input_frame, command=input_text.yview)
input_text.configure(yscrollcommand=input_scroll.set)

input_text.pack(side=tk.LEFT)
input_scroll.pack(side=tk.RIGHT, fill=tk.Y)

# -------------------------------
# BUTTONS
# -------------------------------

button_frame = tk.Frame(root, bg="#2f4f2f")
button_frame.pack(pady=15)

def on_enter(e):
    e.widget['background'] = "#6b8e23"

def on_leave(e):
    e.widget['background'] = "#556b2f"

encrypt_btn = tk.Button(
    button_frame,
    text="Encrypt",
    command=encrypt_message,
    width=12,
    bg="#556b2f",
    fg="white"
)
encrypt_btn.grid(row=0, column=0, padx=5)

decrypt_btn = tk.Button(
    button_frame,
    text="Decrypt",
    command=decrypt_message,
    width=12,
    bg="#556b2f",
    fg="white"
)
decrypt_btn.grid(row=0, column=1, padx=5)

copy_btn = tk.Button(
    button_frame,
    text="Copy",
    command=copy_output,
    width=10,
    bg="#556b2f",
    fg="white"
)
copy_btn.grid(row=0, column=2, padx=5)

save_btn = tk.Button(
    button_frame,
    text="Save",
    command=save_output,
    width=10,
    bg="#556b2f",
    fg="white"
)
save_btn.grid(row=0, column=3, padx=5)

clear_btn = tk.Button(
    button_frame,
    text="Clear",
    command=clear_fields,
    width=10,
    bg="#8b0000",
    fg="white"
)
clear_btn.grid(row=0, column=4, padx=5)

exit_btn = tk.Button(
    button_frame,
    text="Exit",
    command=root.quit,
    width=10,
    bg="black",
    fg="white"
)
exit_btn.grid(row=0, column=5, padx=5)

for btn in button_frame.winfo_children():
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

# -------------------------------
# OUTPUT
# -------------------------------

output_label = tk.Label(
    root,
    text="Output:",
    font=("Arial", 12),
    bg="#2f4f2f",
    fg="white"
)
output_label.pack()

output_frame = tk.Frame(root)
output_frame.pack()

output_text = tk.Text(
    output_frame,
    height=6,
    width=70,
    font=("Arial", 11)
)

output_scroll = tk.Scrollbar(output_frame, command=output_text.yview)
output_text.configure(yscrollcommand=output_scroll.set)

output_text.pack(side=tk.LEFT)
output_scroll.pack(side=tk.RIGHT, fill=tk.Y)

# -------------------------------
# STATUS BAR
# -------------------------------

status_var = tk.StringVar()
status_var.set("Ready")

status_bar = tk.Label(
    root,
    textvariable=status_var,
    bd=1,
    relief=tk.SUNKEN,
    anchor=tk.W,
    bg="black",
    fg="white"
)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

# -------------------------------
# RUN APPLICATION
# -------------------------------

root.mainloop()
