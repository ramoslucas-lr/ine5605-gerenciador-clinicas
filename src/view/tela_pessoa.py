from typing import List


class TelaPessoa:
    def __init__(self):
        pass

    def mostrar_opcoes(self):
        print("\n👥 ---- GERENCIAR PESSOAS ---- 👥")
        print("1 - Incluir Nova Pessoa")
        print("2 - Alterar Pessoa Existente")
        print("3 - Excluir Pessoa")
        print("4 - Listar Todas as Pessoas")
        print("5 - Buscar Pessoa por CPF")
        print("0 - Voltar ao Menu Principal")

        try:
            opcao = int(input("👉 Escolha uma opção: "))
            return opcao
        except ValueError:
            return -1

    def seleciona_pessoa(self):
        cpf = input("🔍 Digite o CPF da pessoa: ")
        return cpf

    def mostra_pessoa(self, nome, celular, cpf, data_nascimento, papeis):
        print(f"\n👤 Nome: {nome}")
        print(f"📱 Celular: {celular}")
        print(f"🪪 CPF: {cpf}")
        print(f"📅 Data de Nascimento: {data_nascimento}")
        for papel in papeis:
            self.mostra_papel(papel)

    def mostra_papel(self, papel: List[dict]):
        if papel["tipo"] == "Paciente":
            print(f"➡️ Papel: 🩺 Paciente")
        elif papel["tipo"] == "Profissional":
            print(f"➡️ Papel: 🥼 Profissional da Saúde")
            print(f"   🧾 Registro Profissional (CRM): {papel['reg_profissional']}")
            print(f"   🧬 Especialidade: {papel['especialidade']}")

    def pega_dados_pessoa(self):
        print("\n📝 Digite os dados da nova pessoa:")
        nome = input("✍️ Nome completo: ")
        celular = input("📞 Celular: ")
        cpf = input("🪪 CPF (apenas números): ")
        data_nascimento = input("📅 Data de Nascimento (dd/mm/aaaa): ")

        if nome and celular and cpf and data_nascimento:
            return {
                "nome": nome,
                "celular": celular,
                "cpf": cpf,
                "data_nascimento": data_nascimento,
            }
        else:
            print("⚠️ Todos os campos são obrigatórios!")
            return None

    def pega_dados_pessoa_alteracao(self, nome, celular, cpf, data_nascimento):
        print("\n✏️ Digite os novos dados (deixe em branco para manter o valor atual):")
        nome = input(f"✍️ Nome completo [{nome}]: ") or nome
        celular = input(f"📞 Celular [{celular}]: ") or celular
        cpf = input(f"🪪 CPF [{cpf}]: ") or cpf
        data_nascimento = (
            input(f"📅 Data de Nascimento (dd/mm/aaaa) [{data_nascimento}]: ")
            or data_nascimento
        )

        return {
            "nome": nome,
            "celular": celular,
            "cpf": cpf,
            "data_nascimento": data_nascimento,
        }

    def pega_parametros_paginacao(self):
        try:
            page = int(input("📖 Digite o número da página desejada: "))
            return page
        except ValueError:
            print("⚠️ Por favor, insira um número válido para a página.")
            return None

    def mostra_mensagem(self, mensagem):
        print(f"✨ {mensagem}")

    def confirma_exclusao(self, nome):
        resposta = input(
            f"❓ Tem certeza absoluta que deseja excluir a pessoa '{nome}'? (s/n): "
        )
        return resposta.lower() == "s"

    def seleciona_tipo_papel(self):
        print("\n💼 Selecione o papel para esta pessoa:")
        print("1 - Paciente")
        print("2 - Profissional da Saúde")
        try:
            opcao = int(input("👉 Escolha uma opção: "))
            return opcao
        except ValueError:
            print("⚠️ Opção inválida. Digite um número.")
            return None

    def pega_dados_papel_profissional(self):
        print("\n🥼 Digite as informações do profissional:")
        reg_profissional = input("🧾 Registro Profissional (CRM/etc): ")
        especialidade = input("🧬 Especialidade médica: ")
        return reg_profissional, especialidade

    def confirma_alteracao_papel(self, nome):
        resposta = input(f"❓ Deseja alterar os papéis da pessoa '{nome}'? (s/n): ")
        return resposta.lower() == "s"

    def mostrar_opcoes_papeis(self):
        print("\n⚙️ -- Gerenciar Papéis da Pessoa --")
        print("1 - Adicionar Papel")
        print("2 - Remover Papel")
        print("0 - Concluir e Voltar")
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
