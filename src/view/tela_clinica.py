import FreeSimpleGUI as sg

class TelaClinica:
    def __init__(self):
        self.__window = None
        self.init_components()

    def mostrar_opcoes(self):
        self.init_components()
        button, values = self.__window.Read()

        opcao = 0
        if button in (None, 'Cancelar'):
            opcao = 0
        elif values:
            if values.get(1):
                opcao = 1
            elif values.get(2):
                opcao = 2
            elif values.get(3):
                opcao = 3
            elif values.get(4):
                opcao = 4
            elif values.get(0):
                opcao = 0
        
        self.close()

        return opcao

    def mensagem(self, msg):
        sg.popup(msg)

    def close(self):
        self.__window.Close()
    
    def init_components(self):
        sg.ChangeLookAndFeel("DarkTeal4")

        layout = [
            [sg.Text("🏥 Gerenciar Clínicas 🏥", font=("Helvetica", 18), justification="center")],
            [sg.Text("Escolha a opção desejada:")],
            [sg.Radio("1 - Incluir Nova Clínica", "RD1", key=1)],
            [sg.Radio("2 - Listar Clínicas", "RD1", key=2)],
            [sg.Radio("3 - Alterar Clínica", "RD1", key=3)],
            [sg.Radio("4 - Excluir Clínica", "RD1", key=4)],
            [sg.Radio("0 - Voltar", "RD1", key=0)],
            [sg.Button("Confirmar"), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window("Gerenciar Clínicas", layout, size=(400, 300))

    def pega_dados_clinica(self):
        sg.theme("DarkBlue3")

        layout = [
            [sg.Text("Nova Clínica", font=("Helvetica", 16), justification="center")],
            [sg.Text("ID:"), sg.Input(key='-ID-')],
            [sg.Text("Nome:"), sg.Input(key='-NOME-')],
            [sg.Text("Localização:"), sg.Input(key='-LOCALIZACAO-')],
            [sg.Text("Descrição:"), sg.Input(key='-DESCRICAO-')],
            [sg.Text("Hora de Abertura (HH:MM):"), sg.Input(key='-HORA_ABERTURA-')],
            [sg.Text("Hora de Fechamento (HH:MM):"), sg.Input(key='-HORA_FECHAMENTO-')],
            [sg.Button("Salvar"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Dados da Clínica", layout, size=(400, 250))

        while True:
            event, values = window.read()
            if event in (None, 'Cancelar'):
                break
            if event == "Salvar":
                try:
                    id_clinica = int(values['-ID-'])
                    if not values['-NOME-'] or not values['-LOCALIZACAO-'] or not values['-DESCRICAO-'] or not values['-HORA_ABERTURA-'] or not values['-HORA_FECHAMENTO-']:
                        sg.popup_error("Nenhum campo pode ficar vazio.")
                        continue
                    window.close()
                    return {
                        "id": id_clinica,
                        "nome": values['-NOME-'],
                        "localizacao": values['-LOCALIZACAO-'],
                        "descricao": values['-DESCRICAO-'],
                        "hora_abertura": values['-HORA_ABERTURA-'],
                        "hora_fechamento": values['-HORA_FECHAMENTO-']
                    }
                except ValueError:
                    sg.popup_error("O ID deve ser um número inteiro.")
        
        window.close()
        return None

    def listar_clinicas(self, clinicas):
        if len(clinicas) == 0:
            sg.popup("Nenhuma clínica cadastrada.")
            return

        sg.ChangeLookAndFeel("DarkBlue3")
        
        headers = ["ID", "Nome", "Localização", "Descrição", "Horário"]
        rows = []

        for clinica in clinicas:
            horario = f"{clinica.hora_abertura.strftime('%H:%M')} - {clinica.hora_fechamento.strftime('%H:%M')}"
            rows.append([
                clinica.id,
                clinica.nome,
                clinica.localizacao,
                clinica.descricao,
                horario
            ])

        layout = [
            [sg.Text("📋 CLÍNICAS CADASTRADAS", font=("Helvetica", 16), justification="center")],
            [sg.Table(values=rows, headings=headers, max_col_width=25, auto_size_columns=True,
                      justification='center', num_rows=min(20, len(rows)), key='-TABLE-')],
            [sg.Button("OK")]
        ]

        window = sg.Window("Lista de Clínicas", layout, finalize=True)
        window.read()
        window.close()
    
    def mostra_mensagem(self, msg):
        sg.popup(msg)
        
    def seleciona_clinica(self):
        sg.ChangeLookAndFeel("DarkBlue3")
        layout = [
            [sg.Text("Selecionar Clínica", font=("Helvetica", 16))],
            [sg.Text("ID da Clínica:", size=(15, 1)), sg.InputText('', key='id')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        window = sg.Window('Selecionar', layout)
        button, values = window.Read()
        window.Close()
        if button in (None, 'Cancelar'):
            return None
        try:
            return int(values['id'])
        except ValueError:
            self.mostra_mensagem("ID deve ser um número inteiro")
            return None