import FreeSimpleGUI as sg
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
        print("1 - Mais caros (Decrescente)")
        print("2 - Mais baratos (Crescente)")
        try:
            ordem = int(input("👉 Escolha a ordem: "))
            return ordem
        except ValueError:
            return 1

    def mostra_atendimentos(self, atendimentos):
        print("\n📋 ==== RESULTADO DOS ATENDIMENTOS ====")
        for atendimento in atendimentos:
            print(f"🔹 {atendimento}")

    def mostra_clinicas(self, clinicas):
        print("\n📋 ==== RESULTADO DAS CLÍNICAS ====")
        for clinica in clinicas:
            print(f"🏥 {clinica}")

    def mostra_procedimentos(self, procedimentos):
        print("\n📋 ==== RESULTADO DOS PROCEDIMENTOS ====")
        for procedimento in procedimentos:
            print(f"🔸 {procedimento}")

    def mostra_opcoes(self):
        print("\n📊 -------- RELATÓRIOS & ESTATÍSTICAS -------- 📊")
        print("1 - Top Clínicas com mais Atendimentos")
        print("2 - Atendimentos mais Caros ou Baratos")
        print("3 - Procedimentos mais Realizados")
        print("4 - Procedimentos mais Caros ou Baratos")
        print("0 - Voltar ao Menu Anterior")
        try:
            op = int(input("👉 Escolha uma opção: "))
            return op
        except ValueError:
            return -1

    def mensagem(self, msg):
        sg.popup(msg)
    
    def close(self):
        self.__window.Close()

    def open(self):
        evento, valores = self.__window.read()
        return evento, valores

    
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

        self.__window = sg.Window("SisClinicas", layout, size=(400, 300))

