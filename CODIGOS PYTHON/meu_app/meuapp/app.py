from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    dia = ['hello world', 'Ola mundo', 'salut monde', 'hola muendo']
    return render_template('index.html', dia=dia)

@app.route('/dia/<string:dia>')
def segunda(dia):
      return render_template('segunda.html', dia=dia)

@app.route('/aula/<int:n>')
def aula(n):
    return f'<h1>Aula de número {n}</h1>'

@app.route('/form', methods=["GET", "POST"])
def formulario():
    lista = ['hello world', 'Ola mundo', 'salut monde', 'hola muendo']
    if 'nome' in request.form:
        lista.append(request.form['nome'])

    return render_template('/form.html', lista=lista)
    


if __name__ == '__main__':
    app.run(debug=True)