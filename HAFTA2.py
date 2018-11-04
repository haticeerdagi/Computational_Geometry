import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

point1=np.array([0,0,0]) #orjinden geçen x=1 y=-2 z=1 olan bir normal var meshgrid yapısı ile oluşturucaz  point - nokta , normal-doğru
normal1=np.array([1,-2,1])

point2=np.array([0,-4,0])
normal2=np.array([0,2,-8])

point3=np.array([0,0,1])
normal3=np.array([-4,5,9])

point_test = np.array([1,-1,1])   #np bu listeleri çarpabiliyor , kullanmadan yaparsak hata alırız
normal_test = np.array([1,-2,1])
np.sum(point_test*normal_test)

d1 = -np.sum(point1*normal1) # dot product -- distance(uzunluk)
d2 = -np.sum(point2*normal2) # dot product -- distance(uzunluk)
d3 = -np.sum(point3*normal3) # dot product -- distance(uzunluk)
d1,d2,d3


#meshgrid:3boyutlu çizim yapmak için kullanılır (np.meshgrid fonksiyonu)

# 4x+5y+6z+7   -<4,5,6>.<x,y,z> = d    skaler çarpma aradaki işlem
xx,yy=np.meshgrid(range(5),range(5))#4x4 kare şeklinde oluyor

xx  # 5^3 değeri 125 tane değer geliyor 3 boyutlu
yy

z1 = (-normal1[0]*xx - normal1[1]*yy - d1)*1./normal1[2]
get_ipython().magic('matplotlib inline')
plt3d = plt.figure().gca(projection='3d')
plt3d.plot_surface(xx,yy,z1,color='blue')  

