from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca: str, modelo: str, precio_base: float):
        # Encapsulamiento con atributos protegidos
        self._marca = marca
        self._modelo = modelo
        self._precio_base = max(1, precio_base)  # validación simple

    # Propiedades de solo lectura
    @property
    def marca(self):
        return self._marca

    @property
    def modelo(self):
        return self._modelo

    @property
    def precio_base(self):
        return self._precio_base

    @abstractmethod
    def impuesto(self) -> float:
        """Método abstracto que será implementado por las clases hijas."""
        pass

    def precio_final(self) -> float:
        """Calcula el precio final sumando el impuesto."""
        return self._precio_base + self.impuesto()

    def ficha(self) -> str:
        """Devuelve una ficha simple del vehículo."""
        return f"{self._marca} {self._modelo} (${self._precio_base:.2f})"

    def __str__(self) -> str:
        """Representación legible del vehículo."""
        return f"{self.ficha()} | Final: ${self.precio_final():.2f}"
