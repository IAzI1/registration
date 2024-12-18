class Database:
    def __init__(self):
        self.db = {}

    def add_user(self, data: dict):
        log = data['lg']
        if self.db.get(log):
            raise 'Такой логин уже существует в базе'
        else:
            pswd = data['pswd']
            self.db[log] = pswd


    def __str__(self):
        return f'{self.db}'