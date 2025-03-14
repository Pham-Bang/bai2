print("Sinh Viên : Phạm Quang Bàng")
print("MSSV : 235752020710007")
j = []
for i in range(500, 1200):
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))
print(','.join(j))
