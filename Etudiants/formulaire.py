from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import *
import datetime
import pymysql
import os

class Formulaire:
    def __init__(self,root):
        self.root=root
        self.root.title("Formulaire")
        self.root.geometry("1366x768+0+0")

        #Frame d'enregistrement
        Creation_frame = LabelFrame(self.root, bg="grey")
        Creation_frame.place(x=500,y=200, width=450, height=450)
        title = Label(Creation_frame, text="Creer un compte", font=("Algerian",14,"bold"),relief=SUNKEN, fg="black", bg="blue")
        title.place(x=0,y=0, width=450)

        #Variables
        self.nometud=StringVar()
        self.prenometud=StringVar()
        self.mailetud=StringVar()
        self.mailetudreapeat=StringVar()
        self.phoneetud=StringVar()
        self.motdepasseetud=StringVar()
        self.motdepasseetudrepeat=StringVar()
        self.datenaiss=StringVar()
        self.questetud=StringVar()
        self.reponseetud=StringVar()
        self.question= ["Selectionner...","Dans quel ville es tu né(e)","Où as tu rencontré ta partenaire actuelle","Quel est le prenomm de ta maman"]


        self.lbl_nom = Label(Creation_frame, text="Noms : ", width=10, bg="grey", fg="white", font=("times new roman",12))
        self.lbl_nom.place(x=10,y=50)
        self.txtnom=Entry(Creation_frame,bg="white", fg="black",textvariable=self.nometud, font=("times new roman",10),width=25)
        self.txtnom.place(x=30,y=75)
        self.lbl_prenom = Label(Creation_frame, text="Prenom : ", width=10, bg="grey",font=("times new roman",12),fg="white" )
        self.lbl_prenom.place(x=200, y=50)
        self.txtprenom=Entry(Creation_frame, bg="white", fg="black", textvariable=self.prenometud, font=("times new roman",10), width=25)
        self.txtprenom.place(x=220, y=75)
        self.lbl_adrmail = Label(Creation_frame, text="Email : ", width=10, bg="grey",fg="white",font=("times new roman", 12))
        self.lbl_adrmail.place(x=5, y=100)
        self.txtadrmail=Entry(Creation_frame,bg="white", fg="black",textvariable=self.mailetud, font=("times new roman",10),width=25)
        self.txtadrmail.place(x=30,y=125)
        self.lbl_adrmail_bis= Label(Creation_frame, text="Repeter Email : ", width=10, bg="grey",fg="white",font=("times new roman", 12))
        self.lbl_adrmail_bis.place(x=220, y=100)
        self.txtadrmailbis=Entry(Creation_frame, bg="white", fg="black", textvariable=self.mailetudreapeat, font=("times new roman",10), width=25)
        self.txtadrmailbis.place(x=220, y=125)
        self.lbl_motdepass = Label(Creation_frame, text="Mot de passe : ", width=10, bg="grey",fg="white",font=("times new roman", 12))
        self.lbl_motdepass.place(x=30, y=150)
        self.lbl_txtmotdepass=Entry(Creation_frame, bg="white", fg="black", textvariable=self.motdepasseetud, show="*" ,font=("times new roman",10), width=25)
        self.lbl_txtmotdepass.place(x=30, y=175)
        self.lbl_motdepassbis = Label(Creation_frame, text="Repeter mot de passe : ", width=20, bg="grey",fg="white",font=("times new roman", 12))
        self.lbl_motdepassbis.place(x=200, y=150)
        self.lbl_txtmotdepassbis=Entry(Creation_frame, bg="white", fg="black", textvariable=self.motdepasseetudrepeat, show="*" ,font=("times new roman",10), width=25)
        self.lbl_txtmotdepassbis.place(x=220, y=175)
        self.lbl_phone = Label(Creation_frame, text="Numero de Telephone : ", width=20, bg="grey",fg="white",font=("times new roman", 12))
        self.lbl_phone.place(x=15, y=200)
        self.lbl_txtphone=Entry(Creation_frame, bg="white", fg="black", textvariable=self.phoneetud,font=("times new roman",10), width=25)
        self.lbl_txtphone.place(x=30, y=225)
        self.lbl_datenaiss=  Label(Creation_frame, text="Date de naissance : ", width=20, bg="grey",fg="white",font=("times new roman", 12))
        self.lbl_datenaiss.place(x=190, y=200)
        self.txtdatenaiss=DateEntry(Creation_frame, textvariable=self.datenaiss, font=("times new roman",10), width=22)
        self.txtdatenaiss.place(x=220, y=225)
        self.lbl_question = Label(Creation_frame, text="Selectionnez une question : ", width=20, bg="grey", fg="white", font=("times new roman",12))
        self.lbl_question.place(x=25,y=250)
        self.txtquestion=ttk.Combobox(Creation_frame,textvariable=self.questetud, font=("times new roman",10),width=25,state="readonly")
        self.txtquestion["values"]=("Dans quel ville es tu né(e)","Où as tu rencontré ta partenaire actuelle","Le prenomm de ta maman")
        #self.txtquestion.current(0)
        self.txtquestion.place(x=30,y=275)
        self.lbl_reponse = Label(Creation_frame, text="Reponse à la question : ", width=20, bg="grey",font=("times new roman",12),fg="white" )
        self.lbl_reponse.place(x=200, y=250)
        self.txtreponse=Entry(Creation_frame, bg="white", fg="black", textvariable=self.reponseetud, font=("times new roman",10), width=25)
        self.txtreponse.place(x=220, y=275)
        self.check=IntVar()
        self.chk = ttk.Checkbutton(Creation_frame, text="J'accepte les termes et les conditions",variable=self.check ,onvalue=1,offvalue=0, width=50)
        self.chk.place(x=30, y=315)
        self.buttonok= Button(Creation_frame, text="Creer le compte", width= 20, font=("algerian",14,"bold"),command=self.creer, foreground="black", background="green", cursor="hand2")
        self.buttonok.place(x=75, y=350)
        self.buttonreset= Button(Creation_frame, text="Reinitialiser ", width= 12, font=("algerian",12,"bold"),command=self.reset, foreground="black", background="red", cursor="hand2")
        self.buttonreset.place(x=25, y=400)
        self.buttonconnect = Button(Creation_frame, text="Connectez vous ", width= 15, font=("algerian",12,"bold"),command="", foreground="black", background="yellow",cursor="hand2")
        self.buttonconnect.place(x=225, y=400)

    def reset (self):
        k=messagebox.askyesno("Reinitialiser","Voulez vous reinitialiser le formulaire ?")
        if k==YES:
            self.nometud.set(str(""))
            self.prenometud.set(str(""))
            self.mailetud.set(str(""))
            self.mailetudreapeat.set(str(""))
            self.motdepasseetud.set(str(""))
            self.motdepasseetudrepeat.set(str(""))
            self.phoneetud.set(str(""))
            self.datenaiss.set(str(""))
            self.questetud.set(str(""))
            self.reponseetud.set(str(""))
            self.check.initialize(value=0)

    def creer(self):
        if(self.nometud.get()=="" or self.prenometud.get()=="" or self.mailetud.get()=="" or self.motdepasseetud.get()=="" or self.phoneetud.get()=="" or self.questetud.get()==self.txtquestion.current(0)):
            messagebox.showerror("Erreur","Veuillez remplir toutes les cases s'il vous plait !")
        elif (self.mailetud.get()!=self.mailetudreapeat.get()):
            messagebox.showerror("Erreur","Verifiez que votre adresse mail correspond s'il vous plait")
        elif (self.motdepasseetud.get()!=self.motdepasseetudrepeat.get()):
            messagebox.showerror("Erreur","Verifiez que votre mot de passe correspond s'il vous plait")
        elif (self.check.get()==0):
            messagebox.showerror("Erreur","Veuillez accepter les termes et conditions en cochant la case s'il vous plait")
        else:
            try:
                con = pymysql.connect(host="localhost",user="root",password="",database="etudiant")
                cur=con.cursor()  #Pour creer un curseur qui sera utilisé pour manipuler la bd
                cur.execute("select * from comptes where email=%s",self.mailetud.get()) #selectionner l'adresse mail dans la table
                row= cur.fetchone()

                if row != None:
                    messagebox.showerror("Erreur","Un compte possédant ce mail existe déja !")
                else:
                    cur.execute("insert into comptes (noms, prenoms, email, password, telephone, date_naissance, question, reponse) values (%s,%s,%s,%s,%s,%s,%s,%s)",
                                
                                (self.nometud.get(), 
                                self.prenometud.get(), 
                                self.mailetud.get(), 
                                self.motdepasseetud.get(), 
                                self.phoneetud.get(), 
                                self.datenaiss.get(), 
                                self.questetud.get(), 
                                self.reponseetud.get())
                    )
                    messagebox.showinfo("Succès", "Votre compte a été crée!")
                con.commit()
                con.close()
            except Exception as ex:
                messagebox.showerror("Erreur",f"Erreur de connexion : {str(ex)}")
        self.reset()
        
           
        





root = Tk()
obj= Formulaire(root)
root.mainloop()
