import view

class Model:
    def tambah(a, b):
        return a + b

    def kurang(a, b):
        return a - b

    def kali(a, b):
        return a * b

    def bagi(a, b):
        return a / b

    def modul(a, b):
        return a % b
    
    def pangkat(a, b):
        return a ** b

    def akar(a, b):
        return a // b

    def factorial(a):
        if a < 2:
            return 1
        else:
            return a * Model.factorial(a-1)
