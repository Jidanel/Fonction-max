from tkinter import *
from tkinter import ttk, messagebox
import pymysql
from tkcalendar import *
import datetime
import os

class pp:
   def __init__(self,root): 

    self.root=root
    self.root.title("Mot de passe oublié")
    self.root.config(bg="white")
    self.root.geometry("400x200+600+300")
    self.root.focus_force()  #Renforce cette fenetre, on ne pourra pas cliquer sur une autre tant que celle ci n'est pas fermée
    self.root.grab_set()

    title=Label(self.root, text="Mot de passe oublié ", font=("algerian",12,"bold"),bg="green", fg="black", relief=SUNKEN)
    title.pack(side=TOP, fill="x")

    self.questetud= StringVar()
    self.reponseetud= StringVar()

    self.lbl_question = Label(self.root, text="Selectionnez votre question utilisée lors de l'enregistrement : ", width=40, bg="white", fg="black", font=("times new roman",12))
    self.lbl_question.place(x=15,y=35)
    self.txtquestion=ttk.Combobox(self.root,textvariable=self.questetud, font=("times new roman",10),width=25,state="readonly")
    self.txtquestion["values"]=("Dans quel ville es tu né(e)","Où as tu rencontré ta partenaire actuelle","Le prenomm de ta maman")
    self.txtquestion.place(x=25,y=60)
    self.lbl_reponse = Label(self.root, text="Reponse à la question : ", width=20, bg="white",font=("times new roman",12),fg="black" )
    self.lbl_reponse.place(x=5, y=90)
    self.txtreponse=Entry(self.root, bg="white", fg="black", textvariable=self.reponseetud, font=("times new roman",10), width=25)
    self.txtreponse.place(x=25, y=120)



root = Tk()
obj = pp(root)
root.mainloop()