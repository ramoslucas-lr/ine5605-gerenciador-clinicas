"""Módulo contendo a entidade principal de Atendimento e suas regras de negócio."""

from datetime import datetime
from decimal import Decimal

from pessoa import Pessoa
from clinica import Clinica
from pagamento import Pagamento
from procedimento import Procedimento
from tipo_atendimento import TipoAtendimento
from papel_paciente import PapelPaciente
from papel_profissional import PapelProfissional


class Atendimento:
    """Registro central de uma consulta ou evento na clínica.

    Esta classe atua como o coração do sistema, cruzando as entidades envolvidas
    (Paciente, Profissional e Clínica) e gerenciando tanto a linha do tempo da
    consulta quanto a consolidação financeira (procedimentos e pagamentos).
    """

    def __init__(
        self,
        ts_inicio: datetime,
        ts_fim: datetime,
        valor: Decimal,
        tipo_atendimento: TipoAtendimento,
        paciente: Pessoa,
        profissional: Pessoa,
        clinica: Clinica,
    ):
        self.ts_inicio = ts_inicio
        self.ts_fim = ts_fim
        self.valor = valor
        self.tipo_atendimento = tipo_atendimento
        self.paciente = paciente
        self.profissional = profissional
        self.clinica = clinica
        self.__procedimentos = []
        self.__pagamentos = []

    @property
    def ts_inicio(self) -> datetime:
        return self.__ts_inicio

    @ts_inicio.setter
    def ts_inicio(self, ts_inicio: datetime):
        if not isinstance(ts_inicio, datetime):
            raise ValueError(
                "A data e hora de início do atendimento "
                "deve ser uma instância de datetime"
            )
        self.__ts_inicio = ts_inicio

    @property
    def ts_fim(self) -> datetime:
        return self.__ts_fim

    @ts_fim.setter
    def ts_fim(self, ts_fim: datetime):
        if not isinstance(ts_fim, datetime):
            raise ValueError(
                "A data e hora de fim do atendimento deve ser uma instância de datetime"
            )
        self.__ts_fim = ts_fim

    @property
    def valor(self) -> Decimal:
        return self.__valor

    @valor.setter
    def valor(self, valor: Decimal):
        if not isinstance(valor, Decimal):
            raise ValueError("O valor do atendimento deve ser uma instância de Decimal")
        self.__valor = valor

    @property
    def tipo_atendimento(self) -> TipoAtendimento:
        return self.__tipo_atendimento

    @tipo_atendimento.setter
    def tipo_atendimento(self, tipo_atendimento: TipoAtendimento):
        if not isinstance(tipo_atendimento, TipoAtendimento):
            raise ValueError(
                "O tipo de atendimento deve ser uma instância de TipoAtendimento"
            )
        self.__tipo_atendimento = tipo_atendimento

    @property
    def paciente(self) -> Pessoa:
        return self.__paciente

    @paciente.setter
    def paciente(self, paciente: Pessoa):
        if not isinstance(paciente, Pessoa):
            raise ValueError("O paciente deve ser uma instância de Pessoa.")
        if not any(isinstance(papel, PapelPaciente) for papel in paciente.papeis):
            raise ValueError("O paciente deve ter o papel de paciente.")

        # Cálculo da idade do paciente no momento do atendimento
        data_consulta = self.ts_inicio.date()
        data_nascimento = paciente.data_nascimento.date()

        # O cálculo de idade considera se o paciente já
        # fez aniversário no ano da consulta
        idade = (
            data_consulta.year
            - data_nascimento.year
            - (
                (data_consulta.month, data_consulta.day)
                < (data_nascimento.month, data_nascimento.day)
            )
        )

        if idade < 18:
            raise ValueError(
                "O paciente deve ser maior de 18 anos para realizar um atendimento."
            )

        self.__paciente = paciente

    @property
    def profissional(self) -> Pessoa:
        return self.__profissional

    @profissional.setter
    def profissional(self, profissional: Pessoa):
        if not isinstance(profissional, Pessoa):
            raise ValueError("O profissional deve ser uma instância de Pessoa.")
        if not any(
            isinstance(papel, PapelProfissional) for papel in profissional.papeis
        ):
            raise ValueError("O profissional deve ter o papel de profissional.")
        self.__profissional = profissional

    @property
    def clinica(self) -> Clinica:
        return self.__clinica

    @clinica.setter
    def clinica(self, clinica: Clinica):
        if not isinstance(clinica, Clinica):
            raise ValueError("A clínica deve ser uma instância de Clinica")
        self.__clinica = clinica

    @property
    def procedimentos(self) -> list[Procedimento]:
        return self.__procedimentos

    @property
    def pagamentos(self) -> list[Pagamento]:
        return self.__pagamentos

    @property
    def valor_pago(self) -> Decimal:
        return sum(pagamento.valor for pagamento in self.__pagamentos)

    @property
    def valor_total(self) -> Decimal:
        valor_procedimentos = sum(
            procedimento.valor for procedimento in self.__procedimentos
        )
        return self.__valor + valor_procedimentos

    @property
    def valor_restante(self) -> Decimal:
        return self.valor_total - self.valor_pago

    def adiciona_procedimento(
        self, descricao: str, valor: Decimal, profissional: Pessoa
    ) -> None:
        """Adiciona um procedimento ao atendimento.

        Args:
            descricao (str): A descrição do procedimento.
            valor (Decimal): O valor do procedimento.
            profissional (Pessoa): O profissional que realizará o procedimento.
        """
        procedimento = Procedimento(descricao, valor, profissional)
        self.__procedimentos.append(procedimento)

    def adiciona_pagamento(self, pagamento: Pagamento) -> None:
        """Adiciona um pagamento ao atendimento.

        Args:
            pagamento (Pagamento): O pagamento a ser adicionado.

        Raises:
            ValueError: Se o pagamento não for uma instância de Pagamento.
        """
        if not isinstance(pagamento, Pagamento):
            raise ValueError("O pagamento deve ser uma instância de Pagamento.")
        self.__pagamentos.append(pagamento)
