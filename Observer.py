# ========================================
# Patrón Observer:
# Sistema de notificación de clima
# ========================================

from abc import ABC, abstractmethod

# ----------------------------------------
# Interfaz del observador
# ----------------------------------------
class Observer(ABC):
    @abstractmethod
    def actualizar(self, temperatura: float, humedad: float):
        pass

# ----------------------------------------
# Interfaz del sujeto (observable)
# ----------------------------------------
class Observable(ABC):
    @abstractmethod
    def agregar_observador(self, observador: Observer):
        pass

    @abstractmethod
    def eliminar_observador(self, observador: Observer):
        pass

    @abstractmethod
    def notificar_observadores(self):
        pass

# ----------------------------------------
# Sujeto concreto: Estación del clima
# ----------------------------------------
class EstacionClima(Observable):
    def __init__(self):
        self._observadores = []
        self._temperatura = 0.0
        self._humedad = 0.0

    def agregar_observador(self, observador: Observer):
        self._observadores.append(observador)

    def eliminar_observador(self, observador: Observer):
        self._observadores.remove(observador)

    def notificar_observadores(self):
        for observador in self._observadores:
            observador.actualizar(self._temperatura, self._humedad)

    # Simula un cambio de clima
    def set_clima(self, temperatura: float, humedad: float):
        print(f"\n📡 Nuevo clima detectado: {temperatura}°C, {humedad}% humedad")
        self._temperatura = temperatura
        self._humedad = humedad
        self.notificar_observadores()

# ----------------------------------------
# Observadores concretos
# ----------------------------------------

class UsuarioAppClima(Observer):
    def __init__(self, nombre):
        self._nombre = nombre

    def actualizar(self, temperatura, humedad):
        print(f"🌤️ {self._nombre} recibió la actualización: {temperatura}°C, {humedad}% humedad")

# ----------------------------------------
# Prueba del patrón Observer
# ----------------------------------------

if __name__ == "__main__":
    estacion = EstacionClima()

    usuario1 = UsuarioAppClima("Carlos")
    usuario2 = UsuarioAppClima("Luisa")
    usuario3 = UsuarioAppClima("Marta")

    estacion.agregar_observador(usuario1)
    estacion.agregar_observador(usuario2)

    # Primer cambio de clima
    estacion.set_clima(25.5, 60)

    # Agregar otro usuario y realizar otro cambio
    estacion.agregar_observador(usuario3)
    estacion.set_clima(28.2, 55)

    # Eliminar un observador
    estacion.eliminar_observador(usuario1)
    estacion.set_clima(22.0, 70)
