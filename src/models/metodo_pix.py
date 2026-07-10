from models.metodo_pagamento import MetodoPagamento


class MetodoPix(MetodoPagamento):

    def __init__(self, chave: str, tipo_chave: str):
        super().__init__()
        self.__chave = chave
        self.__tipo_chave = tipo_chave

    @property
    def chave(self):
        return self.__chave

    @chave.setter
    def chave(self, chave):
        self.__chave = chave

    @property
    def tipo_chave(self):
        return self.__tipo_chave

    @tipo_chave.setter
    def tipo_chave(self, tipo_chave):
        self.__tipo_chave = tipo_chave
