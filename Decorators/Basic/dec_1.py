def divide_2(param):
    return param// 2

def add_2(param):
    return param + 2

def operate(func, param):
    return func(param)

if __name__ == '__main__':
    print(operate(add_2, 4))

