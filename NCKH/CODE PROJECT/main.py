
from init import Person
from man_input import input_info_man as nhap_thong_tin
from input_excel import ExcelWriter as excel
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import pandas as pd

'''
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
'''
def info_nguoi_nhap_data ():
    file_path = "thông tin người nhập.xlsx"
    columns = ["name", "age", "sex", "plane_work", "agent"]
    excel_writer = excel (file_path,columns)
    person_input = nhap_thong_tin()
    
    for i in range (1):
        print("Nhập thông tin người nhập : ")
        person = person_input.Nhap_thong_tin_con_nguoi()
        person.Xuat_thong_tin()
        excel_writer.add_person(person)
    print(f"Đã lưu thông tin vào file {file_path}") 
        
if __name__ == "__main__":
    info_nguoi_nhap_data ()
    open_excel_file()
    display_data ()
    win = Tk()
    win.title( "GIAO DIỆN ĐĂNG NHẬP")
    win.geometry("1280x840")
    win.attributes("-topmost", True) 
    open_button = tk.Button(win, text="Open Excel File", command=open_excel_file)
    open_button.pack(pady=10)
    win.mainloop()  