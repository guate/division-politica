from functools import lru_cache

from aiohttp.web_exceptions import HTTPNotFound

from .models import Departamentos

import chilero.web


@lru_cache()
def departamentos():
    return Departamentos.load()


@lru_cache()
def search(keywords):
    def _do_search():
        for m in departamentos().as_complete_choices():
            for kw in keywords:
                if kw.lower() in m[1].lower():
                    yield m
                    break

    return list(_do_search())


class Municipios(chilero.web.Resource):
    resource_name = 'municipios'

    def collection_options(self, **kwargs):
        return chilero.web.Response(headers=[
            ['Access-Control-Allow-Methods', 'GET, POST, OPTIONS'],
            ['Access-Control-Allow-Origin', '*'],
            ["Access-Control-Allow-Headers",
             "Cookie, Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"]
        ])

    def entity_options(self, **kwargs):
        return chilero.web.Response(headers=[
            ['Access-Control-Allow-Methods', 'GET, PATCH'],
            ['Access-Control-Allow-Origin', '*'],
            ["Access-Control-Allow-Headers",
             "Cookie, Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"]
        ])

    def index(self):
        search_terms = self.request.GET.get('search')
        if search_terms:
            terms = search_terms.lower().split()
            items = search(tuple(terms))
        else:
            items = departamentos().as_complete_choices()

        response = dict(
            self=self.get_self_url(),
            data=dict(
                offset=0,
                limit=0,
                next=None,
                prev=None,
                count=len(items),
                length=len(items)
            ),
            index=[self.serialize_object(i) for i in items]
        )
        return self.response(response)

    def serialize_object(self, obj):
        return dict(
            id=obj[0],
            nombre=obj[1],
            url=self.get_object_url(obj[0]),
            _label=obj[1]
        )

    def show(self, id):
        try:
            m = dict(departamentos().as_complete_choices())[id]
        except KeyError:
            raise HTTPNotFound()

        return self.response(self.serialize_object([id, m]))
