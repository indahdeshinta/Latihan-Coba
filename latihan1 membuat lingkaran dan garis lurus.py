# LATIHAN UNTUK MEMBUAT LINGKARANN DAN GARIS LURUS

import numpy as np
from matplotlib import pyplot as plt

#membuat linkaran
PI = np.pi
sudut = np.linspace(0,2*PI,100)
radius = 5;

x= radius * np.cos(sudut)
y= radius * np.sin(sudut)

#membuat garis
#x= [1,2,3,4,5]
#y= [1,2,3,4,5]


plt.plot(x,y) #inisialisasi plot

plt.show() #tampilkan