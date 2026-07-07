from dao.dao import DAO
from models.clinica import Clinica

class ClinicaDAO(DAO):
    def __init__(self):
        super().__init__("clinicas.pkl")

    def add(self, clinica):
        if not isinstance(clinica, Clinica):
            raise TypeError("Objeto inválido")
        super().add(clinica.id, clinica)

    def update(self, clinica):
        if not isinstance(clinica, Clinica):
            raise TypeError("Objeto inválido")
        super().update(clinica.id, clinica)
    
    def remove(self, id):
        super().remove(id)
    
    def get(self, id):
        return super().get(id)
    
    def get_all(self):
        return super().get_all()
