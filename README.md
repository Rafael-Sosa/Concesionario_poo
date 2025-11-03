# 🚗 Concesionario POO en Python

**Autor:** Rafael Andrés Molina Sosa  
**Fecha:** 3 de noviembre de 2025  

## Descripción

Este proyecto implementa un **mini sistema de concesionario** aplicando los **4 pilares de la Programación Orientada a Objetos (POO)** en Python:

- **Encapsulamiento:** todos los atributos están protegidos con un solo guion bajo (`_`).
- **Herencia:** las clases `Automovil` y `Moto` heredan de la clase abstracta `Vehiculo`.
- **Abstracción:** `Vehiculo` define un método abstracto `impuesto()` que debe implementarse en las subclases.
- **Polimorfismo:** se usa una lista de tipo `Vehiculo` para recorrer distintos objetos (`Automovil` y `Moto`).

## 🧩 Módulos del proyecto

| Archivo | Descripción |
|----------|-------------|
| `vehiculo.py` | Clase abstracta `Vehiculo` (atributos comunes, métodos base). |
| `automovil.py` | Subclase `Automovil` con atributo propio `_puertas` e implementación de `impuesto()`. |
| `moto.py` | Subclase `Moto` con atributo propio `_cc` e implementación de `impuesto()`. |
| `main.py` | Script principal que crea vehículos, los imprime y calcula el total del inventario. |

---

## ⚙️ Cómo ejecutar el programa

### 1️⃣ Clonar el repositorio en GitHub

Abre tu terminal y ejecuta:

```bash
git clone https://github.com/Rafel-Sosa/Concesionario_poo.git
```

### 2️⃣ Descargando el ZIP:

1. En el repositorio, haz clic en el botón verde “Code” → “Download ZIP”

2. Extrae el archivo ZIP.

3. Abre una terminal dentro de la carpeta extraída.

Ejecuta:

```bash
python main.py
```

4. También puedes abrir la carpeta y ejecutar el programa desde Visual Studio Code u otro editor de código de tú preferencia. 
