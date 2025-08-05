# python dictionaries
thisdict = {
    "name" : "le sang",
    "city" : "Phu Tho",
    "age" : 21,
}
print(type(thisdict))
# lưu trữ giá trị theo key: value
# là bộ sưu tập có thể sắp xếp, có thể thay dổi và không được trùng lặp
# có thể tham chiếu bằng cách sử dụng key
print(thisdict['name'])

# len 
print(len(thisdict))

# hàm tạo dict
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)