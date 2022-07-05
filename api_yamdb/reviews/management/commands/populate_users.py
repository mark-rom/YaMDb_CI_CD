from users.models import User

from .base_import_command import BaseImportCommand


class Command(BaseImportCommand):
    help = 'populates users_user table'
    model_name = User

    def row_process(self, row):
        data = {}
        data['id'] = row[0]
        data['username'] = row[1]
        data['email'] = row[2]
        data['role'] = row[3]
        data['bio'] = row[4]
        data['first_name'] = row[5]
        data['last_name'] = row[6]
        self.insert_to_db(data)
