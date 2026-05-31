from models.papel import Papel


class PapelProfissional(Papel):

    def __init__(self, reg_profissional: str, especialidade: str):
        self.__reg_profissional = reg_profissional
        self.__especialidade = especialidade

    @property
    def reg_profissional(self):
        return self.__reg_profissional

    @reg_profissional.setter
    def reg_profissional(self, reg_profissional):
        self.__reg_profissional = reg_profissional

    @property
    def especialidade(self):
        return self.__especialidade

    @especialidade.setter
    def especialidade(self, especialidade):
        self.__especialidade = especialidade
