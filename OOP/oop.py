#OOP trong python
# Giúp phát triển ứng dụng theo module, có thể bảo trì và mở rộng
# Là 1 phương pháp tổ chức mã sử dụng đối tượng và lớp để biểu diễn các thực thể trong thế giới thực và hành vi của chúng
# Đối tượng có các thuộc tính , những thứ chứa dữ liệu cụ thể
# Có thể thực hiện hành động bằng phương thức

# 1) Class
# là 1 tập hợp các thuộc tính và phương thức mà các đối tượng tạo ra
# Một số đặc điểm
# Các lớp tạo ra bằng từ khóa class
# Thuộc tính là các biến thuộc về một lớp
# Thuộc tính luôn công khai và có thể được truy cập bằng (.). VD: Myclass.Myattribute
# Tạo một lớp
class Dog: # Lớp Dog : định nghĩa lớp tên là dog
    species = "Canine" # class attribute: thuộc tính lớp được chia sẻ bởi tất cả các thể hiện của lớp

    def __init__(self,name,age): # Phương thức __init__: khởi tạo thuộc tính name và age khi một đối tượng mới được tạo
        self.name = name
        self.age = age

# 2) Object 
# Đối tượng là thể hiện của Class. sản phẩm cụ thể tạo ra từ bản thiết kế đó
# Bao gồm:
# State: trạng thái các dữ liệu hoặc properties mà đối tượng lưu trữ, - ô tô có : màu đỏ , lượng xăng 30%
# Behavior : Những đối tượng có thể làm (methods) - ô tô có thể : tăng tốc, phanh 
# Identity : Bản sắc - Danh tính duy nhất của đối tượng, dù đối tượng có trạng thái và hành vi

# TẠO ĐỐI TƯỢNG
class Dog:
    species = "Canine" # attribute

    def __init__(self,name,age):
        self.name = name
        self.age = age

dog1 = Dog('Bac',3)

print(dog1.name)
print(dog1.age)
print(Dog.species)

# THAM SỐ self
# tham chiếu đến chính instance(Đối tượng) đạng gọi đến phương thức hoặc đang được khởi tạo
# 

class Dog:
    # Thuộc tính lớp(chung cho tất cả) - biến lớp
    species = "Canine" 

    # Hàm khởi tạo (constructor)
    def __init__(self,name,age):
        # biến thể hiện
        self.name = name # Thuộc tính thể hiện
        self.age = age # Thuộc tính thể hiện

    # Phương thức: in ra thông tin
    def bark(self):
        print(f"{self.name} says: gau gau!")

dog1 = Dog("buddy",3)
dog2 = Dog("charlie",5)

# Gọi thuộc tính và phương thức - Method
print(dog1.name, dog1.age, dog1.species)
print(dog2.name, dog2.age, dog2.species)

dog1.bark()
dog2.bark()

print(Dog.species)

# PHÂN BIỆT 
# | Thành phần trong class                     | Có gì đặc biệt?                                                                   | Áp dụng cho                      |
# | ------------------------------------------ | --------------------------------------------------------------------------------- | -------------------------------- |
# | Thuộc tính lớp (`class attribute`)         | Khai báo **ngoài `__init__`**, thường dùng `biến = giá trị` trực tiếp trong class | **Chung cho mọi đối tượng**      |
# | Thuộc tính thể hiện (`instance attribute`) | Khai báo trong `__init__` với `self`                                              | **Riêng cho từng đối tượng**     |
# | Phương thức (`method`)                     | Hàm có `self`, thao tác với dữ liệu của đối tượng                                 | Dùng để xử lý hoặc in ra dữ liệu |


## KẾ THỪA 
# kế thừa cho phép một lớp ( lớp con ) kế thừa phương thức và thuộc tính của một lớp khác(cha)
# nó hỗ trợ phân loại theo thứ bậc và thúc đẩy việc tái sử dụng mã
# các loại thừa kế
#1 kế thừa đơn: lớp con kế thừa từ một lớp cha duy nhất 
#2 kế thừa đa lớp: lớp con kế thừa từ nhiều lớp cha
#3 kế thừa đa cấp: lớp con kế thừa từ lớp cha, rồi lớp cha lại kế thừa từ một lớp khác
#4 kế thừa phân cấp: nhiều lớp con kế thừa từ một lớp cha duy nhất
#5 kế thừa lai: kết hợp của hai hoặc nhiều loại kế thừa
##========================Kế thừa đơn========================
class Dog: # lớp cha 
    def __init__(self,name):
        self.name = name # thuộc tính dùng chung

    def display_name(self): # phương thức dùng chung
        print(f"dog is name: {self.name}")

class Labrador(Dog): # lớp con kế thừa dog
    def sound(self): # tạo nên 1 phương thức riêng
        print("labrador woofs")

# tạo obj từ lớp con 
lab = Labrador("Buddy")

# Gọi các phương thức lấy từ cha và con 
lab.display_name() # lấy từ cha
lab.sound() # lấy từ con

# giải thích: Class cha có thuộc tính tên chó có sẵn, Tạo 1 class là loài (có tên): nếu thêm thuộc tính tên nữa thì quá dư thừa, nên lấy từ lớp cha luôn 
# ghi nhớ 
# lớp con chỉ nên định nghĩa những gì đặc trưng cho nó, còn gì đã có thì kế thừa lại

####========================Kế thừa đa lớp========================
class GuideDog(Labrador): # kế thừa tiếp từ lớp cha Labrador(là lớp con của Dog) ở trên
    def guide(self): # tạo 1 phương thức riêng
        print(f'{self.name}Guides the way!')
lab = GuideDog('Bấc')
lab.display_name() # lấy của ông nội
lab.sound() # lấy của cha
lab.guide() # tự lấy của mình

####========================Kế thừa đa cấp========================
class Friendly:
    def greet(self):
        print("Friendly!")


