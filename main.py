from database import Database
from user import User

if __name__ == "__main__":

    db = Database()
    while True:

        login = input('Login: ')
        password = input('Password: ')
        confirm_password = input('Repeat the password: ')
        if password != confirm_password:
            print(f"Passwords don't match")
            exit()

        user = User(lg=login, pswd=password)
        db.add_user(user.model_dump())
        print(db)