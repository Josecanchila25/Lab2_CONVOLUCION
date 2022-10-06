import numpy as np
import matplotlib.pyplot as plt
i=0
y=0

I = []  #Vector 1
k = []          #vector 2

print('ingrese el tamaño del primer vector')
t= int(input('Tamaño: '))

for i in range(t):
     print("En el primer vector ingrese el dato", i + 1)
     valor =int( input('Valor: '))
     I.append(valor)

print('ingrese el tamaño del segundo vector')
t2= int(input('Tamaño: '))
 
for y in range(t2):
     print("En el segundo vector ingrese el dato", y + 1)
     valor2 = int(input('Valor: '))
     k.append(valor2)

print('Longitud de la señal de entrada: {}'.format(len(I)))
print('Longitud del kernel de convolucion: {}'.format(len(k)))
fig, axs = plt.subplots(3,sharex=True, sharey=True)

axs[0].stem(I)
axs[1].stem(k)
S=np.convolve(I,k)
print('La longitud de S debe ser (len(I)+ len(k)-1): {}'.format(len(S)))
plt.stem(S)
plt.show()