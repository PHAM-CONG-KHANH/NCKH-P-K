class Person():
    def __init__(self, name, age, sex, plane_work, agent):
        self.name = name
        self.age = age
        self.sex = sex
        self.plane_work = plane_work
        self.agent = agent
    
    def Xuat_thong_tin (self):
        print ("thông tin con người vừa nhập:")
        print ("tên: " + self.name)
        print ("tuổi: " + self.age)
        print ("giới tính: " + self.sex)
        print ("phòng/ban bạn đang làm việc: " + self.plane_work)
        print ("chức vụ của bạn trong phòng/ban: " + self.agent)