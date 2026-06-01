class TelaSistema:
    def tela_opcoes(self):
        print("\n🏥 -------- SisClinicas -------- 🏥")
        print("Escolha a opção desejada:")
        print("1️⃣ - Cadastro de Pessoas (Pacientes / Médicos)")
        print("2️⃣ - Gerenciar Atendimentos (Consultas / Procedimentos)")
        print("3️⃣ - Relatórios e Estatísticas")
        print("0️⃣ - Finalizar o Sistema")
        try:
            op = int(input("👉 Escolha a opção: "))
            return op
        except ValueError:
            return -1

    def mensagem(self, msg):
        print(f"✨ {msg}")
