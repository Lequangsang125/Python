# VÒNG LẶP TUPLE
thisTuple = ('one','two','three','four','five')
for x in thisTuple:
    print(x)

#Lặp qua số chỉ mục
#range(5) tương đương range(0,5) dãy số, nó sẽ tự tạo từ index = 0 đầu tiên
#len() đếm số
for i in range(len(thisTuple)):
    print(thisTuple[i])

# vòng lặp while
i = 0
while i < len(thisTuple):
    print(thisTuple[i])
    i += 1 