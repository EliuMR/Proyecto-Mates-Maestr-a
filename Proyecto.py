import pandas as pd
df=pd.read_excel('Datos.xlsx')
#print(df)
ordenado =df.sort_values('Valores',ascending=True) #Ordenamos los valores en orden ascendente
#print(ordenado.head())
amplitud=80
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
#Como ya tenemos los datos 
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
tabla = list(zip(clase, frecuencia,frecuenciaAcomulada,frecuenciaRelativa,frecuenciaRelativaAcomulada,porcentaje,porcentajeAcomulado))
df = pd.DataFrame(tabla,columns=['Intervalos','Frecuencia fi','Acomulada Fi','Frecuencia Relativa hi','Relativa acomulada Hi','Porcentaje pi %','Porcentaje Acomulada Pi %'])
print(df)


