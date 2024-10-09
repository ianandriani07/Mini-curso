from flask import Flask, jsonify, request, redirect, render_template
from forms import Materia

app = Flask(__name__)

app.config['SECRET_KEY'] = 'minha_chave_secreta'
        
@app.route('/adicionar-materia', methods=['GET', 'POST'])
def adicionar_materia_template():
    form = Materia()
    return render_template('post.html', form=form)

@app.route('/atualizando-materia', methods=['GET', 'POST'])
def atualizar_materia_template():
    form = Materia()
    return render_template('put.html', form=form)

if __name__ == "__main__":
    app.run(port=8000)