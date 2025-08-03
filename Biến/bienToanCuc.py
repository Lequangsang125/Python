# BIẾN TOÀN CỤC
# Các biến được tạo bên ngoài hàm 
# Có thể sử dụng được cả trong và ngoài hàm
x = str(1)
def myFunc():
    print("Python is number", x)
myFunc()

# BIẾN CỤC BỘ
# Là biến tạo bên trong hàm, riêng biệt với bên ngoài hàm
x = "le"
print(x)
def myFunc():
    x = 'sang'
    print('quang', x)
myFunc()

# TỪ KHÓA TOÀN CỤC GLOBAL
# để tạo biến toàn cục từ biến nội bộ
def myFunc():
    global x
    x = " fantasic"
myFunc()
print("Python is" + x)

# ghi đè biến toàn cục bằng 1 biến cục bộ
x = "lee"
def myFunc():
    global x 
    x = 'le'
myFunc()
print(x) #===> le