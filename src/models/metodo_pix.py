from metodo_pagamento import MetodoPagamento


class MetodoPix(MetodoPagamento):

    def __init__(self, cpf_pagador: str):
        super().__init__()

        self.__cpf_pagador = cpf_pagador

    @property
    def cpf_pagador(self):
        return self.__cpf_pagador

    @cpf_pagador.setter
    def cpf_pagador(self, cpf_pagador):
        self.__cpf_pagador = cpf_pagador