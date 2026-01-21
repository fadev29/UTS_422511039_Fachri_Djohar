# Input ukuran array 3 dimensi
lapisan = int(input("Masukkan jumlah lapisan: "))
baris = int(input("Masukkan jumlah baris: "))
kolom = int(input("Masukkan jumlah kolom: "))

# Membuat array 3 dimensi
array3D = []

# Input elemen array
for i in range(lapisan):
    layer = []
    print(f"Lapisan ke-{i}")
    for j in range(baris):
        row = []
        for k in range(kolom):
            nilai = int(input(f"Masukkan elemen [{i}][{j}][{k}]: "))
            row.append(nilai)
        layer.append(row)
    array3D.append(layer)

# Mencari nilai terbesar
maks = array3D[0][0][0]

for i in range(lapisan):
    for j in range(baris):
        for k in range(kolom):
            if array3D[i][j][k] > maks:
                maks = array3D[i][j][k]

# Output
print("Nilai terbesar dalam array 3 dimensi adalah:", maks)
