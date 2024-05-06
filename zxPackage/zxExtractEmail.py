from collections import deque
import urllib.parse
import requests
from bs4 import BeautifulSoup
import re
from urllib.request import *
from urllib.error import *


def zxEmail():
    # Meminta pengguna memasukkan URL website target
    user_url = str(input((("""
┌──[𝙯HaEN✘]-[MASUKKAN TARGET WEBSITE]
└─➣  """))))
    
    # Meminta pengguna memasukkan batas pencarian (misalnya: 10)
    limit = int(input((("""
┌──[𝙯HaEN✘]-[MASUKKAN LIMIT PENCARIAN]
└─➣  """))))
    print("\n")
    # Membuat antrian URL dengan URL target sebagai elemen pertama
    urls = deque([user_url])

    # Set untuk menyimpan URL yang sudah di-scrape
    scraped_urls = set()

    # Set untuk menyimpan alamat email yang ditemukan
    emails = set()

    # Variabel untuk menghitung jumlah URL yang di-scrape
    count = 0

    try:
        while len(urls):
            count += 1
            if count > limit:
                break

            # Mengambil URL dari depan antrian
            url = urls.popleft()

            # Menambahkan URL ke set scraped_urls
            scraped_urls.add(url)

            # Membagi URL menjadi bagian-bagian terpisah
            parts = urllib.parse.urlsplit(url)
            base_url = "{0.scheme}://{0.netloc}".format(parts)
            path = url[: url.rfind("/") + 1] if "/" in parts.path else url

            print("[%d] MEMPROSES %s" % (count, url))
           
            try:
                # Mengirim permintaan GET ke URL
                response = requests.get(url)
            except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError,):
                continue

            # Menggunakan regex untuk mencocokkan pola alamat email
            new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
            emails.update(new_emails)

            # Membuat objek BeautifulSoup dari teks respon
            soup = BeautifulSoup(response.text, features="lxml")

            # Mencari semua elemen <a> di dalam soup
            for anchor in soup.find_all("a"):
                link = anchor.attrs["href"] if "href" in anchor.attrs else " "

                # Memeriksa dan memodifikasi link jika perlu
                if link.startswith("/"):
                    link = base_url + link
                elif not link.startswith("http"):
                    link = path + link

                # Menambahkan link ke antrian urls jika belum ada di dalamnya
                if not link in urls and not link in scraped_urls:
                    urls.append(link)
    except KeyboardInterrupt:
        exit("════════ EXIT ════════")
    
    # Menampilkan alamat email yang ditemukan
    for mail in emails:
        print(" " + mail)
        
    print("\n")
    print(f"┌{'═' * 35}┐")
    print(f"█ {'EMAIL DI TEMUKAN':<28} [{len(emails):02d}] █")
    print(f"└{'═' * 35}┘")



# Memanggil fungsi zx_email untuk menjalankan skrip

# zxEmail()