#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")

        self.create_widgets()

    def create_widgets(self):
        # Title Label
        title = tk.Label(self.root, text="Password Generator", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
        title.pack(pady=10)

        # Password length
        tk.Label(self.root, text="Length:", font=("Helvetica", 12), bg="#f0f0f0").pack()
        self.length_var = tk.IntVar(value=12)
        tk.Entry(self.root, textvariable=self.length_var, width=5, font=("Helvetica", 12)).pack(pady=5)

        # Checkboxes
        self.use_upper = tk.BooleanVar(value=True)
        self.use_lower = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_special = tk.BooleanVar(value=True)

        tk.Checkbutton(self.root, text="Include UPPERCASE letters", variable=self.use_upper, bg="#f0f0f0").pack(anchor='w', padx=20)
        tk.Checkbutton(self.root, text="Include lowercase letters", variable=self.use_lower, bg="#f0f0f0").pack(anchor='w', padx=20)
        tk.Checkbutton(self.root, text="Include digits (0-9)", variable=self.use_digits, bg="#f0f0f0").pack(anchor='w', padx=20)
        tk.Checkbutton(self.root, text="Include special characters (!@#)", variable=self.use_special, bg="#f0f0f0").pack(anchor='w', padx=20)

        # Generate button
        tk.Button(self.root, text="Generate Password", command=self.generate_password, font=("Helvetica", 12), bg="#4CAF50", fg="white").pack(pady=20)

        # Result
        self.result_var = tk.StringVar()
        tk.Entry(self.root, textvariable=self.result_var, font=("Helvetica", 14), width=30, justify='center', state='readonly').pack(pady=10)

    def generate_password(self):
        length = self.length_var.get()
        if length < 4:
            messagebox.showwarning("Invalid Length", "Password length should be at least 4.")
            return

        chars = ""
        if self.use_upper.get():
            chars += string.ascii_uppercase
        if self.use_lower.get():
            chars += string.ascii_lowercase
        if self.use_digits.get():
            chars += string.digits
        if self.use_special.get():
            chars += string.punctuation

        if not chars:
            messagebox.showwarning("No Options", "Please select at least one character type.")
            return

        password = ''.join(random.choice(chars) for _ in range(length))
        self.result_var.set(password)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorGUI(root)
    root.mainloop()


# In[ ]:




