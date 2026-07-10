from dao.dao import DAO
from models.tipo_atendimento import TipoAtendimento

class TipoAtendimentoDAO(DAO):
    def __init__(self):
        super().__init__("tipos_atendimento.pkl")

    def add(self, tipo_atendimento):
        if not isinstance(tipo_atendimento, TipoAtendimento):
            raise TypeError("Objeto inválido")
        super().add(tipo_atendimento.id, tipo_atendimento)

    def update(self, tipo_atendimento):
        if not isinstance(tipo_atendimento, TipoAtendimento):
            raise TypeError("Objeto inválido")
        super().update(tipo_atendimento.id, tipo_atendimento)
    
    def remove(self, id):
        super().remove(id)
    
    def get(self, id):
        return super().get(id)
    
    def get_all(self):
        return super().get_all()
