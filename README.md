[![code style:](https://img.shields.io/badge/Author-zhaenx-blue?logo=python&logoColor=ffff00)](https://github.com/prettier/prettier)
---
<img src="https://i.ibb.co/QHxKjFv/Screenshot-685.png" alt="Screenshot-685" width="1000px" border="0">
--
zhaenxpy :: Tools Python ini adalah sebuah program multifungsi yang dirancang untuk membantu aktivitas dalam bug bounty hunter (Ethical Hacking), Script ini masih sangat sederhana dan masih dalam tahap develop.


## Installation

1. Clone the project https://github.com/R-Mahendra/zhaenxpy.git
2. cd zhaenxpy
3. python3 zhaenx.py --install

---

### Usage

```sh
python3 zhaenx.py -h
```

Ini akan menampilkan opsi/pilahan untuk script tersebut yang ingin digunakan. Berikut adalah pilihan yang bisa anda gunakan.


```console

usage: zhaenx.py [-h] [-Ps] [-Wp632] [-Wp191] [-Em] [-Ch] [--install]

Author :: ZHAENX (Latest version 2.2.5)

options:
  -h, --help            show this help message and exit

  -Ps, --portScanner    Untuk scanning port yang terbuka/tertutup & mendeteksi versi layanan port. [Default Port 1 - 65535]

  -Wp632, --wpEmail     Pengungkapan Email Penulis Postingan Tidak Diautentikasi, memungkinkan penyerang yang tidak diautentikasi
                        mengetahui alamat email pengguna yang telah memublikasikan postingan publik di situs web yang terpengaruh.
                        Jika berhasil dieksploitasi, penyerang dapat mengumpulkan alamat email, sehingga membahayakan privasi pengguna.

  -Wp191, --wpLogin     (WPS-Hide-Login) Bypass Perlindungan dengan Referer-Header. Plugin ini memiliki bug yang memungkinkan untuk
                        mendapatkan halaman login rahasia dengan mengatur string referensi acak dan membuat permintaan
                        ke /wp-admin/options.php sebagai pengguna yang tidak diautentikasi.

  -Em, --exMail         Opsi ini hanya untuk memudahkan mencari tiap-tiap email yang terdapat di situsweb target.

  -Ha, --hashAnalyzer   Script ini untuk memeriksa jenis hash dan menampilkan informasi hash dalam format tabel.
                        Setelah pengguna memasukkan nilai hash, script akan menentukan jenis hashnya (misalnya MD5, SHA-1, dll.)
                        dan menampilkan informasi terkait seperti panjang bit hash, panjang karakter, dan tipe karakter.
                        Jika jenis hash tidak ditemukan, akan ditampilkan pesan bahwa tipe hash tidak ditemukan. Script ini berguna    
                        untuk mengidentifikasi dan memahami jenis hash yang digunakan dalam berbagai keperluan keamanan dan kriptografi.

  -Ts, --TypeHash TYPE  Script Python ini untuk melakukan Dictionary Attacks pada hash MD5,SHA1,SHA224,SHA256,SHA384,SHA512.
                        Program ini meminta input berupa nilai hash dari pengguna dan mencoba mencocokkan hash tersebut dengan
                        password yang ada di dalam wordlist. Jika cocok, program akan mencetak password yang cocok.
                        Jika tidak ada yang cocok, program akan mencetak pesan bahwa password tidak ditemukan.

  --install             Untuk installasi semua requirements yang dibutuhkan.

```

---
<h4 align="center">
  Disclaimer
  <p>Script ini untuk pembelajaran, Segala sesuata hal apapun tanggung jawab sendiri.</p>
</h4>


