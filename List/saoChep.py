# Sao chép danh sách
# không thể sao chép chỉ bằng list2 = list1, vì list2 sẽ tham chiếu list1
# nên thay đổi list 1 list 2 sẽ bị ảnh hướng
list1 = ['le','quang','sang']
list2 = list1.copy()

print(list2)

# dùng hàm cho sẵn list()
list3 = list(list1)
print(list3)

# dùng toán tử : (lát cắt: plice)
list4 = list1[:]
print(list4)

# trong js tham trị khó hơn nên dùng toán tử rải 