from reviews.models import Category

from .base_import_command import BaseImportCommand


class Command(BaseImportCommand):
    help = 'populates reviews_category table'
    model_name = Category

    def row_process(self, row):
        data = {}
        data['id'] = row[0]
        data['name'] = row[1]
        data['slug'] = row[2]
        self.insert_to_db(data)
