from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
  if request.method == 'GET':
    return render_template('index.html')

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        username = request.form['e-mail']
        password = request.form['password']
        
        # Salva l'utente nel database
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        conn.close()



        return redirect(url_for('index'))  # Dopo aver aggiunto l'utente, ritorna alla pagina principale
    
    return render_template('create_account.html')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0',port=4444)