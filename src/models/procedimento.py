"""Módulo de modelo de procedimento. Define a classe Procedimento, representando
um procedimento realizado em um atendimento, com seus atributos e métodos relacionados.
"""

from decimal import Decimal

from pessoa import Pessoa
from papel_profissional import PapelProfissional


class Procedimento:
    """Representa um procedimento realizado em um atendimento, contendo informações
    como descrição, valor e o profissional responsável pelo procedimento."""

    def __init__(self, descricao: str, valor: Decimal, profissional: Pessoa):
        self.__descricao = descricao
        self.__valor = valor
        self.__profissional = profissional

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        if isinstance(descricao, str):
            self.__descricao = descricao
        else:
            raise ValueError("A descrição do procedimento deve ser uma string")

    @property
    def valor(self) -> Decimal:
        return self.__valor

    @valor.setter
    def valor(self, valor: Decimal):
        if isinstance(valor, Decimal):
            self.__valor = valor
        else:
            raise ValueError(
                "O valor do procedimento deve ser uma instância de Decimal"
            )

    @property
    def profissional(self) -> Pessoa:
        return self.__profissional

    @profissional.setter
    def profissional(self, profissional: Pessoa):
        if not isinstance(profissional, Pessoa):
            raise ValueError("O profissional deve ser uma instância da classe Pessoa")
        if not any(
            isinstance(papel, PapelProfissional) for papel in profissional.papeis
        ):
            raise ValueError("O profissional deve ter o papel de profissional.")
        self.__profissional = profissional
