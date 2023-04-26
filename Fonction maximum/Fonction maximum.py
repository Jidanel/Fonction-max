#*-* coding:Latin-1 -*-
from math import *

def tri_nombre(t):
    t=list(t)
    k=input("Entrez le nombre d'éléments souhaités: ")
    k=int(k)
    i=0
    while(i<k):
        x=input("Entrez les nombres: ")   #on prend en entrée les nombres qu'on range dans une liste
        x=float(x)                #on range ces elements comme des reels
        t.append(x)
        i=i+1
    i=0
    while(i<len(t)):
        if(t[i]>t[0]): #on teste la valeur de la position i avec celle de la position 0
           c=t[i]
           t[i]=t[0]   #Si cette valeur est plus grande on permute avec t[0]
           t[0]=c
        else:
            i=i+1       #sinon on passe à la position suivante
    return t[0]
p=[]
p=list(p)
d=tri_nombre(p)
        
print("le nombre le plus grand est :",d)


