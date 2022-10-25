# Author : Alif Radhitya

import numpy as np

opsi_menu = {
    1: 'opsi 1',
    2: 'Keluar',
}

def print_menu():
    for key in opsi_menu.keys():
        print (key, '--', opsi_menu[key] )
def opsi1():
    input_masuk = list(map(int,input()))
    input_masuk = np.asarray(input_masuk)
    x = np.mean(input_masuk)
    print('Maka hasil dari mean dari', input_masuk, 'adalah' , x)

if __name__=='__main__':
    while(True):
        print_menu()
        opsi = ''
        try:
            opsi = int(input('Masukkan pilihan: '))
        except:
            print('Salah cuk ...')

        if opsi == 1:
                opsi1()
        elif opsi == 2:
            print('Makasih dah make :*')
            exit()
        else:
            print('')
