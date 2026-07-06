# T2 - TODO List e Divisão de Trabalho (50%/50%) - VERSÃO TURBINADA

## Objetivo
Refatorar o sistema do Trabalho 1 para incluir:
- Interface gráfica com FreeSimpleGUI
- Persistência em arquivo com pickle e padrão DAO
- CRUD completo para cadastros e registros de negócio
- Relatórios consolidados
- Modelagem UML e submissão validada por commits individuais
---

## Tarefas do projeto

### 👨‍💻 Atribuições - Lucas (Base MVC + Cadastros)
- [ ] Criar a estrutura inicial do projeto T2, separando pacotes de view, controller e DAO.
- [ ] Implementar o `ControladorPrincipal` com padrão Singleton (usando `__new__`) e o método `run()` para abrir a GUI inicial.
- [ ] DAO: Implementar o `PessoaDAO`, `ClinicaDAO` e `TipoAtendimentoDAO` (Lembrete: validar o tipo do objeto com `isinstance` no método `add` da classe filha antes de repassar para o `super().add()`).
- [ ] GUI: Implementar as telas (`PessoaView`, `ClinicaView`, `TipoAtendimentoView`) garantindo a estrutura padrão com `__init__()`, `init_components()`, `open()`, `close()` e `show_message()`.
- [ ] GUI: Implementar o cadastro explícito de pacientes e profissionais dentro da view de pessoa, de forma separada ou bem identificada.
- [ ] GUI/Controller: Implementar listagem, edição e exclusão para as telas de cadastro, não apenas o cadastro inicial.
- [ ] Controller: Integrar os controladores de cadastros com suas respectivas Views e DAOs.

### 👨‍💻 Atribuições - Taylor (Base DAO + Transações/Relatórios)
- [ ] Implementar a tela inicial/menu principal do sistema com FreeSimpleGUI, permitindo o acesso às funcionalidades do T2.
- [ ] Criar a classe abstrata `DAO` com `_datasource`, `_cache`, `_dump()` e `_load()`.
- [ ] Implementar na classe abstrata `DAO` os métodos `add()`, `get_all()`, `get()` e `remove()`. **Regra de ouro:** usar a abordagem EAFP (`try/except KeyError`) no `get` e `remove` em vez de checar com `if`.
- [ ] DAO: Implementar o `AtendimentoDAO`, `ProcedimentoDAO` e `PagamentoDAO` (Lembrete: validar com `isinstance` no método `add` antes do `super().add()`).
- [ ] GUI: Implementar as telas de Atendimento, Procedimento, Pagamento e Relatórios usando a mesma estrutura base das Views (`__init__()`, `init_components()`, `open()`, `close()`, `show_message()`).
- [ ] Controller: Integrar os controladores transacionais com as Views, DAOs e garantir a preservação das regras de negócio originais do T1.
