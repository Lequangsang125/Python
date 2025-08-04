# GIẢI NÉN CÁC BỘ DỮ LIỆU
# thông thường tạo 1 tuple => gọi là đóng gói
# chúng ta có thể giải nén nó
#b1 gán cho nó nghĩa bóng (nghĩa đen là con số:1,2,3... sẽ lỗi)
thislist = ('apple', 'coconut' , 'orange')
# gán phải gán ngược nếu đúng chiều thì là tạo bộ mới rồi
(one,two,three) = thislist 
#b2 in ra và xem thử
print(one)
print(two)
print(three)
# Lưu ý khi gán phải trùng số lượng phần tử

# Có thể dùng * để thu thập phần tử dư thành danh sách
thislist1 = ('apple', 'coconut' , 'orange')
(one,*two) = thislist1
#b2 in ra và xem thử
print(one) # apple
print(two) #['coconut', 'orange']

#Nếu thêm hoa thị vào biến khác, sẽ bị bán giá trị cho đến khi giá trị còn lại khớp số biến còn lại
thislist2 = ('apple', 'coconut' , 'orange','kiwi','tomato','potato','orange')
(one,two,*three,four,five)  = thislist2
print(three) # [orange, kiwi, tomato]



