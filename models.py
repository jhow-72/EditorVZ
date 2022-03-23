class FilaVZ:
    def __init__(self, string):
        self._String = string
        self.num_chars = len(string)

    @property
    def String(self):
        return self._String

    @String.setter
    def String(self, new):
        self._String = new

# classe criada para os objetos colocados no formulario da pagina index
class PropertyVZ:
    def __init__(self, fila, string, id, label, value_default, inicio, numero_de_chars, zfill_check, exatc_check, spaces_check):
        self._fila = fila
        self._string = string
        self._id = id
        self._label = label
        self._value_default = value_default
        self._primeiro_char = inicio
        self._numero_de_chars = numero_de_chars
        self._ultimo_char = self._primeiro_char + numero_de_chars
        self._zfill_check = zfill_check
        self._exatc_check = exatc_check
        self._spaces_check = spaces_check
        self._valor = None
        # self._valor = self._busca_substring_generica()

    def _busca_substring_generica(self):
        return self._string[self._primeiro_char:self._ultimo_char]

    def _check_label(self):
        pass

    ############# PROPRIEDADES #############

    @property
    def id(self):
        return self._id

    @property
    def string(self):
        return self._string

    @property
    def label(self):
        return self._label

    @property
    def value(self):
        return self._value_default

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
    def valor(self):
        return self._valor

    @property
    def zfill_check(self):
        return self._zfill_check

    @property
    def exatc_check(self):
        return self._exatc_check

    @property
    def spaces_check(self):
        return self._spaces_check

    @string.setter
    def string(self, string):
        self._string = string

    @valor.setter
    def valor(self, valor):
        self._valor = valor