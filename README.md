
-----

# Newton-Raphson Method

### Finding Roots of Non-Linear Equations

[](https://www.python.org/downloads/release/python-3130/)

-----

### Deskripsi Proyek

Proyek ini adalah implementasi dari **Metode Newton-Raphson**, sebuah algoritma numerik yang digunakan untuk menemukan akar (solusi) dari persamaan non-linear. Program ini memanfaatkan pustaka `sympy` untuk menghitung turunan fungsi secara otomatis, dan pustaka `rich` untuk menampilkan output yang rapi dan menarik di terminal.

-----

### Cara Menjalankan Program

#### 1\. Persiapan Lingkungan

Proyek ini memerlukan **Python 3.13** dan beberapa pustaka tambahan. Disarankan untuk menggunakan **lingkungan virtual (venv)** untuk mengisolasi dependensi.

```bash
# Buat dan aktifkan lingkungan virtual
python -m venv .venv
.\.venv\Scripts\activate
```

#### 2\. Instalasi Dependensi

Setelah lingkungan virtual aktif, instal pustaka yang diperlukan (`sympy` dan `rich`) menggunakan `pip`:

```bash
pip install sympy rich
```

#### 3\. Menjalankan Kode

Jalankan skrip utama dari terminal:

```bash
python newton-rapshon.py
```

-----

### Analisis Kode

  * **Pustaka `sympy`**: Digunakan untuk melakukan kalkulus simbolis. Ini memungkinkan program menghitung turunan dari fungsi $f(x)$ secara otomatis, menghilangkan kebutuhan untuk memasukkan turunan secara manual.

      * `sp.symbols('x')`: Mendefinisikan `x` sebagai variabel simbolis.
      * `sp.diff(f, x)`: Menghitung turunan pertama dari fungsi.

  * **Pustaka `rich`**: Digunakan untuk memformat output di terminal, membuatnya lebih mudah dibaca dan menarik secara visual dengan tabel dan teks berwarna.

      * `Console()`: Objek utama untuk mencetak output.
      * `Table()`: Membuat tabel terstruktur untuk menampilkan setiap iterasi.

  * **Fungsi `newton_raphson`**:

      * Ini adalah inti dari program. Fungsi ini menerima fungsi, tebakan awal (`x0`), toleransi, dan jumlah iterasi maksimum.
      * Rumus inti yang digunakan:
        $$x_{i+1} = x_i - \frac{f(x_i)}{f'(x_i)}$$
      * Loop iterasi akan terus berjalan sampai nilai `x` konvergen (perubahannya lebih kecil dari `tol`) atau mencapai batas iterasi maksimum.

-----

### Contoh Penggunaan

Kode ini sudah menyediakan contoh untuk mencari akar dari persamaan $f(x) = x^2 - 2$, di mana akarnya adalah $\\sqrt{2} \\approx 1.414213$.

**Output dari program akan terlihat seperti ini:**

Program akan menampilkan tabel iterasi secara rinci, diikuti dengan ringkasan hasil akhir.