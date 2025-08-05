#TRUY CẬP CÁC MỤC
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
# hoặc dùng get
x = thisdict.get("model")

#lấy toàn bộ keys
x = thisdict.keys()
print(x)

# lấy toàn bộ values
x = thisdict.values()
print(x)

# Trả về tục mục trong dict dạng bộ trong danh sách
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.items()

print(x)