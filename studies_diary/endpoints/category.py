from studies_diary.restplus import api
from flask_restplus import Resource
from studies_diary.serializers.category import category_serializer
from studies_diary.business.category import CategoryBus

ns = api.namespace('categories',
                   description='Operations related to categories')


@ns.route('/')
class CategoriesCollection(Resource):

    def __init__(self, api=None, *args, **kwargs):
        super(CategoriesCollection, self).__init__(api, args, kwargs)
        self.bus = CategoryBus()

    @api.marshal_list_with(category_serializer)
    def get(self):
        return self.bus.get_all()

    @api.expect(category_serializer)
    @api.marshal_with(category_serializer, code=201)
    def post(self):
        return self.bus.add(api.payload['title'])


@ns.route('/<int:id>')
@api.response(404, 'Category not found.')
class CategoriesItem(Resource):

    def __init__(self, api=None, *args, **kwargs):
        super(CategoriesItem, self).__init__(api, args, kwargs)
        self.bus = CategoryBus()

    @api.marshal_with(category_serializer)
    def get(self, id):
        return self.bus.get_by_id(id)
