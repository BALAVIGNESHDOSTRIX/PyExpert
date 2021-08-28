def make_pretty(func):
    def inner():
        print("hello world")
        return func()
    return inner

def ordinary():
    print("I am ordinary")


if __name__ == "__main__":
    news = make_pretty(ordinary)
    news()
