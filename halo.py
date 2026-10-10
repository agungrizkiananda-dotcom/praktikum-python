# halo.py - program Python pertama
from datetime import date

nama = input("Masukkan nama Anda: ")
print(f"Halo, {nama}! Selamat datang di praktikum Python.")

while True:
    try:
        tahun_lahir = int(input("Masukkan tahun lahir Anda: "))
        if not 1900 <= tahun_lahir <= date.today().year:
            raise ValueError
        break
    except ValueError:
        print("Input tidak valid. Masukkan tahun lahir berupa angka yang wajar.")

usia = date.today().year - tahun_lahir
print(f"Perkiraan usia Anda adalah {usia} tahun.")
print("Semoga sukses!")
