# NỐI CÁC TẬP HỢP
# union()
set1 = {'a','b','c'}
set2 = {'d','e','f'}
set3 = set1.union(set2)
# hoặc dùng |
set3 = set1 | set2
print(set3)

# Nối nhiều bộ
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
#hoặc 
myset = set1 | set2 | set3 | set4
print(myset)

# Nối set với tuple
set1 = {"a", "b", "c"}
tuple1 = ('d','e')
myset = set1.union(tuple1)
print(myset)

# Update 
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# union và update loại bỏ mục trùng lặp

#intersection() và &
# trả về phần tử trùng lặp
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
set3 = set1 & set2

print(set3)

#intersection_update()
# thay đổi tập hợp gốc thay vì trả về một tập hợp mới.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)

#difference()
# trả về một tập hơn mới chỉ chứa các mục từ tập hợp đầu mà k có trong tập hợp kia
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
set3 = set1 - set2

print(set3)

#symmetric_difference() hoặc ^ giữ lại phần tử không bị trùng lặp
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)