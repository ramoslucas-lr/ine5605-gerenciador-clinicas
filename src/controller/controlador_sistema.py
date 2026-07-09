from controller.controlador_clinica import ControladorClinica
from controller.controlador_tipo_atendimento import ControladorTipoAtendimento
from controller.controlador_atendimento import ControladorAtendimento
from controller.controlador_relatorio import ControladorRelatorio
from view.tela_sistema import TelaSistema
from controller.controlador_pessoa import ControladorPessoa
from controller.controlador_procedimento import ControladorProcedimento


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_pessoa = ControladorPessoa(self)
        self.__controlador_atendimento = ControladorAtendimento(self)
        self.__controlador_procedimento = ControladorProcedimento(self)
        self.__controlador_relatorio = ControladorRelatorio(self)
        self.__controlador_clinica = ControladorClinica(self)
        self.__controlador_tipo_atendimento = ControladorTipoAtendimento(self)
        

    @property
    def controlador_pessoa(self) -> ControladorPessoa:
        return self.__controlador_pessoa

    @property
    def controlador_atendimento(self) -> ControladorAtendimento:
        return self.__controlador_atendimento
    
    @property
    def controlador_clinica(self):
        return self.__controlador_clinica

    @property
    def controlador_tipo_atendimento(self):
        return self.__controlador_tipo_atendimento
    
    @property
    def controlador_procedimento(self):
        return self.__controlador_procedimento

    def inicializa_sistema(self):
        self.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.cadastro_pessoas,
            2: self.cadastro_atendimentos,
            3: self.relatorios,
            4: self.__controlador_clinica.abre_tela,
            5: self.__controlador_tipo_atendimento.abre_tela,
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
        self.__controlador_relatorio.abre_tela()

    def finalizar_sistema(self):
        self.__tela_sistema.mensagem("Sistema finalizado. Até logo!")
        exit()
