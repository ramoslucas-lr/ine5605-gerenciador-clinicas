from dao.procedimento_dao import ProcedimentoDAO
from view.tela_procedimento import TelaProcedimento


class ControladorProcedimento:

    def __init__(self):
        self.__dao = ProcedimentoDAO()
        self.__tela = TelaProcedimento()

    def buscar_procedimento(self, id):
        return self.__dao.get(id)
    
    @property
    def procedimentos(self):
        return self.__dao.get_all()
    
    def incluir_procedimento(self):

        dados = self.__tela.pega_dados_procedimento()

        if dados is None:
            return

        procedimentos = self.__dao.get_all()

        if len(procedimentos) == 0:
            prox_id = 1
        else:
            prox_id = max(procedimento.id for procedimento in procedimentos) + 1

        procedimento = Procedimento(
            prox_id,
            dados["descricao"],
            Decimal(dados["valor"]),
            dados["profissional"]
        )

        self.__dao.add(procedimento)

        self.__tela.show_message(
            "Procedimento cadastrado com sucesso."
        )

    def excluir_procedimento(self):

        id = self.__tela.seleciona_procedimento()

        procedimento = self.buscar_procedimento(id)

        if procedimento is not None:

            self.__dao.remove(id)

            self.__tela.show_message(
                "Procedimento excluído com sucesso."
            )

        else:

            self.__tela.show_message(
                "Procedimento não encontrado."
            )

    def alterar_procedimento(self):

        id = self.__tela.seleciona_procedimento()

        procedimento = self.buscar_procedimento(id)

        if procedimento is not None:

            dados = self.__tela.pega_dados_procedimento()

            procedimento.descricao = dados["descricao"]
            procedimento.valor = Decimal(dados["valor"])

            self.__dao.add(procedimento)

            self.__tela.show_message(
                "Procedimento alterado com sucesso."
            )

        else:

            self.__tela.show_message(
                "Procedimento não encontrado."
            )