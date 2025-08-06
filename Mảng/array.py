#Trong python không hỗ trợ cho mảng nên dùng list thay thế
# dùng list như 1 array, để làm việc với mảng dùng 1 thư viện, như NumPy
# mảng dùng lưu trữ nhiều giá trị trong một biến duy nhất
cars = ['bmw','ford','volvo']

# nếu có danh sách xe, lưu trữ bằng biến
car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"

# Muốn lặp lại các xe và tìm một chiếc cụ thể thì sao
# nếu không có 3 mà là 3oo chiếc xe thì sao

# GIẢi PHÁP : MẢNG
# 1 mảng có thể chứa nhiều giá trị trong 1 biến tên duy nhất
# và có thể truy cập các giá trị bằng cách tham chiếu đến số chỉ mục
print(cars[0])

# Sửa giá trị của phần tử index = 0
cars[0] = 'toyota'
print(cars)

# Dùng len kiểm tra độ dài mảng
print(len(cars))
# Độ dài mảng luôn lớn hơn index cao nhất 1 đơn vị

# Lặp các phần tử mảng
for x in cars:
    print(x)

# Thêm phần tử mảng
# append() thêm phần tử vào cuối mảng
cars.append('mecs')
print(cars)

# Xóa các phần tử mảng
# dùng pop() xóa phần tử bằng index
cars.pop(0)
print(cars)

# dùng remove() để xóa phần tử chỉ định
cars.remove('volvo')
print(cars)

# Dùng Clear() xóa toàn bộ phần tử mảng ===> mảng rỗng
cars.clear()
print(cars)


