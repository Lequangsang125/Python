# NỐI CÁC BỘ
tuple1 = ('orange','coconut','lychee')
tuple2 = ('kiwi',)

tuple3 = tuple1 + tuple2
print(tuple3)

# Nhân các phần tử trong bộ gấp * lần
tuple4 = tuple3 * 2
print(tuple4)

# PHƯƠNG PHÁP 
# count() Trả về số lần một giá trị được chỉ định xuất hiện trong một bộ
print(tuple4.count('kiwi')) # 2
# index() tìm chỉ mục trả về chỉ mục đầu nếu trùng
# Nếu giá trị không tồn tại, Python sẽ báo lỗi ValueError.
print(tuple4.index('kiwi')) # 2
