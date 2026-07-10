import FreeSimpleGUI as sg

class TelaRelatorio:
    def __init__(self):
        self.__window = None

    def mostra_opcoes(self):
        sg.ChangeLookAndFeel("DarkTeal4")
        layout = [
            [sg.Text("📊 RELATÓRIOS & ESTATÍSTICAS 📊", font=("Helvetica", 18), justification="center")],
            [sg.Text("Escolha a opção desejada:")],
            [sg.Radio("1 - Top Clínicas com mais Atendimentos", "RD1", key=1)],
            [sg.Radio("2 - Atendimentos mais Caros ou Baratos", "RD1", key=2)],
            [sg.Radio("3 - Procedimentos mais Realizados", "RD1", key=3)],
            [sg.Radio("4 - Procedimentos mais Caros ou Baratos", "RD1", key=4)],
            [sg.Radio("0 - Voltar ao Menu Anterior", "RD1", key=0)],
            [sg.Button("Confirmar"), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window("Relatórios", layout, size=(400, 300))
        button, values = self.__window.read()
        self.__window.close()

        if button in (None, 'Cancelar'):
            return 0
        if values:
            for k in range(5):
                if values.get(k):
                    return k
        return 0

    def solicita_top_n(self):
        sg.ChangeLookAndFeel("DarkBlue3")
        layout = [
            [sg.Text("Quantos itens deseja listar no ranking? (Padrão: 3)")],
            [sg.Input(default_text="3", key='-N-')],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Ranking", layout)
        button, values = window.read()
        window.close()
        
        if button in (None, 'Cancelar'):
            return 3
        try:
            return int(values['-N-'])
        except ValueError:
            self.mensagem("Valor inválido! Usando padrão de 3 itens.")
            return 3

    def solicita_ordem(self):
        sg.ChangeLookAndFeel("DarkBlue3")
        layout = [
            [sg.Text("Escolha a ordenação:")],
            [sg.Radio("1 - Mais caros (Decrescente)", "ORD", key=1, default=True)],
            [sg.Radio("2 - Mais baratos (Crescente)", "ORD", key=2)],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Ordenação", layout)
        button, values = window.read()
        window.close()

        if button in (None, 'Cancelar'):
            return 1
        
        if values and values.get(2):
            return 2
        return 1

    def mostra_tabela(self, titulo, headers, rows):
        sg.ChangeLookAndFeel("DarkBlue3")
        layout = [
            [sg.Text(titulo, font=("Helvetica", 16), justification="center")],
            [sg.Table(values=rows, headings=headers, auto_size_columns=True, max_col_width=25,
                      justification='center', num_rows=min(15, max(1, len(rows))))],
            [sg.Button("OK")]
        ]
        window = sg.Window("Resultado", layout, finalize=True)
        window.read()
        window.close()

    def mostra_atendimentos(self, atendimentos):
        headers = ["ID", "Valor (R$)", "Data", "Paciente", "Clínica"]
        rows = [
            [a.id, f"R$ {a.valor_total}", a.ts_inicio.strftime('%d/%m/%Y'), a.paciente.nome, a.clinica.nome] 
            for a in atendimentos
        ]
        self.mostra_tabela("📋 RESULTADO DOS ATENDIMENTOS", headers, rows)

    def mostra_clinicas(self, clinicas):
        headers = ["Clínica", "Total de Atendimentos"]
        rows = [[nome, count] for nome, count in clinicas]
        self.mostra_tabela("🏥 RESULTADO DAS CLÍNICAS", headers, rows)

    def mostra_procedimentos_qtd(self, procedimentos):
        headers = ["Descrição do Procedimento", "Quantidade Realizada"]
        rows = [[desc, count] for desc, count in procedimentos]
        self.mostra_tabela("🔸 PROCEDIMENTOS MAIS REALIZADOS", headers, rows)

    def mostra_procedimentos_valor(self, procedimentos):
        headers = ["Descrição", "Valor (R$)", "Profissional"]
        rows = [
            [p.descricao, f"R$ {p.valor}", p.profissional.nome if p.profissional else "N/A"] 
            for p in procedimentos
        ]
        self.mostra_tabela("🔸 PROCEDIMENTOS POR VALOR", headers, rows)

    def mensagem(self, msg):
        sg.popup(msg)
