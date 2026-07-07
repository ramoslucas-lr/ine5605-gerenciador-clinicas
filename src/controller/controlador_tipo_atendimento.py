from decimal import InvalidOperation

from view.tela_tipo_atendimento import TelaTipoAtendimento
from models.tipo_atendimento import TipoAtendimento
from dao.tipo_atendimento_dao import TipoAtendimentoDAO


class ControladorTipoAtendimento:
    def __init__(self, controlador_sistema):
        self.__tipo_atendimento_dao = TipoAtendimentoDAO()

        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaTipoAtendimento()

    def buscar_tipo_atendimento(self, id_tipo: int):
        return self.__tipo_atendimento_dao.get(id_tipo)

    def incluir_tipo_atendimento(self):
        try:
            dados = self.__tela.pega_dados_tipo_atendimento()

            id_tipo = int(dados["id"])

            if self.buscar_tipo_atendimento(id_tipo) is not None:
                self.__tela.mostra_mensagem(
                    "Já existe um tipo de atendimento com esse ID."
                )
                return

            tipo = TipoAtendimento(
                id_tipo,
                dados["nome"],
                dados["codigo"],
                dados["descricao"]
            )

            self.__tipo_atendimento_dao.add(tipo)

            self.__tela.mostra_mensagem(
                "Tipo de atendimento cadastrado com sucesso!"
            )

        except (ValueError, InvalidOperation):
            self.__tela.mostra_mensagem(
                "Dados inválidos."
            )

    def listar_tipos_atendimento(self):
        self.__tela.listar_tipos_atendimento(
            list(self.__tipo_atendimento_dao.get_all())
        )

    def retorna_tela(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_tipo_atendimento,
            2: self.listar_tipos_atendimento,
            0: self.retorna_tela
        }

        while True:
            opcao = self.__tela.mostrar_opcoes()

            if opcao in lista_opcoes:
                lista_opcoes[opcao]()

                if opcao == 0:
                    break
            else:
                self.__tela.mostra_mensagem(
                    "Opção inválida."
                )