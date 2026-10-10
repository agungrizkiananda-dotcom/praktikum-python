# halo.py - program Python pertama
from datetime import date

from colorama import Fore, Style, init

init(autoreset=True)

nama = input("Masukkan nama Anda: ")
print(Fore.GREEN + f"Halo, {nama}! Selamat datang di praktikum Python.")

while True:
    try:
        tahun_lahir = int(input("Masukkan tahun lahir Anda: "))
        if not 1900 <= tahun_lahir <= date.today().year:
            raise ValueError
        break
    except ValueError:
        print(Fore.RED + "Input tidak valid. Masukkan tahun lahir berupa angka yang wajar.")

usia = date.today().year - tahun_lahir
print(Fore.CYAN + Style.BRIGHT + f"Perkiraan usia Anda adalah {usia} tahun.")
print("Semoga sukses!")
