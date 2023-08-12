from tkinter import *
from tkinter import ttk, messagebox
import pymysql
from tkcalendar import *
import datetime
import os

class Connexion:
    def __init__(self,root):
        self.root=root
        self.root.title("Connexion")
        self.root.geometry("1366x768+0+0")

        connexion_frame = LabelFrame(self.root, background="grey")
        connexion_frame.place(x=500, y=200, width=400, height=250)


        titre = Label(connexion_frame, bg="blue", fg="orange", relief=SUNKEN, font=("algerian",14), text="Connexion")
        titre.place(x=0,y=0,width=400)

        #variables
        self.mailetud=StringVar()
        self.motdepassetud=StringVar()
        self.questetud = StringVar()
        self.reponseetud = StringVar()
        self.motdepasseetud = StringVar()

        self.lbl_mail= Label(connexion_frame, text="Adresse Mail :", font=("times new roman", 14),fg="white", bg="grey")
        self.lbl_mail.place(x=5, y=50, width=150)
        self.txtmail= Entry(connexion_frame, font=("times new roman",12), width=30, bg="white", fg="black",textvariable=self.mailetud)
        self.txtmail.place(x=135, y=55)
        
        self.lbl_pass= Label(connexion_frame,text="Mot de passe : ", font=("times new roman",14), fg="white", bg="grey")
        self.lbl_pass.place(x=5, y=85, width=150)
        self.txtpass= Entry(connexion_frame, textvariable=self.motdepassetud, show="*", font=("times new roman", 14),width=27, bg="white", fg="black")
        self.txtpass.place(x=135, y=90)

        self.buttonregister= Button(connexion_frame, command="", text="Créer un compte", font=("times new roman",10), width=20, bg="green", fg="black",cursor="hand2",bd=0)
        self.buttonregister.place(x=50, y=150)

        self.buttonfgtpasswd= Button(connexion_frame, command=self.motdepasse_oublie, text="Mot de passe oublié", font=("times new roman",10), width=20, bg="green", fg="black",cursor="hand2", bd=0)
        self.buttonfgtpasswd.place(x=225, y=150)

        self.buttonok= Button(connexion_frame, command=self.connexion, text="Connexion", font=("algerian",12,"bold"), width=10, bg="green", fg="black",cursor="hand2")
        self.buttonok.place(x=150, y=200)



    def connexion(self):
        try:
            con= pymysql.connect(host="localhost",user="root",password="",database="etudiant")
            cursor = con.cursor()
            cursor.execute("select * from comptes where  email = %s and password=%s",(self.txtmail.get(),self.txtpass.get()))
            row=cursor.fetchone()
            if row==None:
                messagebox.showerror("Erreur","L'adresse mail et le mot de passe sont invalides")
            else:
                messagebox.showinfo("Connexion","Connexion reussie")
                con.close()

        except Exception as ex:
            messagebox.showerror("Erreur",f"Erreur de connexion : {str(ex)}")
        self.mailetud.set("")
        self.motdepassetud.set("")
    
    def motdepasse_oublie(self):
        if self.txtmail.get=="":
            messagebox.showerror("Erreur","Entrez premierement votre adresse mail") #On s'assure que l'utilisateur fournisse son mail pour obtenir le mot de passe
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="etudiant")
                cur= con.cursor()
                cur.execute("select * from comptes where email=%s",self.txtmail.get())
                row= cur.fetchone()
                if row==None:
                    messagebox.showerror("Erreur","Votre adresse mail n'est pas reconnu par le système")
                else:
                    con.close()
                    self.root2=Toplevel()  #Defini une fenetre popup qui sera au dessus de la fenetre parent
                    self.root2.title("Mot de passe oublié")
                    self.root2.config(bg="white")
                    self.root2.geometry("400x400+600+300")
                    self.root2.focus_force()  #Renforce cette fenetre, on ne pourra pas cliquer sur une autre tant que celle ci n'est pas fermée
                    self.root2.grab_set()

                    title=Label(self.root2, text="Mot de passe oublié ", font=("algerian",12,"bold"),bg="green", fg="black", relief=SUNKEN)
                    title.pack(side=TOP, fill="x")
                    #Questions et réponses utilisées pour la creation du compte
                    self.lbl_question = Label(self.root2, text="Selectionnez votre question lors de l'enregistrement : ", width=40, bg="white", fg="black", font=("times new roman",12))
                    self.lbl_question.place(x=15,y=35)
                    self.txtquestion=ttk.Combobox(self.root2,textvariable=self.questetud, font=("times new roman",10),width=25,state="readonly")
                    self.txtquestion["values"]=("Dans quel ville es tu né(e)","Où as tu rencontré ta partenaire actuelle","Le prenomm de ta maman")
                    self.txtquestion.place(x=35,y=60)
                    self.lbl_reponse = Label(self.root2, text="Reponse à la question : ", width=20, bg="white",font=("times new roman",12),fg="black" )
                    self.lbl_reponse.place(x=15, y=90)
                    self.txtreponse=Entry(self.root2, bg="white", fg="black", textvariable=self.reponseetud, font=("times new roman",10), width=25)
                    self.txtreponse.place(x=35, y=120)

                    #champ de création du nouveau mot de passe
                    self.lbl_motdepasse = Label(self.root2, text="Nouveau mot de passe : ", width=20, bg="white",font=("times new roman",12),fg="black" )
                    self.lbl_motdepasse.place(x=15, y=150)
                    self.lbl_txtmotdepass=Entry(self.root2, bg="white", fg="black", textvariable=self.motdepasseetud, show="*" ,font=("times new roman",10), width=25)
                    self.lbl_txtmotdepass.place(x=35, y=185)

            except Exception as ex:
                messagebox.showerror("Erreur",f"Erreur de connexion : {str(ex)}")


        








root = Tk()
obj = Connexion(root)
root.mainloop()