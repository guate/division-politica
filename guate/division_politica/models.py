import json

import pkg_resources
from attrdict import AttrDict


class Collection(list):
    model = AttrDict
    def __init__(self, items=None):
        super(Collection, self).__init__()
        if items is not None:
            for i in items:
                self.append(self.model(i))

    def _by(self, attrname, attrvalue):
        return dict(
                [x[attrname], x] for x in self
            )[attrvalue]


class Departamento(AttrDict):
    def __init__(self, departamento):
        super(AttrDict, self).__init__(departamento)
        self.municipios = Municipios(
            departamento['municipios'], departamento
        )


class Municipio(AttrDict):
    def __init__(self, municipio, departamento=None):
        super(Municipio, self).__init__(municipio)

        self.departamento = departamento

    @property
    def codigo_completo(self):
        return '{0:02d}-{1:02d}'.format(
            self.departamento.codigo, self.codigo
        )

    @property
    def nombre_completo(self):
        return '{} / {}'.format(
            self.departamento.nombre, self.nombre
        )


class Departamentos(Collection):
    model = Departamento

    def __init__(self, departamentos=None):
        super(list, self).__init__()

        if departamentos is not None:
            for i in sorted(departamentos, key=lambda k: k['nombre']):
                self.append(Departamento(i))

    @staticmethod
    def load():
        filename = pkg_resources.resource_filename(
            'guate.division_politica', "data.json"
        )
        with open(filename, 'r') as f:
            data = json.load(f)
            return Departamentos(data['departamentos'])

    def por_nombre(self, nombre):
        return self._by('nombre', nombre)

    def por_codigo(self, codigo):
        return self._by('codigo', codigo)

    def as_choices(self):
        return [
            [x.codigo, x.nombre] for x in self
        ]
    def municipios(self):
        for d in self:
            for m in d.municipios:
                yield Municipio(m, d)

    def as_complete_choices(self):
        return [
            [m.codigo_completo, m.nombre_completo]
            for m in list(self.municipios())
        ]


class Municipios(Collection):
    model = Municipio
    def __init__(self, municipios=None, departamento=None):
        super(list, self).__init__()

        if municipios is not None:
            for i in sorted(municipios, key=lambda k: k['nombre']):
                self.append(Municipio(i, departamento))

    def por_nombre(self, nombre):
        return self._by('nombre', nombre)

    def por_codigo(self, codigo):
        return self._by('codigo', codigo)
