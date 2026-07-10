from datetime import datetime, time
from decimal import Decimal, InvalidOperation
from models.pagamento import Pagamento
from models.metodo_pix import MetodoPix
from models.metodo_cartao import MetodoCartao
from models.metodo_dinheiro import MetodoDinheiro
from models.atendimento import Atendimento
from models.clinica import Clinica
from models.tipo_atendimento import TipoAtendimento
from dao.atendimento_dao import AtendimentoDAO

from view.tela_atendimento import TelaAtendimento


class ControladorAtendimento:
    def __init__(self, controlador_sistema):
        self.__atendimento_dao = AtendimentoDAO()
        self.__controlador_sistema = controlador_sistema
        self.__tela_atendimento = TelaAtendimento()

    @property
    def atendimentos(self):
        return self.__atendimento_dao.get_all()

    def buscar_atendimento(self, id):
        return self.__atendimento_dao.get(id)

    def incluir_atendimento(self):
        dados_atendimento = self.__tela_atendimento.pega_dados_atendimento()

        if dados_atendimento is None:
            return

        atendimentos = self.__atendimento_dao.get_all()

        if len(atendimentos) == 0:
            prox_id = 1
            
        else:
            prox_id = max(atendimento.id for atendimento in atendimentos) + 1

        paciente = self.__controlador_sistema.controlador_pessoa.buscar_pessoa(
            dados_atendimento["cpf_paciente"]
        )
        profissional = self.__controlador_sistema.controlador_pessoa.buscar_pessoa(
            dados_atendimento["cpf_profissional"]
        )

        if paciente is None or not paciente.tem_papel_paciente():
            self.__tela_atendimento.mostra_mensagem(
                "Paciente não encontrado ou sem papel de paciente. Atendimento não incluído."
            )
            return

        if profissional is None or not profissional.tem_papel_profissional():
            self.__tela_atendimento.mostra_mensagem(
                "Profissional não encontrado ou sem papel de profissional. Atendimento não incluído."
            )
            return

        clinica = self.__controlador_sistema.controlador_clinica.buscar_clinica(
            int(dados_atendimento["id_clinica"])
        )

        if clinica is None:
            self.__tela_atendimento.mostra_mensagem(
                "Clínica não encontrada. Atendimento não incluído."
            )
            return
        tipo_atendimento = self.__controlador_sistema.controlador_tipo_atendimento.buscar_tipo_atendimento(
            int(dados_atendimento["tipo_atendimento"])
        )

        if tipo_atendimento is None:
            self.__tela_atendimento.mostra_mensagem(
                "Tipo de atendimento não encontrado. Atendimento não incluído."
            )
            return

        try:
            ts_inicio = datetime.strptime(
                dados_atendimento["ts_inicio"], "%d/%m/%Y %H:%M"
            )
            ts_fim = datetime.strptime(
                dados_atendimento["ts_fim"], "%d/%m/%Y %H:%M"
            )
            valor = Decimal(dados_atendimento["valor"])
                
                
        except (ValueError, InvalidOperation):
            self.__tela_atendimento.mostra_mensagem(
                "Dados de data/hora ou valor inválidos. Atendimento não incluído."
            )
            return

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

        self.__atendimento_dao.add(atendimento)
        clinica.adicionar_atendimento(atendimento)

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
                try:
                    ts_inicio = datetime.strptime(
                        dados_atendimento["ts_inicio"], "%d/%m/%Y %H:%M"
                    )
                    ts_fim = datetime.strptime(
                        dados_atendimento["ts_fim"], "%d/%m/%Y %H:%M"
                    )
                    valor = Decimal(dados_atendimento["valor"])
                except (ValueError, InvalidOperation):
                    self.__tela_atendimento.mostra_mensagem(
                        "Dados de data/hora ou valor inválidos. Alteração não realizada."
                    )
                    return

                paciente = self.__controlador_sistema.controlador_pessoa.buscar_pessoa(
                    dados_atendimento["cpf_paciente"]
                )
                profissional = (
                    self.__controlador_sistema.controlador_pessoa.buscar_pessoa(
                        dados_atendimento["cpf_profissional"]
                    )
                )

                if paciente is None or not paciente.tem_papel_paciente():
                    self.__tela_atendimento.mostra_mensagem(
                        "Paciente não encontrado ou sem papel de paciente. Alteração não realizada."
                    )
                    return

                if profissional is None or not profissional.tem_papel_profissional():
                    self.__tela_atendimento.mostra_mensagem(
                        "Profissional não encontrado ou sem papel de profissional. Alteração não realizada."
                    )
                    return

                clinica = self.__controlador_sistema.controlador_clinica.buscar_clinica(
                    int(dados_atendimento["id_clinica"])
                )
                if clinica is None:
                    self.__tela_atendimento.mostra_mensagem(
                        "Clínica não encontrada. Alteração não realizada."
                    )
                    return

                tipo_atendimento = self.__controlador_sistema.controlador_tipo_atendimento.buscar_tipo_atendimento(
                    int(dados_atendimento["tipo_atendimento"])
                )
                if tipo_atendimento is None:
                    self.__tela_atendimento.mostra_mensagem(
                        "Tipo de atendimento não encontrado. Alteração não realizada."
                    )
                    return

                try:
                    atendimento.ts_inicio = ts_inicio
                    atendimento.ts_fim = ts_fim
                    atendimento.valor = valor
                    atendimento.paciente = paciente
                    atendimento.profissional = profissional
                    atendimento.clinica = clinica
                    atendimento.tipo_atendimento = tipo_atendimento
                    self.__atendimento_dao.update(atendimento)
                    self.__tela_atendimento.mostra_mensagem(
                        "Atendimento alterado com sucesso."
                    )
                except ValueError as e:
                    self.__tela_atendimento.mostra_mensagem(
                        f"Erro ao alterar atendimento: {e}"
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
                if profissional is None or not profissional.tem_papel_profissional():
                    self.__tela_atendimento.mostra_mensagem(
                        "Profissional não encontrado ou sem papel de profissional. Procedimento não incluído."
                    )
                    return
                try:
                    valor = Decimal(dados_procedimento["valor"])
                    atendimento.adiciona_procedimento(
                        dados_procedimento["descricao"],
                        valor,
                        profissional,
                    )
                    self.__atendimento_dao.update(atendimento)
                    self.__tela_atendimento.mostra_mensagem(
                        "Procedimento incluído com sucesso."
                    )
                except (ValueError, InvalidOperation) as e:
                    self.__tela_atendimento.mostra_mensagem(
                        f"Erro ao incluir procedimento: {e}"
                    )
            else:
                self.__tela_atendimento.mostra_mensagem(
                    "Dados do procedimento inválidos."
                )
        else:
            self.__tela_atendimento.mostra_mensagem("Atendimento não encontrado.")

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
            if (
                id_procedimento is not None
                and id_procedimento in atendimento.procedimentos
            ):
                try:
                    atendimento.excluir_procedimento(id_procedimento)
                    self.__atendimento_dao.update(atendimento)
                    self.__tela_atendimento.mostra_mensagem(
                        "Procedimento excluído com sucesso."
                    )
                except ValueError as e:
                    self.__tela_atendimento.mostra_mensagem(f"Erro: {e}")
            else:
                self.__tela_atendimento.mostra_mensagem("Procedimento não encontrado.")
        else:
            self.__tela_atendimento.mostra_mensagem("Atendimento não encontrado.")

    def listar_procedimentos(self):
        id_atendimento = self.__tela_atendimento.seleciona_atendimento()
        if id_atendimento == -1 or id_atendimento is None:
            return

        atendimento: Atendimento = self.buscar_atendimento(id_atendimento)
        if atendimento is not None:
            self.__tela_atendimento.mostra_procedimentos(list(atendimento.procedimentos.values()))
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
            if (
                id_procedimento is not None
                and id_procedimento in atendimento.procedimentos
            ):
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
                    if (
                        profissional is None
                        or not profissional.tem_papel_profissional()
                    ):
                        self.__tela_atendimento.mostra_mensagem(
                            "Profissional não encontrado ou sem papel de profissional. Alteração não realizada."
                        )
                        return
                    try:
                        valor = Decimal(dados_procedimento["valor"])
                        atendimento.alterar_procedimento(
                            id_procedimento,
                            dados_procedimento["descricao"],
                            valor,
                            profissional,
                        )
                        self.__atendimento_dao.update(atendimento)
                        self.__tela_atendimento.mostra_mensagem(
                            "Procedimento alterado com sucesso."
                        )
                    except (ValueError, InvalidOperation) as e:
                        self.__tela_atendimento.mostra_mensagem(
                            f"Erro ao alterar procedimento: {e}"
                        )
                else:
                    self.__tela_atendimento.mostra_mensagem(
                        "Dados do procedimento inválidos."
                    )
            else:
                self.__tela_atendimento.mostra_mensagem("Procedimento não encontrado.")
        else:
            self.__tela_atendimento.mostra_mensagem("Atendimento não encontrado.")

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
            self.__atendimento_dao.remove(id)
            self.__tela_atendimento.mostra_mensagem("Atendimento excluído com sucesso.")
        else:
            self.__tela_atendimento.mostra_mensagem("Atendimento não encontrado.")

    def buscar_atendimentos_por_paciente(self):
        cpf_paciente = self.__tela_atendimento.pega_cpf_paciente()
        return [
            atendimento
            for atendimento in self.__atendimento_dao.get_all()
            if atendimento.paciente.cpf == cpf_paciente
        ]

    def buscar_atendimentos_por_profissional(self):
        cpf_profissional = self.__tela_atendimento.pega_cpf_profissional()
        return [
            atendimento
            for atendimento in self.__atendimento_dao.get_all()
            if atendimento.profissional.cpf == cpf_profissional
        ]

    def buscar_atendimentos_por_clinica(self):
        id_clinica = self.__tela_atendimento.pega_id_clinica()
        return [
            atendimento
            for atendimento in self.__atendimento_dao.get_all()
            if atendimento.clinica.id == id_clinica
        ]

    def buscar_atendimentos_por_data(self):
        try:

            data_inicio = datetime.strptime(
                self.__tela_atendimento.pega_data_inicio(), "%d/%m/%Y"
            )
            data_fim = datetime.strptime(
                self.__tela_atendimento.pega_data_fim(), "%d/%m/%Y"
            )
        except ValueError:
            self.__tela_atendimento.mostra_mensagem("Datas inválidas. Tente novamente.")
            return []
        return [
            atendimento
            for atendimento in self.__atendimento_dao.get_all()
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
            atendimentos = self.__atendimento_dao.get_all()
        elif opcao == 0:
            return
        else:
            self.__tela_atendimento.mostra_mensagem(
                "Opção inválida. Listando todos os atendimentos."
            )
            atendimentos = self.__atendimento_dao.get_all()
        
        self.__tela_atendimento.listar_atendimentos(atendimentos)

    def registrar_pagamento(self):
        id_atendimento = self.__tela_atendimento.seleciona_atendimento()
        if id_atendimento == -1 or id_atendimento is None:
            return

        atendimento = self.buscar_atendimento(id_atendimento)
        if atendimento is None:
            self.__tela_atendimento.mostra_mensagem("Atendimento não encontrado.")
            return

        dados_pagamento = self.__tela_atendimento.pega_dados_pagamento()
        if dados_pagamento is None:
            return

        try:
            valor = Decimal(dados_pagamento["valor"])
            data = datetime.strptime(dados_pagamento["data"], "%d/%m/%Y")
            metodo = dados_pagamento["metodo"]

            if metodo == 1:
                metodo_pagamento = MetodoPix(
                    dados_pagamento["chave_pix"],
                    dados_pagamento["tipo_chave"]
                )
            elif metodo == 2:
                metodo_pagamento = MetodoCartao(
                    dados_pagamento["numero_cartao"],
                    dados_pagamento["bandeira"]
                )
            elif metodo == 3:
                metodo_pagamento = MetodoDinheiro()
            else:
                self.__tela_atendimento.mostra_mensagem("Método inválido.")
                return

            pagamento = Pagamento(
                data,
                valor,
                atendimento.paciente,
                atendimento,
                metodo_pagamento
            )

            atendimento.adiciona_pagamento(pagamento)  
            self.__atendimento_dao.update(atendimento)
            self.__tela_atendimento.mostra_mensagem("Pagamento registrado com sucesso.")

        except (ValueError, InvalidOperation) as erro:
            self.__tela_atendimento.mostra_mensagem(f"Erro ao registrar pagamento: {erro}")

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
             7: self.registrar_pagamento,
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
