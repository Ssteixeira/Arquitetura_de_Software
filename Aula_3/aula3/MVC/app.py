from flask import Flask, render_template, request

app = Flask(__name__)

# Modelo simples: lista de usuários
users = ["Alice", "Bob", "Charlie"]

# Controlador: exibe a lista de usuários
@app.route('/')
def index():
    return render_template('index.html', users=users)

# Controlador: adiciona um novo usuário
@app.route('/add', methods=['POST'])
def add_user():
    new_user = request.form.get('name')
    if new_user:
        users.append(new_user)
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
