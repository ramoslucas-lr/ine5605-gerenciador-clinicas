class TelaAtendimento:
    def __init__(self):
        pass

    def pega_dados_atendimento(self):
        ts_inicio = input(
            "Digite a data e hora de início do atendimento (dd/mm/aaaa HH:MM): "
        )
        ts_fim = input(
            "Digite a data e hora de fim do atendimento (dd/mm/aaaa HH:MM): "
        )
        valor = input("Digite o valor do atendimento: ")
        tipo_atendimento = input("Digite o ID do tipo do atendimento: ")
        cpf_paciente = input("Digite o CPF do paciente: ")
        cpf_profissional = input("Digite o CPF do profissional: ")
        id_clinica = input("Digite o ID da clínica: ")

        return {
            "ts_inicio": ts_inicio,
            "ts_fim": ts_fim,
            "valor": valor,
            "tipo_atendimento": tipo_atendimento,
            "cpf_paciente": cpf_paciente,
            "cpf_profissional": cpf_profissional,
            "id_clinica": id_clinica,
        }

    def mostra_mensagem(self, mensagem: str):
        print(mensagem)

    def seleciona_atendimento(self):
        id = int(input("Digite o ID do atendimento: "))
        return id

    def pega_dados_atendimento_alteracao(
        self,
        ts_inicio,
        ts_fim,
        valor,
        tipo_atendimento,
        cpf_paciente,
        cpf_profissional,
        id_clinica,
    ):
        ts_inicio = (
            input(
                f"Digite a data e hora de início do atendimento (dd/mm/aaaa HH:MM) [{ts_inicio}]: "
            )
            or ts_inicio
        )
        ts_fim = (
            input(
                f"Digite a data e hora de fim do atendimento (dd/mm/aaaa HH:MM) [{ts_fim}]: "
            )
            or ts_fim
        )
        valor = input(f"Digite o valor do atendimento [{valor}]: ") or valor
        tipo_atendimento = (
            input(f"Digite o ID do tipo do atendimento [{tipo_atendimento}]: ")
            or tipo_atendimento
        )
        cpf_paciente = (
            input(f"Digite o CPF do paciente [{cpf_paciente}]: ") or cpf_paciente
        )
        cpf_profissional = (
            input(f"Digite o CPF do profissional [{cpf_profissional}]: ")
            or cpf_profissional
        )
        id_clinica = input(f"Digite o ID da clínica [{id_clinica}]: ") or id_clinica

        return {
            "ts_inicio": ts_inicio,
            "ts_fim": ts_fim,
            "valor": valor,
            "tipo_atendimento": tipo_atendimento,
            "cpf_paciente": cpf_paciente,
            "cpf_profissional": cpf_profissional,
            "id_clinica": id_clinica,
        }

    def mostra_menu_procedimentos(self):
        print("---- Gerenciar Procedimentos ----")
        print("1 - Incluir Procedimento")
        print("2 - Alterar Procedimento")
        print("3 - Excluir Procedimento")
        print("4 - Listar Procedimentos")
        print("0 - Voltar")

        opcao = int(input("Escolha uma opção: "))
        return opcao

    def pega_dados_procedimento(self):
        descricao = input("Digite a descrição do procedimento: ")
        valor = input("Digite o valor do procedimento: ")
        cpf_profissional = input(
            "Digite o CPF do profissional responsável pelo procedimento: "
        )

        return {
            "descricao": descricao,
            "valor": valor,
            "cpf_profissional": cpf_profissional,
        }

    def seleciona_procedimento(self, procedimentos):
        print("Procedimentos:")
        for procedimento in procedimentos:
            print(procedimento)
        id = int(input("Digite o ID do procedimento: "))
        return id

    def mostra_procedimentos(self, procedimentos):
        for procedimento in procedimentos:
            print(procedimento)

    def pega_dados_procedimento_alteracao(self, descricao, valor, cpf_profissional):
        descricao = (
            input(f"Digite a descrição do procedimento [{descricao}]: ") or descricao
        )
        valor = input(f"Digite o valor do procedimento [{valor}]: ") or valor
        cpf_profissional = (
            input(
                f"Digite o CPF do profissional responsável pelo procedimento [{cpf_profissional}]: "
            )
            or cpf_profissional
        )

        return {
            "descricao": descricao,
            "valor": valor,
            "cpf_profissional": cpf_profissional,
        }

    def mostra_atendimento(
        self,
        id,
        ts_inicio,
        ts_fim,
        valor,
        tipo_atendimento,
        paciente_nome,
        profissional_nome,
        clinica_nome,
        procedimentos,
        pagamentos,
        valor_total,
        valor_pago,
    ):
        print(f"ID: {id}")
        print(f"Início: {ts_inicio}")
        print(f"Fim: {ts_fim}")
        print(f"Valor: {valor}")
        print(f"Tipo de Atendimento: {tipo_atendimento.nome}")
        print(f"Paciente: {paciente_nome}")
        print(f"Profissional: {profissional_nome}")
        print(f"Clínica: {clinica_nome}")
        print(f"Procedimentos: {'Nenhum' if not procedimentos else ''}")

        for procedimento in procedimentos:
            print(procedimento)
        print(f"Pagamentos: {'Nenhum' if not pagamentos else ''}")
        for pagamento in pagamentos:
            print(pagamento)
        print(f"Valor Total (Com Procedimentos): {valor_total}")
        print(f"Valor Total Pago: {valor_pago}")

    def opcoes_listar_atendimentos(self):
        print("---- Listar Atendimentos ----")
        print("1 - Listar todos os atendimentos")
        print("2 - Listar atendimentos por paciente")
        print("3 - Listar atendimentos por profissional")
        print("4 - Listar atendimentos por clínica")
        print("5 - Listar atendimentos por data")
        print("0 - Voltar")

        opcao = int(input("Escolha uma opção: "))
        return opcao

    def mostra_menu_pagina(self):
        print(
            "Digite 'n' para próxima página, 'p' para página anterior ou outra tecla para voltar."
        )
        resposta = input("Digite sua escolha: ")
        return resposta

    def tela_opcoes(self):
        print("---- Gerenciar Atendimentos ----")
        print("1 - Mostrar Atendimento")
        print("2 - Excluir Atendimento")
        print("3 - Listar Atendimentos")
        print("4 - Incluir Atendimento")
        print("5 - Alterar Atendimento")
        print("6 - Gerenciar Procedimentos")
        print("0 - Voltar")

        opcao = int(input("Escolha uma opção: "))
        return opcao

    def pega_cpf_paciente(self):
        cpf = input("Digite o CPF do paciente: ")
        return cpf

    def pega_cpf_profissional(self):
        cpf = input("Digite o CPF do profissional: ")
        return cpf

    def pega_id_clinica(self):
        id_clinica = int(input("Digite o ID da clínica: "))
        return id_clinica

    def pega_data_inicio(self):
        data_inicio = input("Digite a data de início (dd/mm/aaaa): ")
        return data_inicio

    def pega_data_fim(self):
        data_fim = input("Digite a data de fim (dd/mm/aaaa): ")
        return data_fim
