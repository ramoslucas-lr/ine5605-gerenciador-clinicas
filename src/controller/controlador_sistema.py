from controller.controlador_atendimento import ControladorAtendimento
from view.tela_sistema import TelaSistema
from controller.controlador_pessoa import ControladorPessoa


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_pessoa = ControladorPessoa(self)
        self.__controlador_atendimento = ControladorAtendimento(self)

    @property
    def controlador_pessoa(self) -> ControladorPessoa:
        return self.__controlador_pessoa

    def inicializa_sistema(self):
        self.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.cadastro_pessoas,
            2: self.cadastro_atendimentos,
            3: self.relatorios,
            0: self.finalizar_sistema,
        }

        while True:
            op = self.__tela_sistema.tela_opcoes()
            funcao = opcoes.get(op, None)
            if funcao:
                funcao()
            else:
                self.__tela_sistema.mensagem("Opção inválida. Tente novamente.")

    def cadastro_pessoas(self):
        self.__controlador_pessoa.abre_tela()

    def cadastro_atendimentos(self):
        self.__controlador_atendimento.abre_tela()

    def relatorios(self):
        print("Relatórios")
        # Lógica para geração de relatórios

    def finalizar_sistema(self):
        self.__tela_sistema.mensagem("Sistema finalizado. Até logo!")
        exit()
