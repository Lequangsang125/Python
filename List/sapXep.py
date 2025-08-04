# SẮP XẾP danh sách

#theo bảng chữ cái
thisList = ['le','sang','quang']
thisList.sort()
print(thisList)

# theo số
thisList = [9,23,56,6,3,2]
thisList.sort()
print(thisList)

# Giảm dần
thisList.sort(reverse=True)
print(thisList)

# Sắp xếp theo điều kiện của hàm
def myFunc(n):
    return abs(n-50) 
thisList = [100,50,65,44,23]
thisList.sort(key= myFunc)
print(thisList)
#Sắp xếp danh sách theo khoảng cách đến 50, thằng nào gần 50 nhất thì xếp lên trước.

#Sắp xếp không phân biệt chữ hoa chữ thường
# mặc định sort() => chữ hoa đứng trước chữ thường
thislist = ['banana','Apple','kiwi','potato','Tomato']
thislist.sort()
print(thislist) #['Apple', 'Tomato', 'banana', 'kiwi', 'potato']
# kết quả không mong muốn nên ta dùng hàm tích hợp là key để xắp xếp
# str.lower là hàm có sẵn 
# k dùng str.lower vì mảng này cần truyền vào 1 hàm chữ k phải kết quả sau khi gọi hàm
thislist.sort(key = str.lower)

# đảo ngược theo index không liên quan bảng chữ cái 
thislist.reverse()
print(thislist)