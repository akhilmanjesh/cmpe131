def allcaps(func):
    def wrapper():
        result = func()
        if isinstance(result, list):
            return [item.upper() for item in result]
        return result.upper()
    return wrapper
