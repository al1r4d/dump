# Author : Alif Radhitya

import numpy as np 
input_masuk = list(map(int,input()))
input_masuk = np.asarray(input_masuk)
x = np.mean(input_masuk)
print('Maka hasil dari mean dari', input_masuk, 'adalah' , x)

