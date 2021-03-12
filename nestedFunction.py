def outer():
    print("outer function")

    def inner():
        print("inner function started")
    print("outer function completed")
    return inner


outer()
