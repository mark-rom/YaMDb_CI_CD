from reviews.models import Genre

from .base_import_command import BaseImportCommand


class Command(BaseImportCommand):
    help = 'populates reviews_genre table'
    model_name = Genre

    def row_process(self, row):
        data = {}
        data['id'] = row[0]
        data['name'] = row[1]
        data['slug'] = row[2]
        self.insert_to_db(data)
