# def allcaps(func):
#     def wrapper():
#         result = func()
#         print(result.upper())
#     return wrapper

def allcaps(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper