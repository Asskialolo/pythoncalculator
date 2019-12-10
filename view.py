import model

m = model.Model

class View:
    # DEF DASAR
    def line():
        print("==========================================================")

    def menu(noList, namaMenu) :
        print('[' + str(noList) + '] - ' + str(namaMenu))

    def n():
        print("")

    def req():
        View.line()
        View.n()
        request = int(input('Pilih Menu : '))
        return request

    def stop():
        print('THANKS FOR TESTING !!')
        print('By : Typogramming')

    # DEF DEVELOPED
    def mainMenu():
        View.n()
        View.line()
        print("\t\tKALKULATOR VERSI PYTHON 2.0")
        View.line()
        View.n()
        View.menu(1, 'Tambah (+)')
        View.menu(2, 'Kurang (-)')
        View.menu(3, 'Kali (*)')
        View.menu(4, 'Bagi (/)')
        View.menu(5, 'Modulus (%)')
        View.menu(6, 'Pangkat (**)')
        View.menu(7, 'Akar (//)')
        View.menu(8, 'Factorial (<-*)')
        View.n()
        req = View.req()
        View.n()
        return req

    def cek(menu):
        View.n()
        check = str(input(menu + ' : [y/n] -> '))
        View.n()
        return check

    def operasi(operasi):
        View.line()
        View.n()
        num = int(input('Masukkan Angka : '))
        View.n()
        
        # total = m.tambah(num, num2)
        if operasi == '+' :
            num2 = int(input(str(num) + ' ' + operasi + ' '))
            View.n()
            total = m.tambah(num, num2)
            result = str(num) + ' ' + operasi + ' ' + str(num2) + ' = ' + str(total)
        elif operasi == '-' :
            num2 = int(input(str(num) + ' ' + operasi + ' '))
            View.n()
            total = m.kurang(num, num2)
            result = str(num) + ' ' + operasi + ' ' + str(num2) + ' = ' + str(total)
        elif operasi == '*' :
            num2 = int(input(str(num) + ' ' + operasi + ' '))
            View.n()
            total = m.kali(num, num2)
            result = str(num) + ' ' + operasi + ' ' + str(num2) + ' = ' + str(total)
        elif operasi == '/' :
            num2 = int(input(str(num) + ' ' + operasi + ' '))
            View.n()
            total = m.bagi(num, num2)
            result = str(num) + ' ' + operasi + ' ' + str(num2) + ' = ' + str(total)
        elif operasi == '%' :
            num2 = int(input(str(num) + ' ' + operasi + ' '))
            View.n()
            total = m.modul(num, num2)
            result = str(num) + ' ' + operasi + ' ' + str(num2) + ' = ' + str(total)
        elif operasi == '**' :
            num2 = int(input(str(num) + ' ' + operasi + ' '))
            View.n()
            total = m.pangkat(num, num2)
            result = str(num) + ' ' + operasi + ' ' + str(num2) + ' = ' + str(total)
        elif operasi == '//' :
            num2 = int(input(str(num) + ' ' + operasi + ' '))
            View.n()
            total = m.akar(num, num2)
            result = str(num) + ' ' + operasi + ' ' + str(num2) + ' = ' + str(total)
        elif operasi == '<-*' :
            total = m.factorial(num)
            result = str(num) + ' ' + operasi + ' = ' + str(total)
            
        return result