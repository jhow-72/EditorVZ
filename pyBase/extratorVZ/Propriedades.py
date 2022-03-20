class PropriedadeVZ:

    def __init__(self, fila, inicio, numero_de_chars, nome):
        self._fila = fila
        self._primeiro_char = inicio
        self._numero_de_chars = numero_de_chars
        self._ultimo_char = self._primeiro_char + numero_de_chars
        self._nome = nome
        self._valor = self._busca_substring_generica()

    def _busca_substring_generica(self):
        return self._fila[self._primeiro_char:self._ultimo_char]

############# PROPRIEDADES #############
    @property
    def i_primeiro_char(self):
        return self._primeiro_char

    @property
    def i_ultimo_char(self):
        return self._ultimo_char

    @property
    def qtd_chars(self):
        return self._numero_de_chars
    @property
    def nome(self):
        return self._nome

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor
