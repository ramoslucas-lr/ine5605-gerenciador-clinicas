class TelaRelatorio:
    def __init__(self):
        pass

    def solicita_top_n(self):
        try:
            top_n = int(input("🔢 Quantos itens deseja listar no ranking? "))
            return top_n
        except ValueError:
            print("⚠️ Valor inválido! Usando padrão de 3 itens.")
            return 3
    
    def solicita_ordem(self):
        print("\n↕️ Escolha a ordenação:")
        print("1️⃣ - Mais caros (Decrescente)")
        print("2️⃣ - Mais baratos (Crescente)")
        try:
            ordem = int(input("👉 Escolha a ordem: "))
            return ordem
        except ValueError:
            return 1
    
    def mostra_atendimentos(self, atendimentos):
        print("\n📋 ==== RESULTADO DOS ATENDIMENTOS ====")
        for atendimento in atendimentos:
            print(f"🔹 {atendimento}")
    
    def mostra_procedimentos(self, procedimentos):
        print("\n📋 ==== RESULTADO DOS PROCEDIMENTOS ====")
        for procedimento in procedimentos:
            print(f"🔸 {procedimento}")
    
    def mostra_opcoes(self):
        print("\n📊 -------- RELATÓRIOS & ESTATÍSTICAS -------- 📊")
        print("1️⃣ - Top Clínicas com mais Atendimentos")
        print("2️⃣ - Atendimentos mais Caros ou Baratos")
        print("3️⃣ - Procedimentos mais Realizados")
        print("4️⃣ - Procedimentos mais Caros ou Baratos")
        print("0️⃣ - Voltar ao Menu Anterior")
        try:
            op = int(input("👉 Escolha uma opção: "))
            return op
        except ValueError:
            return -1

    def mostra_mensagem(self, mensagem):
        print(f"✨ {mensagem}")