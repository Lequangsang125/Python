# SỐ TRONG PYTHON
# có 3 kiểu số 
#int
# là số nguyên dương hoặc âm, k có thập phân, độ dài k giới hạn
x = 1 
y = 3534645624534534534
z = -2343434546

#float 
# là số dương hoặc âm, chứ một hoặc nhiều số thập phân
x = 1.10
y = 1.0 
z = -54.33
# float cũng có thể là số khoa học có chữ "e" để chỉ lũy thừa của 10
x = 35e3
y = 12E4
z = 87.234e100

# số phức
# được viết với chữ 'j' là phần ảo 
x = 3 + 5j
y = 5j
z = -5j

## chuyển đổi loại từ kiểu này sang kiểu khác
x = 1
y = 2.8
z = 1j

a = float(x)
print(a)

b = int(y)
print(b)

c = complex(x)
print(c)

# LUU Y : không thể đổi số phức sang kiểu khác

## Số ngẫu nhiên
# python k có hàm random() để tạo số ngẫu nhiên
# python có module tích hợp có tên random để tạo số nn
import random
print(random.randrange(1,10))