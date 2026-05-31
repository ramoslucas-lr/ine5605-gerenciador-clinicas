"""Módulo que define a classe Clinica, representando uma clínica
médica com seus atributos e métodos relacionados."""

from __future__ import annotations
from datetime import time


class Clinica:
    """Representa uma clínica médica, contendo informações como nome, localização,
    descrição, horário de funcionamento e os atendimentos realizados."""

    def __init__(
        self,
        id: int,
        nome: str,
        localizacao: str,
        descricao: str,
        hora_abertura: time,
        hora_fechamento: time,
    ):
        self.__id = id
        self.__nome = nome
        self.__localizacao = localizacao
        self.__descricao = descricao
        self.__hora_abertura = hora_abertura
        self.__hora_fechamento = hora_fechamento
        self.__atendimentos = []

    @property
    def id(self) -> int:
        return self.__id

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if not isinstance(nome, str):
            raise ValueError("O nome da clínica deve ser uma string")
        self.__nome = nome

    @property
    def localizacao(self) -> str:
        return self.__localizacao

    @localizacao.setter
    def localizacao(self, localizacao: str):
        if not isinstance(localizacao, str):
            raise ValueError("A localização da clínica deve ser uma string")
        self.__localizacao = localizacao

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        if not isinstance(descricao, str):
            raise ValueError("A descrição da clínica deve ser uma string")
        self.__descricao = descricao

    @property
    def atendimentos(self) -> list:
        return self.__atendimentos

    @property
    def hora_abertura(self) -> time:
        return self.__hora_abertura

    @hora_abertura.setter
    def hora_abertura(self, hora_abertura: time):
        if not isinstance(hora_abertura, time):
            raise ValueError(
                "A hora de abertura da clínica deve ser uma instância de datetime.time"
            )
        self.__hora_abertura = hora_abertura

    @property
    def hora_fechamento(self) -> time:
        return self.__hora_fechamento

    @hora_fechamento.setter
    def hora_fechamento(self, hora_fechamento: time):
        if not isinstance(hora_fechamento, time):
            raise ValueError(
                "A hora de fechamento da clínica deve "
                "ser uma instância de datetime.time"
            )
        self.__hora_fechamento = hora_fechamento

    def adicionar_atendimento(self, atendimento):
        """Adiciona um atendimento à clínica, garantindo que o horário do atendimento
        esteja dentro do horário de funcionamento da clínica.

        Args:
            atendimento (Atendimento): O atendimento a ser adicionado.

        Raises:
            ValueError: Se o atendimento não for uma instância de Atendimento ou se
                        o horário do atendimento não estiver dentro do horário de
                        funcionamento da clínica.
        """
        from models.atendimento import Atendimento

        if not isinstance(atendimento, Atendimento):
            raise ValueError(
                "O atendimento deve ser uma instância da classe Atendimento"
            )

        hora_atendimento = atendimento.ts_inicio.time()

        if not (self.hora_abertura <= hora_atendimento <= self.hora_fechamento):
            raise ValueError(
                "O horário do atendimento deve estar dentro do "
                "horário de funcionamento da clínica"
            )

        self.__atendimentos.append(atendimento)
