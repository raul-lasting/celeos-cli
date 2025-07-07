import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import user
import login
import getpass


if __name__ == "__main__":
    user = str(input("Username: "))
    name = str(input("Name: "))
    email = str(input("Email: "))
    password = getpass.getpass("Password: ")
    credentials = user.add_user(user, name, email, password)
    login.login_and_write_token(credentials["user"], credentials["pass"])