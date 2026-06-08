class TelaTipoAtendimento:
    def mostrar_opcoes(self):
        print("\n📋 ---- GERENCIAR TIPOS DE ATENDIMENTO ---- 📋")
        print("1 - Incluir Novo Tipo")
        print("2 - Listar Tipos")
        print("0 - Voltar")

        try:
            opcao = int(input("👉 Escolha uma opção: "))
            return opcao
        except ValueError:
            return -1

    def pega_dados_tipo_atendimento(self):
        while True:
            try:
                id_tipo = int(input("ID: "))
                nome = input("Nome: ").strip()
                codigo = input("Código: ").strip()
                descricao = input("Descrição: ").strip()

                if nome == "" or codigo == "" or descricao == "":
                    print("❌ Nenhum campo pode ficar vazio.")
                    continue

                return {
                    "id": id_tipo,
                    "nome": nome,
                    "codigo": codigo,
                    "descricao": descricao
                }

            except ValueError:
                print("❌ O ID deve ser um número inteiro.")

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def listar_tipos_atendimento(self, tipos):
        if len(tipos) == 0:
            print("Nenhum tipo de atendimento cadastrado.")
            return

        print("\n📋 TIPOS DE ATENDIMENTO")

        for tipo in tipos:
            print("------------------------")
            print(f"ID: {tipo.id}")
            print(f"Nome: {tipo.nome}")
            print(f"Código: {tipo.codigo}")
            print(f"Descrição: {tipo.descricao}")