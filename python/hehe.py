# Author : Alif Radhitya

import numpy as np
import matplotlib.pyplot as plt
opsi_menu = {
    1: 'opsi 1',
    2: 'Keluar',
    3: 'opsi 3',
}

def print_menu():
    for key in opsi_menu.keys():
        print (key, '--', opsi_menu[key] )
def opsi1():
    input_masuk = list(map(int,input()))
    input_masuk = np.asarray(input_masuk)
    x = np.mean(input_masuk)
    print('Maka hasil dari mean dari', input_masuk, 'adalah' , x)
def opsi3():
    input_data = list(map(int,input()))
    maks = max(input_data)
    minim = min(input_data)
    Range = maks-minim
    Deviasi = np.std(input_data)
    print("Deviasi = {}, Maksimum = {}, Minimum = {}, dan Range = {}".format(Deviasi, maks, minim, Range))
    plt.hist(input_data)
    plt.show()
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
        elif opsi == 3:
            opsi3()
        elif opsi == 2:
            print('Makasih dah make :*')
            exit()
        else:
            print('')
