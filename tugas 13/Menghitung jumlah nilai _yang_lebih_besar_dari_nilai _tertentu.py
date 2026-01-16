nilai_siswa = [90, 80, 85, 70, 95]
nilai_pembanding = 85
jumlah = 0

for nilai in nilai_siswa:
    if nilai > nilai_pembanding:
        jumlah += 1

print("Jumlah nilai lebih besar dari", nilai_pembanding, "adalah", jumlah)