from dao.dao import DAO
from models.procedimento import Procedimento


class ProcedimentoDAO(DAO):

    def __init__(self):
        super().__init__("procedimentos.pkl")

    def add(self, procedimento):
        if isinstance(procedimento, Procedimento):
            super().add(procedimento.id, procedimento)

    def update(self, procedimento):
        if isinstance(procedimento, Procedimento):
            super().update(procedimento.id, procedimento)

    def remove(self, id):
        super().remove(id)

    def get(self, id):
        return super().get(id)

    def get_all(self):
        return super().get_all()