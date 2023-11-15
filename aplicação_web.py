from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2

app = Flask(__name__)

#Configuração da Base de Dados
db = {
    'dbname': 'frotadecarros',
    'user': 'postgres',
    'password': 'admin',
    'host': 'localhost',
    'port': '5432'
}

#Conexão com a Base de dados
def connect_db():
    conn = psycopg2.connect(**db)
    return conn

@app.route('/')
def listarfrota():
    conn = connect_db()
    cursor = conn.cursor()

    #Listar todos os registos da tabela frota
    cursor.execute('SELECT * FROM frota;')
    carros = cursor.fetchall()

    cursor.close()
    conn.close()

    #Link para ficheiro HTML
    return render_template('paginainicial.html', carros=carros)


@app.route('/add_carro', methods=['POST'])
def add_carro():
    # Recebe as variaveis do ficheiro HTML
    marca = request.form.get('marca')
    modelo = request.form.get('modelo')
    matricula = request.form.get('matricula')

    conn = connect_db()
    cursor = conn.cursor()

    try:
        # Verifica se a matricula ja existe na base de dados
        cursor.execute('SELECT * FROM frota WHERE matricula = %s;', (matricula,))
        existe = cursor.fetchone()

        if existe:
            # Se ja existe na base de dados envia uma mensagem de erro
            mensagem = "A matricula já existe na Base de Dados"
            return render_template('paginainicial.html', carros=[], error_message=mensagem)

        # Insere o registo na base de dados se a matricula ainda não existe
        cursor.execute('INSERT INTO public.frota(marca, modelo, matricula)VALUES (%s, %s, %s);', (marca, modelo,matricula))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

    return redirect(url_for('listarfrota'))

@app.route('/delete_carro/<matricula>', methods=['GET'])
def delete_carro(matricula):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM frota WHERE matricula = %s;', (matricula,))
    conn.commit()
    
    cursor.close()
    conn.close()

    return redirect(url_for('listarfrota'))

if __name__ == '__main__':
    app.run(debug=True)