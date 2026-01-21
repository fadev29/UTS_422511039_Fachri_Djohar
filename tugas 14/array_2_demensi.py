# Input jumlah baris dan kolom
baris = int(input("Masukkan jumlah baris: "))
kolom = int(input("Masukkan jumlah kolom: "))

# Membuat matriks kosong
matriks = []

# Input elemen matriks
for i in range(baris):
    baris_data = []
    for j in range(kolom):
        nilai = int(input(f"Masukkan elemen [{i}][{j}]: "))
        baris_data.append(nilai)
    matriks.append(baris_data)

# Menghitung jumlah seluruh elemen
total = 0
for i in range(baris):
    for j in range(kolom):
        total += matriks[i][j]

# Output
print("Matriks:", matriks)
print("Jumlah seluruh elemen matriks:", total)
