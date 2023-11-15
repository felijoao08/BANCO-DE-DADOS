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


#ANEXO I: PAGINA 1
@app.route('/')
def paginaAnexoI():
   return render_template('anexoI.html')
@app.route('/anexoI', methods=['POST'])
def anexoI():
    nome = request.form.get('nome') #tabela aluno
    curso = request.form.get('curso') #tabela curso
    Nee = request.form.get('NEE') #tabela aluno
    Emr_nome = request.form.get('EMR-nome') #tabela equipeMutidisciplinar
    Emr_funçao = request.form.get('EMR-funçao') #tabela equipeMutidisciplinar
    Hpe_estudante = request.form.get('HPE-estudante') #tabela anexo 1
    #Nee_Estudante = request.form.get('NEE-Estudante') #REVISAR
    Chcin = request.form.get('CHCIN') #tabela anexo 1
    Dificuadades_apresentadas = request.form.get("Dificuadades-apresentadas") #tabela anexo 1

    #aqui irei cadastrar os dados no bando de dados
    cursor = db.cursor(dictionary=True)

    #aqui irei coloar os dados da tabela aluno
    cursor.execute("INSERT INTO aluno (nome, nessessidadesEspecificas ) VALUES (%s, %s)", (nome, Nee))

    #aqui irei colocar os dados da tabela curso
    #aqui irei colocar os dados da tabela equipeMutidisciplinar
    #aqui irei colocar os dados da tabela anexo 1
    
    
    cursor.close()
    return redirect('/')




#ANEXO II: PAGINA 1
@app.route('/anexoII')
def paginaAnexoII():
   return render_template('anexoII.html')
@app.route('/anexoII', methods=['POST'])
def anexoII():
    return render_template('anexoII.html')




#ANEXO III: PAGINA 1
@app.route('/anexoIII')
def paginaAnexoIII():
   return render_template('anexoIII.html')
@app.route('/anexoIII', methods=['POST'])
def anexoIII():
    return render_template('anexoIII.html')




if __name__ == '__main__':
    app.run(debug=True)