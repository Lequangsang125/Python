# Lambda là một hàm ẩn danh nhỏ
# Có thể sử dụng bất kỳ số lượng đối số nào, nhưng chỉ có thể có 1 biểu thức
# Cú pháp 
# lambda arguments : expression
# Thêm 10 vào đối số a 
x = lambda a : a + 10
print(x(5))

# hàm lambda có thể sử dụng bất kỳ số lượng đối số nào
# nhân đối số a và đối số b và trả về kết quả
x = lambda a,b : a * b 
print(x(5,6))

x = lambda a,b,c : a + b + c
print(x(1,1,1))

# sức mạnh của hàm lambda là khi dùng nó như một hàm ẩn danh trong 1 hàm khác
# giả sử có 1 hàm đối số và đối số * 1 số chưa biết 
def myfunc(n):
    return lambda a: a * n

# dùng hàm này để nó luôn nhân đôi số bạn gửi vào
def myfunc(n):
    return lambda a : a * n 
mydoubler = myfunc(2)
print(mydoubler(3))

# dùng nhân 3 
def myfunc(n):
    return lambda a : a * n 
mytriper = myfunc(3)
print(mytriper(3))

# hoặc sử dụng cùng một định nghĩa hàm để tạo cả hai hàm trong một chương trình
def myfunc(n):
    return lambda a: a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))

#Sử dụng hàm lambda khi cần sử dụng hàm ẩn danh trong thời gian ngắn.