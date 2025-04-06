# ========================================
# Patrón Decorator:
# Decorador para un plato con adicionales (postre, bebida, porción, etc.)
# ========================================

from abc import ABC, abstractmethod

# ----------------------------------------
# Componente base
# ----------------------------------------
class Plato(ABC):
    @abstractmethod
    def descripcion(self) -> str:
        pass

    @abstractmethod
    def costo(self) -> float:
        pass

# ----------------------------------------
# Componente concreto: Plato base
# ----------------------------------------
class PlatoBase(Plato):
    def descripcion(self) -> str:
        return "Plato principal"

    def costo(self) -> float:
        return 15_000  # Precio en COP

# ----------------------------------------
# Clase Decoradora base
# ----------------------------------------
class Adicional(Plato, ABC):
    def __init__(self, plato: Plato):
        self._plato = plato

# ----------------------------------------
# Decoradores concretos
# ----------------------------------------

class Postre(Adicional):
    def descripcion(self) -> str:
        return self._plato.descripcion() + " + Postre"

    def costo(self) -> float:
        return self._plato.costo() + 5_000

class Bebida(Adicional):
    def descripcion(self) -> str:
        return self._plato.descripcion() + " + Bebida"

    def costo(self) -> float:
        return self._plato.costo() + 3_000

class PorcionExtra(Adicional):
    def descripcion(self) -> str:
        return self._plato.descripcion() + " + Porción extra"

    def costo(self) -> float:
        return self._plato.costo() + 4_000

# ----------------------------------------
# Pruebas del decorador
# ----------------------------------------

if __name__ == "__main__":
    # Crear un plato con postre y bebida
    plato = PlatoBase()
    plato_con_postre = Postre(plato)
    plato_completo = Bebida(plato_con_postre)

    print("Descripción:", plato_completo.descripcion())
    print("Costo total:", f"${plato_completo.costo():,.0f} COP")

    # Otro ejemplo con todos los adicionales
    print("\nOtro pedido:")
    full_combo = PorcionExtra(Bebida(Postre(PlatoBase())))
    print("Descripción:", full_combo.descripcion())
    print("Costo total:", f"${full_combo.costo():,.0f} COP")
