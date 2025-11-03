from vehiculo import Vehiculo

class Moto(Vehiculo):
    def __init__(self, marca: str, modelo: str, precio_base: float, cc: int):
        super().__init__(marca, modelo, precio_base)
        self._cc = cc

    def impuesto(self) -> float:
        """5% si ≤ 250cc, 9% si > 250cc."""
        tasa = 0.05 if self._cc <= 250 else 0.09
        return self.precio_base * tasa

    def ficha(self) -> str:
        """Incluye información adicional del cilindraje."""
        return f"Moto | {super().ficha()} | {self._cc}cc"
