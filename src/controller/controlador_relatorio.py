from view.tela_relatorio import TelaRelatorio


class ControladorRelatorio:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_relatorio = TelaRelatorio()

    def top_clinicas_com_mais_atendimentos(self):
        atendimentos = self.__controlador_sistema.controlador_atendimento.atendimentos
        top_n = self.__tela_relatorio.solicita_top_n()

        contagem_clinicas = {}
        for atendimento in atendimentos:
            nome_clinica = atendimento.clinica.nome
            contagem_clinicas[nome_clinica] = contagem_clinicas.get(nome_clinica, 0) + 1

        clinicas_ordenadas = sorted(
            contagem_clinicas.items(), key=lambda x: x[1], reverse=True
        )[:top_n]

        self.__tela_relatorio.mostra_clinicas(clinicas_ordenadas)

    def atendimentos_mais_caros_ou_baratos(self):
        atendimentos = self.__controlador_sistema.controlador_atendimento.atendimentos
        top_n = self.__tela_relatorio.solicita_top_n()
        ordem = self.__tela_relatorio.solicita_ordem()

        atendimentos_ordenados = sorted(
            atendimentos, key=lambda x: x.valor, reverse=(ordem == 1)
        )[:top_n]

        self.__tela_relatorio.mostra_atendimentos(atendimentos_ordenados)

    def procedimentos_mais_realizados(self):
        atendimentos = self.__controlador_sistema.controlador_atendimento.atendimentos
        top_n = self.__tela_relatorio.solicita_top_n()

        contagem_procedimentos = {}
        for atendimento in atendimentos:
            for procedimento in atendimento.procedimentos.values():
                contagem_procedimentos[procedimento.descricao] = (
                    contagem_procedimentos.get(procedimento.descricao, 0) + 1
                )

        procedimentos_ordenados = sorted(
            contagem_procedimentos.items(), key=lambda x: x[1], reverse=True
        )[:top_n]

        self.__tela_relatorio.mostra_procedimentos_qtd(procedimentos_ordenados)

    def procedimentos_mais_caros_ou_baratos(self):
        atendimentos = self.__controlador_sistema.controlador_atendimento.atendimentos
        top_n = self.__tela_relatorio.solicita_top_n()
        ordem = self.__tela_relatorio.solicita_ordem()

        todos_procedimentos = []
        for atendimento in atendimentos:
            todos_procedimentos.extend(atendimento.procedimentos.values())

        procedimentos_ordenados = sorted(
            todos_procedimentos, key=lambda x: x.valor, reverse=(ordem == 1)
        )[:top_n]

        self.__tela_relatorio.mostra_procedimentos_valor(procedimentos_ordenados)

    def abre_tela(self):
        opcoes = {
            1: self.top_clinicas_com_mais_atendimentos,
            2: self.atendimentos_mais_caros_ou_baratos,
            3: self.procedimentos_mais_realizados,
            4: self.procedimentos_mais_caros_ou_baratos,
            0: self.retorna_tela,
        }

        while True:
            op = self.__tela_relatorio.mostra_opcoes()
            funcao = opcoes.get(op, None)
            if funcao:
                funcao()
            else:
                self.__tela_relatorio.mostra_mensagem(
                    "Opção inválida. Tente novamente."
                )

    def retorna_tela(self):
        self.__controlador_sistema.abre_tela()
