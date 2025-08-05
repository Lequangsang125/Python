# | Phương thức                     | Ký hiệu | Mô tả ngắn gọn                                       |
# | ------------------------------- | ------- | ---------------------------------------------------- |
# | `add(elem)`                     |         | Thêm phần tử vào tập hợp                             |
# | `clear()`                       |         | Xóa toàn bộ phần tử                                  |
# | `copy()`                        |         | Trả về bản sao của tập hợp                           |
# | `difference(other)`             | `-`     | Trả về tập hợp phần tử chỉ có trong tập hiện tại     |
# | `difference_update(other)`      | `-=`    | Xóa khỏi tập hiện tại các phần tử trùng với tập khác |
# | `discard(elem)`                 |         | Xóa phần tử nếu tồn tại, không lỗi nếu không có      |
# | `intersection(other)`           | `&`     | Trả về giao của hai tập                              |
# | `intersection_update(other)`    | `&=`    | Cập nhật tập hiện tại chỉ giữ lại phần giao          |
# | `isdisjoint(other)`             |         | Trả về `True` nếu hai tập **không giao nhau**        |
# | `issubset(other)`               | `<=`    | Trả về `True` nếu tập hiện tại là tập con            |
# | *(subset strict)*               | `<`     | Tập con thực sự (khác và nhỏ hơn)                    |
# | `issuperset(other)`             | `>=`    | Trả về `True` nếu tập hiện tại là tập cha            |
# | *(superset strict)*             | `>`     | Tập cha thực sự                                      |
# | `pop()`                         |         | Xóa và trả về phần tử bất kỳ                         |
# | `remove(elem)`                  |         | Xóa phần tử, **lỗi nếu không tồn tại**               |
# | `symmetric_difference(other)`   | `^`     | Trả về các phần tử **khác nhau** giữa 2 tập          |
# | `symmetric_difference_update()` | `^=`    | Cập nhật tập hiện tại với phần tử khác nhau          |
# | `union(other)`                  | `\|`    | Trả về hợp của các tập hợp                           |
# | `update(other)`                 | `\|=`   | Thêm tất cả phần tử từ tập khác (giống hợp)          |
