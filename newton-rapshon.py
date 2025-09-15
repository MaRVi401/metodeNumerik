import sympy as sp
from rich.console import Console
from rich.table import Table

def newton_raphson(f, x0, tol=1e-6, max_iter=100):
    console = Console()
    
    console.print("[bold cyan]=================================================[/bold cyan]")
    console.print("[bold cyan]   METODE NEWTON-RAPHSON UNTUK MENCARI AKAR[/bold cyan]")
    console.print("[bold cyan]=================================================[/bold cyan]")
    console.print(f"Fungsi: [yellow]f(x) = {f.__name__}(x)[/yellow]")
    console.print(f"Tebakan Awal (x0): [yellow]{x0}[/yellow]")
    console.print(f"Toleransi (tol): [yellow]{tol}[/yellow]")
    console.print("-" * 50)
    
    x = x0
    
    try:
        symbol_x = sp.symbols('x')
        df = sp.diff(f(symbol_x), symbol_x)
        f_prime = sp.lambdify(symbol_x, df, 'numpy')
    except Exception as e:
        console.print(f"[red]Error: Terjadi masalah saat menghitung turunan fungsi. Pastikan fungsi Anda valid.\nDetail: {e}[/red]")
        return None

    table = Table(title="Proses Iterasi")
    table.add_column("Iterasi", style="bold", justify="center")
    table.add_column("x_i", style="magenta", justify="center")
    table.add_column("f(x_i)", style="green", justify="center")
    table.add_column("f'(x_i)", style="yellow", justify="center")

    for i in range(max_iter):
        fx = f(x)
        dfx = f_prime(x)
        
        if abs(dfx) < 1e-10:
            console.print("\n[bold red]!!! Peringatan: Turunan mendekati nol. Metode gagal konvergen.[/bold red]")
            return None
        
        x_new = x - fx / dfx
        
        table.add_row(
            str(i),
            f"{x:.6f}",
            f"{fx:.6f}",
            f"{dfx:.6f}"
        )
        
        if abs(x_new - x) < tol:
            console.print(table)
            console.print("\n[bold green]✅ Konvergensi tercapai pada iterasi ke-" + str(i+1) + ".[/bold green]")
            return x_new
        
        x = x_new
    
    console.print(table)
    console.print("\n[bold red]❌ Jumlah iterasi maksimum tercapai. Metode tidak konvergen dalam batas yang ditentukan.[/bold red]")
    return x

def my_function(x):
    return x**2 - 2

tebakan_awal = 1.0

akar = newton_raphson(my_function, tebakan_awal)

if akar is not None:
    console = Console()
    console.print("\n[bold cyan]=================================================[/bold cyan]")
    console.print("[bold cyan]              RINGKASAN HASIL[/bold cyan]")
    console.print("[bold cyan]=================================================[/bold cyan]")
    console.print(f"Akar yang ditemukan:  [bold magenta]{akar:.6f}[/bold magenta]")
    console.print(f"Nilai f(akar):        [bold green]{my_function(akar):.6e}[/bold green]")
    console.print("[bold cyan]=================================================[/bold cyan]")