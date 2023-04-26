#importation des bibliothèques
import tkinter
from subprocess import call  #pour transiter entre les fenetres
from tkinter import ttk, Tk
from tkinter import *
from tkinter import messagebox
import mysql.connector

#definition de la fenetre
root = Tk()
root.title("Logiciel de gestion de notes")  #definition du titre
root.geometry("1350x700+0+0")  #fenetre de 400 de largeur et 300 de hauteur aux coordonnées k(450,200)
root.resizable(False,False)   #fenetre non reductible
root.configure(bg="#091821")   #Couleur

#Ajout de la bande superieure portant le titre
titre=Label(root,borderwidth=3,relief=SUNKEN,text="GESTION DES NOTES", font=("Times New Roman", 20), bg="#091821",fg="white")
titre.place(x=0,y=0,width=1350)


#boucle
root.mainloop()