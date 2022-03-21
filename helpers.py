from models import Property

# tem por objetivo popular os valores das propriedades que aparecerão no html do index
# retorna uma lista com o id, name(label) e value que será usado para criar os campos do form
def CriaPropriedades(dicionario):
    chpras = Property('chpras', 'CHPRAS', dicionario['chpras'])
    data = Property('data_transacao', 'data transação', dicionario['data_transacao'])
    hora = Property('hora_transacao', 'hora transação', dicionario['hora_transacao'])
    dn = Property('dn', 'DN', dicionario['dn'])
    indicador_cv = Property('indicador_cv', 'indicador cartão Virtual', dicionario['indicador_cv'])
    cf = Property('cf', 'CF', dicionario['cf'])
    numero_documento = Property('numero_documento', 'Número Documento', dicionario['numero_documento'])
    indicador_titular = Property('indicador_titular', 'Indicador Titular', dicionario['indicador_titular'])
    nome_estabelecimento = Property('nome_estabelecimento', 'Nome Estabelecimento', dicionario['nome_estabelecimento'])
    tipo_pessoa = Property('tipo_pessoa', 'Tipo Pessoa', dicionario['tipo_pessoa'])
    valor_moeda_transacao = Property('valor_moeda_transacao', 'valor moeda transação', dicionario['valor_moeda_transacao'])
    hash_cartao = Property('hash_cartao', 'hash cartão', dicionario['hash_cartao'])

    lista = [chpras, data, hora, dn, indicador_cv, cf, numero_documento, indicador_titular, nome_estabelecimento,tipo_pessoa, valor_moeda_transacao, hash_cartao,]
    return lista

def replace_values(fila, propriedades_campos_para_alteracao):

    # chamada de cada metodo especifico que altera o valor na fila original
    fila.chpras_replace(propriedades_campos_para_alteracao['chpras'])
    fila.data_transacao_replace(propriedades_campos_para_alteracao['data_transacao'])
    fila.hora_transacao_replace(propriedades_campos_para_alteracao['hora_transacao'])
    fila.dn_replace(propriedades_campos_para_alteracao['dn'])
    fila.indicador_cartao_virtual_replace(propriedades_campos_para_alteracao['indicador_cv'])
    fila.cf_replace(propriedades_campos_para_alteracao['cf'])
    fila.numero_documento_replace(propriedades_campos_para_alteracao['numero_documento'])
    fila.indic_titularidade_replace(propriedades_campos_para_alteracao['indicador_titular'])
    fila.nome_estabelecimento_replace(propriedades_campos_para_alteracao['nome_estabelecimento'])
    fila.tipo_pessoa_replace(propriedades_campos_para_alteracao['tipo_pessoa'])
    fila.valor_transacao_replace(propriedades_campos_para_alteracao['valor_moeda_transacao'])
    fila.hash_cartao_replace(propriedades_campos_para_alteracao['hash_cartao'])

    return fila.string


# como adicionar um campo novo na section "campos para alteração":
# em ExtratorVZ.py, basta adicionar uma linha nova com a nova propriedade no dicionario default e no atualizado
# em helpers.py, crie um novo objeto Property e coloque-o na lista, depois adicione uma linha nova no metodo replace values para o metodo replace da nova prop
# em pyBase.extratorVZ.FilaVZ, adicione a nova propriedade no construtor, crie um @property para busca seu valor e defina o metodo replace dela
