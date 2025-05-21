import tkinter as tk
from tkinter import ttk, messagebox
import math

history = []

def calculate_expression():
    try:
        expr = expression_entry.get()
        result_value = eval(expr)
        result.set(str(result_value))
        history.append(f"{expr} = {result_value}")
        update_history()
    except Exception:
        messagebox.showerror("Lỗi", "Biểu thức không hợp lệ.")

def update_history():
    history_listbox.delete(0, tk.END)
    for item in history[-5:]:
        history_listbox.insert(tk.END, item)

def clear_history():
    history.clear()
    update_history()

def insert_text(text):
    if text == 'sqrt':
        expression_entry.insert(tk.END, 'math.sqrt(')
    elif text == 'abs':
        expression_entry.insert(tk.END, 'abs(')
    else:
        expression_entry.insert(tk.END, text)

# Tạo giao diện
root = tk.Tk()
root.title("Máy tính nâng cao")
root.geometry("480x620")
root.configure(bg="#f0f4f8")

style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=10)
style.configure("TLabel", font=("Arial", 12), background="#f0f4f8")
style.configure("TEntry", font=("Arial", 12))

# Khung chính
frame = tk.Frame(root, bg="#ffffff", bd=2, relief=tk.GROOVE)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=440, height=580)

# Biểu thức
ttk.Label(frame, text="Biểu thức:").pack(pady=10)
expression_entry = ttk.Entry(frame, width=40)
expression_entry.pack()

result = tk.StringVar()
ttk.Label(frame, text="Kết quả:").pack(pady=(10, 0))
ttk.Entry(frame, textvariable=result, state='readonly', width=40).pack()

ttk.Button(frame, text="Tính", command=calculate_expression).pack(pady=10)

# Nút số học cơ bản
button_frame = tk.Frame(frame, bg="#ffffff")
button_frame.pack(pady=10)

btn_texts = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '(', ')'),
    ('**', 'sqrt', 'abs', '+')
]

for row in btn_texts:
    r_frame = tk.Frame(button_frame, bg="#ffffff")
    r_frame.pack()
    for char in row:
        ttk.Button(r_frame, text=char, width=6, command=lambda c=char: insert_text(c)).pack(side=tk.LEFT, padx=2, pady=2)

# Lịch sử
ttk.Label(frame, text="Lịch sử tính toán:").pack(pady=(10, 0))
history_listbox = tk.Listbox(frame, height=5, font=("Arial", 11))
history_listbox.pack(pady=5, fill=tk.X, padx=10)

ttk.Button(frame, text="Xoá lịch sử", command=clear_history).pack(pady=5)

root.mainloop()
