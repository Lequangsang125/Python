# Bộ python
mytuple = ('apple','banana','cherry')
# dùng lưu trữ nhiều mục trong 1 biến 
# là 1 trong 4 kiểu dữ liệu tích hợp trong Python để lưu trữ các tập hợp dữ liệu
# 3 kiểu còn lại : List, Set, Dictionary
# 1 bộ là 1 tập hợp được sắp xếp và không thể thay đổi
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# được sắp xếp theo thứ tự, không thể thay đổi và cho phép các giá trị trùng lặp
# các mục trong bộ đc lập index từ 0 
#Các bộ không thể thay đổi, nghĩa là chúng ta không thể thay đổi, thêm hoặc xóa các mục sau khi bộ đã được tạo.

# Vì các bộ dữ liệu được lập chỉ mục nên chúng có thể có các mục cùng giá trị
thislist = ('apple','kiwi','mango','cherry','tomato','tomato')
print(thislist)

#để xác định độ dài ta dùng len()
print(len(thislist))

# tạo chỉ với 1 phần tử, cần thêm dấu phẩy sau phần tử đó
# nếu không python sẽ không nhận dạng đó là 1 tuple 
thislist = ('sangle')
print(type(thislist)) #str

thislist = ('sangle',)
print(type(thislist))

# các mục tuple có thể thuộc bất kỳ dữ liệu nào
thislist1 = ('sangle','quang')
thislist2 = (1,2,3,4,5,5,6)
thislist3 = (True,False,True)

# Một bộ có thể chứa nhiều kiểu dữ liệu khác nhau
thislist4 = (True, 32,"Alex",False)

# trong python các bộ được định nghĩa là các đối tượng có kiểu dữ liệu 'tuple'

#Hàm tạo tuple 
thislist5 = tuple(('name','age','male'))
print(type(thislist5))


