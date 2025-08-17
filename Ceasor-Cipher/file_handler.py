from tkinter import filedialog

def save_to_file(text):
    filename = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if filename:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(text)
        return filename
    return None

def load_from_file():
    filename = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if filename:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    return None
