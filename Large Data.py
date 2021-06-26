#Group Data


#online sample
import numpy as np
import matplotlib.pyplot as plt
import math

data = np.loadtxt('bigdata.txt')

def mean(data):
    
   return sum(data)/len(data)



mean_value= mean(data)




def SD(data):
    
    return (sum(((data-mean(data)))**(2))/(len(data)-1))**(1/2)

SD_value= SD(data)


print('\t   Mean +/-  STDDEV =', mean_value, '+/-' , SD_value, 'pc')




#plot_data

plt.figure(1)
plt.plot(np.arange(0,1000), data , 'ro')
plt.xlabel('Measurment')
plt.ylabel('Distance pc')
plt.show()
plt.savefig('Large data Distribution.png')

#Histogram



#plt.figure(2)
#plt.hist(data, density=True, bins=11)
#plt.xlabel('Distance (pc)')
#plt.ylabel('Number of measurment')






#part3

photon_data= np.loadtxt('bigdata.txt')


def mean(photon_data):
    
   return sum(photon_data)/len(photon_data)



mean_value= mean(photon_data)




def SD(photon_data):
    
    return (sum(((photon_data-mean(photon_data)))**(2))/(len(photon_data)-1))**(1/2)

SD_value= SD(photon_data)


print('for photon:Mean +/-  STDDEV =', mean_value, '+/-' , SD_value, 'pc')


#poisson
    
meannumber=20

plist = []
for x in range(6,39,1):


    p = (np.exp(-meannumber)*((meannumber**x)/(math.factorial(x))))

  
    
    plist.append(p)


#Gaussian
     
glist= []
for y in range(6,39,1):
    
    g = ((1/((SD_value)*(np.sqrt((2*math.pi)))))*(np.exp((-1/2)*((y - meannumber)/(SD_value))**(2))))  
    glist.append(g)
    
  

plt.figure(3)
plt.hist(photon_data, density=True, bins=11)
plt.xlabel('Number of photon')
plt.ylabel('Number of measurment')

plt.plot(np.arange(6,39,1), plist, 'r-', label="Poisson Distribution" )
plt.plot(np.arange(6,39,1), glist, 'b-', label='Gaussian Distrribution')
plt.legend()
plt.show()
plt.savefig('Large Data Distiribution value .png')


