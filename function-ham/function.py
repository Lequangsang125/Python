# HÀM TRONG PYTHON
# là khối mã được chạy khi gọi

def myfunc():
    print('Hello from a function')
myfunc()

# đối số
def myfunc(doiSo):
    print('toi là', doiSo )

myfunc('le sang')

# Nếu không biết có bao nhiêu đối số được truyền vào
# thêm * trước tên tham số
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")