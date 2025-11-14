print("Kalkulator Sederhana")

# Langkah 1 : Membuat variabel untuk menyimpan angka
a = int(input("Masukan angka pertama : "))  # operand a
b = int(input("Masukan angka kedua : "))  # operand b

print("Masukan operator (+, -, *, /) : ")  
operator = input("opreasi : ")

# Langkah 2 : Menentukan kategori penjumlahan
# operator relasional untuk menentukan kategori penjumblahan.

if operator == "+": 
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    print(a / b)
else:
    print("Operator tidak valid")

# Langkah 3 : Menampilkan Hasil Kalkulator.