# XÓA CÁC INDEX TRONG MẢNG
# nếu có nhiều hơn 1 mục cần xóa remove sẽ xóa cái đầu tiên
thisList = ['apple', 'banana','cherry']
thisList.remove("banana")
print(thisList)

# xóa index đã chỉ định, nếu k chỉ định nó sẽ xóa index cuối
thisList.pop(1)
print(thisList)
# del cũng xóa index chỉ định
del thisList[0]

# del xóa toàn bộ mảng
del thisList

# clear xóa thành mảng rỗng
thisList.clear() 