# Chúng ta có thể thực thi một tập hơn các câu lệnh miễn điều kiện còn đúng
i = 1 
while i <6 :
    print(i)
    i+=1 
# nhớ tăng i không nó sẽ lặp mãi mãi
# break, có thể dừng lặp ngay khi điều kiện while đúng
i = 1 
while i < 6:
    print(i)
    if i == 3:
        break
    i+=1

# continue, có thể dừng vòng lặp hiện tại và tiếp tục vòng lặp tiếp theo
i = 0 
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#else 
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")