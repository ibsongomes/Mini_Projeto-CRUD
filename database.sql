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