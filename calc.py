import tkinter as tk
from tkinter import messagebox
import math

def add():
    try:
        result.set(float(entry1.get()) + float(entry2.get()))
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.")

def subtract():
    try:
        result.set(float(entry1.get()) - float(entry2.get()))
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.")

def multiply():
    try:
        result.set(float(entry1.get()) * float(entry2.get()))
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.")

def divide():
    try:
        num2 = float(entry2.get())
        if num2 == 0:
            raise ZeroDivisionError
        result.set(float(entry1.get()) / num2)
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.")
    except ZeroDivisionError:
        messagebox.showerror("Lỗi", "Không thể chia cho 0.")

def power():
    try:
        result.set(float(entry1.get()) ** float(entry2.get()))
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.")

def square_root():
    try:
        num = float(entry1.get())
        if num < 0:
            raise ValueError
        result.set(math.sqrt(num))
    except ValueError:
        messagebox.showerror("Lỗi", "Không thể lấy căn bậc hai của số âm hoặc nhập sai.")

def percentage():
    try:
        result.set((float(entry1.get()) / 100) * float(entry2.get()))
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.")

def absolute_value():
    try:
        result.set(abs(float(entry1.get())))
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.")

# Giao diện
root = tk.Tk()
root.title("Máy tính bỏ túi nâng cao")
root.geometry("400x400")

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
tk.Button(root, text="Cộng", width=15, command=add).pack(pady=2)
tk.Button(root, text="Trừ", width=15, command=subtract).pack(pady=2)
tk.Button(root, text="Nhân", width=15, command=multiply).pack(pady=2)
tk.Button(root, text="Chia", width=15, command=divide).pack(pady=2)
tk.Button(root, text="Lũy thừa", width=15, command=power).pack(pady=2)
tk.Button(root, text="Căn bậc hai (của số 1)", width=20, command=square_root).pack(pady=2)
tk.Button(root, text="Phần trăm (x% của y)", width=20, command=percentage).pack(pady=2)
tk.Button(root, text="Giá trị tuyệt đối (của số 1)", width=25, command=absolute_value).pack(pady=2)

# Thoát
tk.Button(root, text="Thoát", width=15, command=root.quit).pack(pady=10)

root.mainloop()
