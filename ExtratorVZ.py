from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index')
def ola():
    lista_campos = [['chpras', 'CHPRAS', '00738651124'], ['data_transacao', 'data transacao', "2022-10-07"], ['hora_transacao', 'hora transacao', '12:32:41'], ['dn', 'DN', '01285'], ['indicador_cv', 'indicador cartão virtual', 'N'], ['cf', 'CF', '02'], ['numero_documento', 'número documento', '00004403589281'], ['indicador_titular', 'indicador titular', '0'], ['nome_estabelecimento', 'nome estabelecimento', 'Garoupa'], ['tipo_pessoa', 'tipo pessoa', 'F'], ['valor_moeda_transacao', 'valor moeda transação', '000000000727272'], ['hash_cartao', 'hash cartão', 'F28BE31DBAE83DB283B']]
    for ident, nome, valor in lista_campos:
        print(f'{ident}; {nome}; {valor}')

    return render_template('index.html', titulo='Editor de Massas - VZ', lista_campos=lista_campos)

app.run()


