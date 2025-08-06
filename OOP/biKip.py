# | Khía cạnh                      | JavaScript                                  | Python                                                |
# | ------------------------------ | ------------------------------------------- | ----------------------------------------------------- |
# | Cơ chế kế thừa                 | Dựa trên `prototype chain`                  | Dựa trên `class`, `__mro__` (method resolution order) |
# | Gốc tổ                         | `Object.prototype`                          | `object` (siêu lớp của mọi class)                     |
# | Cách tạo lớp                   | `function A() {}` + `A.prototype.xxx = ...` | `class A:` + method trong `def`                       |
# | Có thể thêm method sau khi tạo | ✅ Rất dễ                                    | ✅ Rất dễ (`ClassName.new_method = ...`)               |
# | Có thể ghi đè method mặc định  | ✅ Thoải mái (ghi vào prototype)             | ✅ Monkey patch được luôn                              |

# 🔝 Tầng 3: Hàm đặc biệt / Thư viện Python
#     ⤷ Ví dụ: __init__(), __len__(), print(), sum(), range(), int(), float(), list(), class, def...

# 🔼 Tầng 2: Câu lệnh Python cơ bản
#     ⤷ Ví dụ: if, for, while, =, +, -, *, and, or, return...

# 🔼 Tầng 1: Bytecode Python (compile từ code source)
#     ⤷ Ví dụ: LOAD_FAST, CALL_FUNCTION, RETURN_VALUE...

# 🔼 Tầng 0: Ngôn ngữ máy / Assembly / Nhị phân
#     ⤷ MOV, JMP, CALL, PUSH/POP, hoặc mã nhị phân trực tiếp (010101...)

