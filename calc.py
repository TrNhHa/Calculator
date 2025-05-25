import tkinter as tk
from tkinter import ttk, messagebox
import math

# Lưu lịch sử
history = []

# Gợi ý cú pháp
syntax_hint = tk.StringVar(value="Ví dụ: 5+2, (3+4)*2, math.sqrt(9), abs(-7), 2**3")

# Tooltip class
class CreateToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tip_window = None
        self.widget.bind("<Enter>", self.show_tip)
        self.widget.bind("<Leave>", self.hide_tip)

    def show_tip(self, event=None):
        if self.tip_window or not self.text:
            return
        x = self.widget.winfo_rootx() + 40
        y = self.widget.winfo_rooty() + 20
        self.tip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.geometry(f"+{x}+{y}")
        label = tk.Label(tw, text=self.text, background="lightyellow", relief='solid',
                         borderwidth=1, font=("Arial", 10))
        label.pack()

    def hide_tip(self, event=None):
        if self.tip_window:
            self.tip_window.destroy()
            self.tip_window = None

# Tính toán
def calculate_expression():
    try:
        expr = expression_entry.get()
        result_value = eval(expr)
        result.set(str(result_value))
        history.append(f"{expr} = {result_value}")
        update_history()
    except Exception:
        messagebox.showerror("Lỗi", "Biểu thức không hợp lệ.")

# Cập nhật lịch sử
def update_history():
    history_listbox.delete(0, tk.END)
    for item in history[-5:]:
        history_listbox.insert(tk.END, item)

# Xoá lịch sử
def clear_history():
    history.clear()
    update_history()

# Thêm vào biểu thức
def insert_text(text):
    if text == 'sqrt':
        expression_entry.insert(tk.END, 'math.sqrt(')
    elif text == 'abs':
        expression_entry.insert(tk.END, 'abs(')
    else:
        expression_entry.insert(tk.END, text)

# Chuyển đổi dark/light mode
is_dark = False

def toggle_theme():
    global is_dark
    if is_dark:
        root.configure(bg="#f0f4f8")
        frame.configure(bg="#ffffff")
        style.configure("TLabel", background="#f0f4f8", foreground="black")
        style.configure("TFrame", background="#ffffff")
    else:
        root.configure(bg="#1e1e1e")
        frame.configure(bg="#2e2e2e")
        style.configure("TLabel", background="#1e1e1e", foreground="white")
        style.configure("TFrame", background="#2e2e2e")
    is_dark = not is_dark

# Tạo giao diện
root = tk.Tk()
root.title("Máy tính nâng cao")
root.geometry("480x660")
root.configure(bg="#f0f4f8")

style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=10)
style.configure("TLabel", font=("Arial", 12), background="#f0f4f8")
style.configure("TEntry", font=("Arial", 12))

# Khung chính
frame = tk.Frame(root, bg="#ffffff", bd=2, relief=tk.GROOVE)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=440, height=620)

# Biểu thức
ttk.Label(frame, text="Biểu thức:").pack(pady=10)
expression_entry = ttk.Entry(frame, width=40)
expression_entry.pack()

# Gợi ý cú pháp
ttk.Label(frame, textvariable=syntax_hint, foreground="gray").pack(pady=(0, 5))

# Kết quả
result = tk.StringVar()
tt_entry = ttk.Entry(frame, textvariable=result, state='readonly', width=40)
ttk.Label(frame, text="Kết quả:").pack(pady=(10, 0))
tt_entry.pack()

# Nút tính và chuyển theme
btn_frame = tk.Frame(frame, bg="#ffffff")
btn_frame.pack(pady=10)
ttk.Button(btn_frame, text="Tính", command=calculate_expression).pack(side=tk.LEFT, padx=5)
ttk.Button(btn_frame, text="Chuyển đổi giao diện", command=toggle_theme).pack(side=tk.LEFT, padx=5)

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

tooltip_dict = {
    'sqrt': 'Căn bậc hai: math.sqrt(x)',
    'abs': 'Giá trị tuyệt đối: abs(x)',
    '**': 'Lũy thừa: x ** y',
    '/': 'Chia: x / y',
    '*': 'Nhân: x * y',
    '-': 'Trừ: x - y',
    '+': 'Cộng: x + y',
    '(': 'Mở ngoặc',
    ')': 'Đóng ngoặc'
}

for row in btn_texts:
    r_frame = tk.Frame(button_frame, bg="#ffffff")
    r_frame.pack()
    for char in row:
        btn = ttk.Button(r_frame, text=char, width=6, command=lambda c=char: insert_text(c))
        btn.pack(side=tk.LEFT, padx=2, pady=2)
        if char in tooltip_dict:
            CreateToolTip(btn, tooltip_dict[char])

# Lịch sử
ttk.Label(frame, text="Lịch sử tính toán:").pack(pady=(10, 0))
history_listbox = tk.Listbox(frame, height=5, font=("Arial", 11))
history_listbox.pack(pady=5, fill=tk.X, padx=10)

ttk.Button(frame, text="Xoá lịch sử", command=clear_history).pack(pady=5)

root.mainloop()
