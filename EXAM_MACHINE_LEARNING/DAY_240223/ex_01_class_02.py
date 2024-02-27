# --------------------------------------
# 상속(Inheritance)
# - 다중 상속 허용
# - 문법 : class 자식클래스명(부모클래스명, ...)
# --------------------------------------
class A:
    @classmethod
    def printInfo(cls):
        print('A')

class B:
    @classmethod
    def printInfo(cls):
        print('B')

class AB(A, B):
    pass

class BA(B, A):
    pass

ab1 = AB()
ab1.printInfo()

ba1 = BA()
ba1.printInfo()
