# THAM GIA DANH SÁCH
# nối danh sách bằng +
list1 = ['a' ,'b' ,'c']
list2 = [1,2,3]
list3 = list1 + list2
print(list3)

# dùng append thêm từng mục một
for x in list2:
    list1.append(x)
print(list1)

# hoặc bạn dùng extend(), thêm phần tử ds này vào ds khác
list1.extend(list2)
print(list1)

## TRONG PY KHÔNG BỊ HOISTING CODE CHẠY 1 CHIỀU TRÊN XUỐNG