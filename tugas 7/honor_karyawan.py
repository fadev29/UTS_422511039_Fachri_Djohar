jam = int(input("Masukkan jumlah jam kerja per minggu: "))

upah_per_jam = 50000

if jam > 48:
    lembur = (jam - 48) * 10000
    total = (48 * upah_per_jam) + lembur
else:
    total = jam * upah_per_jam

print("Total honor: Rp", total)
