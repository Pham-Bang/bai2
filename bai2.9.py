print("Sinh Vien: Phạm Quang Bàng")
print("MSSV:235752020710007")
str=input("Nhập một chuỗi:")
dict = { }
for n in str:
    keys = dict.keys()
    if n in keys:
        dict [n] += 1
    else:
        dict [n] = 1
print (dict)
