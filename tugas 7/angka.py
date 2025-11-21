angka = int(input("Masukkan angka 1–4: "))

match angka:
    case 1:
        print("Satu")
    case 2:
        print("Dua")
    case 3:
        print("Tiga")
    case 4:
        print("Empat")
    case _:
        print("Angka di luar jangkauan")
