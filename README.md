# Praktikum Python

Proyek praktikum Pemrograman Berorientasi Objek: program Python pertama,
virtual environment (venv), dan repositori Git/GitHub.

## Isi proyek

| File | Keterangan |
|------|------------|
| `halo.py` | Menyapa pengguna dan menghitung perkiraan usia dari tahun lahir (dengan validasi `try/except`, keluaran berwarna memakai `colorama`) |
| `tampil.py` | Menampilkan tabel di terminal memakai paket `rich` |
| `requirements.txt` | Daftar dependensi proyek |

## Membuat dan mengaktifkan virtual environment

```bash
# Windows
py -m venv .venv
.venv\Scripts\Activate.ps1        # PowerShell
.venv\Scripts\activate.bat        # Command Prompt

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

Environment aktif jika prompt diawali `(.venv)`. Nonaktifkan dengan `deactivate`.

## Menginstal dependensi

```bash
pip install -r requirements.txt
```

## Menjalankan program

```bash
python halo.py
python tampil.py
```
