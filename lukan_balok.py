print('Menghitung luas permukaan Balok')
print('===============================')

panjang = float(input('Masukkan nilai panjang: '))
lebar = float(input('Masukkan nilai lebar: '))
tinggi = float(input('Masukkan nilai tinggi: '))

lukan = 2 * (panjang*lebar + panjang*tinggi + lebar*tinggi)

print('Hasilnya adalah: ' + str(lukan))
