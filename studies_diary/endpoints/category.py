from studies_diary.restplus import api
from flask_restx import Resource
from studies_diary.serializers.category import category_serializer
from studies_diary.business.category import CategoryBus

# define o namespace category apontando para a api
ns_category = api.namespace('categories',
                            description='Operações relacionadas a categorias')


# As classes CategoryItem e CategoryCollection herdam da classe Resource.
# Cada Resource é uma classe que contêm funções que serão mapeadas em métodos HTTP.
# Ou seja, para implementar um método HTTP put é necessário implementar uma função com o mesmo nome.
# As seguintes funções são mapeadas: get,post,put,delete,path,options e head.
@ns_category.route('/')
class CategoryCollection(Resource):

    def __init__(self, api=None, *args, **kwargs):
        super(CategoryCollection, self).__init__(api, args, kwargs)
        self.bus = CategoryBus()

    @api.marshal_list_with(category_serializer)
    def get(self):
        return self.bus.get_all()

    # Com o model definido, é possível aplicar ele a um método
    # utilizando os decorators @api.expect() e @api.marshal_with().
    @api.expect(category_serializer)
    @api.marshal_with(category_serializer, code=201)
    def post(self):
        return self.bus.add(api.payload['title'])


@ns_category.route('/<int:id>')
# decorator @api.response() documenta quais códigos de status HTTP cada método deve retornar e o que significa.
@api.response(404, 'Categoria não encontrada.')
class CategoryItem(Resource):

    def __init__(self, api=None, *args, **kwargs):
        super(CategoryItem, self).__init__(api, args, kwargs)
        self.bus = CategoryBus()

    @api.marshal_with(category_serializer)
    def get(self, id):
        return self.bus.get_by_id(id)

# Após tudo configurado, observe como fica bem documentado no Swagger UI
