from datetime import datetime

from view.tela_pessoa import TelaPessoa
from models.pessoa import Pessoa
from models.papel_paciente import PapelPaciente
from models.papel_profissional import PapelProfissional
from models.tipo_papel import TipoPapel
from dao.pessoa_dao import PessoaDAO


class ControladorPessoa:
    def __init__(self, controlador_sistema):
        self.__pessoa_dao = PessoaDAO()
        self.__controlador_sistema = controlador_sistema
        self.__tela_pessoa = TelaPessoa()

    def buscar_pessoa(self, cpf):
        return self.__pessoa_dao.get(cpf)

    def mostrar_pessoa(self):
        cpf = self.__tela_pessoa.seleciona_pessoa()
        pessoa = self.buscar_pessoa(cpf)

        if pessoa is not None:
            data_nascimento_str = pessoa.data_nascimento.strftime("%d/%m/%Y")
            papeis_list = []
            for papel in pessoa.papeis:
                if isinstance(papel, PapelPaciente):
                    papeis_list.append({"tipo": "Paciente"})
                elif isinstance(papel, PapelProfissional):
                    papeis_list.append(
                        {
                            "tipo": "Profissional",
                            "reg_profissional": papel.reg_profissional,
                            "especialidade": papel.especialidade,
                        }
                    )
            self.__tela_pessoa.mostra_pessoa(
                pessoa.nome,
                pessoa.celular,
                pessoa.cpf,
                data_nascimento_str,
                papeis_list,
            )
        else:
            self.__tela_pessoa.mostra_mensagem("Pessoa não encontrada.")

    def incluir_pessoa(self):
        dados_pessoa = self.__tela_pessoa.pega_dados_pessoa()

        if dados_pessoa is not None:
            if self.buscar_pessoa(dados_pessoa["cpf"]) is None:
                try:
                    data_nascimento = datetime.strptime(
                        dados_pessoa["data_nascimento"], "%d/%m/%Y"
                    )
                except ValueError:
                    self.__tela_pessoa.mostra_mensagem("Data de nascimento inválida.")
                    return

                pessoa = Pessoa(
                    dados_pessoa["nome"],
                    dados_pessoa["celular"],
                    dados_pessoa["cpf"],
                    data_nascimento,
                )
                self.__pessoa_dao.add(pessoa)
                self.__tela_pessoa.mostra_mensagem("Pessoa incluída com sucesso.")

                while True:
                    tipo_papel = self.__tela_pessoa.seleciona_tipo_papel()

                    if tipo_papel == TipoPapel.PACIENTE.value:
                        pessoa.adicionar_papel_paciente()
                        break
                    elif tipo_papel == TipoPapel.PROFISSIONAL.value:
                        reg_profissional, especialidade = (
                            self.__tela_pessoa.pega_dados_papel_profissional()
                        )
                        pessoa.adicionar_papel_profissional(
                            reg_profissional, especialidade
                        )
                        break
                    else:
                        print("Papel inválido. Nenhum papel adicionado.")
                        continue

            else:
                self.__tela_pessoa.mostra_mensagem(
                    "CPF já cadastrado. Tente novamente."
                )

    def alterar_pessoa(self):
        cpf = self.__tela_pessoa.seleciona_pessoa()
        pessoa = self.buscar_pessoa(cpf)

        if pessoa is not None:
            data_nascimento_str = pessoa.data_nascimento.strftime("%d/%m/%Y")
            dados_pessoa = self.__tela_pessoa.pega_dados_pessoa_alteracao(
                pessoa.nome, pessoa.celular, pessoa.cpf, data_nascimento_str
            )

            if dados_pessoa is not None:
                pessoa.nome = dados_pessoa["nome"]
                pessoa.celular = dados_pessoa["celular"]
                data_nascimento = dados_pessoa["data_nascimento"]
                if isinstance(dados_pessoa["data_nascimento"], str):
                    try:
                        data_nascimento = datetime.strptime(
                            dados_pessoa["data_nascimento"], "%d/%m/%Y"
                        )
                    except ValueError:
                        self.__tela_pessoa.mostra_mensagem(
                            "Data de nascimento inválida."
                        )
                        return
                pessoa.data_nascimento = data_nascimento
                pessoa.cpf = dados_pessoa["cpf"]

                alterar_papeis = self.__tela_pessoa.confirma_alteracao_papel(
                    pessoa.nome
                )
                if alterar_papeis:
                    self.abre_menu_papeis(pessoa)

                self.__pessoa_dao.update(pessoa)

                self.__tela_pessoa.mostra_mensagem("Pessoa alterada com sucesso.")
        else:
            self.__tela_pessoa.mostra_mensagem("Pessoa não encontrada.")

    def excluir_pessoa(self):
        cpf = self.__tela_pessoa.seleciona_pessoa()
        pessoa = self.buscar_pessoa(cpf)

        if pessoa is not None:
            confirma = self.__tela_pessoa.confirma_exclusao(pessoa.nome)
            if confirma:
                self.__pessoa_dao.remove(cpf)
            self.__tela_pessoa.mostra_mensagem("Pessoa excluída com sucesso.")
        else:
            self.__tela_pessoa.mostra_mensagem("Pessoa não encontrada.")

    def listar_pessoas(self):
        pessoas_list = list(self.__pessoa_dao.get_all())
        
        if not pessoas_list:
            self.__tela_pessoa.mostra_mensagem("Nenhuma pessoa cadastrada.")
            return

        dados_pessoas = []
        for pessoa in pessoas_list:
            data_nascimento_str = pessoa.data_nascimento.strftime("%d/%m/%Y")
            papeis_str = []
            for papel in pessoa.papeis:
                if isinstance(papel, PapelPaciente):
                    papeis_str.append("Paciente")
                elif isinstance(papel, PapelProfissional):
                    papeis_str.append(f"Profissional ({papel.especialidade})")
            
            dados_pessoas.append({
                "nome": pessoa.nome,
                "cpf": pessoa.cpf,
                "celular": pessoa.celular,
                "nascimento": data_nascimento_str,
                "papeis": ", ".join(papeis_str)
            })

        self.__tela_pessoa.listar_pessoas(dados_pessoas)

    def retorna_tela(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.incluir_pessoa,
            2: self.alterar_pessoa,
            3: self.excluir_pessoa,
            4: self.listar_pessoas,
            5: self.mostrar_pessoa,
            0: self.retorna_tela,
        }

        while True:
            opcao_escolhida = self.__tela_pessoa.mostrar_opcoes()

            if opcao_escolhida in opcoes:
                opcoes[opcao_escolhida]()
            else:
                self.__tela_pessoa.mostra_mensagem("Opção inválida. Tente novamente.")

    def abre_menu_papeis(self, pessoa):
        opcoes = {
            1: self.adicionar_papel,
            2: self.remover_papel,
        }

        while True:

            opcao_escolhida = self.__tela_pessoa.mostrar_opcoes_papeis()

            if opcao_escolhida in opcoes:
                opcoes[opcao_escolhida](pessoa)
            elif opcao_escolhida == 0:
                break
            else:
                self.__tela_pessoa.mostra_mensagem("Opção inválida. Tente novamente.")

    def adicionar_papel(self, pessoa):
        tipo_papel = self.__tela_pessoa.seleciona_tipo_papel()
        try:
            if tipo_papel == TipoPapel.PACIENTE.value:
                pessoa.adicionar_papel_paciente()
                self.__tela_pessoa.mostra_mensagem("Papel de paciente adicionado.")
            elif tipo_papel == TipoPapel.PROFISSIONAL.value:
                reg_profissional, especialidade = (
                    self.__tela_pessoa.pega_dados_papel_profissional()
                )
                pessoa.adicionar_papel_profissional(reg_profissional, especialidade)
                self.__tela_pessoa.mostra_mensagem(
                    "Papel de profissional da saúde adicionado."
                )
            else:
                self.__tela_pessoa.mostra_mensagem(
                    "Papel inválido. Nenhum papel adicionado."
                )
        except ValueError as e:
            self.__tela_pessoa.mostra_mensagem(f"Erro ao adicionar papel: {e}")

    def remover_papel(self, pessoa):
        tipo_papel = self.__tela_pessoa.seleciona_tipo_papel()
        if tipo_papel == TipoPapel.PACIENTE.value:
            papel = next(
                (p for p in pessoa.papeis if isinstance(p, PapelPaciente)), None
            )
            if papel:
                pessoa.remover_papel(papel)
        elif tipo_papel == TipoPapel.PROFISSIONAL.value:
            papel = next(
                (p for p in pessoa.papeis if isinstance(p, PapelProfissional)), None
            )
            if papel:
                pessoa.remover_papel(papel)
