def ratarata():
    jumlah = 0
    total = 0
    lagi = 'y'
    
    while lagi == 'y' or lagi == 'Y':
        berat = float(input("masukan berat badan : "))

        total = total + berat
        jumlah = jumlah + 1

        lagi = input("apakah anda ingin menambahkan data lagi? (y/n): ")

    if jumlah > 0:
            return total / jumlah
    else:
            return 0

hasil = ratarata()
print("rata rata berat badan: ", str(hasil), "kg")