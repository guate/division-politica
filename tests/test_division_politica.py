from aiohttp import request
from chilero.web import Application
from chilero.web.test import WebTestCase, asynctest

from guate.division_politica import (
    Collection, Departamentos
)
from guate.division_politica.resources import Municipios


def test_data():
    ds = Departamentos.load()

    assert isinstance(ds, Collection)
    assert len(ds) == 22
    assert ds.por_codigo(1).nombre == 'Guatemala'
    assert ds.por_nombre('Chiquimula').nombre == 'Chiquimula'
    assert ds.por_nombre('Chiquimula').codigo == 20

    choices = ds.as_choices()
    assert len(choices) == 22
    for c in choices:
        assert ds.por_codigo(c[0]).nombre == c[1]

    mchoices = ds.as_complete_choices()
    for c in mchoices:
        cd, cm = [int(x) for x in c[0].split('-')]
        d = ds.por_codigo(cd)
        assert c[1].startswith('{} /'.format(d.nombre))
        m = d.municipios.por_codigo(cm)

        assert c[1] == m.nombre_completo


class TestMunicipios(WebTestCase):
    routes = [
        ['/', Municipios]
    ]
    application = Application

    @asynctest
    def test_index(self):
        resp = yield from request('GET', self.full_url('/'))
        assert resp.status == 200
        resp.close()

    @asynctest
    def test_search(self):
        resp = yield from request('GET', self.full_url('/?search=arada'))
        jresp = yield from resp.json()
        assert jresp['index'][0]['nombre'] == 'Chiquimula / San José La Arada'
        resp.close()

    @asynctest
    def test_show(self):
        resp = yield from request('GET', self.full_url('/20-02'))
        jresp = yield from resp.json()
        assert jresp['body']['nombre'] == 'Chiquimula / San José La Arada'
        resp.close()

    @asynctest
    def test_search(self):
        resp = yield from request('GET', self.full_url('/20-12'))
        assert resp.status == 404
        resp.close()

