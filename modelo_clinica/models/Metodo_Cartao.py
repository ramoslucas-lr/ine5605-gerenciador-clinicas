from metodo_pagamento import MetodoPagamento


class MetodoCartao(MetodoPagamento):

    def __init__(self, num_cartao: str, bandeira: str):
        super().__init__()
        self.__num_cartao = num_cartao
        self.__bandeira = bandeira

    @property
    def num_cartao(self):
        return self.__num_cartao

    @num_cartao.setter
    def num_cartao(self, num_cartao):
        self.__num_cartao = num_cartao

    @property
    def bandeira(self):
        return self.__bandeira

    @bandeira.setter
    def bandeira(self, bandeira):
        self.__bandeira = bandeira