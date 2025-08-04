# Cung cấp cú pháp ngắn hơn khi muốn tạo danh sách mới dựa trên giá trị của danh sách hiện có
# dựa vào danh sách trái cây, muốn có danh sách mới, chỉ chứa  loại trái cây có chữ a trong teen
fruits = ['apple', 'banana','cherry','kiwi','mango']
newList = []

for x in fruits:
    if 'a' in x:
        newList.append(x)
print(newList)

# chỉ 1 dòng mã
newList = [x for x in fruits if "a" in x]
print(newList)

# công thức
new_list = [cái muốn lấy for cái đang duyệt in danh sách if điều kiện ]

# tương đương
danh sách mới = []
for cái đang duyệt in danh sách:
    if điều kiện:
        danh sách mới.append(cái muốn lấy)