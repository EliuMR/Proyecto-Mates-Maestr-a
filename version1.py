# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plot
import numpy as np 
import seaborn as sns
print('')
print('********************************')
print('Author: Eliú Moreno Ramírez')
print('Created on Nov 2022')
print('Proyecto Estadística')
print('********************************')
print('En un estudio de ruptura de la urdimbre durante el tejido de telas(Technometrics, 1982:63), se sometieron a prueba 100 muestras de hulo. Se determinó el número de ciclos de esfuerzo hasta ruptura para cada muestra de hilo y se obtuvieron los datos siguientes: ')
df=pd.read_excel('Datos.xlsx')
#print(df)
ordenado =df.sort_values('Valores',ascending=True) #Ordenamos los valores en orden ascendente
oo = np.array(ordenado).reshape(len(ordenado))#creamos el array para la grafica de caja
#print(ordenado.head())
amplitud=85
under=int(ordenado.min())#Guardamos el Xmin de todos los intervalos
rango=int(ordenado.max())-int(ordenado.min())
intervalos=int(rango/amplitud)+1
clase=[]#Creamos una lista donde guardamos los intervalos
frecuencia=[]#Creamos una lista para guardas las frecuancias acomuladas

#Creamos en una lista los intervalos en clase
#Creamos el tamaño de la lista para las frecuecias de acuerdo a los intervalos
for i in range (intervalos):
    subclase=[]
    subfres=[]
    underaux=under
    for i in range(2):#guardamos los intervalos
        subclase.append(underaux)
        underaux=underaux+amplitud
    clase.append(subclase)
    under=under+amplitud
    frecuencia.append(subfres)
datos=ordenado.to_numpy().tolist()

contador=0
#Como ya tenemos los datos ordenados es más fácil calcular la frecuencia en cada clase, que se hace de la siguiente manera
for i in range(intervalos):
    suma=0
    while contador<100:
        if datos[contador][0]<clase[i][1]:
            suma=suma+1
            contador=contador+1
        else:
            break
    frecuencia[i]=suma
frecuenciaAcomulada=[]
frecuenciaRelativa=[]
frecuenciaRelativaAcomulada=[]
porcentaje=[]
porcentajeAcomulado=[]
marcasClase=[]
#Calculamos frecuencia relativa
#Calculamos frecuencia acomulada
#Calculamos frecuencia relativa acomulada
#Calculamos frecuencia porcentaje
#Calculamos frecuencia porcentaje acomulado
for i in range(intervalos):
    frecuenciaRelativa.append(frecuencia[i]/100)
    suma=0
    for j in range(i+1):
        suma=suma+frecuencia[j]
    frecuenciaAcomulada.append(suma)
    frecuenciaRelativaAcomulada.append(suma/100)
    porcentaje.append(frecuenciaRelativa[i]*100)
    suma=0
    for j in range(i+1):
        suma=suma+porcentaje[j]
    porcentajeAcomulado.append(suma)
    marcasClase.append((clase[i][1]-clase[i][0])/2+clase[i][0])
#Mostramos la tabla de frecuenias    
tabla = list(zip(clase, frecuencia,frecuenciaAcomulada,frecuenciaRelativa,frecuenciaRelativaAcomulada,porcentaje,porcentajeAcomulado,marcasClase))
df = pd.DataFrame(tabla,columns=['Intervalos','Frecuencia fi','Acomulada Fi','Frecuencia Relativa hi','Relativa acomulada Hi','Porcentaje pi %','Porcentaje Acomulada Pi %','Marca de Clase'])
print(df)
print('El valor máximo en el registro es: ',int(ordenado.max()))
print('El valor mínimo en el registro es: ',int(ordenado.min()))
print('El rango de los datos es: ',rango)
#Definimos una función para el cálculo de cuantiles
def percentil(k):
    I=(frecuenciaAcomulada[intervalos-1]*k/100)
    busqueda=0
    for i in range (len(frecuenciaAcomulada)):
        if I<frecuenciaAcomulada[i]:
            busqueda=i
            break
    percentil=clase[busqueda][0]+((I-frecuenciaAcomulada[busqueda-1])/(frecuencia[busqueda]))*(clase[busqueda][1]-clase[busqueda][0])
    print('Por lo tanto P'+str(k)+'=',percentil)
print('El cálculo de algunos cuantiles son: ')
#percentil(10)
percentil(25)
percentil(75)
percentil(80)
percentil(90)
bandera=True #Verifica si el usuario gusta calcular un nuevo cuantil
while bandera:
    print('¿Desea calcular otro cuantil?[S/N]')
    respuesta=input()
    if respuesta=='S':
        print('Escriba el número del percentil buscado')
        k=int(input())
        percentil(k)
    else:
        bandera=False
#Media
suma=0

for i in range(frecuenciaAcomulada[-1]):
    suma=datos[i][0]+suma
media=suma/(frecuenciaAcomulada[-1])
print('La media de los datos es: ',media)

#Mediana
mediana=(datos[50][0]+datos[51][0])/2
print('La mediana de los datos es: ', mediana)

#Moda
verificarmoda=np.zeros(100)
for i in range(frecuenciaAcomulada[-1]):
    x=datos[i][0]
    k=0
    for j in range(frecuenciaAcomulada[-1]):
        if(x==datos[j][0]):
            k=k+1
    verificarmoda[i]=k
for i in range(frecuenciaAcomulada[-1]):
    if verificarmoda[i]==np.max(verificarmoda):
        indicemoda=i
print('La moda de los datos son: ',datos[indicemoda][0])   

#varianza
var=0
for i in range(frecuenciaAcomulada[-1]):
    termino=(datos[i][0]-media)**2
    suma=suma+termino
varianza=suma/100
print('La varianza es: ',varianza)

#desviación estandas
desviacionEstandar=np.sqrt(varianza)
print('La desviación estandar es: ', desviacionEstandar)
#Esperanza
print('La Esperanza matemática es: ',media)
#Primer momento
print('El primer momento es: ',media)
#Segundo momento
print('El segundo momento es: ', varianza)
#tercer momento
ter=0
for i in range(100):
    termino=(datos[i][0]-media)**3
    ter=ter+termino
tercer=ter/(100*desviacionEstandar**3)
print('El tercer momento es: ',tercer)

#sns.boxplot(x=oo)
#plot.show()
#Esta Parte es para crear intervalos y agregar el histograma

claseIntervalos=[]
for i in range(intervalos):
    claseIntervalos.append(str(clase[i]))   
"""
plot.bar(claseIntervalos,df['Frecuencia fi'])
plot.show()"""

#Aquí creamos solo un intervalo para crear el histograma
aux=[]
for j in range(intervalos):
    for i in range(frecuencia[j]):
        aux.append(marcasClase[j])
fig, ax = plot.subplots(5, figsize=(4,16))
ax[0].barh(marcasClase,df['Frecuencia fi'],color='r')
ax[0].set_title("Gráfica de Barras")
ax[0].set_xlabel('Frecuencia')
ax[0].set_ylabel('Intervalo')
ax[1].plot(marcasClase,frecuencia,'D')
ax[1].plot(marcasClase,frecuencia,'b')
ax[1].set_title("Poligono de frecuencias")
ax[1].set_ylabel('Frecuencia')
ax[1].set_xlabel('Intervalo')
ax[2].hist(x=aux, bins=intervalos, color='g', rwidth=0.85)
ax[2].set_title("Histograma")
ax[2].set_ylabel('Frecuencia')
ax[2].set_xlabel('Intervalo')
sns.boxplot(ax=ax[3],x=oo)
ax[4].bar(claseIntervalos,df['Frecuencia fi'])

plot.show()