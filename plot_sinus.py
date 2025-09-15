# Import pustaka yang dibutuhkan
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Membuat data untuk diplot ---
# Membuat rentang nilai x dari 0 sampai 2*pi (sekitar 6.28)
# dengan 100 titik di antaranya.
x = np.linspace(0, 2 * np.pi, 100)

# Menghitung nilai y menggunakan fungsi sinus dari setiap nilai x.
y = np.sin(x)

# --- 2. Membuat dan Menampilkan Grafik ---
# Membuat plot. Ini adalah langkah dasar untuk memulai visualisasi.
plt.figure(figsize=(8, 6))

# Menambahkan garis ke dalam plot.
# plt.plot(x, y) akan menggambar grafik dengan data x dan y.
plt.plot(x, y, label='sin(x)')

# Menambahkan judul ke grafik
plt.title('Grafik Fungsi Sinus')

# Menambahkan label untuk sumbu-x dan sumbu-y
plt.xlabel('Nilai x')
plt.ylabel('Nilai sin(x)')

# Menambahkan grid untuk memudahkan pembacaan
plt.grid(True)

# Menambahkan legenda untuk menjelaskan garis yang diplot
plt.legend()

# Menampilkan grafik di jendela baru.
plt.show()

# --- Selesai ---