import FreeSimpleGUI as sg

class TelaAtendimento:
    def __init__(self):
        pass

    def mostra_mensagem(self, mensagem: str):
        sg.popup(mensagem)

    def pega_dados_atendimento(self):
        sg.ChangeLookAndFeel("DarkBlue3")
        layout = [
            [sg.Text("Novo Atendimento / Consulta", font=("Helvetica", 16))],
            [sg.Text("Data Início (dd/mm/aaaa HH:MM):"), sg.Input(key='ts_inicio')],
            [sg.Text("Data Fim (dd/mm/aaaa HH:MM):"), sg.Input(key='ts_fim')],
            [sg.Text("Valor Base (R$):"), sg.Input(key='valor')],
            [sg.Text("ID Tipo Atendimento:"), sg.Input(key='tipo_atendimento')],
            [sg.Text("CPF Paciente:"), sg.Input(key='cpf_paciente')],
            [sg.Text("CPF Profissional:"), sg.Input(key='cpf_profissional')],
            [sg.Text("ID Clínica:"), sg.Input(key='id_clinica')],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Dados", layout)
        while True:
            event, values = window.read()
            if event in (None, 'Cancelar'):
                window.close()
                return None
            if event == 'Confirmar':
                if not all(values.values()):
                    sg.popup_error("Preencha todos os campos.")
                    continue
                window.close()
                return values

    def seleciona_atendimento(self):
        layout = [
            [sg.Text("Selecionar Atendimento", font=("Helvetica", 16))],
            [sg.Text("ID do Atendimento:"), sg.Input(key='id')],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Selecionar", layout)
        event, values = window.read()
        window.close()
        if event in (None, 'Cancelar'):
            return -1
        try:
            return int(values['id'])
        except ValueError:
            self.mostra_mensagem("ID inválido!")
            return -1

    def pega_dados_atendimento_alteracao(self, ts_inicio, ts_fim, valor, tipo_atendimento, cpf_paciente, cpf_profissional, id_clinica):
        layout = [
            [sg.Text("Alterar Atendimento", font=("Helvetica", 16))],
            [sg.Text("Data Início:"), sg.Input(default_text=ts_inicio, key='ts_inicio')],
            [sg.Text("Data Fim:"), sg.Input(default_text=ts_fim, key='ts_fim')],
            [sg.Text("Valor Base:"), sg.Input(default_text=valor, key='valor')],
            [sg.Text("ID Tipo Atendimento:"), sg.Input(default_text=tipo_atendimento, key='tipo_atendimento')],
            [sg.Text("CPF Paciente:"), sg.Input(default_text=cpf_paciente, key='cpf_paciente')],
            [sg.Text("CPF Profissional:"), sg.Input(default_text=cpf_profissional, key='cpf_profissional')],
            [sg.Text("ID Clínica:"), sg.Input(default_text=id_clinica, key='id_clinica')],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Alterar", layout)
        event, values = window.read()
        window.close()
        if event in (None, 'Cancelar'):
            return None
        return values

    def mostra_menu_procedimentos(self):
        layout = [
            [sg.Text("Gerenciar Procedimentos", font=("Helvetica", 16))],
            [sg.Radio("1 - Incluir Novo Procedimento", "RD1", key=1)],
            [sg.Radio("2 - Alterar Procedimento Existente", "RD1", key=2)],
            [sg.Radio("3 - Excluir Procedimento", "RD1", key=3)],
            [sg.Radio("4 - Listar Procedimentos", "RD1", key=4)],
            [sg.Radio("0 - Voltar", "RD1", key=0)],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Procedimentos", layout)
        event, values = window.read()
        window.close()
        if event in (None, 'Cancelar'):
            return 0
        if values:
            for k in range(5):
                if values.get(k): return k
        return 0

    def pega_dados_procedimento(self):
        layout = [
            [sg.Text("Novo Procedimento", font=("Helvetica", 16))],
            [sg.Text("Descrição:"), sg.Input(key='descricao')],
            [sg.Text("Valor (R$):"), sg.Input(key='valor')],
            [sg.Text("CPF Profissional:"), sg.Input(key='cpf_profissional')],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Dados Procedimento", layout)
        event, values = window.read()
        window.close()
        if event in (None, 'Cancelar'): return None
        return values

    def seleciona_procedimento(self, procedimentos):
        proc_str = "\n".join(procedimentos)
        layout = [
            [sg.Text("Procedimentos Vinculados:\n" + proc_str)],
            [sg.Text("ID do Procedimento:"), sg.Input(key='id')],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Selecionar Procedimento", layout)
        event, values = window.read()
        window.close()
        if event in (None, 'Cancelar'): return None
        try:
            return int(values['id'])
        except ValueError:
            self.mostra_mensagem("ID inválido!")
            return None

    def mostra_procedimentos(self, procedimentos):
        if not procedimentos:
            self.mostra_mensagem("Nenhum procedimento encontrado neste atendimento.")
            return

        sg.ChangeLookAndFeel("DarkBlue3")
        headers = ["ID", "Descrição", "Valor", "Profissional"]
        rows = []
        for p in procedimentos:
            rows.append([
                p.id,
                p.descricao,
                f"R$ {p.valor}",
                p.profissional.nome if p.profissional else "N/A"
            ])
            
        layout = [
            [sg.Text("📋 PROCEDIMENTOS 📋", font=("Helvetica", 16), justification="center")],
            [sg.Table(values=rows, headings=headers, auto_size_columns=True, max_col_width=25,
                      justification='center', num_rows=min(15, len(rows)))],
            [sg.Button("OK")]
        ]
        window = sg.Window("Lista de Procedimentos", layout, finalize=True)
        window.read()
        window.close()

    def pega_dados_procedimento_alteracao(self, descricao, valor, cpf_profissional):
        layout = [
            [sg.Text("Alterar Procedimento", font=("Helvetica", 16))],
            [sg.Text("Descrição:"), sg.Input(default_text=descricao, key='descricao')],
            [sg.Text("Valor (R$):"), sg.Input(default_text=valor, key='valor')],
            [sg.Text("CPF Profissional:"), sg.Input(default_text=cpf_profissional, key='cpf_profissional')],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Alterar Procedimento", layout)
        event, values = window.read()
        window.close()
        if event in (None, 'Cancelar'): return None
        return values

    def mostra_atendimento(self, id, ts_inicio, ts_fim, valor, tipo_atendimento, paciente_nome, profissional_nome, clinica_nome, procedimentos, pagamentos, valor_total, valor_pago):
        texto = f"ID: #{id}\n"
        texto += f"Início: {ts_inicio}\nFim: {ts_fim}\n"
        texto += f"Valor Base: R$ {valor}\nTipo: {tipo_atendimento.nome}\n"
        texto += f"Paciente: {paciente_nome}\nProfissional: {profissional_nome}\n"
        texto += f"Clínica: {clinica_nome}\n\nProcedimentos:\n"
        texto += "\n".join(procedimentos) if procedimentos else "(Nenhum)"
        texto += "\n\nPagamentos:\n"
        texto += "\n".join(pagamentos) if pagamentos else "(Nenhum)"
        texto += f"\n\nValor Total: R$ {valor_total}\nValor Pago: R$ {valor_pago}"
        
        layout = [[sg.Multiline(texto, size=(60, 20), disabled=True)], [sg.Button("OK")]]
        window = sg.Window("Detalhes Atendimento", layout)
        window.read()
        window.close()

    def opcoes_listar_atendimentos(self):
        layout = [
            [sg.Text("Buscar Atendimentos", font=("Helvetica", 16))],
            [sg.Radio("1 - Todos", "RD1", key=1)],
            [sg.Radio("2 - Por Paciente (CPF)", "RD1", key=2)],
            [sg.Radio("3 - Por Profissional (CPF)", "RD1", key=3)],
            [sg.Radio("4 - Por Clínica (ID)", "RD1", key=4)],
            [sg.Radio("5 - Por Datas", "RD1", key=5)],
            [sg.Radio("0 - Voltar", "RD1", key=0)],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Listar", layout)
        event, values = window.read()
        window.close()
        if event in (None, 'Cancelar'): return 0
        if values:
            for k in range(6):
                if values.get(k): return k
        return 0

    def listar_atendimentos(self, atendimentos):
        if not atendimentos:
            self.mostra_mensagem("Nenhum atendimento encontrado.")
            return

        sg.ChangeLookAndFeel("DarkBlue3")
        headers = ["ID", "Início", "Fim", "Tipo", "Paciente", "Profissional", "Clínica", "Valor Total", "Valor Pago"]
        rows = []
        for a in atendimentos:
            rows.append([
                a.id,
                a.ts_inicio.strftime("%d/%m/%Y %H:%M"),
                a.ts_fim.strftime("%d/%m/%Y %H:%M"),
                a.tipo_atendimento.nome,
                a.paciente.nome,
                a.profissional.nome,
                a.clinica.nome,
                f"R$ {a.valor_total}",
                f"R$ {a.valor_pago}"
            ])
            
        layout = [
            [sg.Text("📋 ATENDIMENTOS 📋", font=("Helvetica", 16), justification="center")],
            [sg.Table(values=rows, headings=headers, auto_size_columns=True, max_col_width=20,
                      justification='center', num_rows=min(20, len(rows)))],
            [sg.Button("OK")]
        ]
        window = sg.Window("Lista de Atendimentos", layout, finalize=True)
        window.read()
        window.close()

    def tela_opcoes(self):
        sg.ChangeLookAndFeel("DarkTeal4")
        layout = [
            [sg.Text("Gerenciar Atendimentos", font=("Helvetica", 18), justification="center")],
            [sg.Radio("1 - Mostrar Detalhes", "RD1", key=1)],
            [sg.Radio("2 - Excluir Atendimento", "RD1", key=2)],
            [sg.Radio("3 - Listar Atendimentos", "RD1", key=3)],
            [sg.Radio("4 - Incluir Atendimento", "RD1", key=4)],
            [sg.Radio("5 - Alterar Atendimento", "RD1", key=5)],
            [sg.Radio("6 - Gerenciar Procedimentos", "RD1", key=6)],
            [sg.Radio("7 - Registrar Pagamento", "RD1", key=7)],
            [sg.Radio("0 - Voltar ao Menu Principal", "RD1", key=0)],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Atendimentos", layout, size=(400, 350))
        event, values = window.read()
        window.close()
        if event in (None, 'Cancelar'): return 0
        if values:
            for k in range(8):
                if values.get(k): return k
        return 0

    def pega_dados_pagamento(self):
        sg.ChangeLookAndFeel("DarkBlue3")
        layout = [
            [sg.Text("Registrar Pagamento", font=("Helvetica", 16))],
            [sg.Text("Valor (R$):"), sg.Input(key='valor')],
            [sg.Text("Data (dd/mm/aaaa):"), sg.Input(key='data')],
            [sg.Text("Método de Pagamento:")],
            [sg.Radio("Pix", "RD_PAG", key='pix', enable_events=True),
             sg.Radio("Cartão", "RD_PAG", key='cartao', enable_events=True),
             sg.Radio("Dinheiro", "RD_PAG", key='dinheiro', enable_events=True, default=True)],
            [sg.Text("Chave PIX:", key='lbl_pix1', visible=False), sg.Input(key='chave_pix', visible=False)],
            [sg.Text("Tipo da Chave:", key='lbl_pix2', visible=False), sg.Input(key='tipo_chave', visible=False)],
            [sg.Text("Número do Cartão:", key='lbl_car1', visible=False), sg.Input(key='numero_cartao', visible=False)],
            [sg.Text("Bandeira:", key='lbl_car2', visible=False), sg.Input(key='bandeira', visible=False)],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Pagamento", layout)
        
        while True:
            event, values = window.read()
            if event in (None, 'Cancelar'):
                window.close()
                return None
                
            if event in ('pix', 'cartao', 'dinheiro'):
                is_pix = values['pix']
                is_car = values['cartao']
                
                window['lbl_pix1'].update(visible=is_pix)
                window['chave_pix'].update(visible=is_pix)
                window['lbl_pix2'].update(visible=is_pix)
                window['tipo_chave'].update(visible=is_pix)
                
                window['lbl_car1'].update(visible=is_car)
                window['numero_cartao'].update(visible=is_car)
                window['lbl_car2'].update(visible=is_car)
                window['bandeira'].update(visible=is_car)
                continue
                
            if event == "Confirmar":
                metodo = 3
                if values['pix']: metodo = 1
                elif values['cartao']: metodo = 2
                
                dados = {
                    "valor": values['valor'],
                    "data": values['data'],
                    "metodo": metodo,
                    "chave_pix": values.get('chave_pix', ''),
                    "tipo_chave": values.get('tipo_chave', ''),
                    "numero_cartao": values.get('numero_cartao', ''),
                    "bandeira": values.get('bandeira', '')
                }
                window.close()
                return dados

    def pega_cpf_paciente(self):
        return self._input_dialog("CPF Paciente", "CPF do paciente:")

    def pega_cpf_profissional(self):
        return self._input_dialog("CPF Profissional", "CPF do profissional:")

    def pega_id_clinica(self):
        val = self._input_dialog("ID Clínica", "ID da clínica:")
        try: return int(val) if val else -1
        except: return -1

    def pega_data_inicio(self):
        return self._input_dialog("Data Início", "Data de início (dd/mm/aaaa):")

    def pega_data_fim(self):
        return self._input_dialog("Data Fim", "Data de fim (dd/mm/aaaa):")
        
    def _input_dialog(self, title, text):
        layout = [[sg.Text(text)], [sg.Input(key='val')], [sg.Button("Confirmar"), sg.Button("Cancelar")]]
        window = sg.Window(title, layout)
        event, values = window.read()
        window.close()
        if event in (None, 'Cancelar'): return None
        return values['val']
