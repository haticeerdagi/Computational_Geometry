#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Drawing ellipse
import matplotlib.pyplot as plt
a=3
b=5
#plot the ellipse
x=np.linspace(-5.0, 5.0, num=100000)
y=(b**2*(1-(x**2)/(a**2)))**.5
plt.plot(x,y)
plt.plot(x,-y)
plt.show()


# In[ ]:




