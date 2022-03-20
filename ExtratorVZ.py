from flask import Flask, render_template, request
import models

app = Flask(__name__)

lista_campos = models.CriaPropriedades()
massa_default = '----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'

@app.route('/index')
def ola():
    for campo in lista_campos:
        print(f'{campo.id}; {campo.label}; {campo.value}')

    return render_template('index.html', titulo='Editor de Massas - VZ', massa_default=massa_default, lista_campos=lista_campos, massa_atualizada=massa_default)

@app.route('/atualizar-propertySet')
def update():
    chpras = request.form['chpras']
    data_transacao = request.form['data_transacao']
    hora_transacao = request.form['hora_transacao']
    dn = request.form['dn']
    indicador_cv = request.form['indicador_cv']
    cf = request.form['cf']
    numero_documento = request.form['numero_documento']
    indicador_titular = request.form['indicador_titular']
    nome_estabelecimento = request.form['nome_estabelecimento']
    tipo_pessoa = request.form['tipo_pessoa']
    valor_moeda_transacao = request.form['valor_moeda_transacao']
    hash_cartao = request.form['hash_cartao']



app.run()


