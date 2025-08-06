# Lớp và đối tượng python
# PYthon là ngôn ngữ lập trình hướng đối tượng
# Hầu như mọi thứ trong python là đối tượng, với thuộc tính và phương thức riêng
# Lớp giống như 1 trình xây dựng đối tượng hoặc template để tạo ra các đối tượng

# Tạo 1 lớp
class MyClass:
    x = 5

# Tạo 1 đối tượng từ lớp
p1 = MyClass()
print(p1.x)

# Các ví dụ trên dạng đơn giản nhất và không hữu ích thực tế
# Phương thức __init__()
# phương thức tích hợp sẵn, luôn được thực thi khi lớp khởi tạo
# để gán giá trị cho các thuộc tính của đối tượng hoặc các thao tác khác cần thực hiện khi tạo đối tượng
# Tạo 1 lớp có tên là Person, dùng __init__() để gán giá trị cho tên và tuổi
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = Person("John",36)

print(p1.name)
print(p1.age)

# Phương thức __str__()
# kiểm soát những gì sẽ được trả về khi đối tượng lớp được biểu diễn dưới dạng chuỗi
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} {self.age}"
p1 = Person("John",36)
print(p1)

# tạo method riêng 
# method là hàm thuộc đối tượng
class Person:
    def __init__(self,name,age):
        pass