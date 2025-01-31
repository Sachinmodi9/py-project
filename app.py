import tkinter as tk
from tkinter import messagebox

# Define functions
def add_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = add(num1, num2)
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers!")

def subtract_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = subtract(num1, num2)
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers!")

# Core math functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Create UI Window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x250")

# Create Labels and Entry Fields
tk.Label(root, text="Enter first number:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack()

# Buttons for operations
tk.Button(root, text="Add", command=add_numbers, width=10).pack(pady=5)
tk.Button(root, text="Subtract", command=subtract_numbers, width=10).pack(pady=5)

# Result label
result_label = tk.Label(root, text="Result: ", font=("Arial", 12))
result_label.pack(pady=10)

# Run the application
root.mainloop()
