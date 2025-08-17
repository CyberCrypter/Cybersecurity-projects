import tkinter as tk
from tkinter import messagebox
from cipher import encrypt, decrypt
from file_handler import save_to_file, load_from_file

def encrypt_message():
    text = text_input.get("1.0", tk.END).strip()
    try:
        shift = int(shift_input.get())
        encrypted = encrypt(text, shift)
        result_output.delete("1.0", tk.END)
        result_output.insert(tk.END, encrypted)
    except ValueError:
        messagebox.showerror("Error", "Shift value must be an integer")

def decrypt_message():
    text = text_input.get("1.0", tk.END).strip()
    try:
        shift = int(shift_input.get())
        decrypted = decrypt(text, shift)
        result_output.delete("1.0", tk.END)
        result_output.insert(tk.END, decrypted)
    except ValueError:
        messagebox.showerror("Error", "Shift value must be an integer")

def save_message():
    text = result_output.get("1.0", tk.END).strip()
    if text:
        filename = save_to_file(text)
        if filename:
            messagebox.showinfo("Saved", f"Message saved to {filename}")
    else:
        messagebox.showwarning("Warning", "No message to save!")

def load_message():
    content = load_from_file()
    if content:
        text_input.delete("1.0", tk.END)
        text_input.insert(tk.END, content)

def clear_text():
    """Clear both input and output fields"""
    text_input.delete("1.0", tk.END)
    result_output.delete("1.0", tk.END)
    shift_input.delete(0, tk.END)

# Main Window
root = tk.Tk()
root.title("Caesar Cipher Tool")
root.geometry("520x420")

# Message Input
tk.Label(root, text="Enter Message:").pack()
text_input = tk.Text(root, height=5)
text_input.pack()

# Shift Value
tk.Label(root, text="Shift Value:").pack()
shift_input = tk.Entry(root)
shift_input.pack()

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Encrypt", command=encrypt_message).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Decrypt", command=decrypt_message).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Save to File", command=save_message).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Load from File", command=load_message).grid(row=0, column=3, padx=5)
tk.Button(btn_frame, text="Clear", command=clear_text, fg="red").grid(row=0, column=4, padx=5)

# Result Output
tk.Label(root, text="Result:").pack()
result_output = tk.Text(root, height=5)
result_output.pack()

root.mainloop()
