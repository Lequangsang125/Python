# # vòng lặp for dùng để lặp qua một chuỗi( danh sách, bộ, từ điển,tập hợp hoặc chuỗi)
# # với for ta có thể thực thi một tập hợp câu lệnh, một lần cho mỗi mục trong danh sách
# fruits = ['apple','watermelon','banana','cherry']
# for x in fruits:
#     print(x)
# # không yêu cầu thiết lập biến chỉ mục trước

# # Lặp qua một chuỗi
# for x in "banana":
#     print(x)

# # break, có thể dừng vòng lặp trước khi nó lặp qua tất cả các mục
# fruits = ['apple','watermelon','banana','cherry']
# for x in fruits:
#     print(x)
#     if x == 'banana':
#         break

# # thoát lặp khi x == chuối luôn
# fruits = ['apple','watermelon','banana','cherry']
# for x in fruits:
#     if x == 'banana':
#         break
#     print(x)

# # continue có thể dừng lặp hiện tại và tiếp tục lặp tiếp theo
# fruits = ['apple','banana','cherry']
# for x in fruits:
#     if x == 'banana': # không in chuối
#         continue
#     print(x)

# #range()
# # để lặp qua 1 tập hợp mã 1 số lần nhất định
# for x in range(6):
#     print(x)
#Lưu ý rằng range(6) không phải là các giá trị từ 0 đến 6, mà là các giá trị từ 0 đến 5.
#Hàm range () mặc định là 0 làm giá trị bắt đầu, tuy nhiên có thể chỉ định giá trị bắt đầu bằng cách thêm tham số: range(2, 6) , nghĩa là các giá trị từ 2 đến 6 (nhưng không bao gồm 6):
#Hàm range mặc định tăng chuỗi lên 1, tuy nhiên có thể tăng giá trị thêm x sau mỗi vòng lặp 
for x in range(2,10,2):
    print(x) # 2 , 4 , 6 , 8
