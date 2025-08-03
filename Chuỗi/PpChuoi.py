
#BIẾN ĐỔI CHỮ
# | Phương thức    | Ý nghĩa                                                |
# | -------------- | ------------------------------------------------------ |
# | `lower()`      | Thành chữ thường toàn bộ                               |
# | `upper()`      | Thành chữ hoa toàn bộ                                  |
# | `capitalize()` | Viết hoa chữ cái đầu chuỗi                             |
# | `title()`      | Viết hoa chữ cái đầu mỗi từ                            |
# | `swapcase()`   | Đổi chữ hoa ↔ thường                                   |
# | `casefold()`   | Giống `lower()` nhưng mạnh hơn (xử lý Unicode tốt hơn) |

# XỬ LÝ KHOẢNG TRẮNG CĂN LỀ
# | Phương thức | Ý nghĩa                            |
# | ----------- | ---------------------------------- |
# | `strip()`   | Xóa khoảng trắng 2 đầu chuỗi       |
# | `lstrip()`  | Xóa bên trái                       |
# | `rstrip()`  | Xóa bên phải                       |
# | `center(n)` | Căn giữa chuỗi trong độ dài `n`    |
# | `ljust(n)`  | Căn trái chuỗi với độ dài `n`      |
# | `rjust(n)`  | Căn phải chuỗi với độ dài `n`      |
# | `zfill(n)`  | Thêm số 0 vào đầu để đủ độ dài `n` |

# TÌM KIẾM KIỂM TRA
# | Phương thức     | Ý nghĩa                                         |
# | --------------- | ----------------------------------------------- |
# | `find(x)`       | Trả về vị trí đầu tiên của `x`, -1 nếu không có |
# | `rfind(x)`      | Vị trí cuối cùng của `x`                        |
# | `index(x)`      | Giống `find()`, nhưng lỗi nếu không tìm thấy    |
# | `rindex(x)`     | Giống `rfind()`, lỗi nếu không tìm thấy         |
# | `startswith(x)` | Chuỗi bắt đầu bằng `x`? (True/False)            |
# | `endswith(x)`   | Chuỗi kết thúc bằng `x`? (True/False)           |
# | `count(x)`      | Đếm số lần xuất hiện của `x`                    |

# KIỂM TRA NỘI DUNG CHUỖI 
# | Phương thức      | Ý nghĩa                         |
# | ---------------- | ------------------------------- |
# | `isalnum()`      | Chỉ gồm chữ và số?              |
# | `isalpha()`      | Chỉ gồm chữ cái?                |
# | `isdigit()`      | Chỉ gồm số?                     |
# | `isdecimal()`    | Chỉ là số thập phân?            |
# | `isnumeric()`    | Là dạng số? (kể cả số đặc biệt) |
# | `islower()`      | Tất cả là chữ thường?           |
# | `isupper()`      | Tất cả là chữ hoa?              |
# | `istitle()`      | Theo kiểu tiêu đề?              |
# | `isspace()`      | Toàn khoảng trắng?              |
# | `isascii()`      | Toàn ký tự ASCII?               |
# | `isidentifier()` | Tên biến hợp lệ không?          |
# | `isprintable()`  | In được không?                  |

# BIẾN ĐỔI THAY THẾ
# | Phương thức     | Ý nghĩa                          |
# | --------------- | -------------------------------- |
# | `replace(a, b)` | Thay `a` bằng `b`                |
# | `format()`      | Chèn biến vào chuỗi (`f-string`) |
# | `join(list)`    | Nối danh sách thành chuỗi        |
# | `translate()`   | Dịch chuỗi theo bảng đã tạo      |
# | `maketrans()`   | Tạo bảng chuyển đổi ký tự        |

# CẮT CHUỖI
# | Phương thức     | Ý nghĩa                                 |
# | --------------- | --------------------------------------- |
# | `split()`       | Cắt chuỗi thành list theo dấu phân cách |
# | `rsplit()`      | Cắt từ phải sang                        |
# | `splitlines()`  | Cắt theo dòng                           |
# | `partition(x)`  | Cắt chuỗi thành 3 phần tại `x`          |
# | `rpartition(x)` | Như trên nhưng từ phải sang             |

# MÃ HÓA TAB ĐẶC BIỆT
# | Phương thức     | Ý nghĩa                            |
# | --------------- | ---------------------------------- |
# | `encode()`      | Mã hóa chuỗi thành bytes           |
# | `expandtabs(n)` | Chuyển `\t` thành `n` khoảng trắng |
