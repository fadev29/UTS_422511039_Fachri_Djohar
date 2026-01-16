nilai_siswa = [90, 81, 84, 70, 95, 88]
jumlah = 0
count = 0

for nilai in nilai_siswa:
    if nilai % 2 == 0:
        jumlah += nilai
        count += 1

if count > 0:
    rata_rata = jumlah / count
    print("Rata-rata nilai genap:", rata_rata)
else:
    print("Tidak ada nilai genap")
