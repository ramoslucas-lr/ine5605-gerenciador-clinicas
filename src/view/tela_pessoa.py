from typing import List

from models.papel_paciente import PapelPaciente
from models.papel_profissional import PapelProfissional


class TelaPessoa:
    def __init__(self):
        pass

    def mostrar_opcoes(self):
        print("---- PESSOAS ----")
        print("1 - Incluir pessoa")
        print("2 - Alterar pessoa")
        print("3 - Excluir pessoa")
        print("4 - Listar pessoas")
        print("5 - Buscar pessoa")
        print("0 - Voltar")

        opcao = int(input("Escolha uma opção: "))
        return opcao

    def seleciona_pessoa(self):
        cpf = input("Digite o CPF da pessoa: ")
        return cpf

    def mostra_pessoa(self, nome, celular, cpf, data_nascimento, papeis):
        print(f"Nome: {nome}")
        print(f"Celular: {celular}")
        print(f"CPF: {cpf}")
        print(f"Data de Nascimento: {data_nascimento}")
        for papel in papeis:
            self.mostra_papel(papel)

    def mostra_papel(self, papel: List[dict]):
        print(f"Papel: {papel['tipo']}")
        if papel['tipo'] == 'Profissional':
            print(f"Registro Profissional: {papel['reg_profissional']}")
            print(f"Especialidade: {papel['especialidade']}")

    def pega_dados_pessoa(self):
        nome = input("Digite o nome da pessoa: ")
        celular = input("Digite o celular da pessoa: ")
        cpf = input("Digite o CPF da pessoa: ")
        data_nascimento = input("Digite a data de nascimento da pessoa (dd/mm/aaaa): ")

        if nome and celular and cpf and data_nascimento:
            return {
                "nome": nome,
                "celular": celular,
                "cpf": cpf,
                "data_nascimento": data_nascimento,
            }
        else:
            print("Todos os campos são obrigatórios.")
            return None

    def pega_dados_pessoa_alteracao(self, nome, celular, cpf, data_nascimento):
        nome = input(f"Digite o nome da pessoa [{nome}]: ") or nome
        celular = (
            input(f"Digite o celular da pessoa [{celular}]: ") or celular
        )
        cpf = input(f"Digite o CPF da pessoa [{cpf}]: ") or cpf
        data_nascimento = (
            input(
                f"Digite a data de nascimento da pessoa (dd/mm/aaaa) [{data_nascimento}]: "
            )
            or data_nascimento
        )

        return {
            "nome": nome,
            "celular": celular,
            "cpf": cpf,
            "data_nascimento": data_nascimento,
        }

    def pega_parametros_paginacao(self):
        try:
            page = int(input("Digite o número da página: "))
            return page
        except ValueError:
            print("Por favor, digite números válidos para número da página.")
            return None

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def confirma_exclusao(self, nome):
        resposta = input(
            f"Tem certeza que deseja excluir a pessoa {nome}? (s/n): "
        )
        return resposta.lower() == "s"

    def seleciona_tipo_papel(self):
        print("Selecione o tipo de papel:")
        print("1 - Paciente")
        print("2 - Profissional")
        try:
            opcao = int(input("Escolha uma opção: "))
            return opcao
        except ValueError:
            print("Por favor, digite um número válido.")
            return None

    def pega_dados_papel_profissional(self):
        reg_profissional = input("Digite o registro profissional: ")
        especialidade = input("Digite a especialidade: ")
        return reg_profissional, especialidade

    def confirma_alteracao_papel(self, nome):
        resposta = input(f"Deseja alterar os papéis da pessoa {nome}? (s/n): ")
        return resposta.lower() == "s"

    def mostrar_opcoes_papeis(self):
        print("1 - Adicionar papel")
        print("2 - Remover papel")
        print("0 - Voltar")
        opcao = int(input("Escolha uma opção: "))
        return opcao

    def mostra_menu_pagina(self):
        print("Digite 'n' para próxima página, 'p' para página anterior ou outra tecla para voltar.")
        resposta = input("Digite sua escolha: ")
        return resposta