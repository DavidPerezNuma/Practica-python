# ========================================
# Patrón Adapter:
# Adaptador para traducción entre idiomas
# ========================================

# Clase existente que tiene un método diferente al esperado
class EnglishTranslator:
    def translate_word(self, word):
        translations = {
            "hola": "hello",
            "adiós": "goodbye",
            "gracias": "thank you"
        }
        return translations.get(word.lower(), "Translation not found")

# Interfaz esperada por el cliente
class TranslatorInterface:
    def traducir(self, palabra):
        pass

# Adaptador que convierte la interfaz existente a la que el cliente espera
class TranslatorAdapter(TranslatorInterface):
    def __init__(self, english_translator):
        self.english_translator = english_translator

    def traducir(self, palabra):
        return self.english_translator.translate_word(palabra)

# Cliente que usa el adaptador
def cliente(adapter: TranslatorInterface, palabra: str):
    print(f"Traducción de '{palabra}': {adapter.traducir(palabra)}")

# ----------------------------------------
# Pruebas
# ----------------------------------------

if __name__ == "__main__":
    english_translator = EnglishTranslator()
    adapter = TranslatorAdapter(english_translator)

    cliente(adapter, "hola")
    cliente(adapter, "adiós")
    cliente(adapter, "gracias")
    cliente(adapter, "perro")  # palabra no encontrada
