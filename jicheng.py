class FatherA(object):
    def __init__(self):
        print("in FatherA")


class FatherB(object):
    def __init__(self):
        print("in FatherB")


class SonC(FatherA, FatherB):
    pass


if __name__ == '__main__':
    myfunc = SonC()