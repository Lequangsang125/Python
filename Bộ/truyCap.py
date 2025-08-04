# Truy cập vào các mục trong tuple
# Tham chiếu đến số chỉ mục, bên trong dấu ngoặc vuông
thislist = ("apple","cherry","potato")
print(thislist[1]) # cherry

#Chỉ số tiêu cực
print(thislist[-1]) # potato

# Phạm vi chỉ mục
# chỉ ra nơi bắt đầu và kết thúc, tạo 1 bộ mới bộ cũ giữ nguyên
thislist = ('apple','cherry','potato','tomato','banana','kiwi')
print(thislist[2:5]) # potato , tomato, banana
print(thislist) # bộ cũ giữ nguyên k bị thay đổi

# nếu bỏ qua bắt đầu [bắt đầu: kết thúc] thì nó bắt đầu từ index = 0
print(thislist[:5]) # apple, cherry, potato , tomato, banana

# nếu bỏ qua kết thúc thì phạm vi đến cuối bộ
print(thislist[2:]) # potato , tomato, banana, kiwi

#Phạm vi âm nếu muốn tìm kiếm từ cuối bộ 
print(thislist[-4:-1])  #potato , tomato, banana,

## LƯU Ý : GIÁ TRỊ BẮT ĐẦU LUÔN ĐƯỢC GIỮ LẠI

# Kiểm tra mục có tồn tại không
if "apple" in thislist:
    print("Có tồn tại")