# // | Phương thức        | Chức năng chính                                          |
# // | ------------------ | -------------------------------------------------------- |
# // | `append(x)`        | Thêm `x` vào **cuối danh sách**                          |
# // | `clear()`          | Xoá **toàn bộ phần tử** trong danh sách                  |
# // | `copy()`           | Trả về **bản sao** của danh sách                         |
# // | `count(x)`         | Đếm **số lần xuất hiện** của `x`                         |
# // | `extend(iterable)` | Thêm **nhiều phần tử** vào cuối danh sách                |
# // | `index(x)`         | Trả về **vị trí đầu tiên** của `x`                       |
# // | `insert(i, x)`     | Chèn `x` vào **vị trí `i`**                              |
# // | `pop(i)`           | Xoá và trả về phần tử ở vị trí `i` (mặc định là cuối)    |
# // | `remove(x)`        | Xoá **phần tử đầu tiên có giá trị `x`**                  |
# // | `reverse()`        | Đảo ngược **thứ tự phần tử**                             |
# // | `sort()`           | Sắp xếp danh sách theo **bảng chữ cái hoặc số tăng dần** |

mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi', 'mango']
print(mylist)