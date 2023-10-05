use biblioteca;

SELECT * FROM Autor;

/*
======================ADICONANDO UMA RESTRIÇAO PARA O EMAIL========================
ALTER TABLE Usuario ADD CONSTRAINT emailUnico UNIQUE (email);
ALTER TABLE Autor ADD CONSTRAINT cpfUnico UNIQUE(cpf);
/*

/*
======================EDITANDO REGISTRO NA TABELA DO AUTO===========================
UPDATE Autor
SET cpf = 635
WHERE AutorID = 4;

SELECT * FROM Autor;
*/

/**/
