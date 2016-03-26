from guate.division_politica import (
    Collection, Departamentos
)


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


