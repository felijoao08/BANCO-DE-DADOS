use enapne;

/*TODAS AS INFORMAÇOES DOS 3 ANEXOS DE DETERMINADO ALUNO

SELECT 
	aluno.nome AS Nome_do_Aluno,
    anexo1.*,
    anexo2.* ,
    anexo3.*
FROM
	pei
		INNER JOIN 
	aluno ON pei.matriculaAluno = aluno.matricula
    	INNER JOIN 
	anexo1 ON anexo1.numeroPei = pei.numero
		INNER JOIN 
	anexo2 ON anexo2.numeroPei = pei.numero
    	INNER JOIN 
	anexo3 ON anexo3.numeroPei = pei.numero
WHERE
	aluno.matricula = 22222222;

*/

/*INFROMAÇOES DE CURSO DE DETERMINADO ALUNO
SELECT
	aluno.nome as NomeDoAluno,
    curso.nome as Curso,
    curso.coordenador as coordebadorCurso,
    curso.campus as Campus,
    curso.nivelEnsino as NivelDeEnsino
FROM
	curso
		INNER JOIN
    aluno ON aluno.codigoCurso = curso.codigo
WHERE
	aluno.matricula = '33333333'
*/


/*INFORMAÇOES DE ACOMPANHAMENTO DE DETERINADO ALUNO
SELECT 
	aluno.nome AS NOME_ALUNO,
    acompanhamento.*
FROM
	pei
		INNER JOIN
	aluno ON aluno.matricula = pei.matriculaAluno
		INNER JOIN
	anexo2 ON pei.numero = anexo2.numeroPei
		INNER JOIN
	acompanhamento ON anexo2.id = acompanhamento.idAnexo2 
WHERE 
	aluno.matricula = '22222222'
*/