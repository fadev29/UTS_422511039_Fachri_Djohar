temp = float(input("Masukkan suhu air (°C): "))

if temp <= 0:
    print("Keadaan: Padat")
elif temp <= 100:
    print("Keadaan: Cair")
else:
    print("Keadaan: Gas")
