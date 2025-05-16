import sympy
from sympy.abc import x
import matplotlib.pyplot as plt
import numpy as np

a = int(input("¿En donde empieza la integral?\n"))
b = int(input("¿En donde termina la integral?\n"))
n = int(input("¿Cuántas particiones?\n"))
expr = input("¿Cuál es la funcion que quieres integrar?\npor ejemplo: E**(-x**2)\n")

p = (b - a)/n #calculamos las particiones
s = 0 #iniciamos la suma en 0


f = lambdify(x, expr) #convertimos la expresion en una funcion usable en python

for i in range(n): #calculamos la suma de la altura de todos los rectangulos
    s += f(a + p*i )

I = s*p #multiplicamos la suma de las alturas por el ancho de cada rectangulo, para tener el valor de la suma de Riemann

print(f"la suma de Riemann de la función {expr}, que inicia en {a} y termina en {b}, con {n} particiones da igual a {I}")

fig, ax = plt.subplots() #inicializamos el gráfico
z = np.linspace(a,b,1000) #El dominio para graficar la función
h = np.linspace(a+p/2, b-p/2, n)#El domino para graficar las barras
ax.plot(z,f(z),color = 'black')#Graficamos la función
ax.bar(h,f(h-p/2), width = p, linewidth=0)#Graficamos las barras
ax.grid(True)
ax.axhline(0,color = 'black',linewidth = 0.9)#Graficamos una linea para visualizar mejor el eje x
plt.style.use('ggplot')