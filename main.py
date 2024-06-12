from flask import Flask, render_template
import random

app = Flask(__name__)

# Lista de mensagens fofas
mensagens = [
    "Eu amo compartilhar a vida com você!",
    "Eu te amo!",
    "Cada momento ao seu lado é inesquecível!",
    "Vou estar sempre ao seu lado!",
    "Obrigada por tanto!!!",
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mensagem')
def mensagem():
    Clique_para_ler_uma_nova_mensagem = random.choice(mensagens)
    return render_template('message.html', mensagem=Clique_para_ler_uma_nova_mensagem)

if __name__ == '__main__':
    app.run(debug=True)
