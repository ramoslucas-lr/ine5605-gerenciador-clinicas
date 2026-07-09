from dao.dao import DAO
from models.pagamento import Pagamento


class PagamentoDAO(DAO):

    def __init__(self):
        super().__init__("pagamentos.pkl")

    def add(self, pagamento):

        if isinstance(pagamento, Pagamento):
            super().add(pagamento.id, pagamento)