from studies_diary.restplus import api
from flask_restplus import Resource
from studies_diary.serializers.category import category_serializer
from studies_diary.business.category import CategoryBus

ns_category = api.namespace('categories',
                            description='Operations related to categories')


@ns_category.route('/')
class CategoryCollection(Resource):

    def __init__(self, api=None, *args, **kwargs):
        super(CategoryCollection, self).__init__(api, args, kwargs)
        self.bus = CategoryBus()

    @api.marshal_list_with(category_serializer)
    def get(self):
        return self.bus.get_all()

    @api.expect(category_serializer)
    @api.marshal_with(category_serializer, code=201)
    def post(self):
        return self.bus.add(api.payload['title'])


@ns_category.route('/<int:id>')
@api.response(404, 'Category not found.')
class CategoryItem(Resource):

    def __init__(self, api=None, *args, **kwargs):
        super(CategoryItem, self).__init__(api, args, kwargs)
        self.bus = CategoryBus()

    @api.marshal_with(category_serializer)
    def get(self, id):
        return self.bus.get_by_id(id)
