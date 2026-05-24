from flask_login import UserMixin

class Admin(UserMixin):

    def __init__(self, id):

        self.id = id