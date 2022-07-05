from reviews.models import Category, Title

from .base_import_command import BaseImportCommand


class Command(BaseImportCommand):
    help = 'populates reviews_title table'
    model_name = Title

    def row_process(self, row):
        data = {}
        data['id'] = row[0]
        data['name'] = row[1]
        data['year'] = row[2]
        data['category'] = Category.objects.get(pk=row[3])
        self.insert_to_db(data)
