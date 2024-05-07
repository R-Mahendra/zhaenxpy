import time
import sys

def loadTrue():
    total_items = 100  # Total item yang akan diproses
    length = 40  # Panjang loading bar
    for zhaenx in range(total_items + 1):
        if zhaenx > total_items:
            break  # Jika zhaenx melebihi total_items, keluar dari loop
        elif zhaenx == total_items:
            bar = "█" * length  # Jika zhaenx sama dengan total_items, loading bar penuh
            percentage = 100  # Persentase 100%
        else:
            percent = zhaenx / total_items  # Menghitung persentase progres
            filled_length = int(
                length * percent
            )  # Menghitung panjang loading bar yang terisi
            bar = "█" * filled_length + "═" * (
                length - filled_length
            )  # Membentuk loading bar
            percentage = round(
                percent * 100,
            )  # Menghitung persentase dengan 1 angka di belakang koma

        sys.stdout.write(
            f"\r[𝙯HaEN✘]-{bar}] {percentage}% "
        )  # Menulis loading bar dan persentase
        sys.stdout.flush()

        if zhaenx == total_items:
            sys.stdout.write("\n")  # Menulis baris baru setelah loading selesai
            sys.stdout.flush()
            time.sleep(0.5)
            # Menghapus baris saat ini di terminal
            print("\033[A                                                           \033[A")
            print("\n")
            sys.stdout.flush()

        time.sleep(0.02)  # Delay untuk simulasi proses yang sedang berlangsung



