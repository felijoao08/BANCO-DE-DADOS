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


SELECT
	aluno.nome as Nome,
    curso.nome as Curso,
    curso.campus as Campus,
    anexo1.historico as Historico
FROM
	pei
		INNER JOIN
	aluno on pei.matriculaAluno = aluno.matricula
		INNER JOIN
	curso on aluno.codigoCurso = curso.codigo
		INNER JOIN
	anexo1 on anexo1.numeroPei = pei.numero
	*/
    
/*
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
	aluno.matricula = '99999999';
*/




SELECT
	curso.nome AS nome_curso,
	curso.nivelEnsino AS Nive_de_Ensino,
    curso.coordenador AS coordenador,
    aluno.nome AS nome_aluno,
    aluno.necessidadesEspecificas AS necessidades_Especificas,
    aluno.matricula As matricula,
    equipeMultiDisciplinar.nome AS Equipe_nome,
    equipeMultiDisciplinar.funcao AS funcao, 
    anexo1.historico AS historico,
    anexo1.conhecimentosHabilidades AS conhecimentos_habilidades,
    anexo1.dificuldades As dificuldades,
    anexo1.observacoes AS observacoes,
    anexo2.disciplina AS disciplina,
    anexo2.docente AS docente,
	anexo2.objetivosPlanoDisciplina AS OPD,
    anexo2.objetivosAdaptacoesDisciplina AS OAD,
    anexo2.conteudoPlanoDisciplina AS CPD,
    anexo2.conteudoAdaptacoesDisciplina AS CAD,
    anexo2.metodologiaPlanoDisciplina AS MPD, 
    anexo2.metodologiaAdaptacoesDisciplina AS MAD,
    anexo2.recursoDidaticoPlanoDisciplina AS RDPD,
    anexo2.recursoDidaticoAdaptacoesDisciplina AS RDAD, 
    anexo2.avaliacaoPlanoDisciplina AS APD,
    anexo2.avaliacaoAdaptacoesDisciplina AS AAD,
    anexo3.avancos AS avancos,
    anexo3.parecer AS parecer,
    
    