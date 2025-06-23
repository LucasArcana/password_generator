import tkinter as tk
from tkinter import messagebox
import string
import random

#As long as user asks to generate 8 characters
def generate_pw():
    try:
        charNo = int(entry.get())
        if charNo < 8:
            messagebox.showerror("Error", "Number should be at least 8")
            return
    except ValueError:
        messagebox.showerror("Error", "Enter numbers only.")
        return

    #Generate from different character types
    chartype1 = list(string.ascii_lowercase)
    chartype2 = list(string.ascii_uppercase)
    chartype3 = list(string.digits)
    chartype4 = list(string.punctuation)
    random.shuffle(chartype1)
    random.shuffle(chartype2)
    random.shuffle(chartype3)
    random.shuffle(chartype4)
    chunk1 = round(charNo * (30/100))
    chunk2 = round(charNo * (20/100))
    result = []

    for x in range(chunk1):
        result.append(chartype1[x])
        result.append(chartype2[x])

    for x in range(chunk2):
        result.append(chartype3[x])
        result.append(chartype4[x])

    #Shuffle and print
    random.shuffle(result)
    password = "".join(result)
    output.config(state='normal')
    output.delete(0, tk.END)
    output.delete(0, password)
    output.config(state='readonly')

root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Number of characters:").pack()
entry = tk.Entry(root)
entry.pack()
tk.Button(root, text="Generate", command=generate_pw).pack()
output = tk.Entry(root, state='readonly', width=30)
output.pack()
root.mainloop()