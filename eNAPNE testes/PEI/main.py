from flask import Flask,  request, jsonify, render_template, redirect, flash, session


import mysql.connector
 
app = Flask(__name__)
app.config['SECRET_KEY'] = "568425806"

db = mysql.connector.connect (
    host = 'localhost',
    user = "root",
    password = 'felipe09',
    database = "enapne"
)


#CADASTRO:PAGINA 1
@app.route('/')
def paginaCadastro():
   return render_template('cadastro.html')
@app.route('/cadastro', methods=['POST'])
def cadastro():
    #requisiçoes do curso
    codigo_curso = request.form.get('codigo_curso')
    nome_curso = request.form.get('Curso_nome')
    coordenador = request.form.get('coordenador')
    campus = request.form.get('campus')
    nivel_ensino = request.form.get('nivel_ensino')
    #requisiçoes do aluno
    nome_aluno = request.form.get('nome_aluno')
    matricula_aluno = request.form.get('matricula_aluno')
    codigo_curso_aluno = request.form.get('codigo_curso_aluno')
    Nessessidades_especificas= request.form.get('NEE')
    #requisiçao do numero do pei
    numero_pei = request.form.get('numero_pei')
    #requisiçoes da equipe multidisciplinar
    codigo_equipe = request.form.get('codigo_equipe')
    nome_equipe = request.form.get('nome_equipe')
    funçao_equipe = request.form.get('funçao_equipe')
    numero_pei_equipe = request.form.get('numero_pei_equipe')


    #aqui irei cadastrar os dados na tabela curso
    cursor = db.cursor(dictionary=True)
    cursor.execute("INSERT INTO curso (codigo, nome, coordenador, campus, nivelEnsino) VALUES (%s, %s, %s, %s, %s)", (codigo_curso, nome_curso, coordenador, campus, nivel_ensino))
    #aqui irei cadastrar os dados na tabela aluno
    cursor.execute("INSERT INTO aluno (matricula, nome, codigoCurso, necessidadesEspecificas) VALUES (%s, %s, %s, %s)", ( matricula_aluno, nome_aluno, codigo_curso_aluno, Nessessidades_especificas))
    #aqui irei inserir os dados na tabela pei
    cursor.execute("INSERT INTO pei (numero, matriculaAluno) VALUES  (%s, %s)", (numero_pei, matricula_aluno))
    #aqui irei inserir os dados na tabela da equipe multidisciplinar
    cursor.execute("INSERT INTO equipeMultiDisciplinar(codigo, nome, funcao, numeroPei) VALUES (%s, %s, %s, %s)", (codigo_equipe, nome_equipe, funçao_equipe, numero_pei_equipe))
    db.commit()
    cursor.close()
    return redirect('/anexoI')


#ANEXO I: PAGINA 2
@app.route('/anexoI')
def paginaAnexoI():
   return render_template('anexoI.html')
@app.route('/anexoI', methods=['POST'])
def anexoI():
    cursor = db.cursor(dictionary=True)
    #requisiçao do numero pei
    numero_pei_anexoI = request.form.get('numero_pei_anexoI')
    #requisiçao do historico escolar
    Hpe_estudante = request.form.get('HPE-estudante')
    #requisiçao CHCI
    Conhecimentos_Habilidades_Capacidades = request.form.get('CHCIN')
    #requisiçao dificuldades apresentadas
    Dificuadades_apresentadas = request.form.get('Dificuadades-apresentadas')
    #requisiçao observaçoes
    observaçoes = request.form.get('observaçoes')
    

    #aqui irei inserir os dados do anexo I
    cursor.execute("INSERT INTO anexo1 (numeroPei, historico, conhecimentosHabilidades, dificuldades, observacoes ) VALUES (%s, %s, %s, %s, %s)", (numero_pei_anexoI, Hpe_estudante, Conhecimentos_Habilidades_Capacidades, Dificuadades_apresentadas, observaçoes))
    db.commit()
    cursor.close()
    return redirect('/anexoII')


#ANEXO II: PAGINA 3
@app.route('/anexoII')
def paginaAnexoII():
   return render_template('anexoII.html')
@app.route('/anexoII', methods=['POST'])
def anexoII():
    cursor = db.cursor(dictionary=True)
    #requisiçao do numero do pei
    numero_pei_anexoII = request.form.get('numero_pei_anexoII')
    #requisiçao do componente curricular/disciplina
    Componente_Curricular_Disciplina= request.form.get('CC-D')
    #requisiçao do docente
    Docente = request.form.get('Docente')
    #Objetivos
    Objetivos = request.form.get('Objetivos')
    Adaptaçõeso_objetivo = request.form.get('Adaptaçõeso-objetivo')
    #Conteúdos Programáticos 
    ConteúdosProgramáticos = request.form.get('ConteúdosProgramáticos')
    ConteúdosProgramáticosAdaptaçoes = request.form.get('ConteúdosProgramáticosAdaptaçoes')
    #Metodologias
    Metodologias = request.form.get('Metodologias')
    MetodologiasAdaptaçoes = request.form.get('MetodologiasAdaptaçoes')
    #Recursos Didáticos
    RecursosDidáticos = request.form.get('RecursosDidáticos')
    RecursosDidáticosAdaptaçoes = request.form.get('RecursosDidáticosAdaptaçoes')
    #avaliaçao, plano da disciplina
    Avaliaçao_PlanoDisciplina = request.form.get('Avaliaçao_PlanoDisciplina')
    Avaliaçao_PlanoDisciplinaAdaptaçoes = request.form.get('Avaliaçao_PlanoDisciplinaAdaptaçoes')

    #aqui irei inserir os dados do anexo II
    cursor.execute("INSERT INTO anexo2 (numeroPei, disciplina, docente, objetivosPlanoDisciplina, objetivosAdaptacoesDisciplina, conteudoPlanoDisciplina, conteudoAdaptacoesDisciplina, metodologiaPlanoDisciplina, metodologiaAdaptacoesDisciplina, recursoDidaticoPlanoDisciplina, recursoDidaticoAdaptacoesDisciplina, avaliacaoPlanoDisciplina, avaliacaoAdaptacoesDisciplina) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (numero_pei_anexoII, Componente_Curricular_Disciplina, Docente, Objetivos, Adaptaçõeso_objetivo, ConteúdosProgramáticos, ConteúdosProgramáticosAdaptaçoes, Metodologias, MetodologiasAdaptaçoes, RecursosDidáticos, RecursosDidáticosAdaptaçoes, Avaliaçao_PlanoDisciplina, Avaliaçao_PlanoDisciplinaAdaptaçoes ))
    db.commit()
    cursor.close()
    return redirect('/anexoIII')


#ANEXO III: PAGINA 4
@app.route('/anexoIII')
def paginaAnexoIII():
   return render_template('anexoIII.html')
@app.route('/anexoIII', methods=['POST'])
def anexoIII():
    cursor = db.cursor(dictionary=True)
    #requisiçao do numero pei
    numero_pei_anexoIII = request.form.get('numero_pei_anexoIII')
    #requisiçao Descrever avanços do/a estudante durante o acompanhamento de elaboração e execução do PEI.
    Descrever_avanços_estudante = request.form.get('DAEDAEEpei')
    #requisiçao PARECER DA EQUIPE MULTIPROFISSIONAL
    parecer_equipe = request.form.get('PEM')

    #aqui irei guardar os dados do anexo 3
    cursor.execute("INSERT INTO anexo3 (numeroPei, avancos, parecer) VALUES (%s, %s, %s)", (numero_pei_anexoIII, Descrever_avanços_estudante, parecer_equipe))
    db.commit()
    cursor.close()
    return redirect('/')




if __name__ == '__main__':
    app.run(debug=True)