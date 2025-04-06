import threading

# ========================================
# Patrón Singleton: Conexión a una base de datos
# Esta clase garantiza que solo exista una única
# instancia de conexión a la base de datos.
# ========================================
class DatabaseConnection:
    _instance = None                   # Atributo para guardar la única instancia
    _lock = threading.Lock()          # Lock para evitar condiciones de carrera en hilos

    # Método especial para controlar la creación de la instancia
    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                # Si no existe una instancia, se crea
                print("Estableciendo nueva conexión a la base de datos...")
                cls._instance = super(DatabaseConnection, cls).__new__(cls)
                cls._instance._connected = False  # Estado de conexión inicial
            return cls._instance

    # Método para simular la conexión a la base de datos
    def connect(self):
        if not self._connected:
            print("Conectado a la base de datos.")
            self._connected = True
        else:
            print("Ya estás conectado.")

    # Método para simular la desconexión
    def disconnect(self):
        if self._connected:
            print("Desconectado de la base de datos.")
            self._connected = False
        else:
            print("No estás conectado.")

# ========================================
# Prueba del patrón Singleton
# Se crean dos objetos pero ambos apuntan a
# la misma instancia de conexión
# ========================================
if __name__ == "__main__":
    db1 = DatabaseConnection()  # Primera instancia
    db2 = DatabaseConnection()  # Segunda instancia (referencia a la misma)

    db1.connect()               # Se realiza la conexión
    db2.connect()               # Ya está conectado (misma instancia)

    # Verificamos que ambas variables apuntan al mismo objeto
    print(f"¿db1 es db2?: {db1 is db2}")  # Debería imprimir True

    db1.disconnect()           # Se desconecta desde db1
