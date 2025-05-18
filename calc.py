import tkinter as tk
from tkinter import messagebox
import math

history = []

def update_result(value):
    result.set(value)
    history.append(value)
    history_listbox.insert(tk.END, value)

def clear_history():
    history.clear()
    history_listbox.delete(0, tk.END)

def calculate_expression():
    expr = expression_entry.get()
    try:
        res = eval(expr, {"__builtins__": {}}, math.__dict__)
        update_result(f"{expr} = {res}")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Biểu thức không hợp lệ.\n{e}")

def add(): perform(lambda x, y: x + y, "+")
def subtract(): perform(lambda x, y: x - y, "-")
def multiply(): perform(lambda x, y: x * y, "*")
def divide():
    try:
        x, y = float(entry1.get()), float(entry2.get())
        if y == 0:
            raise ZeroDivisionError("Không thể chia cho 0.")
        update_result(f"{x} / {y} = {x / y}")
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

def power(): perform(lambda x, y: x ** y, "^")
def percentage(): perform(lambda x, y: (x / 100) * y, "%")
def square_root():
    try:
        x = float(entry1.get())
        if x < 0:
            raise ValueError("Không thể căn bậc hai số âm.")
        update_result(f"√{x} = {math.sqrt(x)}")
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

def absolute_value():
    try:
        x = float(entry1.get())
        update_result(f"|{x}| = {abs(x)}")
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

def perform(operation, op_symbol):
    try:
        x, y = float(entry1.get()), float(entry2.get())
        res = operation(x, y)
        update_result(f"{x} {op_symbol} {y} = {res}")
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

def toggle_theme():
    global is_dark
    is_dark = not is_dark
    bg = "#2e2e2e" if is_dark else "SystemButtonFace"
    fg = "#ffffff" if is_dark else "#000000"
    root.configure(bg=bg)
    for widget in root.winfo_children():
        try:
            widget.configure(bg=bg, fg=fg)
        except:
            pass

def toggle_transparent():
    root.attributes("-alpha", 0.85 if not transparent.get() else 1.0)
    transparent.set(not transparent.get())

# Giao diện chính
root = tk.Tk()
root.title("🧮 Máy tính bỏ túi nâng cao")
root.geometry("500x600")

is_dark = False
transparent = tk.BooleanVar(value=False)

# Biểu thức
tk.Label(root, text="Nhập biểu thức:").pack()
expression_entry = tk.Entry(root, width=40)
expression_entry.pack()
tk.Button(root, text="Tính biểu thức", command=calculate_expression).pack(pady=5)

# Nhập số cơ bản
tk.Label(root, text="Số thứ nhất:").pack()
entry1 = tk.Entry(root)
entry1.pack()
tk.Label(root, text="Số thứ hai:").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Kết quả
result = tk.StringVar()
tk.Label(root, text="Kết quả:", font=('Arial', 12, 'bold')).pack()
tk.Entry(root, textvariable=result, state='readonly', width=40).pack(pady=5)

# Nút chức năng
for text, func in [
    ("Cộng", add), ("Trừ", subtract), ("Nhân", multiply), ("Chia", divide),
    ("Lũy thừa", power), ("Căn bậc hai (số 1)", square_root),
    ("Phần trăm (x% của y)", percentage), ("Giá trị tuyệt đối (số 1)", absolute_value)
]:
    tk.Button(root, text=text, width=25, command=func).pack(pady=1)

# Lịch sử
tk.Label(root, text="🧾 Lịch sử tính toán:").pack(pady=(10, 0))
history_listbox = tk.Listbox(root, height=6, width=50)
history_listbox.pack()
tk.Button(root, text="🗑 Xoá lịch sử", command=clear_history).pack(pady=5)

# Giao diện
tk.Button(root, text="🌙 Chuyển giao diện sáng/tối", command=toggle_theme).pack()
tk.Checkbutton(root, text="🔲 Giao diện trong suốt", variable=transparent, command=toggle_transparent).pack()

# Thoát
tk.Button(root, text="🚪 Thoát", command=root.quit).pack(pady=10)

root.mainloop()
