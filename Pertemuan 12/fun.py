def cetak_nama (*args):
    for nama in args:
        print(nama)

cetak_nama("fachri", "fachri", "fachri")

def jumlah(*angka):
    total = 0
    for x in angka:
        total += x
    return total

