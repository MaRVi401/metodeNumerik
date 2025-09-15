
-----

### **Newton-Raphson Method**

#### Finding Roots of Non-Linear Equations

[](https://www.python.org/downloads/release/python-3130/)

-----

### **Tentang Proyek**

Proyek ini adalah implementasi **Metode Newton-Raphson**, sebuah algoritma numerik yang efisien untuk menemukan akar (solusi) dari persamaan non-linear. Berbeda dengan metode lainnya, pendekatan ini memanfaatkan turunan fungsi untuk mempercepat konvergensi menuju solusi.

Program ini dirancang untuk:

  * Mencari turunan fungsi secara otomatis menggunakan pustaka **SymPy**.
  * Menampilkan proses iterasi dan hasil akhir dengan tabel yang terstruktur dan berwarna menggunakan pustaka **Rich**.

-----

### **Cara Menjalankan**

Ikuti langkah-langkah di bawah ini untuk menginstal dependensi dan menjalankan program.

#### **1. Persiapan Lingkungan**

Proyek ini membutuhkan Python 3.13. Disarankan untuk menggunakan **lingkungan virtual** (`venv`) untuk mengisolasi dependensi dan menghindari konflik dengan proyek lain.

```bash
# Buat lingkungan virtual
python -m venv .venv

# Aktifkan lingkungan virtual
# Pada Windows
.\.venv\Scripts\activate
# Pada macOS/Linux
source .venv/bin/activate
```

#### **2. Instalasi Dependensi**

Setelah lingkungan virtual aktif, instal pustaka yang dibutuhkan (`sympy` dan `rich`) menggunakan `pip`.

```bash
pip install sympy rich
```

#### **3. Menjalankan Kode**

Setelah instalasi selesai, jalankan skrip utama dari terminal:

```bash
python newton-rapshon.py
```

-----

### **Penjelasan Kode**

#### **1. Komponen Utama**

  * **Pustaka `sympy`**: Perpustakaan matematika simbolis yang memungkinkan program ini menghitung **turunan** (`sp.diff()`) dari fungsi secara otomatis, yang merupakan inti dari algoritma Newton-Raphson.
  * **Pustaka `rich`**: Digunakan untuk meningkatkan tampilan output di terminal. `Console()` memungkinkan output berwarna dan `Table()` memformat data iterasi menjadi tabel yang rapi dan mudah dibaca.

#### **2. Fungsi `newton_raphson`**

Ini adalah fungsi utama yang mengimplementasikan algoritma.

  * **Parameter**:
      * `f`: Fungsi non-linear yang akarnya akan dicari.
      * `x0`: **Tebakan awal** (`initial guess`) yang menjadi titik permulaan iterasi.
      * `tol`: **Toleransi error** yang menentukan kapan iterasi harus berhenti (misalnya, `1e-6` untuk akurasi tinggi).
      * `max_iter`: Jumlah iterasi maksimum untuk mencegah perulangan tak terbatas.

#### **3. Alur Algoritma**

1.  **Inisialisasi**: Variabel `x` diinisialisasi dengan `x0`.
2.  **Perhitungan Turunan**: Pustaka `sympy` menghitung turunan fungsi $f(x)$ dan mengubahnya menjadi fungsi numerik yang siap digunakan.
3.  **Iterasi (Loop)**:
      * Di setiap iterasi, nilai `f(x)` dan `f'(x)` dihitung pada titik `x` saat ini.
      * **Rumus Newton-Raphson** diterapkan:
        $$x_{i+1} = x_i - \frac{f(x_i)}{f'(x_i)}$$
      * Rumus ini menghasilkan tebakan baru (`x_{i+1}`) yang secara geometris merupakan perpotongan garis singgung dengan sumbu-x.
4.  **Kondisi Berhenti**:
      * Jika perubahan antara tebakan baru dan tebakan sebelumnya (`|x_{i+1} - x_i|`) lebih kecil dari `tol`, konvergensi dianggap tercapai, dan loop berhenti.
      * Jika `max_iter` tercapai tanpa konvergensi, program akan memberikan pesan bahwa metode gagal menemukan akar dalam batas yang ditentukan.

-----

### **Contoh Penggunaan**

Program ini menyertakan contoh untuk menemukan akar dari persamaan $f(x) = x^2 - 2$, di mana akarnya adalah $\\sqrt{2} \\approx 1.414213$.

**Output di Terminal:**
Program akan menampilkan tabel yang merinci setiap iterasi, diikuti dengan ringkasan hasil akhir yang jelas.
