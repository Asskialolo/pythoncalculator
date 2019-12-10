import view
import model

# Penyingkat Variabel
f = model.Model
v = view.View

class Main:
    def mainMenu():
        req = v.mainMenu()

        if req == 1 :
            result = v.operasi('+')
            print(result)
            check = v.cek('Mau Lagi ??')
            
            if check == 'y' :
                Main.mainMenu()
            elif check == 'n' :
                v.stop()
            else :
                print('ERROR PROCCESSING :')
                print('  Traceback (error proccessing request client) :')
                print('   Input is : <' + check + 'x0010> ValueError')
        elif req == 2 :
            result = v.operasi('-')
            print(result)
            check = v.cek('Mau Lagi ??')
            
            if check == 'y' :
                Main.mainMenu()
            elif check == 'n' :
                v.stop()
            else :
                print('ERROR PROCCESSING :')
                print('  Traceback (error proccessing request client) :')
                print('   Input is : <' + check + 'x0010> ValueError')    
        elif req == 3 :
            result = v.operasi('*')
            print(result)
            check = v.cek('Mau Lagi ??')
            
            if check == 'y' :
                Main.mainMenu()
            elif check == 'n' :
                v.stop()
            else :
                print('ERROR PROCCESSING :')
                print('  Traceback (error proccessing request client) :')
                print('   Input is : <' + check + 'x0010> ValueError')
        elif req == 4 :
            result = v.operasi('/')
            print(result)
            check = v.cek('Mau Lagi ??')
            
            if check == 'y' :
                Main.mainMenu()
            elif check == 'n' :
                v.stop()
            else :
                print('ERROR PROCCESSING :')
                print('  Traceback (error proccessing request client) :')
                print('   Input is : <' + check + 'x0010> ValueError')
        elif req == 5 :
            result = v.operasi('%')
            print(result)
            check = v.cek('Mau Lagi ??')
            
            if check == 'y' :
                Main.mainMenu()
            elif check == 'n' :
                v.stop()
            else :
                print('ERROR PROCCESSING :')
                print('  Traceback (error proccessing request client) :')
                print('   Input is : <' + check + 'x0010> ValueError')
        elif req == 6 :
            result = v.operasi('**')
            print(result)
            check = v.cek('Mau Lagi ??')
            
            if check == 'y' :
                Main.mainMenu()
            elif check == 'n' :
                v.stop()
            else :
                print('ERROR PROCCESSING :')
                print('  Traceback (error proccessing request client) :')
                print('   Input is : <' + check + 'x0010> ValueError')
        elif req == 7 :
            result = v.operasi('//')
            print(result)
            check = v.cek('Mau Lagi ??')
            
            if check == 'y' :
                Main.mainMenu()
            elif check == 'n' :
                v.stop()
            else :
                print('ERROR PROCCESSING :')
                print('  Traceback (error proccessing request client) :')
                print('   Input is : <' + check + 'x0010> ValueError')
        elif req == 8 :
            result = v.operasi('<-*')
            print(result)
            check = v.cek('Mau Lagi ??')
            
            if check == 'y' :
                Main.mainMenu()
            elif check == 'n' :
                v.stop()
            else :
                print('ERROR PROCCESSING :')
                print('  Traceback (error proccessing request client) :')
                print('   Input is : <' + check + 'x0010> ValueError')
        
        else:
            print("Error Inputing Data !!")
            Main.mainMenu()
        
Main.mainMenu()