from flask import Flask,  request, jsonify, render_template, redirect, flash, session


import mysql.connector
 
app = Flask(__name__)
app.config['SECRET_KEY'] = "568425806"

db = mysql.connector.connect (
    host = 'localhost',
    user = "root",
    password = 'felipe09',
    database = "cadastros"
)

#PAGINA INICIAL 
@app.route('/')
def homepage():
   return render_template('homepage.html')


#ROTA PARA O CADASTRO DE PESSOAS
@app.route('/cadastro')
def homecadastro():
    return render_template('index.html')
@app.route('/cadastro', methods=['POST'])
def cadastro():
    usuario = request.form.get('usuario')
    Password = request.form.get('Password')

    #aqui irei cadastrar os dados no bando de dados
    cursor = db.cursor(dictionary=True)
    cursor.execute("INSERT INTO usuarios (nome, senha) VALUES (%s, %s)", (usuario, Password))
    db.commit()
    session['usuario'] = True #Criando a sessao do usuario cadastrado
    cursor.close()
    return redirect('/resposta')


#ROTA PARA LOGIN(VERIFICAR SE ESTAR CADASTRADO)
@app.route('/login')
def verificarlogin():
    return render_template('login.html')
@app.route('/login', methods=['POST'])
def login():
    usuario = request.form.get('usuario')
    Password = request.form.get('Password')

    #aqui irei verificar se o usuario esta cadastrado ou nao
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT nome, senha FROM usuarios')
    objetos =  cursor.fetchall()

    #pegando os valores que quero do dicionario(o banco de dados)
    for dicionario in objetos: #estou verificando cada um dos dicionarios, pois 'objetos' é uma lista de dicionarios
        name = dicionario['nome'] 
        senha = dicionario['senha']

        #verificando se os valores sao correspondendes e parando o laço de repetição
        if name == usuario and senha == Password:
            break

    #verificando se os valores sao correspondentes 
    if name == usuario and senha == Password:
        session['usuario'] = True
        cursor.close()
        return redirect('/resposta')
    #emitindo uma mensagem de erro caso o usuario n esteja cadastrado ou erro de digitação
    else:
        flash("Invalid password or user")
        cursor.close()
        return redirect('/login')


#ROTA PARA LOGOUT
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

#ROTA PARA QUANDO ENTRAR NO SITE
@app.route('/resposta')
def resposta():
    if session.get('usuario'):
        return render_template('resposta.html')
    else:
        return render_template('paginaProtegida.html')

if __name__ == '__main__':
    app.run(debug=True)