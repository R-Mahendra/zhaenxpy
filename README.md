[![code style:](https://img.shields.io/badge/Author-zhaenx-blue?logo=python&logoColor=ffff00)](https://github.com/prettier/prettier)

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum


## Installation

1. Fork the project
2. Clone the project https://github.com/R-Mahendra/zhaenxpy.git
3. cd zhaenxpy
4. python3 zhaenx.py --install

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
  -h, --help          show this help message and exit

  -Ps, --portScanner  Untuk scanning port yang terbuka/tertutup & mendeteksi versi layanan port. [Default Port 1 - 65535]

  -Wp632, --wpEmail   Pengungkapan Email Penulis Postingan Tidak Diautentikasi, memungkinkan penyerang yang tidak diautentikasi
                      mengetahui alamat email pengguna yang telah memublikasikan postingan publik di situs web yang terpengaruh.
                      Jika berhasil dieksploitasi, penyerang dapat mengumpulkan alamat email, sehingga membahayakan privasi pengguna.

  -Wp191, --wpLogin   (WPS-Hide-Login) Bypass Perlindungan dengan Referer-Header. Plugin ini memiliki bug yang memungkinkan untuk
                      mendapatkan halaman login rahasia dengan mengatur string referensi acak dan membuat permintaan
                      ke /wp-admin/options.php sebagai pengguna yang tidak diautentikasi.

  -Em, --exMail       Opsi ini hanya untuk memudahkan mencari tiap-tiap email yang terdapat di situsweb target.

  -Ch, --cxH          Skrip Python ini untuk melakukan [Dictionary Attacks] pada nilai hash. Ini meminta nilai hash dan
                      path ke wordlist dari pengguna. Kemudian, mencoba setiap password dalam wordlist, mengubahnya menjadi hash,
                      dan membandingkannya dengan hash yang diberikan oleh pengguna. Jika ada kecocokan,program mencetak password
                      yang cocok dan waktu saat ini. Jika tidak ada kecocokan, program mencetak pesan bahwa password tidak ditemukan.

  --install           Untuk installasi semua requirements yang di butuhkan.

```

---
<h4 align="center">
  Disclaimer
  <p><i>Script ini untuk pembelajaran, Segala sesuata hal apapun tanggung jawab sendiri.</i></p>
</h4>


