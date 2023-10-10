def allcaps(func):
    def wrapper():
        result = func()
        print(result.upper())
    return wrapper