import string
import random

userLogin = "".join(random.sample((string.ascii_lowercase), 6))
userPass = "".join(random.sample((string.ascii_letters + string.digits), 8))
print("login: ", userLogin)
print("password: ", userPass)