# 🩺 Sistema de Gestão de Atendimentos Clínicos
### Disciplina: INE5605 - Desenvolvimento de Sistemas Orientados a Objetos I (Trabalho 1)
### Autores: Lucas dos Santos Ramos e Taylor de Paula Mini

---

## 📋 Sobre o Projeto

Este projeto consiste na implementação de um sistema orientado a objetos em Python voltado para o gerenciamento de clínicas médicas, profissionais da saúde, atendimentos e fluxo de controle financeiro/pagamentos. O desenvolvimento foi estruturado seguindo rigorosamente os padrões de **Arquitetura MVC (Model-View-Controller)**, com forte ênfase em **Programação Defensiva**, **Encapsulamento** e conformidade com os princípios da **UML (Unified Modeling Language)**.

O escopo do sistema abrange desde o cadastro básico de entidades reguladoras e atores do domínio até a execução de regras complexas de negócio, como validação de maioridade de pacientes, restrição de horários de atendimento atrelados ao funcionamento da clínica, fracionamento de parcelas (pagamentos parciais) e emissão de relatórios gerenciais e estatísticos.

---

## 🏗️ Arquitetura do Sistema e Camada de Domínio (Model)

A camada de modelos (`Model`) foi projetada de forma isolada e pura, garantindo que as regras essenciais de consistência fiquem blindadas contra estados inválidos. Abaixo está a discriminação técnica das entidades desenvolvidas para a **Parte 1** do projeto:

### 1. Pessoa (`pessoa.py`)
Entidade central para representação de atores no sistema. Implementa uma relação de **Composição** estrita com a classe abstrata `Papel`. Uma única pessoa física possui uma lista privada de papéis, permitindo o acúmulo dinâmico e consistente de funções (uma mesma pessoa pode atuar simultaneamente como paciente e profissional de saúde).
* **Validações**: Nome, celular e CPF são validados estritamente como instâncias de `str`. A data de nascimento é tratada via `datetime`.
* **Programação Defensiva**: Métodos como `adiciona_papel_paciente` e `adiciona_papel_profissional` utilizam varreduras com `any(isinstance(...))` para mitigar e impedir a duplicidade ilegal de papéis em um mesmo cadastro.

### 2. Papel, PapelPaciente e PapelProfissional (`papel.py`, `papel_paciente.py`, `papel_profissional.py`)
Implementação prática do pilar de **Herança e Abstração**. 
* `Papel` atua como classe abstrata mãe.
* `PapelPaciente` herda de papel de forma limpa, estendendo o comportamento básico.
* `PapelProfissional` estende a classe mãe adicionando os atributos específicos de domínio exigidos pelo enunciado: `reg_profissional` (registro do conselho de classe) e `especialidade`.

### 3. Clinica (`clinica.py`)
Entidade agregadora que representa as unidades físicas de saúde. Gerencia as restrições operacionais de tempo e infraestrutura.
* **Atributos**: Nome, localização (cidade), descrição, `hora_abertura` e `hora_fechamento` (tratados nativamente como `datetime.time`).
* **Relação de Agregação**: Possui uma coleção privada (`__atendimentos`) de consultas agendadas para aquela unidade. Os atendimentos existem de forma independente caso a clínica altere seu escopo.

### 4. Atendimento (`atendimento.py`)
O coração operacional e agregador do domínio. Cruza dinamicamente as referências de Paciente, Profissional, Clínica e Tipo de Atendimento. 
* **Gerenciamento Temporal**: Controlado via `ts_inicio` e `ts_fim` (`datetime`).
* **Consolidação Financeira**: Possui propriedades calculadas em tempo de execução (**Atributos Derivados**):
    * `/ valor_total`: Soma algébrica do valor base do atendimento com todos os custos de procedimentos injetados.
    * `/ valor_pago`: Consolidação dinâmica da soma de todos os pagamentos parciais ou totais liquidados.
    * `/ valor_restante`: Diferença exata entre o total acumulado e o montante já pago.
* **Composição de Procedimentos**: Gerencia em regime de ciclo de vida fechado a fabricação e destruição de seus procedimentos internos.

### 5. Procedimento (`procedimento.py`)
Classe que mapeia os serviços ou intervenções clínicas adicionais realizadas no decorrer de um atendimento específico. Contém descrição, valor (`Decimal`) e a validação do profissional executor responsável.

### 6. Pagamento (`pagamento.py`)
Mapeamento de transações financeiras. Esta entidade foi projetada para atuar sob o conceito de **Snapshot**. No momento de sua instanciação, calcula o saldo devedor atual do atendimento e armazena de forma imutável em `__valor_restante`, registrando historicamente a situação contábil daquele exato segundo de transação.

### 7. MetodoPagamento e Especializações
Abstração utilizando Polimorfismo e Herança para as modalidades de transação financeira exigidas:
* `MetodoPagamento` (Classe Abstrata Mãe).
* `MetodoDinheiro`: Liquidação física simples.
* `MetodoPix`: Especialização que obriga a captura e validação do `cpf_pagador`.
* `MetodoCartao`: Especialização contendo strings validadas de `num_cartao` e `bandeira`.

---

## 🔐 Implementação de Regras de Negócio (Camada Defensiva)

As restrições explícitas determinadas pelo enunciado foram blindadas diretamente no core das entidades (Models), impossibilitando burlar regras por meio de controladores externos:

1.  **Validação de Idade (Maioridade)**: Dentro do `atendimento.paciente.setter`, o sistema executa o cálculo de idade exata comparando o ano, mês e dia da consulta (`ts_inicio.date()`) com o nascimento do paciente. Impede consultas independentes para menores de 18 anos.
2.  **Janela de Funcionamento da Clínica**: O método `adicionar_atendimento` na classe `Clinica` extrai a porção de hora/minuto (`.time()`) do início do atendimento e valida logicamente se está contida na janela fechada determinada por `hora_abertura <= hora_atendimento <= hora_fechamento`.
3.  **Prazo de Pagamento**: O construtor de `Pagamento` impede transações com data posterior (`data.date() > atendimento.ts_inicio.date()`) ao início do atendimento clínico, bloqueando quitações retroativas ilegais.
4.  **Consistência de Papéis**: Setters de `Atendimento` e `Procedimento` verificam ativamente se as instâncias de `Pessoa` fornecidas possuem em suas listas privadas os respectivos objetos `PapelPaciente` ou `PapelProfissional`, bloqueando, por exemplo, que um paciente execute um procedimento ou que um profissional seja agendado sem registro ativo.

---

## 💡 Contexto das Ferramentas e Decisões Técnicas

Para mantermos o projeto alinhado e com padrões de qualidade profissionais, adotamos as seguintes ferramentas e práticas de desenvolvimento:

* **Black (`pyproject.toml`)**: É o nosso formatador de código automático. Ele padroniza o estilo de escrita de arquivos de ambos (espaçamentos, quebras de linha, aspas), evitando conflitos desnecessários de git merge e mantendo uma estética limpa. Configurado com o limite estrito de **88 caracteres** por linha.
* **Flake8 (`.flake8`)**: É a ferramenta de *linting* (análise estática). Funciona como um revisor automático que monitora as diretrizes da **PEP 8**, alertando sobre variáveis declaradas e não utilizadas, imports redundantes ou sintaxes perigosas antes do código ser executado.
* **PEP 257 e Docstrings**: Todas as classes públicas, módulos e métodos complexos foram documentados utilizando docstrings estruturadas no formato *Google Style* (contendo blocos de `Args:` e `Raises:`), garantindo legibilidade e manutenabilidade.

---

## 🎓 Mapeamento de Critérios de Avaliação (Para o Professor)

Este checklist correlaciona os requisitos do plano de ensino com as decisões de engenharia de software aplicadas na entrega:

| Critério de Avaliação | Abordagem e Localização no Código | Status |
| :--- | :--- | :---: |
| **Associação Simples** | `Pagamento` conhece `MetodoPagamento` de forma direta e unidirecional. | Na pasta `/models` | ✅ |
| **Agregação** | `Clinica` possui agregação de `Atendimento` (`self.__atendimentos`). O atendimento pode existir fora do ciclo de vida da clínica. | Na pasta `/models` | ✅ |
| **Composição** | `Pessoa` compõe `Papel` e `Atendimento` compõe `Procedimento`. As partes são instanciadas internamente pelas classes "Todo" (`adiciona_papel_...` e `adiciona_procedimento`). | Na pasta `/models` | ✅ |
| **Herança e Classes Abstratas** | Implementado nas famílias `Papel` (mãe de `PapelPaciente` e `PapelProfissional`) e `MetodoPagamento` (mãe de `MetodoDinheiro`, `MetodoPix`, `MetodoCartao`). | Na pasta `/models` | ✅ |
| **Tratamento de Exceções** | Utilização sistemática de `raise ValueError` nos setters para validação imediata de tipagem (`isinstance`) e lógica de negócio (*Fail-Fast*). | Todos os modelos | ✅ |
| **Utilização correta do MVC** | Camada `Model` totalmente pura. Não possui dependências com rotinas de entrada/saída de dados (`input`/`print`), que serão isoladas nas Views/Controllers na Parte 2. | Estrutura de Pastas | ✅ |

---

## 📁 Estrutura de Pastas (Parte 1)

```text
├── .flake8                  # Configurações do Linter Flake8
├── pyproject.toml           # Configurações do Formatador Black
├── requirements.txt         # Dependências do projeto (black, flake8)
└── src/
    └── models/
        ├── atendimento.py       # Lógica central de consultas e cálculo derivado
        ├── clinica.py           # Gestão de horários de funcionamento e atendimentos
        ├── metodo_pagamento.py  # Classe abstrata e especializações de pagamento
        ├── pagamento.py         # Registro histórico e snapshot contábil
        ├── papel.py             # Abstração de papéis de pessoas
        ├── papel_paciente.py    # Especialização de paciente
        ├── papel_profissional.py # Especialização de profissional de saúde
        ├── pessoa.py            # Composição de papéis e dados cadastrais base
        ├── procedimento.py      # Serviços internos agregados ao atendimento
        └── tipo_atendimento.py  # Enumeração/Cadastro dos tipos de consultas
