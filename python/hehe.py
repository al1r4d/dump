# Author : Alif Radhitya

import numpy as np
import math
import matplotlib.pyplot as plt
import statistics as st
import pandas as pd
import random

print("""
          __          __                            
  _______/  |______ _/  |_  ______    ______ ___.__.
 /  ___/\   __\__  \\   __\/  ___/    \____ <   |  |
 \___ \  |  |  / __ \|  |  \___ \     |  |_> >___  |
/____  > |__| (____  /__| /____  > /\ |   __// ____|
     \/            \/          \/  \/ |__|   \/     
""")
print('Alif Radhitya | Hanya untuk bersenang - senang')
opsi_menu = {
    1: 'opsi 1',
    2: 'Keluar',
}

def print_menu():
    for key in opsi_menu.keys():
        print (key, '--', opsi_menu[key] )
def opsi1():
    input_masuk = list(map(int, input('Masukkan data yang diinginkan: ').split(",")))
    check_input_masuk = print('Inilah data yang anda masukkan: ', input_masuk)
    input_masuk = np.array(input_masuk)
    suku = len(input_masuk)
    print('Jumlah suku adalah', suku)
    data_mean = print('Mean:', np.mean(input_masuk))
    data_modus = print('Modus:', st.mode(input_masuk))
    data_median = print('Median:', st.median(input_masuk))
    sturgess = 1+3.3*math.log10(suku)
    print('Maka hasil dari sturgess adalah' , sturgess)
    sturgess_round = print('dan dibulatkan menjadi', round(sturgess))
    interval = (max(input_masuk)-min(input_masuk))/round(sturgess)
    print('Interval:', interval)
    batas = min(input_masuk)+interval-1
    print('Batas:', batas) 
    #histogram = np.random.normal(input_masuk)
    #plt.hist(histogram)
    #plt.show()
    #interval = print('I:', print((max(input_masuk)-min(input_masuk)/print(1+3.3*math.log10(len(input_masuk))))))
  #  batas_atas_data_pertama = print('batas atas: ', min(input_masuk)-print((max(input_masuk)-min(input_masuk)/(1+3.3*math.log10(len(input_masuk))+1))))
    # k = np.histogram_bin_edges(n, bins='auto')
def opsi3():
    input_data = list(map(int,input().split(",")))
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
