CREATE DATABASE biblioteca;
USE biblioteca;

CREATE TABLE Autor (
	autorID INT auto_increment primary key,
    nome VARCHAR(150) NOT NULL,
    cpf INT NOT NULL
);

CREATE TABLE Editora (
	editoraID INT auto_increment primary key,
    nome VARCHAR(150) NOT NULL,
    telefone VARCHAR(13),
    endereco varchar(150)
);

CREATE TABLE Livro (
    livroID INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    ano INT NOT NULL,
    autorID INT NOT NULL,
    editoraID INT NOT NULL,
    foreign key(autorID) REFERENCES Autor(autorID),
    foreign key(editoraID) REFERENCES Editora(editoraID)
);

CREATE TABLE Usuario (
	userID INT auto_increment primary key,
    nome VARCHAR(150) NOT NULL,
    email VARCHAR(150) NOT NULL,
    telefone VARCHAR(150) NOT NULL,
    endereco VARCHAR(150) NOT NULL   
);

CREATE TABLE Emprestimo(
	emprestimoID INT auto_increment primary key,
    userID INT,
    livroID INT,
    DataEmprestimo DATE,
    DataDevolucao DATE,
    foreign key(userID) REFERENCES Usuario(userID),
    foreign key(livroID) REFERENCES Livro(livroID)
);