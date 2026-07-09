from dao.dao import DAO
from models.procedimento import Procedimento


class ProcedimentoDAO(DAO):

    def __init__(self):
        super().__init__("procedimentos.pkl")

    def add(self, procedimento):

        
        if isinstance(procedimento, Procedimento):
            super().add(procedimento.id, procedimento)