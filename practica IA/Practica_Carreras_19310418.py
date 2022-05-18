import random
import numpy as np
import cv2
import networkx as nx
import matplotlib.pyplot as plt


#Grupos que van a competir
Seleccion_Alfa=["Flad","Aron","Azufel","Chuntaro","Rapidash"]
Seleccion_Lobo=["Buda","Gary","Dash","Ponyta","Alucard"]
Seleccion_Buena_onda=["Leomord","Sun","Rodger","Martin","Dom"]
Seleccion_Maravilla=["Richy","Jon jon","Charin","Miguel","Ninsi"]
Seleccion_Anillos=["Gandalf","Frodo","Gimble","Sam","Legolas"]
print('Putazos 1:',Seleccion_Alfa)
print('Putazos 2:',Seleccion_Lobo)
print('Putazos 3:',Seleccion_Buena_onda)
print('Putazos 4:',Seleccion_Maravilla)
print('Putazos 5:',Seleccion_Anillos)

#Ciclos para determinar la rapidez

Rapidez=np.zeros((5,5))
Dimension=Rapidez.shape
for x in range(Dimension[0]):
    for y in range(Dimension[0]):
        Rapidez[x,y]=random.randint(50,125)
print('\n Puntuaciones')

for x in range(5):
    Rapidez[x].sort()

Rapidez=Rapidez[np.argsort(Rapidez[:,-1])]
for x in range(5):
    print("Putazos",5-x,":",Rapidez[x])
#Acomodo para obtener los 5 primeros ganaores(carreras)
for x in range(5):
    print('Chingon Seleccion',5-x,Rapidez[x,4])
#Arreglo de carrera 6
Putazos_6 =Rapidez[np.argsort(Rapidez[:, -1])]
Putazos_6.sort()
for x in range(5):
  print(Putazos_6[x]) 
print("Putazos 6:", Putazos_6, "\n")  
print("Caballo más chingon: ", int(Putazos_6[4,4]), "Rapidez total\n")
#Arreglo de carrera 7
Putazos_7= [Putazos_6[2, 4], Putazos_6[3, 4], Putazos_6[3, 3], Putazos_6[4, 3], Putazos_6[4, 2]]
Putazos_7.sort()
print("Putazos 7:", Putazos_7, "\n")
print ("Caballo casi mas chingon: ", int(Putazos_7[4]), "Rapidez total")
print(" Podio:\n El mas chingon: ",int(Putazos_6[4,4]),"en Rapidez total ","\n Casi mas chingon: ",int(Putazos_7[4]),"en rapidez total")


#Grafo
Mas_Chingon= Putazos_6[4,4]
Casi_Chingon= Putazos_7[4]
Chingones = nx.Graph()  
Chingones.add_edge('Chingones ',Mas_Chingon) 
Chingones.add_edge('Chingones ',Casi_Chingon) 
fig, ax = plt.subplots()
nx.draw(Chingones, ax=ax, with_labels=True, )
plt.show()


