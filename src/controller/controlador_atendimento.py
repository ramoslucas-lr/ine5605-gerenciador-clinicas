from datetime import datetime, time
from decimal import Decimal

from models.atendimento import Atendimento
from models.clinica import Clinica
from models.tipo_atendimento import TipoAtendimento

from view.tela_atendimento import TelaAtendimento


class ControladorAtendimento:
    def __init__(self, controlador_sistema):
        self.__atendimentos = {}
        self.__controlador_sistema = controlador_sistema
        self.__tela_atendimento = TelaAtendimento()

    @property
    def atendimentos(self):
        return self.__atendimentos.values()

    def buscar_atendimento(self, id):
        return self.__atendimentos.get(id)

    def incluir_atendimento(self):
        dados_atendimento = self.__tela_atendimento.pega_dados_atendimento()

        if dados_atendimento is not None:
            prox_id = max(self.__atendimentos.keys(), default=0) + 1

            paciente = self.__controlador_sistema.controlador_pessoa.buscar_pessoa(
                dados_atendimento["cpf_paciente"]
            )
            profissional = self.__controlador_sistema.controlador_pessoa.buscar_pessoa(
                dados_atendimento["cpf_profissional"]
            )
            # TODO: clinica = self.__controlador_sistema.controlador_clinica.buscar_clinica(dados_atendimento["id_clinica"])
            clinica = Clinica(
                1,
                "Clinica Exemplo",
                "Endereço Exemplo",
                "Descrocap Exemplo",
                hora_abertura=time(8, 0),
                hora_fechamento=time(18, 0),
            )
            # TODO: tipo_atendimento = self.__controlador_sistema.controlador_tipo_atendimento.buscar_tipo_atendimento(dados_atendimento["id_tipo_atendimento"])
            tipo_atendimento = TipoAtendimento(1, "Exame", "Raio-X")

            ts_inicio = datetime.strptime(
                dados_atendimento["ts_inicio"], "%d/%m/%Y %H:%M"
            )
            ts_fim = datetime.strptime(dados_atendimento["ts_fim"], "%d/%m/%Y %H:%M")
            valor = Decimal(dados_atendimento["valor"])
            atendimento = Atendimento(
                prox_id,
                ts_inicio,
                ts_fim,
                valor,
                tipo_atendimento,
                paciente,
                profissional,
                clinica,
            )
            print(atendimento)
            print(atendimento.id)

            self.__atendimentos[atendimento.id] = atendimento
            print(self.__atendimentos)
            # TODO: self.__controlador_sistema.controlador_clinica.adicionar_atendimento_clinica(clinica.id, atendimento)

            self.__tela_atendimento.mostra_mensagem("Atendimento incluído com sucesso.")

    def alterar_atendimento(self):
        id = self.__tela_atendimento.seleciona_atendimento()
        atendimento = self.buscar_atendimento(id)

        if atendimento is not None:
            dados_atendimento = (
                self.__tela_atendimento.pega_dados_atendimento_alteracao(
                    atendimento.ts_inicio.strftime("%d/%m/%Y %H:%M"),
                    atendimento.ts_fim.strftime("%d/%m/%Y %H:%M"),
                    str(atendimento.valor.quantize(Decimal("0.01"))),
                    atendimento.tipo_atendimento.id,
                    atendimento.paciente.cpf,
                    atendimento.profissional.cpf,
                    atendimento.clinica.id,
                )
            )
            if dados_atendimento is not None:
                atendimento.ts_inicio = datetime.strptime(
                    dados_atendimento["ts_inicio"], "%d/%m/%Y %H:%M"
                )
                atendimento.ts_fim = datetime.strptime(
                    dados_atendimento["ts_fim"], "%d/%m/%Y %H:%M"
                )
                atendimento.valor = Decimal(dados_atendimento["valor"])

                # TODO: adicionar buscar por tipo_atendimento
                # atendimento.tipo_atendimento = self.__controlador_sistema.controlador_tipo_atendimento.buscar_tipo_atendimento(
                #     dados_atendimento["id_tipo_atendimento"]
                # )

                atendimento.paciente = (
                    self.__controlador_sistema.controlador_pessoa.buscar_pessoa(
                        dados_atendimento["cpf_paciente"]
                    )
                )
                atendimento.profissional = (
                    self.__controlador_sistema.controlador_pessoa.buscar_pessoa(
                        dados_atendimento["cpf_profissional"]
                    )
                )

                # TODO: adicionar busca por clinica
                # atendimento.clinica = (
                #     self.__controlador_sistema.controlador_clinica.buscar_clinica(
                #         dados_atendimento["id_clinica"]
                #     )
                # )
                self.__tela_atendimento.mostra_mensagem(
                    "Atendimento alterado com sucesso."
                )
        else:
            self.__tela_atendimento.mostra_mensagem("Atendimento não encontrado.")

    def abre_menu_procedimentos(self):
        opcoes = {
            1: self.incluir_procedimento,
            2: self.alterar_procedimento,
            3: self.excluir_procedimento,
            4: self.listar_procedimentos,
        }
        while True:
            opcao = self.__tela_atendimento.mostra_menu_procedimentos()
            funcao = opcoes.get(opcao, None)
            if funcao:
                funcao()
            elif opcao == 0:
                break
            else:
                self.__tela_atendimento.mostra_mensagem(
                    "Opção inválida. Tente novamente."
                )

    def incluir_procedimento(self):
        id_atendimento = self.__tela_atendimento.seleciona_atendimento()
        atendimento: Atendimento = self.buscar_atendimento(id_atendimento)
        if atendimento is not None:
            dados_procedimento = self.__tela_atendimento.pega_dados_procedimento()
            if dados_procedimento is not None:
                profissional = (
                    self.__controlador_sistema.controlador_pessoa.buscar_pessoa(
                        dados_procedimento["cpf_profissional"]
                    )
                )
                atendimento.adiciona_procedimento(
                    dados_procedimento["descricao"],
                    Decimal(dados_procedimento["valor"]),
                    profissional,
                )
                self.__tela_atendimento.mostra_mensagem(
                    "Procedimento incluído com sucesso."
                )
            else:
                self.__tela_atendimento.mostra_mensagem(
                    "Dados do procedimento inválidos."
                )

    def excluir_procedimento(self):
        id_atendimento = self.__tela_atendimento.seleciona_atendimento()
        atendimento: Atendimento = self.buscar_atendimento(id_atendimento)
        if atendimento is not None:
            procedimento_list_str = []
            for procedimento in atendimento.procedimentos.values():
                procedimento_list_str.append(str(procedimento))
            id_procedimento = self.__tela_atendimento.seleciona_procedimento(
                procedimento_list_str
            )
            if id_procedimento is not None:
                atendimento.excluir_procedimento(id_procedimento)
                self.__tela_atendimento.mostra_mensagem(
                    "Procedimento excluído com sucesso."
                )
            else:
                self.__tela_atendimento.mostra_mensagem("Procedimento não encontrado.")
        else:
            self.__tela_atendimento.mostra_mensagem("Atendimento não encontrado.")

    def listar_procedimentos(self):
        id_atendimento = self.__tela_atendimento.seleciona_atendimento()
        atendimento: Atendimento = self.buscar_atendimento(id_atendimento)
        if atendimento is not None:
            procedimentos_str = [
                str(procedimento) for procedimento in atendimento.procedimentos.values()
            ]
            self.__tela_atendimento.mostra_procedimentos(procedimentos_str)
        else:
            self.__tela_atendimento.mostra_mensagem("Atendimento não encontrado.")

    def alterar_procedimento(self):
        id_atendimento = self.__tela_atendimento.seleciona_atendimento()
        atendimento: Atendimento = self.buscar_atendimento(id_atendimento)
        if atendimento is not None:
            procedimento_list_str = []
            for procedimento in atendimento.procedimentos.values():
                procedimento_list_str.append(str(procedimento))
            id_procedimento = self.__tela_atendimento.seleciona_procedimento(
                procedimento_list_str
            )
            if id_procedimento is not None:
                procedimento = atendimento.procedimentos[id_procedimento]
                dados_procedimento = (
                    self.__tela_atendimento.pega_dados_procedimento_alteracao(
                        procedimento.descricao,
                        str(procedimento.valor.quantize(Decimal("0.01"))),
                        procedimento.profissional.cpf,
                    )
                )
                if dados_procedimento is not None:
                    profissional = (
                        self.__controlador_sistema.controlador_pessoa.buscar_pessoa(
                            dados_procedimento["cpf_profissional"]
                        )
                    )
                    atendimento.alterar_procedimento(
                        id_procedimento,
                        dados_procedimento["descricao"],
                        Decimal(dados_procedimento["valor"]),
                        profissional,
                    )
                    self.__tela_atendimento.mostra_mensagem(
                        "Procedimento alterado com sucesso."
                    )
                else:
                    self.__tela_atendimento.mostra_mensagem(
                        "Dados do procedimento inválidos."
                    )
            else:
                self.__tela_atendimento.mostra_mensagem("Procedimento não encontrado.")

    def mostrar_atendimento(self):
        id = self.__tela_atendimento.seleciona_atendimento()
        atendimento = self.buscar_atendimento(id)

        if atendimento is not None:
            procedimento_list_str = []
            for procedimento in atendimento.procedimentos.values():
                procedimento_list_str.append(str(procedimento))
            pagamentos_list_str = []
            for pagamento in atendimento.pagamentos:
                pagamentos_list_str.append(str(pagamento))
            self.__tela_atendimento.mostra_atendimento(
                atendimento.id,
                atendimento.ts_inicio,
                atendimento.ts_fim,
                atendimento.valor,
                atendimento.tipo_atendimento,
                atendimento.paciente.nome,
                atendimento.profissional.nome,
                atendimento.clinica.nome,
                procedimento_list_str,
                pagamentos_list_str,
                atendimento.valor_total,
                atendimento.valor_pago,
            )
        else:
            self.__tela_atendimento.mostra_mensagem("Atendimento não encontrado.")

    def excluir_atendimento(self):
        id = self.__tela_atendimento.seleciona_atendimento()
        atendimento = self.buscar_atendimento(id)

        if atendimento is not None:
            del self.__atendimentos[id]
            self.__tela_atendimento.mostra_mensagem("Atendimento excluído com sucesso.")
        else:
            self.__tela_atendimento.mostra_mensagem("Atendimento não encontrado.")

    def buscar_atendimentos_por_paciente(self):
        cpf_paciente = self.__tela_atendimento.pega_cpf_paciente()
        return [
            atendimento
            for atendimento in self.__atendimentos.values()
            if atendimento.paciente.cpf == cpf_paciente
        ]

    def buscar_atendimentos_por_profissional(self):
        cpf_profissional = self.__tela_atendimento.pega_cpf_profissional()
        return [
            atendimento
            for atendimento in self.__atendimentos.values()
            if atendimento.profissional.cpf == cpf_profissional
        ]

    def buscar_atendimentos_por_clinica(self):
        id_clinica = self.__tela_atendimento.pega_id_clinica()
        return [
            atendimento
            for atendimento in self.__atendimentos.values()
            if atendimento.clinica.id == id_clinica
        ]

    def buscar_atendimentos_por_data(self):
        data_inicio = datetime.strptime(
            self.__tela_atendimento.pega_data_inicio(), "%d/%m/%Y"
        )
        data_fim = datetime.strptime(
            self.__tela_atendimento.pega_data_fim(), "%d/%m/%Y"
        )
        return [
            atendimento
            for atendimento in self.__atendimentos.values()
            if atendimento.ts_inicio >= data_inicio and atendimento.ts_fim <= data_fim
        ]

    def listar_atendimentos(self):
        opcoes = {
            2: self.buscar_atendimentos_por_paciente,
            3: self.buscar_atendimentos_por_profissional,
            4: self.buscar_atendimentos_por_clinica,
            5: self.buscar_atendimentos_por_data,
        }
        opcao = self.__tela_atendimento.opcoes_listar_atendimentos()

        funcao = opcoes.get(opcao, None)
        if funcao:
            atendimentos = funcao()
        elif opcao == 1:
            atendimentos = self.__atendimentos.values()
        elif opcao == 0:
            return
        else:
            self.__tela_atendimento.mostra_mensagem(
                "Opção inválida. Listando todos os atendimentos."
            )
            atendimentos = self.__atendimentos.values()
        self.listar_atendimentos_paginados(atendimentos)

    def listar_atendimentos_paginados(self, atendimentos, page=1):
        page_size = 5
        atendimentos_list = list(atendimentos)
        total_atendimentos = len(atendimentos_list)
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        atendimentos_page = atendimentos_list[start_index:end_index]

        for atendimento in atendimentos_page:
            total_pages = (
                (total_atendimentos + page_size - 1) // page_size
                if page_size > 0
                else 1
            )
            showing_start = start_index + 1 if total_atendimentos > 0 else 0
            showing_end = min(end_index, total_atendimentos)
            self.__tela_atendimento.mostra_mensagem(
                f"Página {page}/{total_pages} - Mostrando {showing_start}-{showing_end} de {total_atendimentos}"
            )
            self.__tela_atendimento.mostra_atendimento(
                atendimento.id,
                atendimento.ts_inicio,
                atendimento.ts_fim,
                atendimento.valor,
                atendimento.tipo_atendimento,
                atendimento.paciente.nome,
                atendimento.profissional.nome,
                atendimento.clinica.nome,
                atendimento.procedimentos,
                atendimento.pagamentos,
                atendimento.valor_total,
                atendimento.valor_pago,
            )
            self.__tela_atendimento.mostra_mensagem("-" * 20)

        if total_atendimentos // page_size > 1:
            while True:
                resposta = self.__tela_atendimento.mostra_menu_pagina()
                if resposta.lower() == "n":
                    if end_index < total_atendimentos:
                        self.listar_atendimentos(page + 1)
                    else:
                        self.__tela_atendimento.mostra_mensagem(
                            "Você já está na última página."
                        )
                elif resposta.lower() == "p":
                    if start_index > 0:
                        self.listar_atendimentos(page - 1)
                    else:
                        self.__tela_atendimento.mostra_mensagem(
                            "Você já está na primeira página."
                        )
                else:
                    break

    def retorna_tela(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.mostrar_atendimento,
            2: self.excluir_atendimento,
            3: self.listar_atendimentos,
            4: self.incluir_atendimento,
            5: self.alterar_atendimento,
            6: self.abre_menu_procedimentos,
            0: self.retorna_tela,
        }

        while True:
            op = self.__tela_atendimento.tela_opcoes()
            funcao = opcoes.get(op, None)
            if funcao:
                funcao()
            else:
                self.__tela_atendimento.mostra_mensagem(
                    "Opção inválida. Tente novamente."
                )
