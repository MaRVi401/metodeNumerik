import math
import os
import matplotlib.pyplot as plt

# --- Definisi variabel warna di awal file ---
HEADER = '\033[95m'
GREEN = '\033[92m'
RED = '\033[91m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
BOLD = '\033[1m'
ENDC = '\033[0m'

# Menyesuaikan warna dengan terminal Windows jika diperlukan
if os.name == 'nt':
    os.system('color')

# --- Logika Bisection ---
def bisection(func, a, b, tol=1e-6, max_iter=100):
    if func(a) * func(b) >= 0:
        print(f"\n{RED}❌ {BOLD}Metode bisection gagal: Fungsi tidak berubah tanda pada interval ini.{ENDC}")
        return None

    # Menggunakan karakter ASCII sederhana untuk garis
    table_width = 85
    column_widths = [10, 15, 15, 15, 15]

    print(f"\n{BLUE}+{'-' * (table_width - 2)}+{ENDC}")
    print(f"{BLUE}|{'':^8}{'PROSES ITERASI METODE BISECTION':^65}{'':^8}  |{ENDC}")
    print(f"{BLUE}+{'-' * (table_width - 2)}+{ENDC}")
    
    header_row = f"| {'ITER':<{column_widths[0]}} | {'a':<{column_widths[1]}} | {'b':<{column_widths[2]}} | {'c':<{column_widths[3]}} | {'f(c)':<{column_widths[4]}}|"
    print(f"{BOLD}{header_row}{ENDC}")
    
    print(f"{BLUE}+{'-' * (table_width - 2)}+{ENDC}")

    # Menyiapkan list untuk data grafik
    c_values = []
    f_c_values = []

    for i in range(max_iter):
        c = (a + b) / 2
        f_c = func(c)
        c_values.append(c)
        f_c_values.append(f_c)

        f_c_str = f"{f_c:.6f}"
        effective_len = len(f_c_str)
        
        if abs(f_c) < tol:
            f_c_display = f"{YELLOW}{BOLD}{f_c_str}{ENDC}"
        elif f_c < 0:
            f_c_display = f"{RED}{f_c_str}{ENDC}"
        else:
            f_c_display = f"{GREEN}{f_c_str}{ENDC}"
        
        print(f"| {i+1:<{column_widths[0]}} | {a:<{column_widths[1]}.6f} | {b:<{column_widths[2]}.6f} | {c:<{column_widths[3]}.6f} | {f_c_display.ljust(column_widths[4] + (len(f_c_display) - effective_len))}|")

        if abs(f_c) < tol:
            print(f"{BLUE}+{'-' * (table_width - 2)}+{ENDC}")
            print(f"\n{GREEN}✅ {BOLD}Akar ditemukan pada iterasi {i+1} dengan toleransi yang diinginkan.{ENDC}")
            return c, c_values, f_c_values

        if func(a) * f_c < 0:
            b = c
        else:
            a = c
    
    print(f"{BLUE}+{'-' * (table_width - 2)}+{ENDC}")
    print(f"\n{RED}❌ {BOLD}Jumlah iterasi maksimum tercapai tanpa menemukan akar yang akurat.{ENDC}")
    return (a + b) / 2, c_values, f_c_values

# --- Fungsi yang tersedia ---
FUNCTIONS = {
    1: (lambda x: x**3 - x - 2, "x³ - x - 2", 1.0, 2.0),
    2: (lambda x: math.cos(x) - x, "cos(x) - x", 0.0, 1.0),
    3: (lambda x: math.exp(-x) - x, "e⁻ˣ - x", 0.0, 1.0)
}

# --- Main Program ---
def main():
    print(f"{HEADER}{BOLD}=================================================================== {ENDC}")
    print(f"{'SELAMAT DATANG DI PROGRAM BISECTION INTERAKTIF':^67}")
    print("="*67)
    
    print("\nPilih fungsi yang ingin dicari akarnya:")
    for key, val in FUNCTIONS.items():
        print(f"  {BLUE}{key}. f(x) = {val[1]}{ENDC}")
    
    try:
        choice = int(input(f"\n{BLUE}▶ Masukkan nomor fungsi (1, 2, atau 3): {ENDC}"))
        
        if choice not in FUNCTIONS:
            print(f"\n{RED}Pilihan tidak valid. Program akan dihentikan.{ENDC}")
            return

        selected_func, func_name, a_val, b_val = FUNCTIONS[choice]
        
        print(f"\n{BOLD}MENGHITUNG AKAR UNTUK f(x) = {func_name} di interval [{a_val}, {b_val}]...{ENDC}")
        
        root, c_values, f_c_values = bisection(selected_func, a_val, b_val)

        # Plotting the function and bisection points
        if root is not None:
            plt.figure(figsize=(10, 6))
            x_range = [a_val + i * (b_val - a_val) / 100 for i in range(101)]
            y_range = [selected_func(x) for x in x_range]

            plt.plot(x_range, y_range, label=f'f(x) = {func_name}')
            plt.plot(c_values, f_c_values, 'ro', label='Titik Iterasi')
            plt.axhline(0, color='black', linewidth=0.5)
            plt.axvline(root, color='gray', linestyle='--', label=f'Akar (x = {root:.6f})')
            
            plt.title(f"Visualisasi Metode Bisection untuk f(x) = {func_name}")
            plt.xlabel("x")
            plt.ylabel("f(x)")
            plt.legend()
            plt.grid(True)
            plt.show()

        # Display final results
        print(f"\n{HEADER}{BOLD}{'-' * 18} HASIL AKHIR {'-' * 18}{ENDC}".center(85))
        if root is not None:
            print(f"{BLUE}  Fungsi                 :{ENDC} {func_name}")
            print(f"{BLUE}  Perkiraan Akar         :{ENDC} {GREEN}{BOLD}{root:.6f}{ENDC}")
            print(f"{BLUE}  Nilai Fungsi pada Akar :{ENDC} {GREEN}{selected_func(root):.6f}{ENDC}")
        print("="*85)

    except ValueError:
        print(f"\n{RED}Input tidak valid. Harap masukkan angka.{ENDC}")

if __name__ == "__main__":
    main()