from dao.dao import DAO
from models.atendimento import Atendimento


class AtendimentoDAO(DAO):

    def __init__(self):
        super().__init__("atendimentos.pkl")

    def add(self, atendimento):
        if isinstance(atendimento, Atendimento):
            super().add(atendimento.id, atendimento)

    def update(self, atendimento):
        if isinstance(atendimento, Atendimento):
            super().update(atendimento.id, atendimento)

    def remove(self, id):
        super().remove(id)

    def get(self, id):
        return super().get(id)

    def get_all(self):
        return super().get_all()