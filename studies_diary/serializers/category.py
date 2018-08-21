from studies_diary.restplus import api
from flask_restplus import fields

category_serializer = api.model('Category', {
    'id': fields.Integer(readonly=True),
    'title': fields.String(required=True, description='The category title')
})
