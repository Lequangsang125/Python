from abc import ABC, abstractmethod

class Pet(ABC):
    def __init__(self,name:str,age:int):
        self.name = name
        self._age = age

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def get_type(self):
        pass

    def get_info(self):
        return f'{self.get_type()} - Tên: {self.name}, Tuổi: {self._age}'
    
# Lớp dog kế thừa từ pet
class Dog(Pet):
    def make_sound(self):
        print(f"{self.name} says: Gâu gâu!")
    def get_type(self):
        return "Chó"
# Lớp cat 
class Cat(Pet):
    def make_sound(self):
        print(f'{self.name} says: Meo Meo!')
    def get_type(self):
        return "Mèo"
# Lớp vẹt
class Parrot(Pet):
    def make_sound(self):
        print(f'{self.name} says: Két Két!')
    
    def get_type(self):
        return "Vẹt"

#tạo danh sách quản lý thú cưng
list_pet = []
def show_menu():
    print("\n--- Hệ thống quản lý thú cưng ---")
    print("1. Thêm thú cưng")
    print("2. Hiển thị danh sách thú cưng")
    print("3. Gọi tất cả thú cưng kêu")
    print("0. Thoát")

# hàm thêm thú cưng
def add_pet():
    print("\nChọn loại thú cưng:")
    print("1. Chó")
    print("2. Mèo")
    print("3. Vẹt") 

    choice = input("Nhập lừa chọn(1-3):")
    name = input("Tên thú cưng:")
    age = int(input("Tuổi:"))

    if choice == '1':
        pet = Dog(name,age)
    elif choice == '2':
        pet = Cat(name,age)
    elif choice == '3':
        pet = Parrot(name,age)
    else:
        print("Lựa chọn không hợp lệ")
        return
    
list_pet.append(pet)
print("Đã thêm thú cưng")

while True:
    show_menu()
    opt = input("Chọn thao tác: ")

    if opt == "1":
        add_pet()
    elif opt == "2":
        print("\n📋 Danh sách thú cưng:")
        for pet in list_pet:
            print(pet.get_info())
    elif opt == "3":
        print("\n🔊 Các thú cưng kêu lên:")
        for pet in list_pet:
            pet.make_sound()
    elif opt == "0":
        print("Tạm biệt!")
        break
    else:
        print("Lựa chọn không hợp lệ.")
