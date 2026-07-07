from dao.dao import DAO
from models.tipo_atendimento import TipoAtendimento

class TipoAtendimentoDAO(DAO):
    def __init__(self):
        super().__init__("tipos_atendimento.pkl")

    def add(self, tipo_atendimento):
        if not isinstance(tipo_atendimento, TipoAtendimento):
            raise TypeError("Objeto inválido")
        super().add(tipo_atendimento.codigo, tipo_atendimento)

    def update(self, tipo_atendimento):
        if not isinstance(tipo_atendimento, TipoAtendimento):
            raise TypeError("Objeto inválido")
        super().update(tipo_atendimento.codigo, tipo_atendimento)
    
    def remove(self, codigo):
        super().remove(codigo)
    
    def get(self, codigo):
        return super().get(codigo)
    
    def get_all(self):
        return super().get_all()
