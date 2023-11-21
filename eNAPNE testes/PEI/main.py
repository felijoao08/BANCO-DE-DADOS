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



#GERAR DOCUMENTAÇAO PEI: PAGINA 5
@app.route('/pei')
def paginapei():
   return render_template('pdf.html')
@app.route('/pei', methods=['POST'])
def pei():
    #Aqui irei pegar as informaçoes de determinado aluno pela matricula
    cursor = db.cursor(dictionary=True)
    matriculaPDF = request.form.get('matriculaPDF')
    #aqui irei verificar qual a açao do botao
    açao = request.form['açao']
    #executando a açao ao clicar no botao analisar aluno
    if açao == 'Procurar':
        cursor.execute("select aluno.nome, aluno.necessidadesEspecificas FROM aluno WHERE aluno.matricula = %s", (matriculaPDF,))
        aluno = cursor.fetchall()
        try:
            nome_aluno = aluno
        except:
            nome_aluno = 'Não há aluno corrrespondente a está matricula.'
        db.commit()
        cursor.close()
        return render_template('pdf.html', nome_aluno=nome_aluno)
    #executando a açao ao clicar no botao de gerar pei
    elif açao == 'Gerar-Pei':
        #pegando a matricula de determinado aluno
        matricula = request.form.get('confirmar_matricula')
        #Aqui irei coletar todas as informaçoes da documentaçao e guardar de forma organizada para gerar o pei
        cursor.execute("SELECT curso.nome AS nome_curso, curso.nivelEnsino AS Nive_de_Ensino, curso.coordenador AS coordenador, aluno.nome AS nome_aluno, aluno.necessidadesEspecificas AS necessidades_Especificas, aluno.matricula As matricula, equipeMultiDisciplinar.nome AS Equipe_nome, equipeMultiDisciplinar.funcao AS funcao, anexo1.historico AS historico, anexo1.conhecimentosHabilidades AS conhecimentos_habilidades, anexo1.dificuldades As dificuldades, anexo1.observacoes AS observacoes, anexo2.disciplina AS disciplina, anexo2.docente AS docente, anexo2.objetivosPlanoDisciplina AS OPD, anexo2.objetivosAdaptacoesDisciplina AS OAD, anexo2.conteudoPlanoDisciplina AS CPD, anexo2.conteudoAdaptacoesDisciplina AS CAD, anexo2.metodologiaPlanoDisciplina AS MPD,  anexo2.metodologiaAdaptacoesDisciplina AS MAD, anexo2.recursoDidaticoPlanoDisciplina AS RDPD, anexo2.recursoDidaticoAdaptacoesDisciplina AS RDAD, anexo2.avaliacaoPlanoDisciplina AS APD, anexo2.avaliacaoAdaptacoesDisciplina AS AAD, anexo3.avancos AS avancos, anexo3.parecer AS parecer FROM curso INNER JOIN aluno ON aluno.codigoCurso = curso.codigo INNER JOIN pei ON aluno.matricula = pei.matriculaAluno INNER JOIN equipeMultidisciplinar ON equipeMultidisciplinar.numeroPei = pei.numero INNER JOIN anexo1 ON anexo1.numeroPei = pei.numero INNER JOIN anexo2 ON anexo2.numeroPei = pei.numero INNER JOIN anexo3 ON anexo3.numeroPei = pei.numero WHERE aluno.matricula =%s", (matricula,))
        dados_pei = cursor.fetchall()
        try:
            Nivel_ensino = dados_pei[0]['Nive_de_Ensino']
            Nome_estudante = dados_pei[0]['nome_aluno']
            Nome_curso = dados_pei[0]['nome_curso']
            Necessidades_Educacionais_Específicas = dados_pei[0]['necessidades_Especificas']
            Equipe_multiprofissional_responsável_nome = dados_pei[0]['Equipe_nome']
            Equipe_multiprofissional_responsável_funcao = dados_pei[0]['funcao']
            hsitorico = dados_pei[0]['historico']
            Conhecimentos_Habilidades_Capacidades = dados_pei[0]['conhecimentos_habilidades']
            Dificuldades_apresentadas = dados_pei[0]['dificuldades']
            observacoes = dados_pei[0]['observacoes']
            Componente_Curricular_Disciplina = dados_pei[0]['disciplina']
            Docente = dados_pei[0]['docente']
            Objetivos = dados_pei[0]['OPD']
            adaptaçoes_objetivos = dados_pei[0]['OAD']
            Conteúdos_Programáticos = dados_pei[0]['CPD']
            Conteúdos_Programáticos_Adaptacoes = dados_pei[0]['CAD']
            Metodologias = dados_pei[0]['MPD']
            Metodologias_Adaptacoes = dados_pei[0]['MAD']
            Recursos_Didáticos = dados_pei[0]['RDPD']
            Recursos_Didáticos_Adaptacoes = dados_pei[0]['RDAD']
            Avaliações = dados_pei[0]['APD']
            Avaliações_Adaptacoes = dados_pei[0]['AAD']
            Acompanhamento  = 'Qualquer informaçao pois nao sei como cadastrar esta tabela'
            avancos = dados_pei[0]['avancos']
            parecer = dados_pei[0]['parecer']
            matricula_aluno = dados_pei[0]['matricula']
            coordenador = dados_pei[0]['coordenador']
            equipe_Napene = 'qualque informaçao...'
            contextualizaçao = 'qualquer informaçao'
        except:
            erro = 'Não há aluno com está matricula'
            return render_template('Pdf.html', erro=erro)
        db.commit()
        cursor.close()
        return render_template('testes.html', dados_pei=dados_pei, Nivel_ensino=Nivel_ensino, Nome_estudante=Nome_estudante, Nome_curso=Nome_curso, Necessidades_Educacionais_Específicas=Necessidades_Educacionais_Específicas, Equipe_multiprofissional_responsável_nome=Equipe_multiprofissional_responsável_nome,  Equipe_multiprofissional_responsável_funcao= Equipe_multiprofissional_responsável_funcao, hsitorico=hsitorico, Conhecimentos_Habilidades_Capacidades=Conhecimentos_Habilidades_Capacidades, Dificuldades_apresentadas=Dificuldades_apresentadas,  observacoes=observacoes, Componente_Curricular_Disciplina=Componente_Curricular_Disciplina, Docente=Docente, Objetivos=Objetivos, adaptaçoes_objetivos=adaptaçoes_objetivos, Conteúdos_Programáticos=Conteúdos_Programáticos, Conteúdos_Programáticos_Adaptacoes=Conteúdos_Programáticos_Adaptacoes,  Metodologias=Metodologias, Metodologias_Adaptacoes=Metodologias_Adaptacoes, Recursos_Didáticos=Recursos_Didáticos, Recursos_Didáticos_Adaptacoes=Recursos_Didáticos_Adaptacoes, Avaliações=Avaliações, Avaliações_Adaptacoes= Avaliações_Adaptacoes, Acompanhamento=Acompanhamento, avancos=avancos, parecer=parecer, matricula_aluno=matricula_aluno, coordenador=coordenador,  equipe_Napene=equipe_Napene, contextualizaçao=contextualizaçao )

    
 
  

if __name__ == '__main__':
    app.run(debug=True)