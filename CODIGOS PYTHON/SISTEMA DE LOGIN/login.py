from flask import Flask,  request, jsonify

import mysql.connector
 
app = Flask(__name__)

db = mysql.connector.connect (
    host = 'localhost',
    user = "root",
    password = 'labinfo',
    database = "atividade"
)

@app.route('/login', method =['POST']) 
def login():
    data = request.json
    cursor = db.cursor(dictionary=True)

    cursor.execute('SELECT * FROM usuario WHERE email = %s AND semha = %s, (data['email'], data[senha])')
    user = cursor.fetchone()
    cursor.close()

    if user:
        return jsonify({"login bem sucedido!"})
    else:
        return jsonify({"email ou senha incorreta!"})
        
if __name__ == '__main__':
    app.run()
    