def decorator_func(func):
    def wrapper(*args, **kwargs):
        spec_sym = r"!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        while True:
            print("""Your password must contain at least 1 letter, 1 number, 1 special character and the
                    length must be more than 8 characters """)
            password = func(*args, **kwargs)
            if password is None:
                print("You cant use Space, Tab or any tab symbol")
            elif len([i for i in password if i.isalpha()]) == 0:
                print("Your password must contain at least 1 letter")
            elif len([i for i in password if i.isdigit()]) == 0:
                print("Your password must contain at least 1 number")
            elif len([i for i in password if i in spec_sym]) == 0:
                print("Your password must contain at least 1 special character")
            elif len(password) < 8:
                print("The length must be more than 8 characters")
            else:
                print("Password accepted. Your password is -", password)
                break

    return wrapper


@decorator_func
def password_func():
    password = input("Type your password:")
    return None if len(password) == 0 or password.count(' ') else password


if __name__ == "__main__":
    password_func()
