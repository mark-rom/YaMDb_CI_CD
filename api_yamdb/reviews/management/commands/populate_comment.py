from reviews.models import Comment, Review, User

from .base_import_command import BaseImportCommand


class Command(BaseImportCommand):
    help = 'populates reviews_comment table'
    model_name = Comment

    def row_process(self, row):
        data = {}
        data['id'] = row[0]
        data['review'] = Review.objects.get(pk=row[1])
        data['text'] = row[2]
        data['author'] = User.objects.get(pk=row[3])
        data['pub_date'] = row[4]
        self.insert_to_db(data)
