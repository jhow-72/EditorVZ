from flask import Flask, render_template, request
import helpers
from models import FilaVZ
# from pyBase.extratorVZ.FilaVZ import FilaVZ

app = Flask(__name__)

# essas propriedades são as que aparecerão no index inicial
propriedades_campos_para_alteracao = {
    'chpras': '738651124',
    'data_transacao': '2022-10-07',
    'hora_transacao': '12:32:41',
    'dn': '01285',
    'indicador_cv': 'N',
    'cf': '02',
    'numero_documento': '4403589281',
    'indicador_titular': '0',
    'nome_estabelecimento': 'Garoupa',
    'tipo_pessoa': 'F',
    'valor_moeda_transacao': '000000000727272',
    'hash_cartao': 'F28BE31DBAE83DB283B',
}

# gera as propriedades iniciais
massa_default = '----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
fila = FilaVZ(massa_default)
lista_campos = helpers.CriaPropriedades(fila, fila.String, propriedades_campos_para_alteracao)

# gera a pagina inicial, nesse estágio "massa_atualizada = massa_default" pois não houve nenhuma alteração ainda
@app.route('/')
def index():
    return render_template('index.html', titulo='Editor de Massas - VZ', massa_default=massa_default, lista_campos=lista_campos, massa_atualizada=massa_default)

# aqui é a base da atualização da massa
@app.route('/atualizar-propertySet', methods=['POST',])
def propertySet():

    # cria um novo dicionario que será usado para atualizar os valores da massa e manter o estado do form
    # os valores são recebidos via POST e as chaves são as mesmas que as setadas em helpers.CriaPropriedades
    propriedades_campos_para_alteracao_atualizado = {
        'chpras': request.form['chpras'],
        'data_transacao': request.form['data_transacao'],
        'hora_transacao': request.form['hora_transacao'],
        'dn': request.form['dn'],
        'indicador_cv': request.form['indicador_cv'],
        'cf': request.form['cf'],
        'numero_documento': request.form['numero_documento'],
        'indicador_titular': request.form['indicador_titular'],
        'nome_estabelecimento': request.form['nome_estabelecimento'],
        'tipo_pessoa': request.form['tipo_pessoa'],
        'valor_moeda_transacao': request.form['valor_moeda_transacao'],
        'hash_cartao': request.form['hash_cartao'],
    }

    lista_campos_atualizada = helpers.CriaPropriedades(fila, fila.String, propriedades_campos_para_alteracao)
    massa_atualizada = helpers.replace_values(fila, propriedades_campos_para_alteracao_atualizado, lista_campos_atualizada)
    lista_campos_atualizada = helpers.CriaPropriedades(fila, massa_atualizada, propriedades_campos_para_alteracao_atualizado)


    # renderiza o template index.html com os valores atualizados
    return render_template('index.html', titulo='Editor de Massas - VZ', massa_default=massa_default, lista_campos=lista_campos_atualizada, massa_atualizada=massa_atualizada)

app.run(debug=True)

