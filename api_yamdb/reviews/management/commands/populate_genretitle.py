from reviews.models import Genre, Title, TitleGenre

from .base_import_command import BaseImportCommand


class Command(BaseImportCommand):
    help = 'populates reviews_genretitle table'
    model_name = TitleGenre

    def row_process(self, row):
        data = {}
        data['id'] = row[0]
        data['title'] = Title.objects.get(pk=row[1])
        data['genre'] = Genre.objects.get(pk=row[2])
        self.insert_to_db(data)
