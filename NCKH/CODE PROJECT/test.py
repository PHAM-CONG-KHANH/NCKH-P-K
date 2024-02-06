from openpyxl import Workbook

class Person:
    def __init__(self, name, age, gender, position):
        self.name = name
        self.age = age
        self.gender = gender
        self.position = position

class ExcelWriter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.workbook = Workbook()
        self.sheet = self.workbook.active
        self.sheet.append(["Họ Tên", "Tuổi", "Giới Tính", "Chức Vụ"])  # Tiêu đề cột

    def add_person(self, person):
        self.sheet.append([person.name, person.age, person.gender, person.position])

    def save(self):
        self.workbook.save(self.file_path)

class PersonInfoInput:
    def input_person_info(self):
        name = input("Nhập họ tên: ")
        age = input("Nhập tuổi: ")
        gender = input("Nhập giới tính: ")
        position = input("Nhập chức vụ: ")
        return Person(name, age, gender, position)

def main():
    file_path = "people_info.xlsx"
    excel_writer = ExcelWriter(file_path)
    person_input = PersonInfoInput()

    num_people = int(input("Nhập số người muốn nhập thông tin: "))
    for i in range(num_people):
        print(f"\nNhập thông tin cho người thứ {i+1}:")
        person = person_input.input_person_info()
        excel_writer.add_person(person)

    excel_writer.save()
    print(f"Đã lưu thông tin vào file {file_path}")

if __name__ == "__main__":
    main()
