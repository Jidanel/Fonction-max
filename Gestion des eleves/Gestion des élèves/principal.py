#importation des bibliothèques
import tkinter
from subprocess import run  #pour transiter entre les fenetres
from tkinter import ttk, Tk
from tkinter import *
from tkinter import messagebox
import mysql.connector

#fonction de manipulation de base de données
#fonction ajouter
def Ajouter():
    matricule=txtmatricule.get()
    noms=txtnoms.get()
    prenoms=txtprenoms.get()
    sexe=valeursexe.get()
    classe=comboclass.get()
    matiere=txtmatières.get()
    note= txtnotes.get()

    maBase = mysql.connector.connect(host="localhost", user="root", password="",database="gestion_eleves")
    meconnect=maBase.cursor()

    try:
        sql="INSERT INTO notes (Matricule, Noms, Prenoms, Sexe, Classe, Matieres, Notes) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val= (matricule,noms,prenoms,sexe,classe,matiere,note)
        meconnect.execute(sql,val)
        maBase.commit()
        derniermatricule = meconnect.lastrowid
        messagebox.showinfo('Information', 'Enregistrement reussi')
        root.destroy()
        run(['python, principal.py'])

    except Exception as e:
        print(e)
        maBase.rollback()
        maBase.close()


#definition de la fenetre
root = Tk()
root.title("Logiciel de gestion de notes")  #definition du titre
root.geometry("1350x700+0+0")  #fenetre de 400 de largeur et 300 de hauteur aux coordonnées k(450,200)
root.resizable(False,False)   #fenetre non reductible
root.configure(bg="#091821")   #Couleur

#Ajout de la bande superieure portant le titre
titre=Label(root,borderwidth=3,relief=SUNKEN,text="GESTION DES NOTES", font=("Times New Roman", 20), bg="#091821",fg="white")
titre.place(x=0,y=0,width=1350)

#Creation du formulaire
#matricule
lblmatricule=Label(root,text="Matricule :", font=("Arial",15),bg="#091821",fg="white")
lblmatricule.place(x=0,y=100,width=150)

txtmatricule=Entry(root,bd=4,font=("Arial",12,"bold"))
txtmatricule.place(x=160,y=100,width=250, height=30)

#Noms
lblnoms=Label(root,text="Noms :", font=("Arial",12),bg="#091821",fg="white")
lblnoms.place(x=0,y=150,width=150)

txtnoms=Entry(root,bd=4,font=("Arial",12, "bold"))
txtnoms.place(x=160,y=150,width=250, height=30)

#Prenoms
lblprenoms=Label(root,text="Prenoms :", font=("Arial",12),bg="#091821",fg="white")
lblprenoms.place(x=0,y=200,width=150)

txtprenoms=Entry(root,bd=4,font=("Arial",12, "bold"))
txtprenoms.place(x=160,y=200,width=250, height=30)

#Sexe
valeursexe= StringVar()
lblsexe=Label(root,text="Sexe :", font=("Arial",15),bg="#091821",fg="white")
lblsexe.place(x=0,y=250,width=150)
lblsexem= Radiobutton(root,text="M", value="M", variable=valeursexe, indicatoron=0,font=("Arial",15),bg="red",fg="black")
lblsexem.place(x=160,y=250,width=30)
lblsexef= Radiobutton(root,text="F", value="F", variable=valeursexe, indicatoron=0,font=("Arial",15),bg="red",fg="black")
lblsexef.place(x=200,y=250,width=30,)
#indicatoron veut dire indicateur on donc allumer le bouton radio

#Liste des classes
lblclass=Label(root,text="Classe :", font=("Arial",15),bg="#091821",fg="white")
lblclass.place(x=0,y=300, width=150)
comboclass=ttk.Combobox(root,font=("Times New Romain",14))
comboclass['values']=['6e','5e','4e All','4e Esp','3e All','3e Esp','2ndeA4 All','2ndeA4 ESP','2nde C','1ereA4 All','1ereA4 Esp','1ere C','1ere D','TleA4 All','TleA4 Esp','Tle C','Tle D']
comboclass.place(x=160,y=300,width=100)

#Matières
lblmatières=Label(root,text="Matières :", font=("Arial",12),bg="#091821",fg="white")
lblmatières.place(x=0,y=350,width=150)

txtmatières=Entry(root,bd=4,font=("Arial",12, "bold"))
txtmatières.place(x=160,y=350,width=250, height=30)

#Notes
lblnotes=Label(root,text="Notes :", font=("Arial",12),bg="#091821",fg="white")
lblnotes.place(x=0,y=400,width=150)

txtnotes=Entry(root,bd=4,font=("Arial",12, "bold"))
txtnotes.place(x=160,y=400,width=250, height=30)

#Bouton Enregistrer
btnenregistrer=Button(root,text="Ajouter", font=("Arial",12),bg="red",fg="white", command=Ajouter)
btnenregistrer.place(x=160, y=450,width=200)

#Bouton Modifier
btnmodifier=Button(root,text="Modifier", font=("Arial",12),bg="red",fg="white")
btnmodifier.place(x=160, y=500,width=200)

#Bouton Supprimer
btnmodifier=Button(root,text="Supprimer", font=("Arial",12),bg="red",fg="white")
btnmodifier.place(x=160, y=550,width=200)

#base de données

#affichage de la table des enregistrements
table=ttk.Treeview(root,columns=(1,2,3,4,5,6,7), height=7, show="headings")
table.place(x=450, y=100, width=850, height=500)

#En têtes
table.heading(1,text="Mle")
table.heading(2,text="Noms")
table.heading(3,text="Prenoms")
table.heading(4,text="Sexe")
table.heading(5,text="Classe")
table.heading(6,text="Matière")
table.heading(7,text="Notes")

#Definir la taille des colonnes
table.column(1,width=50)
table.column(2,width=200)
table.column(3,width=200)
table.column(4,width=100)
table.column(5,width=100)
table.column(6,width=150)
table.column(7,width=50)

#afficher les infos de la bd
maBase= mysql.connector.connect(host="localhost", user="root", password="", database="gestion_eleves")
meconnect=maBase.cursor()
meconnect.execute("select * from notes")
for r in meconnect:
    table.insert('',END,value=r)
maBase.close()



#boucle
root.mainloop()
