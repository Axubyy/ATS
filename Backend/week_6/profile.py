from .main_utils import AuthUtils


class Profile(AuthUtils):
    def __init__(self):
        super().__init__()
        self.user_data = AuthUtils.get_csv_data()

    def get_id(self, id):
        for user in self.user_data:
            if user["id"] == id:
