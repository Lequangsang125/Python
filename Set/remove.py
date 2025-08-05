# XÓA CÁC MỤC: remove() or discard()
thisset = {'apple','banana','cherry'}
thisset.remove('apple') # nếu apple k tồn tại thì gây lỗi
# thisset.remove('apple') # nếu apple k tồn tại thì gây lỗi

thisset.discard('banana') # nếu banana k tồn tại k gây lỗi
thisset.discard('banana') # nếu banana k tồn tại k gây lỗi
print(thisset)

# Xóa ngẫu nhiên pop()
thisset = {'apple','banana','cherry'}
thisset.pop() # nếu apple k tồn tại thì gây lỗi
print(thisset)

# Clear làm rỗng tập hợp
thisset = {'apple','banana','cherry'}
thisset.clear() # nếu apple k tồn tại thì gây lỗi
print(thisset)

# Del xóa toàn bộ biến tập hợp
thisset = {'apple','banana','cherry'}
del thisset # nếu apple k tồn tại thì gây lỗi
print(thisset)