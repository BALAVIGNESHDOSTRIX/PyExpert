def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        s = func(*args, **kwargs)
        print("*" * 30)
        return s
    return inner

def at(func):
    def inner(*args, **kwargs):
        print("@" * 30)
        s = func(*args, **kwargs)
        print("@" * 30)
        return s
    return inner 


@star
@at
def printer(msg="Hello"):
    print(msg)


if __name__ == '__main__':
    printer()