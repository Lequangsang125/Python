## CHUỖI TRONG PYTHON
# bao quanh bởi '' hoặc ""
# hiển thị chuỗi bằng print()
print('Hello')
print("Hello")

#Trích dẫn trong chuỗi
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#Gán chuỗi cho một biến
a = "hello"
print(a)

#Chuỗi nhiều dòng: dùng """ ... """ hoặc 3 dấu '''
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Chuỗi là mảng 
a = 'le quang sang'
print(a[1])

# Lặp qua chuỗi: vì chuỗi là mảng nên lặp đc
for x in "banana":
    print(x)

# Chiều dài chuỗi: hàm len()
x = 'sang le'
y = len(x)
print(y)

# Kiểm tra chuỗi xem có ký tự hay chuỗi trong chuỗi k
txt = "Toi la le quang sang"
x = "sang" in txt
print(x) #true
# sử dụng if
if 'sang' in txt:
    print("co ky tu nay")
# dùng nếu không not in
if 'sán' not in txt:
    print("khong co ky tu nay")