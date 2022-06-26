from flask import Flask, render_template, request
import helpers
from models import FilaVZ
# from pyBase.extratorVZ.FilaVZ import FilaVZ

app = Flask(__name__)

# essas propriedades são as que aparecerão no index inicial

propriedades_campos_para_alteracao = helpers.cria_dicionario(False, [])

# gera as propriedades iniciais
massa_default = '----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
fila = FilaVZ(massa_default)

# gera a pagina inicial, nesse estágio "massa_atualizada = massa_default" pois não houve nenhuma alteração ainda
@app.route('/')
def index():
    lista_campos = helpers.CriaPropriedades(fila, fila.String, propriedades_campos_para_alteracao)
    return render_template('index.html', titulo='Editor de Massas - VZ', massa_default=massa_default, lista_campos=lista_campos, massa_atualizada=massa_default)

# aqui é a base da atualização da massa
@app.route('/atualizar-propertySet', methods=['POST',])
def propertySet():

    # cria um novo dicionario que será usado para atualizar os valores da massa e manter o estado do form
    # os valores são recebidos via POST e as chaves são as mesmas que as setadas em helpers.CriaPropriedades
    propriedades_campos_para_alteracao_atualizado = request.form

    lista_campos_atualizada = helpers.CriaPropriedades(fila, fila.String, propriedades_campos_para_alteracao_atualizado)
    massa_atualizada = helpers.replace_values(fila, propriedades_campos_para_alteracao_atualizado, lista_campos_atualizada)

    # renderiza o template index.html com os valores atualizados
    return render_template('index.html', titulo='Editor de Massas - VZ', massa_default=massa_default, lista_campos=lista_campos_atualizada, massa_atualizada=massa_atualizada)

@app.route('/atualizaMassaPadrao/<massa_atualizada>', methods=['POST'])
def atualizaMassaPadrao(massa_atualizada):
    string_padrão_nova = request.form['Massa-Default']

    propriedades_campos_para_alteracao_atualizado = helpers.cria_dicionario(True, string_padrão_nova)
    lista_campos_atualizada = helpers.CriaPropriedades(fila, fila.String, propriedades_campos_para_alteracao_atualizado)

    return render_template('index.html', titulo='Editor de Massas - VZ', massa_default=string_padrão_nova, lista_campos=lista_campos_atualizada, massa_atualizada=massa_atualizada)


app.run(debug=True)

