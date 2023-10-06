USE biblioteca;
CREATE TABLE Autor (
	autorID INT auto_increment primary key,
    nome VARCHAR(150) NOT NULL,
    telefone VARCHAR(13),
    cpf INT NOT NULL
);

CREATE TABLE Editora (
	editoraID INT auto_increment primary key,
    nome VARCHAR(150) NOT NULL,
    telefone VARCHAR(13)
);

CREATE TABLE Livro (
	livroID INT auto_increment primary key,
    nome VARCHAR(150) NOT NULL,
	num_pag INT NOT NULL,
    autorID INT,
    editoraID INT,
    foreign key(autorID) REFERENCES Autor(autorID),
    foreign key(editoraID) REFERENCES Editora(editoraID)
);

CREATE TABLE Usuario (
	usuarioID INT auto_increment primary key,
    nome VARCHAR(150) NOT NULL,
    telefone VARCHAR(13),
    email VARCHAR(150),
	endereco VARCHAR(500)
);

CREATE TABLE Emprestimo (
	emprestimo INT auto_increment primary key,
    livroID INT,
    usuarioID INT,
	foreign key(livroID) REFERENCES Livro(livroID),
    foreign key(usuarioID) REFERENCES Usuario(usuarioID)
);