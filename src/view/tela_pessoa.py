import FreeSimpleGUI as sg
from typing import List

class TelaPessoa:
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel("DarkTeal4")
        layout = [
            [sg.Text("👥 GERENCIAR PESSOAS 👥", font=("Helvetica", 18), justification="center")],
            [sg.Text("Escolha a opção desejada:")],
            [sg.Radio("1 - Incluir Nova Pessoa", "RD1", key=1)],
            [sg.Radio("2 - Alterar Pessoa Existente", "RD1", key=2)],
            [sg.Radio("3 - Excluir Pessoa", "RD1", key=3)],
            [sg.Radio("4 - Listar Todas as Pessoas", "RD1", key=4)],
            [sg.Radio("5 - Buscar Pessoa por CPF", "RD1", key=5)],
            [sg.Radio("0 - Voltar ao Menu Principal", "RD1", key=0)],
            [sg.Button("Confirmar"), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window("Gerenciar Pessoas", layout, size=(400, 350))

    def mostrar_opcoes(self):
        self.init_components()
        button, values = self.__window.Read()

        opcao = 0
        if values:
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
            elif values[0] or button in (None, 'Cancelar'):
                opcao = 0
        else:
            opcao = 0
        
        self.close()
        return opcao

    def close(self):
        if self.__window:
            self.__window.Close()

    def seleciona_pessoa(self):
        sg.ChangeLookAndFeel("DarkBlue3")
        layout = [
            [sg.Text("🔍 Digite o CPF da pessoa:")],
            [sg.Input(key='-CPF-')],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Selecionar Pessoa", layout)
        
        cpf = ""
        while True:
            event, values = window.read()
            if event in (None, 'Cancelar'):
                break
            if event == "Confirmar":
                cpf = values['-CPF-']
                break
        window.close()
        return cpf

    def mostra_pessoa(self, nome, celular, cpf, data_nascimento, papeis):
        sg.ChangeLookAndFeel("DarkBlue3")
        
        papeis_str = ""
        for papel in papeis:
            if papel["tipo"] == "Paciente":
                papeis_str += "➡️ Papel: 🩺 Paciente\n"
            elif papel["tipo"] == "Profissional":
                papeis_str += "➡️ Papel: 🥼 Profissional da Saúde\n"
                papeis_str += f"   🧾 Registro Profissional (CRM): {papel['reg_profissional']}\n"
                papeis_str += f"   🧬 Especialidade: {papel['especialidade']}\n"
                
        layout = [
            [sg.Text("👤 Dados da Pessoa", font=("Helvetica", 16))],
            [sg.Text(f"Nome: {nome}")],
            [sg.Text(f"Celular: {celular}")],
            [sg.Text(f"CPF: {cpf}")],
            [sg.Text(f"Data de Nascimento: {data_nascimento}")],
            [sg.Multiline(papeis_str, size=(40, 5), disabled=True, no_scrollbar=True)],
            [sg.Button("OK")]
        ]
        window = sg.Window("Pessoa", layout)
        window.read()
        window.close()

    def mostra_papel(self, papel: List[dict]):
        msg = ""
        if papel["tipo"] == "Paciente":
            msg = "➡️ Papel: 🩺 Paciente"
        elif papel["tipo"] == "Profissional":
            msg = "➡️ Papel: 🥼 Profissional da Saúde\n"
            msg += f"🧾 Registro Profissional (CRM): {papel['reg_profissional']}\n"
            msg += f"🧬 Especialidade: {papel['especialidade']}"
        sg.popup(msg, title="Papel")

    def pega_dados_pessoa(self):
        sg.ChangeLookAndFeel("DarkBlue3")
        layout = [
            [sg.Text("📝 Digite os dados da nova pessoa:")],
            [sg.Text("✍️ Nome completo:"), sg.Input(key='-NOME-')],
            [sg.Text("📞 Celular:"), sg.Input(key='-CELULAR-')],
            [sg.Text("🪪 CPF (apenas números):"), sg.Input(key='-CPF-')],
            [sg.Text("📅 Data de Nascimento (dd/mm/aaaa):"), sg.Input(key='-DATA_NASCIMENTO-')],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Dados da Pessoa", layout)
        
        while True:
            event, values = window.read()
            if event in (None, 'Cancelar'):
                window.close()
                return None
            if event == "Confirmar":
                if values['-NOME-'] and values['-CELULAR-'] and values['-CPF-'] and values['-DATA_NASCIMENTO-']:
                    window.close()
                    return {
                        "nome": values['-NOME-'],
                        "celular": values['-CELULAR-'],
                        "cpf": values['-CPF-'],
                        "data_nascimento": values['-DATA_NASCIMENTO-']
                    }
                else:
                    sg.popup_error("⚠️ Todos os campos são obrigatórios!")

    def pega_dados_pessoa_alteracao(self, nome, celular, cpf, data_nascimento):
        sg.ChangeLookAndFeel("DarkBlue3")
        layout = [
            [sg.Text("✏️ Digite os novos dados (deixe em branco para manter o valor atual):")],
            [sg.Text("Nome completo:"), sg.Input(default_text=nome, key='-NOME-')],
            [sg.Text("Celular:"), sg.Input(default_text=celular, key='-CELULAR-')],
            [sg.Text("CPF:"), sg.Input(default_text=cpf, key='-CPF-')],
            [sg.Text("Data de Nascimento:"), sg.Input(default_text=data_nascimento, key='-DATA_NASCIMENTO-')],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Alterar Pessoa", layout)
        
        while True:
            event, values = window.read()
            if event in (None, 'Cancelar'):
                window.close()
                return None
            if event == "Confirmar":
                window.close()
                return {
                    "nome": values['-NOME-'] or nome,
                    "celular": values['-CELULAR-'] or celular,
                    "cpf": values['-CPF-'] or cpf,
                    "data_nascimento": values['-DATA_NASCIMENTO-'] or data_nascimento
                }

    def mostra_mensagem(self, mensagem):
        sg.popup(f"✨ {mensagem}")

    def confirma_exclusao(self, nome):
        resposta = sg.popup_yes_no(f"❓ Tem certeza absoluta que deseja excluir a pessoa '{nome}'?", title="Confirmar Exclusão")
        return resposta == "Yes"

    def seleciona_tipo_papel(self):
        sg.ChangeLookAndFeel("DarkBlue3")
        layout = [
            [sg.Text("💼 Selecione o papel para esta pessoa:")],
            [sg.Radio("1 - Paciente", "RD1", key=1)],
            [sg.Radio("2 - Profissional da Saúde", "RD1", key=2)],
            [sg.Button("Confirmar"), sg.Cancel('Cancelar')]
        ]
        window = sg.Window("Selecionar Papel", layout)
        
        opcao = None
        event, values = window.read()
        if event == "Confirmar":
            if values[1]:
                opcao = 1
            elif values[2]:
                opcao = 2
        window.close()
        return opcao

    def pega_dados_papel_profissional(self):
        sg.ChangeLookAndFeel("DarkBlue3")
        layout = [
            [sg.Text("🥼 Digite as informações do profissional:")],
            [sg.Text("🧾 Registro Profissional (CRM/etc):"), sg.Input(key='-REG-')],
            [sg.Text("🧬 Especialidade médica:"), sg.Input(key='-ESP-')],
            [sg.Button("Confirmar"), sg.Cancel('Cancelar')]
        ]
        window = sg.Window("Dados do Profissional", layout)
        
        reg_profissional = ""
        especialidade = ""
        event, values = window.read()
        if event == "Confirmar":
            reg_profissional = values['-REG-']
            especialidade = values['-ESP-']
        window.close()
        return reg_profissional, especialidade

    def confirma_alteracao_papel(self, nome):
        resposta = sg.popup_yes_no(f"❓ Deseja alterar os papéis da pessoa '{nome}'?", title="Alterar Papéis")
        return resposta == "Yes"

    def mostrar_opcoes_papeis(self):
        sg.ChangeLookAndFeel("DarkBlue3")
        layout = [
            [sg.Text("⚙️ -- Gerenciar Papéis da Pessoa --")],
            [sg.Radio("1 - Adicionar Papel", "RD1", key=1)],
            [sg.Radio("2 - Remover Papel", "RD1", key=2)],
            [sg.Radio("0 - Concluir e Voltar", "RD1", key=0)],
            [sg.Button("Confirmar"), sg.Cancel('Cancelar')]
        ]
        window = sg.Window("Gerenciar Papéis", layout)
        
        opcao = -1
        event, values = window.read()
        if event == "Confirmar":
            if values[1]:
                opcao = 1
            elif values[2]:
                opcao = 2
            elif values[0]:
                opcao = 0
        window.close()
        return opcao

    def listar_pessoas(self, pessoas_dados):
        sg.ChangeLookAndFeel("DarkBlue3")
        
        headers = ["Nome", "Celular", "CPF", "Nascimento", "Papéis"]
        rows = []

        for p in pessoas_dados:
            rows.append([
                p["nome"],
                p["celular"],
                p["cpf"],
                p["nascimento"],
                p["papeis"]
            ])

        layout = [
            [sg.Text("📋 PESSOAS CADASTRADAS", font=("Helvetica", 16), justification="center")],
            [sg.Table(values=rows, headings=headers, max_col_width=35, auto_size_columns=True,
                      justification='center', num_rows=min(20, len(rows)), key='-TABLE-')],
            [sg.Button("OK")]
        ]

        window = sg.Window("Lista de Pessoas", layout, finalize=True)
        window.read()
        window.close()
