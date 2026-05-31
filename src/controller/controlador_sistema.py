from view.tela_sistema import TelaSistema
from controller.controlador_pessoa import ControladorPessoa


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_pessoa = ControladorPessoa(self)

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
                print("Opção inválida. Tente novamente.")

    def cadastro_pessoas(self):
        self.__controlador_pessoa.abre_tela()

    def cadastro_atendimentos(self):
        print("Cadastro de Atendimentos")
        # Lógica para cadastro de atendimentos

    def relatorios(self):
        print("Relatórios")
        # Lógica para geração de relatórios

    def finalizar_sistema(self):
        print("Finalizando o sistema. Até logo!")
        exit()
