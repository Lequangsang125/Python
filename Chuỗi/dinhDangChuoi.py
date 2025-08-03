#Python - Định dạng - Chuỗi
# Vấn đề: không thể kết hợp chuỗi và số

# age = 36 
# txt = 'My name is John, i am' + age
# print(txt)

# Dùng f hoặc format()
# đặt f trước chuỗi và đặt biến hoặc phép tính vào {}
age = 21 
txt = f"my name is sang, i am {age}"
print(txt)

# Định dạng với trình sửa đổi 
price = 59
txt = f"The price is {price:.3f} dollars" 
print(txt) #The price is 59.000 dollars

# Phép toán trong {}
txt = f"The price is {20 * 59} dollars"
print(txt) #The price is 1180 dollars

