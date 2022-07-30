

#Modules
import numpy as np 
import matplotlib.pyplot as plt 


T = np.array ([0.1 , 0.2 , 1])  # Temperature Grid

Beta = 1/T   # Inverse Temperature

Mu = np.linspace (-5 , 5 , 1001)  # chemical potential grid



# Partition function for single site Hubbard Model 

def partition_function ( beta , mu , U): 

    return np.exp (-beta*U/4) + 2* np.exp (beta * (U/4 + mu)) + np.exp (- beta * (U/4 - (2*mu)))  # U is hubbard parameter


# n = n_up + n_down 

def number_density (beta , mu ,  U ):

    Z = partition_function (beta , mu , U )

    return (2/Z) * (np.exp (beta*(U/4 + mu)) + np.exp (-beta * (U/4 - (2*mu)) ))



for j in Beta:

    Rho = number_density (j , Mu , 3)
    plt.plot (Mu , Rho, label = 'T = ' + str(1/j))

plt.xlabel (r'$\mu$')
plt.ylabel (r'$n$')
plt.grid()
plt.legend()
plt.show()

