# BOOLEAN : true or false
# so sánh 2 biểu thức
print(10 > 9)
print(10 == 9)
print(10 < 9)

# chạy lệnh if 
a = 200
b=33

if b>a :
    print(" b lớn hơn a")
else:
    print("b nhỏ hơn a")

# ĐÁNH GIÁ GIÁ TRỊ VÀ BIẾN
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#====> Hầu hết giá trị đều đúng 
# chuỗi luôn true trừ chuỗi rỗng
# số nào cũng true trừ số 0

#FALSE
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})