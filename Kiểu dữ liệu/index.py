# Các kiểu dữ liệu Python
''' 
| Kiểu dữ liệu | Mô tả ngắn                           | Ví dụ                   |
| ------------ | ------------------------------------ | ----------------------- |
| `str`        | Chuỗi ký tự                          | `"hello"`               |
| `int`        | Số nguyên                            | `20`                    |
| `float`      | Số thực (có thập phân)               | `20.5`                  |
| `complex`    | Số phức (có phần ảo)                 | `1j`                    |
| `list`       | Danh sách, có thứ tự, thay đổi được  | `['a', 'b']`            |
| `tuple`      | Giống list nhưng không thay đổi được | `('a', 'b')`            |
| `range`      | Dãy số                               | `range(6)`              |
| `dict`       | Từ điển key-value                    | `{"name": "Sang"}`      |
| `set`        | Tập hợp không trùng lặp              | `{"a", "b"}`            |
| `frozenset`  | Tập hợp bất biến                     | `frozenset({"a", "b"})` |
| `bool`       | Giá trị đúng/sai                     | `True`, `False`         |
| `bytes`      | Dữ liệu nhị phân không đổi           | `b"Hello"`              |
| `bytearray`  | Dữ liệu nhị phân có thể thay đổi     | `bytearray(5)`          |
| `memoryview` | Truy cập bộ nhớ nhị phân             | `memoryview(bytes(5))`  |
| `NoneType`   | Không có giá trị                     | `None`                  |
'''
x = "hello world"                                #str
x = 20                                           #int
x = 20.5                                         #float
x = 1j                                           #complex
x = ['apple','banana','cherry']                  #list 
x = ('apple','banana','cherry')                  #tuple
x = range(6)                                     #range
x = {"name" : "sang" , "age" : 21}               #dict
x =  {"apple", "banana", "cherry"}               #set
x = frozenset({'apple','banana','cherry'})       #frozenset
x = True                                         #bool
x = b"Hello"                                     #bytes
x = bytearray(5)                                 #bytearray
x = memoryview(bytes(5))                         #memoryview
x = None                                         #NoneType
