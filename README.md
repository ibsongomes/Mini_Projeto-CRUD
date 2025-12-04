# Mini_Projeto-CRUD

Este é um mini projeto desenvolvido para fazer um CRUD utilizando Python e o MySQL Workbench.

Este projeto foi realizado por [Ibson](https://github.com/ibsongomes), [Gabriel](https://github.com/GABRIELR48O) e [Rodrigo](https://github.com/rodrigocesar12309-droid).


## O que é um CRUD?

**CRUD** é um acrônimo, onde:

- C - Crate (Criar)
- R - Read (Ler)
- U - Update (Atualizar)
- D - Delete (Excluir)

Ou seja, A função do CRUD é permitir criar, consultar, atualizar e excluir dados de um sistema de forma organizada e padronizada.

## Sobre o Projeto

O objetivo é fazer um sistema simples de CRUD para cadastro de funcionários que permite registrar e gerenciar os dados: nome, cargo, salário, setor, telefone, email e data de admissão, com interface gráfica.

Neste projeto foi utilizado o Python, Tkinter (biblioteca nativa do Python), Mysql-Connector-Python (biblioteca não nativa do Python), Mysql, e 3 arquivos diferentes para a integridade do código.

#### REQUISITOS PARA RODAR O CRUD:

- Instalar Python;
- Instalar o Mysql Server e o Mysql Workbench;
- Instalar o VsCode;
- Instalar a biblioteca mysql-connector-python no terminal;

#### FUNCIONALIDADES:

- Cadastrar funcionários (nome, cargo, salário, setor, telefone, email, data de admissão).
- Listar todos os funcionários em uma tabela.
- Buscar por ID e carregar os dados de funcionários já existentes no formulário.
- Atualizar campos específicos de um funcionário já cadastrado.
- Deletar funcionário por ID (com confirmação).

#### BANCO DE DADOS:

Para criar o banco de dados, você deve executar esses comandos no Mysql Workbench:
```
CREATE DATABASE empresa;
USE empresa;

CREATE TABLE funcionarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    cargo VARCHAR(100),
    salario DECIMAL(10,2),
    setor VARCHAR(100),
    telefone VARCHAR(30),
    email VARCHAR(150),
    data_admissao DATE
);
```
