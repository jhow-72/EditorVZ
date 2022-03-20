class Property:
    def __init__(self, id, label, value):
        self._id = id
        self._label = label
        self._value = value

    @property
    def id(self):
        return self._id

    @property
    def label(self):
        return self._label

    @property
    def value(self):
        return self._value

def CriaPropriedades():
    chpras = Property('chpras', 'CHPRAS', '00738651124')
    data = Property('data_transacao', 'data transacao', '2022-10-07')
    hora = Property('hora_transacao', 'hora transacao', '12:32:41')
    dn = Property('dn', 'DN', '01285')
    indicador_cv = Property('indicador_cv', 'indicador cartão Virtual', 'N')
    cf = Property('cf', 'CF', '02')
    numero_documento = Property('numero_documento', 'Número Documento', '00004403589281')
    indicador_titular = Property('indicador_titular', 'Indicador Titular', '0')
    nome_estabelecimento = Property('nome_estabelecimento', 'Nome Estabelecimento', 'Garoupa')
    tipo_pessoa = Property('tipo_pessoa', 'Tipo Pessoa', 'F')
    valor_moeda_transacao = Property('valor_moeda_transacao', 'valor moeda transação', '000000000727272')
    hash_cartao = Property('hash_cartao', 'hash cartão', 'F28BE31DBAE83DB283B')

    lista = [chpras, data, hora, dn, indicador_cv, cf, numero_documento, indicador_titular, nome_estabelecimento,tipo_pessoa, valor_moeda_transacao, hash_cartao,]
    return lista


