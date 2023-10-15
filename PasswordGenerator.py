import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Password Generator")

        self.label = tk.Label(self.root, text="Password Generator", font=('Arial', 36))
        self.label.pack(padx=10, pady=10)

        self.checkbox_vars = [tk.IntVar() for _ in range(4)]  # for numbers, special characters, uppercase, lowercase

        self.button_frame = tk.Frame(self.root)
        self.button_frame.columnconfigure(0, weight=1)
        
        checkbox_texts = ['Number', 'Special Character', 'Uppercase', 'Lowercase']
        for i, text in enumerate(checkbox_texts):
            btn = tk.Checkbutton(self.button_frame, text=text, font=('Arial', 16), variable=self.checkbox_vars[i])
            btn.grid(row=i, column=0, sticky=tk.W + tk.E)

        self.button_frame.pack(fill='y')

        self.label_length = tk.Label(self.root, text="Password Length:", font=('Arial', 16))
        self.label_length.pack(padx=10, pady=10)

        self.entry_length = tk.Entry(self.root, font=('Arial', 20))
        self.entry_length.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text='Generate Password', font=('Arial', 24), command=self.generate)
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()

    def generate(self):
        characters = ''

        if self.checkbox_vars[0].get() == 1:  # Include numbers
            characters += string.digits

        if self.checkbox_vars[1].get() == 1:  # Include special characters
            characters += string.punctuation

        if self.checkbox_vars[2].get() == 1:  # Include uppercase letters
            characters += string.ascii_letters.upper()

        if self.checkbox_vars[3].get() == 1:  # Include lowercase letters
            characters += string.ascii_letters.lower()

        if not characters:
            messagebox.showinfo(title='Password', message='Please select at least one option.')
            return

        password_length_str = self.entry_length.get()
        try:
            password_length = int(password_length_str)
            if password_length <= 0:
                raise ValueError
        except ValueError:
            messagebox.showinfo(title='Password', message='Please enter a valid positive integer for the password length.')
            return

        password = ''.join(random.choice(characters) for _ in range(password_length))
        messagebox.showinfo(title='Password', message=f'Generated Password: {password}')

if __name__ == "__main__":
    PasswordGenerator()
