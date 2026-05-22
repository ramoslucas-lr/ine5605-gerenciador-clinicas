"""Módulo que define a classe Pessoa, representando uma pessoa que
pode ter os papéis de paciente e/ou profissional."""

from datetime import datetime

from papel import Papel
from papel_paciente import PapelPaciente
from papel_profissional import PapelProfissional


class Pessoa:
    """Representa uma pessoa, que pode ter os papéis de paciente e/ou profissional."""

    def __init__(
        self, nome: str, celular: str, cpf: str, data_nascimento: datetime
    ) -> None:
        self.nome = nome
        self.celular = celular
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.__papeis = []

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        if not isinstance(nome, str):
            raise ValueError("O nome deve ser uma instância de str.")
        self.__nome = nome

    @property
    def celular(self) -> str:
        return self.__celular

    @celular.setter
    def celular(self, celular: str) -> None:
        if not isinstance(celular, str):
            raise ValueError("O celular deve ser uma instância de str.")
        self.__celular = celular

    @property
    def cpf(self) -> str:
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str) -> None:
        if not isinstance(cpf, str):
            raise ValueError("O CPF deve ser uma instância de str.")
        self.__cpf = cpf

    @property
    def data_nascimento(self) -> datetime:
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: datetime) -> None:
        if not isinstance(data_nascimento, datetime):
            raise ValueError("A data de nascimento deve ser uma instância de datetime.")
        self.__data_nascimento = data_nascimento

    @property
    def papeis(self) -> list[Papel]:
        return self.__papeis

    def adicionar_papel_paciente(self) -> None:
        """Adiciona o papel de paciente à pessoa.

        Raises:
            ValueError: Se a pessoa já tiver o papel de paciente.
        """
        if any(isinstance(papel, PapelPaciente) for papel in self.__papeis):
            raise ValueError("A pessoa já tem o papel de paciente.")

        papel_paciente = PapelPaciente()
        self.__papeis.append(papel_paciente)

    def adicionar_papel_profissional(
        self, reg_profissional: str, especialidade: str
    ) -> None:
        """Adiciona o papel de profissional à pessoa.

        Args:
            reg_profissional (str): O registro profissional do profissional.
            especialidade (str): A especialidade do profissional.

        Raises:
            ValueError: Se a pessoa já tiver o papel de profissional.
        """
        if any(isinstance(papel, PapelProfissional) for papel in self.__papeis):
            raise ValueError("A pessoa já tem o papel de profissional.")

        papel_profissional = PapelProfissional(reg_profissional, especialidade)
        self.__papeis.append(papel_profissional)

    def remover_papel(self, papel: Papel):
        """Remove um papel da pessoa."""
        if papel in self.__papeis:
            self.__papeis.remove(papel)
