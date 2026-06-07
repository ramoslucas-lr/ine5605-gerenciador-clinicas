class TelaClinica:
    def mostrar_opcoes(self):
        print("\n🏥 ---- GERENCIAR CLÍNICAS ---- 🏥")
        print("1 - Incluir Nova Clínica")
        print("2 - Listar Clínicas")
        print("0 - Voltar")

        try:
            opcao = int(input("👉 Escolha uma opção: "))
            return opcao
        except ValueError:
            return -1

    def pega_dados_clinica(self):
        while True:
            try:
                id_clinica = int(input("ID da clínica: "))
                nome = input("Nome da clínica: ").strip()
                localizacao = input("Localização: ").strip()
                descricao = input("Descrição: ").strip()

                if nome == "" or localizacao == "" or descricao == "":
                    print("❌ Nenhum campo pode ficar vazio.")
                    continue

                return {
                    "id": id_clinica,
                    "nome": nome,
                    "localizacao": localizacao,
                    "descricao": descricao
                }

            except ValueError:
                print("❌ O ID deve ser um número inteiro.")

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def listar_clinicas(self, clinicas):
        if len(clinicas) == 0:
            print("Nenhuma clínica cadastrada.")
            return

        print("\n📋 CLÍNICAS CADASTRADAS")

        for clinica in clinicas:
            print("------------------------")
            print(f"ID: {clinica.id}")
            print(f"Nome: {clinica.nome}")
            print(f"Localização: {clinica.localizacao}")
            print(f"Descrição: {clinica.descricao}")