# Sistema-de-Matricula (Python + SQLite)

Sistema robusto de gestão academica (CRUD) desenvolvido em Python puro, com foco em fundamentos de Engenharia de dados, persistência relacional e arquitetura modular.

## Arquitetura do Projeto

O projeto foi desenvolvido em três camadas lógicas para facilitar a manutenção e escalabilidade:
* **`main.py`**: Interface de utilizador (CLI) e orquestação de fluxo de execução.
* **`banco_dados.py`**: Camada de persistência, gestão de execuções seguras com SQLite e rotinas de migração de dados.
* **`validacoes.py`**: Motor de regas de negócio, sanitização de inputs (Engenharia Defensiva) e cálculo em tempo real.

## Funcionalidades e Práticas de Engenharia Aplicadas

* **CRUD Completo**: Criação, Leitura, Atualização e Exclusão de registros acadêmicos.
* **Sanitização de Dados**:Tratamento silencioso de inputs (remoção de pontuação de CPFs, conversão dinâmica de datas, formatação de strings).
* **Catálogo Fechado (Normalização)**: Mapeamento inteligente de inputs do utilizador para padronização de cursos na base de dados.
* **Tratamento de Exceções Avançado**: Prevenção de falhas (Crash Prevention) e libertação controlada de recursos do S.O. (blocos `try/finally`).
* **Auditoria e Logs**: Rastreamento de operações críticas (Insert, Update, Delete) gravadas automaticamente no ficheiro `sistema.log` utilizando a biblioteca nativa `logging`.
* **Migração Automática (Data Cleanup)**: Rotinas que padronizam dados inconsistentes gerados em versões anteriores do sistema.

## ⚙️ Como Executar

O sistema não possui dependências externas, utilizando apenas a biblioteca padrão do Python.

1. Clone o repositório:
   ```bash
   git clone [https://github.com/Gustavo-nauan/Sistema-de-Matricula.git](https://github.com/Gustavo-nauan/Sistema-de-Matricula.git)