
from studies_diary.models.category import Category
from studies_diary.db import db


class CategoryBus(object):

    def add(self, title):
        category = Category(title=title)
        db.session.add(category)
        db.session.commit()
        return category

    def get_all(self):
        return Category.query.all()

    def get_by_id(self, id):
        print('teste')
        return Category.query.filter(Category.id == id).one()
