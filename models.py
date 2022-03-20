# classe criada para os objetos colocados no formulario da pagina index
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
