from automovil import Automovil
from moto import Moto
from tabulate import tabulate  # Librería para imprimir tablas

def main():
    # Lista de vehículos (polimorfismo)
    inventario = [
        Automovil("Toyota", "Yaris", 40000, 5),
        Moto("Ducati", "Hypermotard 950", 18000, 199),
        Automovil("Volkswagen", "Virtus", 23000, 4),
        Moto("BMW", "F 900 XR", 38000, 350)
    ]

    # Crear tabla para mostrar la información
    tabla = []
    total = 0
    for v in inventario:
        tipo = v.__class__.__name__
        ficha = v.ficha()
        precio_final = v.precio_final()
        tabla.append([tipo, ficha, f"${precio_final:,.2f}"])
        total += precio_final

    print("\n=== INVENTARIO DEL CONCESIONARIO ===\n")
    print(tabulate(tabla, headers=["Tipo", "Ficha", "Precio Final"], tablefmt="fancy_grid"))
    print(f"\nValor total del inventario: ${total:,.2f}\n")

if __name__ == "__main__":
    main()
