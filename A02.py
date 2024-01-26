from flask import Flask, render_template

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def home():
    # Renderiza um template HTML chamado 'index.html', passando um título e uma mensagem como variáveis
    return render_template('index.html', title='A02', message='Teste')

if __name__ == '__main__':
    app.run(debug=True)
