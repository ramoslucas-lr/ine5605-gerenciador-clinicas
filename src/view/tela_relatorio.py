class TelaRelatorio:
    def __init__(self):
        pass

    def solicita_top_n(self):
        top_n = int(input("Quantos itens deseja listar? "))
        return top_n
    
    def solicita_ordem(self):
        print("1 - Mais caros")
        print("2 - Mais baratos")
        ordem = int(input("Escolha a ordem: "))
        return ordem
    
    def mostra_atendimentos(self, atendimentos):
        for atendimento in atendimentos:
            print(atendimento)
    
    def mostra_procedimentos(self, procedimentos):
        for procedimento in procedimentos:
            print(procedimento)
    
    def mostra_opcoes(self):
        print("--- Relatórios ---")
        print("1 - Top clínicas com mais atendimentos")
        print("2 - Atendimentos mais caros ou baratos")
        print("3 - Procedimentos mais realizados")
        print("4 - Procedimentos mais caros ou baratos")
        print("0 - Voltar")
        op = int(input("Escolha uma opção: "))
        return op

    def mostra_mensagem(self, mensagem):
        print(mensagem)