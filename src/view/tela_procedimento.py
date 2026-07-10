import FreeSimpleGUI as sg

class TelaProcedimento:
    def __init__(self):
        pass

    def pega_dados_procedimento(self):
        sg.ChangeLookAndFeel("DarkBlue3")
        layout = [
            [sg.Text("Novo Procedimento", font=("Helvetica", 16))],
            [sg.Text("Descrição:"), sg.Input(key='-DESCRICAO-')],
            [sg.Text("Valor:"), sg.Input(key='-VALOR-')],
            [sg.Text("CPF do Profissional:"), sg.Input(key='-CPF_PROFISSIONAL-')],
            [sg.Button("Salvar"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Dados do Procedimento", layout)

        while True:
            event, values = window.read()
            if event in (None, 'Cancelar'):
                window.close()
                return None
            if event == "Salvar":
                if not values['-DESCRICAO-'] or not values['-VALOR-'] or not values['-CPF_PROFISSIONAL-']:
                    sg.popup_error("Nenhum campo pode ficar vazio.")
                    continue
                window.close()
                return {
                    "descricao": values['-DESCRICAO-'],
                    "valor": values['-VALOR-'],
                    "profissional": values['-CPF_PROFISSIONAL-']
                }

    def seleciona_procedimento(self):
        sg.ChangeLookAndFeel("DarkBlue3")
        layout = [
            [sg.Text("Selecionar Procedimento", font=("Helvetica", 16))],
            [sg.Text("ID do Procedimento:"), sg.Input(key='-ID-')],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Selecionar", layout)
        event, values = window.read()
        window.close()
        
        if event in (None, 'Cancelar'):
            return None
            
        try:
            return int(values['-ID-'])
        except ValueError:
            self.show_message("O ID deve ser um número inteiro.")
            return None

    def show_message(self, msg):
        sg.popup(msg)
