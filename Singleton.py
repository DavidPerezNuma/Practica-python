import threading

class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()  # Para manejo en entornos multihilo

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                print("Estableciendo nueva conexión a la base de datos...")
                cls._instance = super(DatabaseConnection, cls).__new__(cls)
                cls._instance._connected = False
            return cls._instance

    def connect(self):
        if not self._connected:
            print("Conectado a la base de datos.")
            self._connected = True
        else:
            print("Ya estás conectado.")

    def disconnect(self):
        if self._connected:
            print("Desconectado de la base de datos.")
            self._connected = False
        else:
            print("No estás conectado.")

# --- Pruebas del Singleton ---
if __name__ == "__main__":
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()

    db1.connect()
    db2.connect()

    print(f"¿db1 es db2?: {db1 is db2}")  # True, misma instancia

    db1.disconnect()
