from reviews.models import Review, Title
from users.models import User

from .base_import_command import BaseImportCommand


class Command(BaseImportCommand):
    help = 'populates reviews_review table'
    model_name = Review

    def row_process(self, row):
        data = {}
        data['id'] = row[0]
        data['title'] = Title.objects.get(pk=row[1])
        data['text'] = row[2]
        data['author'] = User.objects.get(pk=row[3])
        data['score'] = row[4]
        data['pub_date'] = row[5]
        self.insert_to_db(data)
