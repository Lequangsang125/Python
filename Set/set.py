# Tập hợp - set python
# dùng để lưu trữ nhiều mục trong một biến duy nhất
# một tập hợp là 1 tập hợp k đc sắp xếp, k thay đổi, k lập chỉ mục
myset = {'apple', ' banana','cherry'}
print(myset)
# k đc xắp xếp nên k biết các mục xuất hiện ntn
# k cho phép trùng lặp, không sắp xếp, không thay đổi 
# không thể đc tham chiếu theo index khoặc khóa do k đc sắp xếp
# không thể thay đổi mục sau khi tạo nhưng có thể xóa và thêm mục mới

# trùng lặp
myset = {'apple',"apple", ' banana','cherry'}
print(myset) # trùng lặp sẽ bị bỏ qua

# các giá trị True và 1 bị coi là trùng lặp
thisset = { True, 1}
print(thisset) #True

# False và 0 bị coi là trùng lặp
thisset = { False,0}
print(thisset) #False

# lấy độ dài len
print(len(thisset))

# Set có thể có bất kỳ kiểu dữ liệu nào
# 1 tập hợp có thể có nhiều kiểu dữ liệu khác nhau
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

# Hàm tạo set
thisset = set(("apple",'banana','cherry'))
print(thisset)