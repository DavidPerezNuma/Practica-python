# ========================================
# Patrón Abstract Factory:
# Fábrica para crear instituciones públicas y privadas
# ========================================

from abc import ABC, abstractmethod

# ----------------------------------------
# Interfaces abstractas
# ----------------------------------------

# Producto abstracto: Colegio
class School(ABC):
    @abstractmethod
    def describe(self):
        pass

# Producto abstracto: Hospital
class Hospital(ABC):
    @abstractmethod
    def describe(self):
        pass

# Fábrica abstracta
class InstitutionFactory(ABC):
    @abstractmethod
    def create_school(self) -> School:
        pass

    @abstractmethod
    def create_hospital(self) -> Hospital:
        pass

# ----------------------------------------
# Implementaciones públicas
# ----------------------------------------

class PublicSchool(School):
    def describe(self):
        return "Soy un colegio público financiado por el estado."

class PublicHospital(Hospital):
    def describe(self):
        return "Soy un hospital público de atención gratuita."

class PublicInstitutionFactory(InstitutionFactory):
    def create_school(self) -> School:
        return PublicSchool()

    def create_hospital(self) -> Hospital:
        return PublicHospital()

# ----------------------------------------
# Implementaciones privadas
# ----------------------------------------

class PrivateSchool(School):
    def describe(self):
        return "Soy un colegio privado financiado por mensualidades."

class PrivateHospital(Hospital):
    def describe(self):
        return "Soy un hospital privado con atención especializada."

class PrivateInstitutionFactory(InstitutionFactory):
    def create_school(self) -> School:
        return PrivateSchool()

    def create_hospital(self) -> Hospital:
        return PrivateHospital()

# ----------------------------------------
# Cliente que utiliza la fábrica
# ----------------------------------------

def describe_institutions(factory: InstitutionFactory):
    school = factory.create_school()
    hospital = factory.create_hospital()
    print(school.describe())
    print(hospital.describe())

# ----------------------------------------
# Pruebas
# ----------------------------------------

if __name__ == "__main__":
    print("== Instituciones Públicas ==")
    describe_institutions(PublicInstitutionFactory())

    print("\n== Instituciones Privadas ==")
    describe_institutions(PrivateInstitutionFactory())
