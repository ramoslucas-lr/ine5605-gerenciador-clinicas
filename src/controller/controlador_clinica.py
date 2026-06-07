from decimal import InvalidOperation

from view.tela_clinica import TelaClinica
from models.clinica import Clinica


class ControladorClinica:

    def __init__(self, controlador_sistema):
        self.__clinicas = {}
        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaClinica()

    def buscar_clinica(self, id_clinica):
        return self.__clinicas.get(id_clinica)

    def incluir_clinica(self):
        try:
            dados = self.__tela.pega_dados_clinica()

            id_clinica = int(dados["id"])

            if id_clinica in self.__clinicas:
                self.__tela.mostra_mensagem(
                    "Clínica já cadastrada."
                )
                return

            clinica = Clinica(
                id_clinica,
                dados["nome"],
                dados["localizacao"],
                dados["descricao"]
            )

            self.__clinicas[id_clinica] = clinica

            self.__tela.mostra_mensagem(
                "Clínica cadastrada com sucesso."
            )

        except (ValueError, InvalidOperation):
            self.__tela.mostra_mensagem(
                "Dados inválidos."
            )

    def listar_clinicas(self):
        self.__tela.listar_clinicas(
            self.__clinicas.values()
        )

    def retorna_tela(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.incluir_clinica,
            2: self.listar_clinicas,
            0: self.retorna_tela
        }

        while True:
            opcao = self.__tela.mostrar_opcoes()

            if opcao in opcoes:
                opcoes[opcao]()

                if opcao == 0:
                    break
            else:
                self.__tela.mostra_mensagem(
                    "Opção inválida."
                )