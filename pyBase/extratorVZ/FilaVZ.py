from Propriedades import PropriedadeVZ


class FilaVZ:

############# Contrutor e Metodos Privados #############

    def __init__(self, fila_recebida):
        self._fila = fila_recebida
        self._chpras = PropriedadeVZ(self._fila, 19, 11, 'chpras')
        self._data_transacao = PropriedadeVZ(self._fila, 68, 10, 'data_transacao')
        self._hora_transacao = PropriedadeVZ(self._fila, 78, 8, 'hora_transacao')
        self._dn = PropriedadeVZ(self._fila, 117, 5, 'DN')
        self._indic_cv = PropriedadeVZ(self._fila, 123, 1, 'indicador_cartao_virtual')
        self._CF_configuracao = PropriedadeVZ(self._fila, 124, 2, 'CF')
        self._numero_documento = PropriedadeVZ(self._fila, 135, 15, 'numero_documento')
        self._indic_titularidade = PropriedadeVZ(self._fila, 150, 1, 'indicador_titularidade')
        self._nome_estabelecimento = PropriedadeVZ(self._fila, 151, 45, 'nome_estabelecimento')
        self._tipo_pessoa = PropriedadeVZ(self._fila, 256, 1, 'tipo_pessoa')
        self._valor_moeda_transacao = PropriedadeVZ(self._fila, 266, 15, 'valor_moeda_transacao')
        self._hash_cartao = PropriedadeVZ(self._fila, 540, 19, 'hash_cartao')

    def _replace(self, parte_nova, propriedade_do_contexto):
        string_atualizada = self._replace_handler(parte_nova, propriedade_do_contexto)
        propriedade_do_contexto.valor = parte_nova

        self._fila = string_atualizada

    def _replace_handler(self, parte_nova, propriedade):
        before = self._fila[:propriedade.i_primeiro_char]
        after = self._fila[propriedade.i_ultimo_char:]
        return before + parte_nova + after

    def _replace_check_zfill(self, valor_novo, objeto_atual):
        if len(valor_novo) > objeto_atual.qtd_chars:
            raise ValueError(f"{objeto_atual.nome} deve ter {objeto_atual.qtd_chars} chars ou menos")
        else:
            return valor_novo.zfill(objeto_atual.qtd_chars)

    def _replace_check_exact(self, valor_novo, objeto_atual):
        if len(valor_novo) != objeto_atual.qtd_chars:
            raise ValueError(f"{objeto_atual.nome} deve ter exatamente {objeto_atual.qtd_chars} chars")

    def _replace_check_spaces(self, valor_novo, objeto_atual):
        if len(valor_novo) > objeto_atual.qtd_chars:
            raise ValueError(f"{objeto_atual.nome} deve ter {objeto_atual.qtd_chars} chars ou menos")
        else:
            valor_novo = valor_novo.ljust(objeto_atual.qtd_chars)
            return valor_novo

############# Propriedades - valor #############

    @property
    def chpras(self):
        return self._chpras.valor

    @property
    def data_transacao(self):
        return self._data_transacao.valor

    @property
    def hora_transacao(self):
        return self._hora_transacao.valor

    @property
    def dn(self):
        return self._dn.valor

    @property
    def indicador_cartao_virtual(self):
        return self._indic_cv.valor

    @property
    def CF(self):
        return self._CF_configuracao.valor

    @property
    def numero_documento(self):
        return self._numero_documento.valor

    @property
    def indic_titularidade(self):
        return self._indic_titularidade.valor

    @property
    def nome_estabelecimento(self):
        return self._nome_estabelecimento.valor

    @property
    def tipo_pessoa(self):
        return self._tipo_pessoa.valor

    @property
    def valor_transacao(self):
        return self._valor_moeda_transacao.valor

    @property
    def hash_cartao(self):
        return self._hash_cartao.valor


############# Metodos publicos #############

    def chpras_replace(self, novo_chpras):
        novo_chpras = self._replace_check_zfill(novo_chpras, self._chpras)
        self._replace(novo_chpras, self._chpras)

    def data_transacao_replace(self, nova_data):

        self._replace_check_exact(nova_data, self._data_transacao)
        self._replace(nova_data, self._data_transacao)

    def hora_transacao_replace(self, nova_hora):
        self._replace_check_exact(nova_hora, self._hora_transacao)
        self._replace(nova_hora, self._hora_transacao)

    def dn_replace(self, nova_dn):
        nova_dn = self._replace_check_zfill(nova_dn, self._dn)
        self._replace(nova_dn, self._dn)

    def indicador_cartao_virtual_replace(self, novo_indicador_cv):
        self._replace_check_exact(novo_indicador_cv, self._indic_cv)
        self._replace(novo_indicador_cv, self._indic_cv)

    def CF_replace(self, nova_cf):
        self._replace_check_exact(nova_cf, self._CF_configuracao)
        self._replace(nova_cf, self._CF_configuracao)

    def numero_documento_replace(self, novo_numero_documento):
        novo_numero_documento = self._replace_check_zfill(novo_numero_documento, self._numero_documento)
        self._replace(novo_numero_documento, self._numero_documento)

    def indic_titularidade_replace(self, novo_indicador_titularidade):
        self._replace_check_exact(novo_indicador_titularidade, self._indic_titularidade)
        self._replace(novo_indicador_titularidade, self._indic_titularidade)

    def nome_estabelecimento_replace(self, novo_nome_estabelecimento):
        novo_nome_estabelecimento = self._replace_check_spaces(novo_nome_estabelecimento, self._nome_estabelecimento)
        self._replace(novo_nome_estabelecimento, self._nome_estabelecimento)

    def tipo_pessoa_replace(self, novo_tipo_pessoa):
        self._replace_check_exact(novo_tipo_pessoa, self._tipo_pessoa)
        self._replace(novo_tipo_pessoa, self._tipo_pessoa)

    def valor_transacao_replace(self, novo_valor_transacao):
        novo_valor_transacao = self._replace_check_zfill(novo_valor_transacao, self._valor_moeda_transacao)
        self._replace(novo_valor_transacao, self._valor_moeda_transacao)

    def hash_cartao_replace(self, nova_hash_cartao):
        self._replace_check_exact(nova_hash_cartao, self._hash_cartao)
        self._replace(nova_hash_cartao, self._hash_cartao)
