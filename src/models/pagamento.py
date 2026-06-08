"""Módulo de modelo de pagamento. Define a classe Pagamento,
representando um pagamento realizado por um paciente em um atendimento,
com seus atributos e métodos relacionados."""

from decimal import Decimal
from datetime import datetime

from models.pessoa import Pessoa
from models.atendimento import Atendimento
from models.metodo_pagamento import MetodoPagamento
from models.papel_paciente import PapelPaciente


class Pagamento:
    """Representa um pagamento realizado por um paciente em um atendimento,
    contendo informações como data, valor, paciente, atendimento associado
    e método de pagamento."""

    def __init__(
        self,
        data: datetime,
        valor: Decimal,
        paciente: Pessoa,
        atendimento: Atendimento,
        metodo_pagamento: MetodoPagamento,
    ):
        self.__data = data
        self.__valor = valor
        self.__paciente = paciente
        self.__atendimento = atendimento
        self.__metodo_pagamento = metodo_pagamento

        # Registra o snapshot do saldo devedor no momento do pagamento
        self.__valor_restante = atendimento.valor_restante - self.valor

        if data.date() > atendimento.ts_inicio.date():
            raise ValueError(
                "A data do pagamento não pode ser posterior à data do atendimento."
            )

    @property
    def data(self) -> datetime:
        return self.__data

    @data.setter
    def data(self, data: datetime):
        if not isinstance(data, datetime):
            raise ValueError("A data do pagamento deve ser uma instância de datetime")
        self.__data = data

    @property
    def valor(self) -> Decimal:
        return self.__valor

    @valor.setter
    def valor(self, valor: Decimal):
        if not isinstance(valor, Decimal):
            raise ValueError("O valor do pagamento deve ser uma instância de Decimal")
        self.__valor = valor

    @property
    def paciente(self) -> Pessoa:
        return self.__paciente

    @paciente.setter
    def paciente(self, paciente: Pessoa):
        if not isinstance(paciente, Pessoa):
            raise ValueError("O paciente deve ser uma instância de Pessoa.")
        if not any(isinstance(papel, PapelPaciente) for papel in paciente.papeis):
            raise ValueError("O paciente deve ter o papel de paciente.")
        self.__paciente = paciente

    @property
    def atendimento(self) -> Atendimento:
        return self.__atendimento

    @atendimento.setter
    def atendimento(self, atendimento: Atendimento):
        if not isinstance(atendimento, Atendimento):
            raise ValueError("O atendimento deve ser uma instância de Atendimento.")
        self.__atendimento = atendimento

    @property
    def metodo_pagamento(self) -> MetodoPagamento:
        return self.__metodo_pagamento

    @metodo_pagamento.setter
    def metodo_pagamento(self, metodo_pagamento: MetodoPagamento):
        if not isinstance(metodo_pagamento, MetodoPagamento):
            raise ValueError(
                "O método de pagamento deve ser uma instância de MetodoPagamento."
            )
        self.__metodo_pagamento = metodo_pagamento

    @property
    def valor_restante(self) -> Decimal:
        return self.__valor_restante

    def __str__(self):
        metodo = self.metodo_pagamento.__class__.__name__.replace('Metodo', '')
        return f"Pagamento de R$ {self.valor} em {self.data.strftime('%d/%m/%Y')} (Via {metodo})"
