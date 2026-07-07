from dao.dao import DAO
from models.pessoa import Pessoa

class PessoaDAO(DAO):
    def __init__(self):
        super().__init__("pessoas.pkl")

    def add(self, pessoa):
        if not isinstance(pessoa, Pessoa):
            raise TypeError("Objeto inválido")
        super().add(pessoa.cpf, pessoa)

    def update(self, pessoa):
        if not isinstance(pessoa, Pessoa):
            raise TypeError("Objeto inválido")
        super().update(pessoa.cpf, pessoa)
    
    def remove(self, cpf):
        super().remove(cpf)
    
    def get(self, cpf):
        return super().get(cpf)
    
    def get_all(self):
        return super().get_all()