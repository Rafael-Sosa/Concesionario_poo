from vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, marca: str, modelo: str, precio_base: float, puertas: int):
        super().__init__(marca, modelo, precio_base)
        self._puertas = puertas

    def impuesto(self) -> float:
        """8% del precio base; si tiene 5 puertas, se resta 1%."""
        imp = self.precio_base * 0.08
        desc = self.precio_base * 0.01 if self._puertas == 5 else 0
        return imp - desc

    def ficha(self) -> str:
        """Incluye información adicional de las puertas."""
        return f"Automóvil | {super().ficha()} | {self._puertas} puertas"
