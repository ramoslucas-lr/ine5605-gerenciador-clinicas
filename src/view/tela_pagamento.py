import FreeSimpleGUI as sg


class TelaPagamento:

    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel("DarkTeal4")

        layout = [
            [sg.Text("Cadastro de Pagamento", font=("Helvetica", 16))],

            [sg.Text("Código:"), sg.Input(key="codigo")],

            [sg.Text("Código do Atendimento:"), sg.Input(key="atendimento")],

            [sg.Text("Valor:"), sg.Input(key="valor")],

            [sg.Text("Forma de Pagamento:"),
             sg.Combo(
                 ["Dinheiro", "Pix", "Cartão de Débito", "Cartão de Crédito"],
                 key="forma",
                 readonly=True
             )],

            [sg.Text("Data:"), sg.Input(key="data")],

            [sg.Button("Salvar"),
             sg.Button("Cancelar")]
        ]

        self.__window = sg.Window("Pagamento", layout)

    def open(self):
        evento, valores = self.__window.read()
        return evento, valores

    def close(self):
        self.__window.close()

    def mensagem(self, msg):
        sg.popup(msg)

    def pega_dados_pagamento(self):
        evento, valores = self.open()

        if evento in (sg.WIN_CLOSED, "Cancelar"):
            self.close()
            return None

        dados = {
            "codigo": valores["codigo"],
            "atendimento": valores["atendimento"],
            "valor": valores["valor"],
            "forma": valores["forma"],
            "data": valores["data"]
        }

        self.close()

        return dados
