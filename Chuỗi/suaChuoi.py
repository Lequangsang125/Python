#SỬA CHUỖI : in hoa,...
# Chữ in hoa
x = " le quang sang "
print(x.upper())

# Chữ thường
print(x.lower())

# Xóa khoảng trắng ở đầu và sau 
y = x.strip()
print(y)
print(len(y))

# Thay thế chuỗi
print(x.replace('e','ee'))

# chia chuỗi split() chia thành chuỗi con nếu thấy ký tự truyền vào
print(x.split(' '))
