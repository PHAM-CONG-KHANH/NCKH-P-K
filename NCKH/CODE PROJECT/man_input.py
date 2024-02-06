
from init import Person as Person


class input_info_man :
    def Nhap_thong_tin_con_nguoi (self):
        name = input ("nhập tên: ")
        age = input ("nhập tuổi:")
        sex = input ("nhập giới tính:")
        plane_work = input ("nhập phòng/ban bạn làm việc: ")
        agent = input ("nhập chức vụ của bạn trong phòng/ban: ")
        return Person ( name, age, sex, plane_work, agent ) 
    



