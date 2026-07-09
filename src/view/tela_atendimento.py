import FreeSimpleGUI as sg
class TelaAtendimento:
    def __init__(self):
        pass


    def init_components(self):
        sg.ChangeLookAndFeel("DarkTeal4")

        layout = [
            [sg.Text("SisClinicas", font=("Helvetica", 18), justification="center")],
            [sg.Text("Escolha a opção desejada:")],
            [sg.Radio("1 - Cadastro de Pessoas (Pacientes / Médicos)", "RD1", key=1)],
            [sg.Radio("2 - Gerenciar Atendimentos (Consultas / Procedimentos)", "RD1", key=2)],
            [sg.Radio("3 - Relatórios e Estatísticas", "RD1", key=3)],
            [sg.Radio("4 - Cadastro de Clinicas", "RD1", key=4)],
            [sg.Radio("5 - Cadastro de Tipos de Atendimento", "RD1", key=5)],
            [sg.Radio("0 - Finalizar o Sistema", "RD1", key=0)],
            [sg.Button("Confirmar"), sg.Cancel('Cancelar')]
        ]

    def mensagem(self, msg):
        sg.popup(msg)
    
    def close(self):
        self.__window.Close()

    def open(self):
        evento, valores = self.__window.read()
        return evento, valores


        self.__window = sg.Window("SisClinicas", layout, size=(400, 300))
    def pega_dados_atendimento(self):
        print("\n📅 ---- Novo Atendimento / Consulta ---- 📅")
        ts_inicio = input("✍️ Data e hora de início (dd/mm/aaaa HH:MM): ")
        ts_fim = input("✍️ Data e hora de fim (dd/mm/aaaa HH:MM): ")
        valor = input("💰 Valor do atendimento (R$): ")
        tipo_atendimento = input("🏷️ ID do tipo do atendimento: ")
        cpf_paciente = input("🩺 CPF do paciente: ")
        cpf_profissional = input("🥼 CPF do profissional/médico: ")
        id_clinica = input("🏥 ID da clínica: ")

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
        print(f"✨ {mensagem}")

    def seleciona_atendimento(self):
        try:
            id = int(input("🔍 Digite o ID do atendimento: "))
            return id
        except ValueError:
            print("⚠️ ID inválido!")
            return -1

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
        print("\n✏️ Editar Atendimento (deixe em branco para manter o valor atual):")
        ts_inicio = (
            input(f"✍️ Data e hora de início (dd/mm/aaaa HH:MM) [{ts_inicio}]: ")
            or ts_inicio
        )
        ts_fim = (
            input(f"✍️ Data e hora de fim (dd/mm/aaaa HH:MM) [{ts_fim}]: ") or ts_fim
        )
        valor = input(f"💰 Valor do atendimento [{valor}]: ") or valor
        tipo_atendimento = (
            input(f"🏷️ ID do tipo do atendimento [{tipo_atendimento}]: ")
            or tipo_atendimento
        )
        cpf_paciente = input(f"🩺 CPF do paciente [{cpf_paciente}]: ") or cpf_paciente
        cpf_profissional = (
            input(f"🥼 CPF do profissional/médico [{cpf_profissional}]: ")
            or cpf_profissional
        )
        id_clinica = input(f"🏥 ID da clínica [{id_clinica}]: ") or id_clinica

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
        print("\n🛠️ ---- GERENCIAR PROCEDIMENTOS ---- 🛠️")
        print("1 - Incluir Novo Procedimento")
        print("2 - Alterar Procedimento Existente")
        print("3 - Excluir Procedimento")
        print("4 - Listar Procedimentos do Atendimento")
        print("0 - Voltar ao Menu Anterior")

        try:
            opcao = int(input("👉 Escolha uma opção: "))
            return opcao
        except ValueError:
            return -1

    def pega_dados_procedimento(self):
        print("\n🧬 Novo Procedimento no Atendimento:")
        descricao = input("✍️ Descrição / Nome do procedimento: ")
        valor = input("💰 Valor do procedimento (R$): ")
        cpf_profissional = input(
            "🥼 CPF do profissional responsável pelo procedimento: "
        )

        return {
            "descricao": descricao,
            "valor": valor,
            "cpf_profissional": cpf_profissional,
        }

    def seleciona_procedimento(self, procedimentos):
        print("\n🧬 Procedimentos vinculados:")
        for procedimento in procedimentos:
            print(f"🔸 {procedimento}")
        try:
            id = int(input("👉 Digite o ID do procedimento desejado: "))
            return id
        except ValueError:
            print("⚠️ ID inválido!")
            return -1

    def mostra_procedimentos(self, procedimentos):
        print("\n📋 Lista de Procedimentos do Atendimento:")
        for procedimento in procedimentos:
            print(f"🔸 {procedimento}")

    def pega_dados_procedimento_alteracao(self, descricao, valor, cpf_profissional):
        print("\n✏️ Alterar Procedimento (deixe em branco para manter o valor atual):")
        descricao = input(f"✍️ Descrição [{descricao}]: ") or descricao
        valor = input(f"💰 Valor [{valor}]: ") or valor
        cpf_profissional = (
            input(f"🥼 CPF do profissional responsável [{cpf_profissional}]: ")
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
        print(f"\n📋 Atendimento ID: #{id}")
        print(f"📅 Início: {ts_inicio}")
        print(f"🏁 Fim: {ts_fim}")
        print(f"💰 Valor Base: R$ {valor}")
        print(f"🏷️ Tipo de Atendimento: {tipo_atendimento.nome}")
        print(f"🩺 Paciente: {paciente_nome}")
        print(f"🥼 Profissional: {profissional_nome}")
        print(f"🏥 Clínica: {clinica_nome}")

        print(f"🧬 Procedimentos vinculados: {'(Nenhum)' if not procedimentos else ''}")
        for procedimento in procedimentos:
            print(f"   🔸 {procedimento}")

        print(f"💳 Pagamentos realizados: {'(Nenhum)' if not pagamentos else ''}")
        for pagamento in pagamentos:
            print(f"   💵 {pagamento}")

        print(f"💵 Valor Total (Base + Procedimentos): R$ {valor_total}")
        print(f"✅ Valor Total Pago até o momento: R$ {valor_pago}")

    def opcoes_listar_atendimentos(self):
        print("\n📋 -------- BUSCAR & LISTAR ATENDIMENTOS -------- 📋")
        print("1 - Listar TODOS os Atendimentos")
        print("2 - Buscar Atendimentos por Paciente (CPF)")
        print("3 - Buscar Atendimentos por Profissional (CPF)")
        print("4 - Buscar Atendimentos por Clínica (ID)")
        print("5 - Buscar Atendimentos por Intervalo de Datas")
        print("0 - Voltar ao Menu Anterior")

        try:
            opcao = int(input("👉 Escolha uma opção: "))
            return opcao
        except ValueError:
            return -1

    def mostra_menu_pagina(self):
        print(
            "➡️ Digite 'n' para próxima página, 'p' para página anterior ou qualquer outra tecla para voltar."
        )
        resposta = input("👉 Sua escolha: ")
        return resposta

    def tela_opcoes(self):
        print("\n📅 ---- GERENCIAR ATENDIMENTOS & CONSULTAS ---- 📅")
        print("1 - Mostrar Detalhes de um Atendimento")
        print("2 - Excluir Atendimento")
        print("3 - Buscar & Listar Atendimentos")
        print("4 - Incluir Novo Atendimento")
        print("5 - Alterar Atendimento Existente")
        print("6 - Gerenciar Procedimentos de um Atendimento")
        print("7 - Registrar Pagamento")
        print("0 - Voltar ao Menu Principal")

        try:
            opcao = int(input("👉 Escolha uma opção: "))
            return opcao
        except ValueError:
            return -1

    def pega_cpf_paciente(self):
        cpf = input("🩺 Digite o CPF do paciente: ")
        return cpf

    def pega_cpf_profissional(self):
        cpf = input("🥼 Digite o CPF do profissional/médico: ")
        return cpf

    def pega_id_clinica(self):
        try:
            id_clinica = int(input("🏥 Digite o ID da clínica: "))
            return id_clinica
        except ValueError:
            print("⚠️ ID inválido!")
            return -1

    def pega_data_inicio(self):
        data_inicio = input("📅 Digite a data de início (dd/mm/aaaa): ")
        return data_inicio

    def pega_data_fim(self):
        data_fim = input("📅 Digite a data de fim (dd/mm/aaaa): ")
        return data_fim
