from view.tela_relatorio import TelaRelatorio


class ControladorRelatorio:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_relatorio = TelaRelatorio()

    def atendimentos_mais_caros_ou_baratos(self):
        atendimentos = self.__controlador_sistema.controlador_atendimento.atendimentos
        top_n = self.__tela_relatorio.solicita_top_n()
        ordem = self.__tela_relatorio.solicita_ordem()

        atendimentos_ordenados = sorted(
            atendimentos, key=lambda x: x.valor, reverse=(ordem == 1)
        )[:top_n]

        atendimentos_str = [
            f"ID: {atendimento.id}, Valor: {atendimento.valor}, Data: {atendimento.ts_inicio.strftime('%Y-%m-%d')}"
            for atendimento in atendimentos_ordenados
        ]
        self.__tela_relatorio.mostra_atendimentos(atendimentos_str)

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

        procedimentos_str = [
            f"Descrição: {procedimento[0]}, Quantidade: {procedimento[1]}"
            for procedimento in procedimentos_ordenados
        ]
        self.__tela_relatorio.mostra_procedimentos(procedimentos_str)

    def abre_tela(self):
        opcoes = {
            # 1: self.top_clinicas_com_mais_atendimentos,
            2: self.atendimentos_mais_caros_ou_baratos,
            3: self.procedimentos_mais_realizados,
            # 4: self.procedimentos_mais_caros_ou_baratos,
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
