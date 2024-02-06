import tkinter as tk
from tkinter import *
from tkinter import filedialog
import pandas as pd

win = Tk()
win.title( "GIAO DIỆN ĐĂNG NHẬP")
win.geometry("1280x840")
win.attributes("-topmost", True) 



def open_excel_file():
    filepath = filedialog.askopenfilename(title="Open Excel File", filetypes=[("thông tin người nhập", "*.xlsx *.xls")])
    if filepath:
        df = pd.read_excel(filepath)  # Đọc dữ liệu từ tệp Excel vào DataFrame
        display_data(df)

def display_data(dataframe):
    name = Label(win, text="thông tin người nhập", font = ('Time New Roman', 14), fg= 'red')
    name.place (x=60, y=200)
    # Tạo cửa sổ mới để hiển thị dữ liệu
    display_window = tk.Toplevel(name)
    
    # Tạo một Text Widget để hiển thị dữ liệu
    text_widget = tk.Text(display_window, wrap="none")
    text_widget.pack(fill="both", expand=True)
    
    # Chuyển DataFrame thành dạng văn bản và hiển thị trên Text Widget
    text_widget.insert("1.0", dataframe.to_string(index=False))

open_button = tk.Button(win, text="Open Excel File", command=open_excel_file)
open_button.pack(pady=10)
win.mainloop()