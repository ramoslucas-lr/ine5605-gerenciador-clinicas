from dao.dao import DAO
from models.atendimento import Atendimento


class AtendimentoDAO(DAO):

    def __init__(self):
        super().__init__("atendimentos.pkl")

    def add(self, atendimento):

        if isinstance(atendimento, Atendimento):
            super().add(atendimento.id, atendimento)