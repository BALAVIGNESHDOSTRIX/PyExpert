def smart_divide(func):
    def inner(a,b):
        print("divide %s/%s is:" % (a,b))
        return func(a,b)
    return inner


@smart_divide
def divide(a,b):
    return a/b


if __name__ == '__main__':
    print(divide(10,5))
    ''' 
        divide = smart_divide(divide)
    '''


