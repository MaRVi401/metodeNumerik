def regula_falsi_method(f, a, b, tol=1e-6, max_iter=100):
    """
    Menerapkan Metode Regula Falsi untuk menemukan akar dari suatu fungsi.

    Args:
        f (function): Fungsi yang akan dicari akarnya.
        a (float): Batas bawah interval.
        b (float): Batas atas interval.
        tol (float): Toleransi error yang diinginkan.
        max_iter (int): Jumlah iterasi maksimum.

    Returns:
        float: Nilai akar yang ditemukan.
    """
    if f(a) * f(b) >= 0:
        print("Metode Regula Falsi gagal. Fungsi tidak berubah tanda pada interval ini.")
        return None

    for i in range(max_iter):
        # Hitung titik c menggunakan rumus Regula Falsi
        c = b - f(b) * (b - a) / (f(b) - f(a))
        
        # Periksa apakah c adalah akar atau sudah dalam toleransi
        if abs(f(c)) < tol:
            print(f"Akar ditemukan pada iterasi {i+1}.")
            return c
            
        # Perbarui interval
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
            
    print("Jumlah iterasi maksimum tercapai tanpa menemukan akar yang akurat.")
    return c

# --- Contoh Penggunaan ---
# Definisikan fungsi yang ingin dicari akarnya
def my_function_2(x):
    return x**3 - x - 2

# Tentukan interval awal
a_val_2 = 1
b_val_2 = 2

# Cari akarnya
root_2 = regula_falsi_method(my_function_2, a_val_2, b_val_2)
if root_2 is not None:
    print(f"Akar dari f(x) = x^3 - x - 2 adalah sekitar {root_2:.6f}")