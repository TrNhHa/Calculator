import tkinter as tk
from tkinter import messagebox, scrolledtext
import math

# Dữ liệu
calculation_history = []

# Giao diện
root = tk.Tk()
root.title("🧮 Máy tính nâng cao")
root.geometry("520x670")
root.attributes('-alpha', 0.95)  # Giao diện trong suốt

current_theme = "light"

# Hàm xử lý
def update_history(entry):
    calculation_history.append(entry)
    history_box.config(state='normal')
    history_box.insert(tk.END, entry + '\n')
    history_box.config(state='disabled')

def clear_history():
    calculation_history.clear()
    history_box.config(state='normal')
    history_box.delete(1.0, tk.END)
    history_box.config(state='disabled')

def calculate(op):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get()) if entry2.get() else 0

        if op == '+':
            res = num1 + num2
            desc = f"{num1} + {num2} = {res}"
        elif op == '-':
            res = num1 - num2
            desc = f"{num1} - {num2} = {res}"
        elif op == '*':
            res = num1 * num2
            desc = f"{num1} * {num2} = {res}"
        elif op == '/':
            if num2 == 0:
                raise ZeroDivisionError
            res = num1 / num2
            desc = f"{num1} / {num2} = {res}"
        elif op == '^':
            res = num1 ** num2
            desc = f"{num1} ^ {num2} = {res}"
        elif op == '%':
            res = (num1 / 100) * num2
            desc = f"{num1}% của {num2} = {res}"
        elif op == '|':
            res = abs(num1)
            desc = f"|{num1}| = {res}"
        elif op == '√':
            if num1 < 0:
                raise ValueError
            res = math.sqrt(num1)
            desc = f"√{num1} = {res}"
        else:
            return

        result.set(res)
        update_history(desc)
    except ZeroDivisionError:
        messagebox.showerror("Lỗi", "Không thể chia cho 0.")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.")

# Giao diện tối/sáng
def switch_theme():
    global current_theme
    if current_theme == "light":
        set_dark_theme()
    else:
        set_light_theme()

def set_dark_theme():
    global current_theme
    current_theme = "dark"
    bg = "#2e2e2e"
    fg = "#ffffff"
    entry_bg = "#3a3a3a"

    root.configure(bg=bg)
    for widget in root.winfo_children():
        if isinstance(widget, (tk.Label, tk.Button)):
            widget.configure(bg=bg, fg=fg)
        elif isinstance(widget, tk.Entry):
            widget.configure(bg=entry_bg, fg=fg, insertbackground=fg)
    history_box.configure(bg=entry_bg, fg=fg, insertbackground=fg)

def set_light_theme():
    global current_theme
    current_theme = "light"
    bg = "#f0f0f0"
    fg = "#000000"
    entry_bg = "#ffffff"

    root.configure(bg=bg)
    for widget in root.winfo_children():
        if isinstance(widget, (tk.Label, tk.Button)):
            widget.configure(bg=bg, fg=fg)
        elif isinstance(widget, tk.Entry):
            widget.configure(bg=entry_bg, fg=fg, insertbackground=fg)
    history_box.configure(bg=entry_bg, fg=fg, insertbackground=fg)

# Menu theme
menu = tk.Menu(root)
theme_menu = tk.Menu(menu, tearoff=0)
theme_menu.add_command(label="Chuyển đổi Sáng/Tối", command=switch_theme)
menu.add_cascade(label="🎨 Giao diện", menu=theme_menu)
root.config(menu=menu)

# Widgets
tk.Label(root, text="Số thứ nhất:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Số thứ hai:").pack()
entry2 = tk.Entry(root)
entry2.pack()

result = tk.StringVar()
tk.Label(root, text="Kết quả:", font=('Arial', 12, 'bold')).pack(pady=5)
tk.Entry(root, textvariable=result, state='readonly').pack()

# Nút chức năng
buttons = [
    ("Cộng", '+'), ("Trừ", '-'), ("Nhân", '*'), ("Chia", '/'),
    ("Lũy thừa", '^'), ("Căn bậc hai (số 1)", '√'),
    ("Phần trăm (x% của y)", '%'), ("Giá trị tuyệt đối (số 1)", '|')
]
for text, op in buttons:
    tk.Button(root, text=text, width=25, command=lambda o=op: calculate(o)).pack(pady=2)

# Lịch sử
tk.Label(root, text="📜 Lịch sử tính toán:", font=('Arial', 12, 'bold')).pack(pady=5)
history_box = scrolledtext.ScrolledText(root, height=10, state='disabled', wrap='word')
history_box.pack(fill='both', expand=True, padx=10)

tk.Button(root, text="🗑 Xoá lịch sử", width=20, command=clear_history).pack(pady=5)
tk.Button(root, text="Thoát", width=20, command=root.quit).pack(pady=5)

# Khởi tạo giao diện sáng mặc định
set_light_theme()

root.mainloop()
