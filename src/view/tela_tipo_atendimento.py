import FreeSimpleGUI as sg

class TelaTipoAtendimento:
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel("DarkTeal4")
        layout = [
            [sg.Text("📋 GERENCIAR TIPOS DE ATENDIMENTO 📋", font=("Helvetica", 18), justification="center")],
            [sg.Text("Escolha a opção desejada:")],
            [sg.Radio("1 - Incluir Novo Tipo", "RD1", key=1)],
            [sg.Radio("2 - Listar Tipos", "RD1", key=2)],
            [sg.Radio("3 - Alterar Tipo", "RD1", key=3)],
            [sg.Radio("4 - Excluir Tipo", "RD1", key=4)],
            [sg.Radio("0 - Voltar", "RD1", key=0)],
            [sg.Button("Confirmar"), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window("Tipos de Atendimento", layout, size=(400, 250))

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

    def close(self):
        if self.__window:
            self.__window.Close()

    def pega_dados_tipo_atendimento(self):
        sg.ChangeLookAndFeel("DarkBlue3")
        layout = [
            [sg.Text("Novo Tipo de Atendimento", font=("Helvetica", 16))],
            [sg.Text("ID:"), sg.Input(key='-ID-')],
            [sg.Text("Nome:"), sg.Input(key='-NOME-')],
            [sg.Text("Código:"), sg.Input(key='-CODIGO-')],
            [sg.Text("Descrição:"), sg.Input(key='-DESCRICAO-')],
            [sg.Button("Salvar"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Dados do Tipo de Atendimento", layout)

        while True:
            event, values = window.read()
            if event in (None, 'Cancelar'):
                window.close()
                return None
            if event == "Salvar":
                try:
                    id_tipo = int(values['-ID-'])
                    nome = values['-NOME-'].strip()
                    codigo = values['-CODIGO-'].strip()
                    descricao = values['-DESCRICAO-'].strip()

                    if nome == "" or codigo == "" or descricao == "":
                        sg.popup_error("Nenhum campo pode ficar vazio.")
                        continue

                    window.close()
                    return {
                        "id": id_tipo,
                        "nome": nome,
                        "codigo": codigo,
                        "descricao": descricao
                    }
                except ValueError:
                    sg.popup_error("O ID deve ser um número inteiro.")

    def mostra_mensagem(self, mensagem):
        sg.popup(mensagem)

    def listar_tipos_atendimento(self, tipos):
        if len(tipos) == 0:
            sg.popup("Nenhum tipo de atendimento cadastrado.")
            return

        sg.ChangeLookAndFeel("DarkBlue3")
        
        headers = ["ID", "Nome", "Código", "Descrição"]
        rows = []

        for tipo in tipos:
            rows.append([
                tipo.id,
                tipo.nome,
                tipo.codigo,
                tipo.descricao
            ])

        layout = [
            [sg.Text("📋 TIPOS DE ATENDIMENTO", font=("Helvetica", 16), justification="center")],
            [sg.Table(values=rows, headings=headers, max_col_width=35, auto_size_columns=True,
                      justification='center', num_rows=min(20, len(rows)), key='-TABLE-')],
            [sg.Button("OK")]
        ]

        window = sg.Window("Lista de Tipos", layout, finalize=True)
        window.read()
        window.close()

    def seleciona_tipo(self):
        sg.ChangeLookAndFeel("DarkBlue3")
        layout = [
            [sg.Text("Selecionar Tipo", font=("Helvetica", 16))],
            [sg.Text("ID do Tipo:", size=(15, 1)), sg.InputText('', key='id')],
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