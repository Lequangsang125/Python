# XỬ LÝ NGOẠI LỆ PYTHON
# Xử lý các lỗi xảy ra trong quá trình thực thi chương trình
# Cho phép phản hồi lỗi thay vì làm sập chương trình
# Cho phép phát hiện và quản lý lỗi 
# ví dụ
n = 10
try:
    res = n / 0 
except ZeroDivisionError:
    print("Không thể chia hết cho 0")
# chúng in ra lỗi thay vì dừng chương trình
# sự khác biệt 
# lỗi: là những vấn đề nghiêm trọng mà một chương trình không nên cố xử lý, lỗi cú pháp và lỗi bộ nhớ
# ngoại lệ: ít nghiêm trọng hơn lỗi và có thể xử lý bởi chường trình,dữ liệu input không hợp lệ, tệp thiếu hoặc sự cố mạng
# lỗi cú pháp
# print("hello world" # lỗi thiếu dấu đóng
    
# ngoại lệ
# n = 10
# res = n / 0 

try:
    n = 0
    res = 100 / n 
except ZeroDivisionError:
    print("Bạn không thể chia hết cho 0")
except ValueError:
    print("Nhập lại số hợp lệ")
else: # chạy nếu không lỗi 
    print("Kết quả:", res)
finally:
    print("hoàn thành ")