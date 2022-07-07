import csv
import os

from django.core.management.base import BaseCommand, CommandError

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
))


class BaseImportCommand(BaseCommand):
    help = None
    model_name = None

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='filename for csv file')

    def get_current_app_path(self):
        return os.path.join(BASE_DIR, "static")

    def get_csv_file(self, filename):
        app_path = self.get_current_app_path()
        return os.path.join(app_path, "data", filename)

    def clear_model(self):
        try:
            self.model_name.objects.all().delete()
        except Exception as e:
            raise CommandError(
                f'Error in clearing {self.model_name}: {str(e)}'
            )

    def insert_to_db(self, data):
        try:
            self.model_name.objects.create(**data)
        except Exception as e:
            raise CommandError(
                f'Error in inserting {self.model_name.__name__}: {str(e)}'
            )

    def row_process(self, row):
        raise NotImplementedError()

    def handle(self, *args, **kwargs):
        filename = kwargs['filename']
        self.stdout.write(self.style.SUCCESS(f'filename:{filename}'))
        file_path = self.get_csv_file(filename)
        line_count = 0
        try:
            csv_file = open(file_path, encoding='utf-8')
        except FileNotFoundError:
            raise CommandError(f'File {file_path} does not exist')

        csv_reader = csv.reader(csv_file, delimiter=',')
        self.clear_model()
        for row in csv_reader:
            if row != '' and line_count >= 1:
                self.row_process(row)
            line_count += 1
        csv_file.close()

        self.stdout.write(
            self.style.SUCCESS(
                f'{line_count} entries added to {self.model_name.__name__}'
            )
        )
