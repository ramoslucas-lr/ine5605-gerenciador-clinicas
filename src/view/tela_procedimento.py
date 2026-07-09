import FreeSimpleGUI as sg

class TelaProcedimento:
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
