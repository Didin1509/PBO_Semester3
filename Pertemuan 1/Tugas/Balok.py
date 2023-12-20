# Mengambil Input untuk panjang, lebar, dan tinggi balok
panjang = float(input("Masukkan panjang balok: "))
lebar = float(input("Masukkan lebar balok: "))
tinggi = float(input("Masukkan tinggi balok: "))


luas = ((2 * panjang*lebar)+(2 * panjang*tinggi)+(2 * lebar*tinggi))
volume = (panjang*lebar*tinggi)

print(f"luas adalah:{luas}")
print(f"volume adalah:{volume}")