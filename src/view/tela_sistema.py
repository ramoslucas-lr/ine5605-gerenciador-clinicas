import FreeSimpleGUI as sg

class TelaSistema:
    def __init__(self):
        self.__window = None
        self.init_components()

    def tela_opcoes(self):
        self.init_components()
        button, values = self.__window.Read()

        opcao = 0
        print(values)
        if values[1]:
            opcao = 1
        elif values[2]:
            opcao = 2
        elif values[3]:
            opcao = 3
        elif values[4]:
            opcao = 4
        elif values[5]:
            opcao = 5
        elif values[0] or button in (None,'Cancelar'):
            opcao = 0
        
        self.close()

        return opcao

    def mensagem(self, msg):
        print(f"✨ {msg}")
    
    def close(self):
        self.__window.Close()
    
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
