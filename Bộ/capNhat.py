# CẬP NHẬT TUPLE
# không thể thay đổi nhưng vẫn có giải pháp khắc phục
# nó là bất biến nhưng có cách lách luật
# tuple ====> Danh sách ====> tuple
# b1 chuyển tuple x thành list y 
x = ('apple','cherry','banana','coconut')
y = list(x)
#b2 thay đổi phần tử trong list y
y[1] = 'kiwi'
#b3 biến ngược list y thành tuple x
x = tuple(y)
print(x)

# Thêm mục cũng như vậy vì tuple bất biến còn list thì có nhiều hàm làm việc
# append()
#b1 chuyển tuple a thành list b
a = ('rabbit','dog','cat','fish','elephant')
b = list(a)
#b2 Thêm mục vào cuối danh sách của b 
b.append('chicken')
print(b)
#b3 chuyển ngược lại thành bộ tuple
b = tuple(a)

# Thêm tuple vào tuple
thistuple = ('apple','banana','cherry')
x = ('coconut',)
thistuple += x
print(thistuple)

# xóa mục 
thistuple1 = ('apple','banana','cherry')
y = list(thistuple1)
y.remove('apple')
thistuple1 = tuple(y)
print(thistuple1)

# Xóa toàn bộ bằng del
thistuple2 = ('apple','banana','cherry')
del(thistuple2)
print(thistuple2)


