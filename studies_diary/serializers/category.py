from studies_diary.restplus import api
from flask_restx import fields


# O RESTPlus permite validar e documentar automaticamente o formato dos objetos JSON recebidos
# usando API models. Uma API model define o formato do objeto listando os campos esperados.
# Cada campo deve ter um tipo associado (string,integer,datetime), o que determinará qual valor é considerado válido.
# Na nossa API, os models estão localizados no diretório /serializers/. Abaixo é possível visualizar um exemplo de API model:
category_serializer = api.model('Category', {
    'id': fields.Integer(readonly=True),
    'title': fields.String(required=True, description='O título da Categoria')
})

# Como no model o campo id está definido como read only,
# o método post vai esperar somente pelo campo title,
# contudo, após inserido o valor, ele vai retornar o title junto com o id gerado.
