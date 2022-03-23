from models import FilaVZ, PropertyVZ


# tem por objetivo popular os valores das propriedades que aparecerão no html do index
# retorna uma lista com o id, name(label) e value que será usado para criar os campos do form
def CriaPropriedades(fila, fila_string, dicionario):

    lista_campos = [
        PropertyVZ(fila, fila_string, 'chpras', 'CHPRAS', dicionario['chpras'], 19, 11, True, False, False),
        PropertyVZ(fila, fila_string,'data_transacao', 'data transação', dicionario['data_transacao'], 68, 10, False, True, False),
        PropertyVZ(fila, fila_string,'hora_transacao', 'hora transação', dicionario['hora_transacao'], 78, 8, False, True, False),
        PropertyVZ(fila, fila_string,'dn', 'DN', dicionario['dn'], 117, 5, True, False, False),
        PropertyVZ(fila, fila_string,'indicador_cv', 'indicador cartão Virtual', dicionario['indicador_cv'], 123, 1, False, True, False),
        PropertyVZ(fila, fila_string,'cf', 'CF', dicionario['cf'], 124, 2, False, True, False),
        PropertyVZ(fila, fila_string,'numero_documento', 'Número Documento', dicionario['numero_documento'], 135, 15, True, False, False),
        PropertyVZ(fila, fila_string,'indicador_titular', 'Indicador Titular', dicionario['indicador_titular'], 150, 1, False, True, False),
        PropertyVZ(fila, fila_string,'nome_estabelecimento', 'Nome Estabelecimento', dicionario['nome_estabelecimento'], 151, 45, False, False, True),
        PropertyVZ(fila, fila_string,'tipo_pessoa', 'Tipo Pessoa', dicionario['tipo_pessoa'], 256, 1, False, True, False),
        PropertyVZ(fila, fila_string,'valor_moeda_transacao', 'valor moeda transação', dicionario['valor_moeda_transacao'], 266, 15, True, False, False),
        PropertyVZ(fila, fila_string,'hash_cartao', 'hash cartão', dicionario['hash_cartao'], 540, 19, False, True, False),
    ]

    return lista_campos

def replace_values(fila, propriedades_campos_para_alteracao, lista_campos_atualizada):

    for key, value in propriedades_campos_para_alteracao.items():
        for j, campo in enumerate(lista_campos_atualizada):
            if key == campo.id:
                if campo.zfill_check:
                    value = _replace_check_zfill(value, campo)
                if campo.exatc_check:
                    _replace_check_exact(value, campo)
                if campo.spaces_check:
                    value = _replace_check_spaces(value, campo)

                _replace(fila, value, campo)
                break

    return fila.String

    # # chamada de cada metodo especifico que altera o valor na fila original
    # fila.chpras_replace(propriedades_campos_para_alteracao['chpras'])
    # fila.data_transacao_replace(propriedades_campos_para_alteracao['data_transacao'])
    # fila.hora_transacao_replace(propriedades_campos_para_alteracao['hora_transacao'])
    # fila.dn_replace(propriedades_campos_para_alteracao['dn'])
    # fila.indicador_cartao_virtual_replace(propriedades_campos_para_alteracao['indicador_cv'])
    # fila.cf_replace(propriedades_campos_para_alteracao['cf'])
    # fila.numero_documento_replace(propriedades_campos_para_alteracao['numero_documento'])
    # fila.indic_titularidade_replace(propriedades_campos_para_alteracao['indicador_titular'])
    # fila.nome_estabelecimento_replace(propriedades_campos_para_alteracao['nome_estabelecimento'])
    # fila.tipo_pessoa_replace(propriedades_campos_para_alteracao['tipo_pessoa'])
    # fila.valor_transacao_replace(propriedades_campos_para_alteracao['valor_moeda_transacao'])
    # fila.hash_cartao_replace(propriedades_campos_para_alteracao['hash_cartao'])


def _replace(fila, parte_nova, propriedade_do_contexto):
    string_atualizada = _replace_handler(fila, parte_nova, propriedade_do_contexto)
    propriedade_do_contexto.valor = parte_nova

    fila.String = string_atualizada

# criado um metodo auxiliar para o replace pois a funcao built-in do python não me atende
# ou ela mudava todas as menções ao que eu estava procurando ou um número específcio
# não conseguia fazer ela trocar a partir de um determinado index
def _replace_handler(fila, parte_nova, propriedade):
    before = fila.String[:propriedade.i_primeiro_char]
    after = fila.String[propriedade.i_ultimo_char:]
    return before + parte_nova + after


# as funcoes abaixo são usadas para validar o q for necessário antes de fazer o replace


def _replace_check_zfill(valor_novo, objeto_atual):
    if len(valor_novo) > objeto_atual.qtd_chars:
        raise ValueError(f"{objeto_atual.id} deve ter {objeto_atual.qtd_chars} chars ou menos")
    else:
        return valor_novo.zfill(objeto_atual.qtd_chars)


def _replace_check_exact(valor_novo, objeto_atual):
    if len(valor_novo) != objeto_atual.qtd_chars:
        raise ValueError(f"{objeto_atual.id} deve ter exatamente {objeto_atual.qtd_chars} chars")


def _replace_check_spaces(valor_novo, objeto_atual):
    if len(valor_novo) > objeto_atual.qtd_chars:
        raise ValueError(f"{objeto_atual.id} deve ter {objeto_atual.qtd_chars} chars ou menos")
    else:
        valor_novo = valor_novo.ljust(objeto_atual.qtd_chars)
        return valor_novo


# como adicionar um campo novo na section "campos para alteração":
# em ExtratorVZ.py, basta adicionar uma linha nova com a nova propriedade no dicionario default e no atualizado
# em helpers.py, crie um novo objeto Property e coloque-o na lista, depois adicione uma linha nova no metodo replace values para o metodo replace da nova prop
# em pyBase.extratorVZ.FilaVZ, adicione a nova propriedade no construtor, crie um @property para busca seu valor e defina o metodo replace dela
