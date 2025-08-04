# Danh sách vòng lặp
# Lặp qua một danh sách for
thisList = ['apple','banana','cherry']
for x in thisList:
    print(x)

# Lặp qua các index
# đếm số phần tử trong mảng, tạo 1 danh sách index từ 0 rồi lặp
for i in range(len(thisList)):
    print(thisList[i])

# Vòng lặp while
i = 0 
while i < len(thisList):
    print(thisList[i])
    i = i + 1 

# Sử dụng List Comprehension
[print(x) for x in thisList]