import socket
from colorama import Fore
from zxPackage.zxLoad import loadTrue

def portScanner():
    # Meminta alamat IP target dari pengguna
    target_ip = input((("""
┌──[𝙯HaEN✘]-[Masukkan IP]
└─➣  """)))
    
    # Meminta rentang port dari pengguna
    nomer_port = input((("""
┌──[𝙯HaEN✘]-[Masukkan Port]
└─➣  """)))
    loadTrue()
    # Mengecek jika rentang port tidak diisi
    if not nomer_port:
        scan_smua_port = True
    else:
        scan_smua_port = False
    
    # Menghitung jumlah port
    port_open = 0
    port_close = 0
    
    # Mengecek jika scanning semua port, maka akan dijalankan semua port 1-65535
    if scan_smua_port:
        port_awal, port_akhir = 1, 65535
    
    else: # mengecek rentang port yang ditentukan, periksa apakah rentang port valid
        port_awal = port_akhir = None
        if '-' in nomer_port:
            port_awal, port_akhir = map(int, nomer_port.split('-'))
    
        elif nomer_port.isdigit(): # Jika rentang port yang di masukan 1 port (misal: 22), Maka akan dijalankan ini 
            port_awal = port_akhir = int(nomer_port)
            
        else: # jika rentang port tidak valid (misal:100-50) , maka akan di jalankan semua port
            print("Rentang port tidak valid. Menggunakan semua port.")
            port_awal, port_akhir = 1, 65535
    
    # Melakukan iterasi pada setiap port dalam rentang yang ditentukan
    for port in range(port_awal, port_akhir + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        
        try:
            # Mengecek status koneksi ke port
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(Fore.LIGHTGREEN_EX+f"Port {port} :: Terbuka" )
                port_open += 1
                try:
                    # Mengambil versi layanan jika ada
                    service_version = versi_port(target_ip, port)
                    if service_version:
                        print(Fore.LIGHTGREEN_EX+f"   Versi Layanan :: {service_version}")
                    else:
                        print(Fore.LIGHTYELLOW_EX+f"Port {port} :: Terbuka (tidak ada informasi versi layanan yang tersedia)".title())
                except:
                    print(Fore.LIGHTYELLOW_EX+f"Port {port} :: Terbuka (gagal mendapatkan versi layanan)".title())
            else:
                print(Fore.LIGHTRED_EX+f"Port {port} :: Tertutup")
                port_close += 1
        except socket.gaierror as e:
            print(f"Gagal melakukan scanning pada port {nomer_port} \n periksa koneksi internet anda...!!! {str(e)}".title())
            port_close += 1
        sock.close()
        
    print(f"═══════════════════════════════════════════════\n")
    print(f"Target IP             :: {target_ip}")
    print(f"Jumlah port terbuka   :: {port_open}")
    print(f"Jumlah port tertutup  :: {port_close}")

def versi_port(target_ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(4)
        sock.connect((target_ip, port))
        
        # Kirim permintaan data ke layanan
        sock.sendall(b"GET / HTTP/1.1\r\n\r\n")
        
        # Baca respons dari layanan
        response = sock.recv(1024)
        
        # Ambil versi layanan dari respons
        service_version = response.decode("UTF-8").split("\n")[0]
        return service_version
        
    except:
        return None