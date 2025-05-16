import tkinter as tk
from tkinter import messagebox, scrolledtext
import math

# Lưu lịch sử tính toán
calculation_history = []

def update_history(entry):
    calculation_history.append(entry)
    history_box.config(state='normal')
    history_box.insert(tk.END, entry + '\n')
    history_box.config(state='disabled')

def add():
    try:
        res = float(entry1.get()) + float(entry2.get())
        result.set(res)
        update_history(f"{entry1.get()} + {entry2.get()} = {res}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.")

def subtract():
    try:
        res = float(entry1.get()) - float(entry2.get())
        result.set(res)
        update_history(f"{entry1.get()} - {entry2.get()} = {res}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.")

def multiply():
    try:
        res = float(entry1.get()) * float(entry2.get())
        result.set(res)
        update_history(f"{entry1.get()} * {entry2.get()} = {res}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.")

def divide():
    try:
        num2 = float(entry2.get())
        if num2 == 0:
            raise ZeroDivisionError
        res = float(entry1.get()) / num2
        result.set(res)
        update_history(f"{entry1.get()} / {entry2.get()} = {res}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.")
    except ZeroDivisionError:
        messagebox.showerror("Lỗi", "Không thể chia cho 0.")

def power():
    try:
        res = float(entry1.get()) ** float(entry2.get())
        result.set(res)
        update_history(f"{entry1.get()} ^ {entry2.get()} = {res}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.")

def square_root():
    try:
        num = float(entry1.get())
        if num < 0:
            raise ValueError
        res = math.sqrt(num)
        result.set(res)
        update_history(f"√{entry1.get()} = {res}")
    except ValueError:
        messagebox.showerror("Lỗi", "Không thể lấy căn bậc hai của số âm hoặc nhập sai.")

def percentage():
    try:
        res = (float(entry1.get()) / 100) * float(entry2.get())
        result.set(res)
        update_history(f"{entry1.get()}% của {entry2.get()} = {res}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.")

def absolute_value():
    try:
        res = abs(float(entry1.get()))
        result.set(res)
        update_history(f"|{entry1.get()}| = {res}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.")

# Giao diện
root = tk.Tk()
root.title("🧮 Máy tính bỏ túi nâng cao")
root.geometry("500x600")

tk.Label(root, text="Số thứ nhất:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Số thứ hai:").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Kết quả
result = tk.StringVar()
tk.Label(root, text="Kết quả:", font=('Arial', 12, 'bold')).pack(pady=5)
tk.Entry(root, textvariable=result, state='readonly').pack()

# Các nút chức năng
tk.Button(root, text="Cộng", width=20, command=add).pack(pady=2)
tk.Button(root, text="Trừ", width=20, command=subtract).pack(pady=2)
tk.Button(root, text="Nhân", width=20, command=multiply).pack(pady=2)
tk.Button(root, text="Chia", width=20, command=divide).pack(pady=2)
tk.Button(root, text="Lũy thừa", width=20, command=power).pack(pady=2)
tk.Button(root, text="Căn bậc hai (số 1)", width=25, command=square_root).pack(pady=2)
tk.Button(root, text="Phần trăm (x% của y)", width=25, command=percentage).pack(pady=2)
tk.Button(root, text="Giá trị tuyệt đối (số 1)", width=25, command=absolute_value).pack(pady=2)

# Lịch sử tính toán
tk.Label(root, text="📜 Lịch sử tính toán:", font=('Arial', 12, 'bold')).pack(pady=5)
history_box = scrolledtext.ScrolledText(root, height=10, state='disabled', wrap='word')
history_box.pack(fill='both', expand=True, padx=10)

# Thoát
tk.Button(root, text="Thoát", width=15, command=root.quit).pack(pady=10)

root.mainloop()
