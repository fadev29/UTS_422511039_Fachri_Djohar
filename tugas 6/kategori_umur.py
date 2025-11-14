# menentukan kategori umur 

# Langkah 1 : Membuat variabel untuk menyimpan umur
umur = float(input("Masukan umur anda : "))  # operand

# Langkah 2 : Menentukan kategori umur
if umur <= 12:    # operator relasional untuk menentukan kategori umur anda.
    print("Anda termasuk anak-anak")
elif umur <= 17:
    print("Anda termasuk remaja")
elif umur <= 59:
    print("Anda termasuk dewasa")
else:
    print("Anda termasuk lansia")

# Langkah 3 : Menampilkan kategori umur