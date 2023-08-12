from tkinter import *  #interface graphique
from tkinter import messagebox, ttk  #Boites de dialogues et affichages de la BD sur l'interface graphique
import tempfile   #Pour creer des fichiers temporaires
import random  #pour generer les numeros de factures
from time import strftime   #Pour l'heure
from PIL import ImageTk, Image  #Pour les images
import os  #Pour nous permettre de gérer l'impression

class SuperMarche:        #Cette classe défini  le programme principal 
    def __init__(self, root):  #Cette fonction défini  les caracteristiques de la fenetre et initialise la class supermarché
        self.root=root
        self.root.title('SuperMarché')   #Pour le titre de la fenêtre
        self.root.geometry("1366x768+0+0")  #taille de la fenêtre
        self.root.resizable(False,False)  #On ne peut pas aggrandir

        title = Label(self.root, font=("Arial Black",30,"bold"),bg="Blue", fg="white", relief=SUNKEN, text="SUPERMARCHE JIDANEL")
        title.place(x=0,y=0, width=1366)

       
        #Affichage de l'heure
        Labelheure= Label(self.root, font=("Arial Black", 12, "bold"), bg="blue", fg="white", text="HH:MM:SS")
        Labelheure.place(x=0, y=10, width= 250, height=30)

        #Fonction pour l'heure
        def heure():
            h=strftime("%H:%M:%S")
            Labelheure.config(text=h)  #On remplace le texte de label heure par le contenu de la variable h qui contient l'heure fourni par sfrtime
            Labelheure.after(1000,heure)  #Pour faire boucler et afficher l'heure en temps reel

         

        heure()   #On appelle la fonction heure dans le programme

        #Les variables du programmes####

        self.c_nom= StringVar()   #Pour recuperer le nom du client
        self.c_phone= StringVar()   #Pour recuperer le contact du client
        self.c_fact= StringVar()   #Pour recuperer le numero facture du client
        z=random.randint(1000,9999)  #on utilise rand qui va choisir le numero de facture entre 10000 et 9999
        self.c_fact.set(z)   #Au numero de facture on associe z
        self.c_email= StringVar()  #Pour recuperer l'email du client
        self.rech_fact=StringVar()  #Pour rechercher la facture du client
        self.produit=StringVar()  #Pour recuperer le nom du produit
        self.prix=IntVar()  #Pour recuperer le prix du produit
        self.qte=IntVar()    ##Pour recuperer la quantité du produit acheté
        self.totalbrut=StringVar()   #Pour recuperer le total sans taxe
        self.taxe=StringVar()   #Pour recuperer la taxe
        self.totalnet=StringVar()  #Pour recuperer le total net
        self.l=[]
        self.selection=["Selectionner..."]
        self.list_categorie=["Selectionner...","Habillement","Alimentation","Ordinateurs"] #Liste des categories

        self.list_souscateghabillement=["Selectionner...","Pantalons","Chemises","T-shirt"]
        self.list_pantalons=["Selectionner...","levis","sebago","calvin klein","global"]
        '''self.prix_levis=5000
        self.prix_sebago=4000
        self.prix_calvink=5000
        self.prix_global=3500'''
        self.list_chemises=["Selectionner...","givenchy","armany","vera wang","calvin klein"]
        self.list_tshirt=["Selectionner...","D&G","Calvin Klein","Lacoste"]

        self.list_souscategalimentation=["Selectionner...","Farine","Lait","Boisson"]
        self.list_farine=["Selectionner...","Pain","Beignets","Gateaux"]
        self.list_lait=["Selectionner...","Nido","Alma","Nursy","Guiguoz"]
        self.list_boisson=["Selectionner...","jus","whisky","beer"]

        self.list_souscategordi=["Selectionner...","Acer","Hp","Dell"]
        self.list_acer=["Selectionner...","P4","core i4","notebook"]
        self.list_hp=["Selectionner...","ipad","tablette","core i3","pentium M"]
        self.list_dell=["Selectionner...","core i9","core i7","notebook"]





        #On crée une frame mere qui va porter les differentes catégories
        Main_frame= Frame(self.root,bd=2,relief=GROOVE,bg="white")
        Main_frame.place(x=10,y=65,width=1336,height=700)

        #Categorie client
        client_frame= LabelFrame(Main_frame,text="Clients", font=("times new roman",12),bg="white")
        client_frame.place(x=5,y=3,width=280,height=115)

        #Informations contenues dans la categorie client
        self.lblcontact = Label(client_frame, text="Contact :", font=("times new roman",12,"bold"),bg="white")
        self.lblcontact.grid(row=0,column=0,sticky="w",padx=5,pady=2)
        self.txtcontact=ttk.Entry(client_frame,font=("times new roman",12),textvariable=self.c_phone)
        self.txtcontact.grid(row=0,column=1,padx=5,pady=2)

        self.lblnomclient = Label(client_frame, text="Nom Client :", font=("times new roman",12,"bold"),bg="white")
        self.lblnomclient.grid(row=1,column=0,sticky="w",padx=5,pady=2)
        self.txtnomclient=ttk.Entry(client_frame,font=("times new roman",12),textvariable=self.c_nom)
        self.txtnomclient.grid(row=1,column=1,padx=5,pady=2)


        self.lblemail = Label(client_frame, text="E-mail :", font=("times new roman",12,"bold"),bg="white")
        self.lblemail.grid(row=2,column=0,sticky="w",padx=5,pady=2)
        self.txtemail=ttk.Entry(client_frame,font=("times new roman",12),textvariable=self.c_email)
        self.txtemail.grid(row=2,column=1,padx=5,pady=2)

        #frame des produits constitué d'une categorie, sous categorie et nom du produit
        produits_frame=LabelFrame(Main_frame,bg="white",text="Produits",font=("times new romain",12))
        produits_frame.place(x=305,y=3,width=380,height=115)

        self.lblcateg=Label(produits_frame,text="Catégorie :", font=("times new roman",12,"bold"),bg="white")
        self.lblcateg.grid(sticky="w", row=0,column=0,padx=5,pady=2)
        self.txtcateg=ttk.Combobox(produits_frame,font=("times new roman",10),width=13, state="readonly",values=self.list_categorie)  #state: etat ie lecture ou ecriture
        self.txtcateg.grid(row=0,column=1,sticky="w",padx=5,pady=2)
        self.txtcateg.current(0)   #ce sera toujours le premier élément sélectionné par defaut
        self.txtcateg.bind("<<ComboboxSelected>>",self.fonct_categorie)  #bind permet de faire appel à une fonction dans un formulaire par exemple

        self.lblsouscateg=Label(produits_frame,text="Sous catégorie :", font=("times new roman",12,"bold"),bg="white")
        self.lblsouscateg.grid(sticky="w", row=1,column=0,padx=5,pady=2)
        self.txtsouscateg=ttk.Combobox(produits_frame,font=("times new roman",10),width=13, state="readonly",values=[""])  #state: etat ie lecture ou ecriture
        self.txtsouscateg.grid(row=1,column=1,sticky="w",padx=5,pady=2)
        self.txtsouscateg.current(0)   #ce sera toujours le premier élément sélectionné par defaut
        self.txtsouscateg.bind("<<ComboboxSelected>>",self.fonct_souscateg)   #bind permet de faire appel à une fonction dans un formulaire par exemple

        self.lblnomprod=Label(produits_frame,text="Nom du Produit :", font=("times new roman",12,"bold"),bg="white")
        self.lblnomprod.grid(sticky="w", row=2,column=0,padx=5,pady=2)
        self.txtnomprod=ttk.Combobox(produits_frame,font=("times new roman",10),width=13, state="readonly",textvariable=self.produit)  #state: etat ie lecture ou ecriture
        self.txtnomprod.grid(row=2,column=1,sticky="w",padx=5,pady=2)

        self.lblprix=Label(produits_frame,text="Prix :", font=("times new roman",12,"bold"),bg="white")
        self.lblprix.grid(sticky="w", row=0,column=2,padx=5,pady=2)
        self.txtprix=ttk.Entry(produits_frame,font=("times new roman",12),textvariable=self.prix, width=8)
        self.txtprix.grid(row=0,column=3,padx=5,pady=2)

        self.lblqte=Label(produits_frame,text="Qté :", font=("times new roman",13,"bold"),bg="white")
        self.lblqte.grid(sticky="w", row=1,column=2,padx=5,pady=2)
        self.txtqte=ttk.Entry(produits_frame,font=("times new roman",12),textvariable=self.qte, width=8)
        self.txtqte.grid(row=1,column=3,padx=5,pady=2)
        #recherche facture
        recherche_frame=LabelFrame(Main_frame, bg="white", font=("Times new roman",15), bd=0)
        recherche_frame.place(x=700,y=14, width=350,height=70)
        self.lblrecherche=Label(recherche_frame,text="N° Facture :",font=("times new roman",13,"bold"),bg="white")
        self.lblrecherche.grid(row=0,column=0,sticky="w",padx=5,pady=2)
        self.txtrecherche = ttk.Entry(recherche_frame,textvariable=self.rech_fact,font=("times new roman",13),width=15)
        self.txtrecherche.grid(row=0,column=1,sticky="w",padx=5,pady=3)
        self.buttonrecherch = Button(recherche_frame,command=self.rechercher, font=("times new roman",10,"bold"),text="Rechercher", bg="yellow",fg="black",cursor="hand2")
        self.buttonrecherch.grid(row=0,column=2,sticky="w",padx=5,pady=3)

        #Espace facture
        Facture_frame=LabelFrame(Main_frame,text="Facture Client",bg="white",font=("times new roman",13,"bold"))
        Facture_frame.place(x=700,y=50,width=630,height=450)
        scroll_y=Scrollbar(Facture_frame,orient=VERTICAL)       #barre de defilemment verticale
        self.txtarea=Text(Facture_frame,font=("times new roman",12,"bold"),bg="white",fg="blue",yscrollcommand=scroll_y.set)  #zone de texte facture client
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        #Espace Commande
        bas_frame=LabelFrame(Main_frame,bd=2,bg="white",text="Commandes",font=("times new roman",12))
        bas_frame.place(x=0,y=500,width=1330,height=160)

        self.lbl_totalbrut=Label(bas_frame,text="Total Brut :",font=("times new roman",15,"bold"),fg="black",bg="white")
        self.lbl_totalbrut.grid(row=0,column=0,sticky=W, padx=5,pady=2)
        self.txt_totalbrut=ttk.Entry(bas_frame,textvariable=self.totalbrut,font=("times nes roman",15),width=12, state="readonly")
        self.txt_totalbrut.grid(row=0,column=1,sticky=W,padx=5,pady=3)

        self.lbl_taxe=Label(bas_frame,text="Taxe :",font=("times new roman",15,"bold"),fg="black",bg="white")
        self.lbl_taxe.grid(row=1,column=0,sticky=W, padx=5,pady=2)
        self.txt_taxe=ttk.Entry(bas_frame,textvariable=self.taxe,font=("times new roman",15),width=12, state="readonly",background="white",foreground="black")
        self.txt_taxe.grid(row=1,column=1,sticky=W,padx=5,pady=3)


        self.lbl_totalnet=Label(bas_frame,text="Total Net :",font=("times new roman",15,"bold"),fg="black",bg="white")
        self.lbl_totalnet.grid(row=2,column=0,sticky=W, padx=5,pady=2)
        self.txt_totalnet=ttk.Entry(bas_frame,textvariable=self.totalnet,font=("times nes roman",15),width=12, state="readonly")
        self.txt_totalnet.grid(row=2,column=1,sticky=W,padx=5,pady=3)

        #image
        self.logo=ImageTk.PhotoImage(Image.open("C:/Users/Jidanel/AppData/Local/Programs/Python/Python311/Projects/Supermarché/images/supermarche.jpg"))
        self.lblimg=Label(image=self.logo)
        self.lblimg.place(x=40,y=200)
        #boutons
        
        self.ajoutpanier=Button(bas_frame,command=self.ajouter,text="Ajouter panier",height=3,fg="black",font=("times new roman",11,"bold"),bg="yellow",width=17,cursor="hand2")
        self.ajoutpanier.grid(row=1,column=2,padx=5,pady=2)

        self.generer=Button(bas_frame,command=self.genererfacture,text="Generer Facture",height=3,fg="black",font=("times new roman",11,"bold"),bg="yellow",width=17,cursor="hand2")
        self.generer.grid(row=1,column=3,padx=5,pady=2)

        self.sauvegarde=Button(bas_frame,command=self.sauvegarder,text="Enregistrer facture",height=3,fg="black",font=("times new roman",11,"bold"),bg="yellow",width=15,cursor="hand2")
        self.sauvegarde.grid(row=1,column=4,padx=5,pady=2)

        self.imprimer=Button(bas_frame,command=self.imprimer,text="Imprimer",height=3,fg="black",font=("times new roman",11,"bold"),bg="yellow",width=17,cursor="hand2")
        self.imprimer.grid(row=1,column=5,padx=5,pady=2)

        self.reset=Button(bas_frame,command=self.reinitialiser,text="Reinitialiser",height=3,fg="black",font=("times new roman",11,"bold"),bg="yellow",width=17,cursor="hand2")
        self.reset.grid(row=1,column=6,padx=5,pady=2)

        self.quit=Button(bas_frame,command=self.quitter,text="Quitter",height=3,fg="black",font=("times new roman",11,"bold"),bg="yellow",width=17,cursor="hand2")
        self.quit.grid(row=1,column=7,padx=5,pady=2)

        self.bienvenue()


        #Fonctions des commandes
    def bienvenue(self):
        self.txtarea.delete(1.0, END)   #A l'appel de cette fonction on supprime le contenu
        self.txtarea.insert(END, "\t\t Bienvenue au Supermarché Jidanel")
        self.txtarea.insert(END, f"\n Numero Facture : {self.c_fact.get()}") #On va 2 fois à la ligne puis on insère le n° de facture
       # self.txtarea.insert(END, f"\n Nom Client : {self.c_nom.get()}") #On va 2 fois à la ligne puis on insère lenom du client
        #self.txtarea.insert(END, f"\n Numero Client : {self.c_phone.get()}") #On va 2 fois à la ligne puis on insère le telephone du client
        self.txtarea.insert(END, "\n***************************************************************************")
        self.txtarea.insert(END, f"\n\n\tArticles\t\tQuantité \t\tPrix") 
        self.txtarea.insert(END, "\n\n***************************************************************************")
    def ajouter(self):
        self.n=self.prix.get()   #range le prix dans n
        self.pht = self.qte.get()*self.n        #total brut = qte * pris
        self.l.append(self.pht)  #on ajoute le resultat à une liste L
        if self.produit.get()=="" or self.produit.get()=="Selectionner..." or self.prix.get()==0 or self.qte.get()==0 :  #si on a choisi aucun produit
            messagebox.showerror("Erreur","Données incorrectes, reverifiez les informations saisies")
        else:
            self.txtarea.insert(END, f"\n\t{self.produit.get()}\t\t{self.qte.get()}\t\t{self.pht}\n")   
            #End pour ne pas aller à la ligne, f"\n pour completer à la suite, \t : 1e tabulation
            self.totalbrut.set(str("cfa %.2f"%(sum(self.l))))
            #2f : 2 chiffres après la virgule
            self.taxe.set(("%.2f"%((0.01925))))
            self.k= 1.01925
            self.totalnet.set(str("cfa %.2f"%((sum(self.l)*(self.k)))))
       

    def genererfacture(self):
        if self.produit.get()=="" or self.produit.get()=="Selectionner..." or self.prix.get()==0 or self.qte.get()==0 :  #si on a choisi aucun produit
            messagebox.showerror("Erreur","Données incorrectes, reverifiez les informations saisies")
        else:
            text = self.txtarea.get(1.0,END)
            self.txtarea.delete(1.0, END)
            text= self.txtarea.insert(END, text)  #On reproduit le text dans la facture
            self.txtarea.insert(END, "\n\n")
            self.txtarea.insert(END, "\n***************************************************************************")
            self.txtarea.insert(END, f"\n\n Nom du client : {self.c_nom.get()}")
            self.txtarea.insert(END, f"\n Telephone : {self.c_phone.get()}")
            self.txtarea.insert(END, f"\n Total Brute : \t\t {self.totalbrut.get()}")
            self.txtarea.insert(END, f"\n Taxe : \t\t {self.taxe.get()}")
            self.txtarea.insert(END, f"\n Total à Payer : \t\t {self.totalnet.get()}")
            self.txtarea.insert(END, f"\n Merci d'être passé chez nous !!")

    def sauvegarder(self):
        op=messagebox.askyesno("Sauvegarder","Voulez vous vraiment sauvegarder cette facture?")
        if op==True:
            self.donneefacture=self.txtarea.get(1.0,END)
            f1=open("C:/Users/Jidanel/AppData/Local/Programs/Python/Python311/Projects/Supermarché/factures/"+str(self.c_fact.get())+".txt","w") #On ouvre le dossier image et on enregistre un fichier txt en mode ecriture avec comme nom le numero de la facture
            f1.write(self.donneefacture)
            messagebox.showinfo("Sauvegarde",f"La facture n° {self.c_fact.get()} a été enregistrée avec succès")
            f1.close()

    def imprimer(self):
        fichier = tempfile.mktemp(".txt") #on cree un fichier temporaire dans lequel les données à imprimer seront écrites 
        open(fichier,"w").write(self.txtarea.get(1.0,END))  #on ouvre le fichier en mode ecriture  puis on y copie le contenu du text area
        os.startfile(fichier,"print") #on imprime

    def rechercher(self):
        trouver= "non"
        for i in os.listdir("C:/Users/Jidanel/AppData/Local/Programs/Python/Python311/Projects/Supermarché/factures/"):
            if i.split(".")[0]==self.rech_fact.get(): #si en regardant de la position 0 du nom du fichier jusqu'au point, la faleur est égale au numero de la facture inséré
                f1=open(f"C:/Users/Jidanel/AppData/Local/Programs/Python/Python311/Projects/Supermarché/factures/{i}","r") #on ouvre le fichier trouvé i en mode lecture
                self.txtarea.delete(1.0, END) #on supprime le contenu de txt area
                for d in f1:
                    self.txtarea.insert(END,d)  #on insere le contenu dans txtarea
                    f1.close
                    trouver="oui"
        if trouver=="non":
            messagebox.showerror("erreur", f"La facture n° {self.rech_fact.get()} n'existe pas !")

    def reinitialiser(self):
            self.c_nom.set("")
            self.c_phone.set("")
            self.c_email.set("")
            self.qte.set(0)
            self.prix.set(0)
            self.rech_fact.set("")
            self.bienvenue()
            self.txtcateg.current(0)
            self.txtsouscateg.current(0)
            self.txtnomprod.current(0)
            self.totalbrut.set("")
            self.taxe.set("")
            self.totalnet.set("")
            self.l=[0]
    
    def quitter(self):
        k = messagebox.askyesno("Quitter","Voulez vous quitter la fenêtre?")
        if k==True:
            self.root.destroy()


                    
        #Fonctions de selection des choix des differentes sous categories
    def fonct_categorie(self,event=""):
        if self.txtcateg.get()=="Selectionner...":
            self.txtsouscateg.config(values=self.selection)
            self.txtnomprod.config(values=self.selection)
            self.txtsouscateg.current(0)
            self.txtnomprod.current(0)

        if self.txtcateg.get()=="Habillement":
            self.txtsouscateg.config(values=self.list_souscateghabillement)
            self.txtsouscateg.current(0)

        if self.txtcateg.get()=="Alimentation":
            self.txtsouscateg.config(values=self.list_souscategalimentation)
            self.txtsouscateg.current(0)

        
        if self.txtcateg.get()=="Ordinateurs":
            self.txtsouscateg.config(values=self.list_souscategordi)
            self.txtsouscateg.current(0)
        
    

    def fonct_souscateg(self,event=""):
        if self.txtsouscateg.get()=="Selectionner...":
            self.txtnomprod.config(values=self.selection)
            self.txtnomprod.current(0)

        #Vetements
        if self.txtsouscateg.get()=="Pantalons":      #Si la categorie choisie est pantalon
            self.txtnomprod.config(values=self.list_pantalons) #on affecte au formmulaire les éléments de la sous categorie pantalon
            self.txtnomprod.current(0)     #on affecte la 1ere valeur comme valeur par défaut

        if self.txtsouscateg.get()=="Chemises":      #Si la categorie choisie est chemises
            self.txtnomprod.config(values=self.list_chemises) #on affecte au formmulaire les éléments de la sous categorie chemises
            self.txtnomprod.current(0)     #on affecte la 1ere valeur comme valeur par défaut
        

        if self.txtsouscateg.get()=="T-Shirt":      #Si la categorie choisie est tshirt
            self.txtnomprod.config(values=self.list_tshirt) #on affecte au formmulaire les éléments de la sous categorie pantalon
            self.txtnomprod.current(0)     #on affecte la 1ere valeur comme valeur par défaut
        
        #alimentation
        if self.txtsouscateg.get()=="Farine":      #Si la categorie choisie est farine
            self.txtnomprod.config(values=self.list_farine) #on affecte au formmulaire les éléments de la sous categorie farine
            self.txtnomprod.current(0)     #on affecte la 1ere valeur comme valeur par défaut

        if self.txtsouscateg.get()=="Lait":      #Si la categorie choisie est farine
            self.txtnomprod.config(values=self.list_lait) #on affecte au formmulaire les éléments de la sous categorie lait
            self.txtnomprod.current(0)     #on affecte la 1ere valeur comme valeur par défaut

        if self.txtsouscateg.get()=="Boisson":      #Si la categorie choisie est farine
            self.txtnomprod.config(values=self.list_boisson) #on affecte au formmulaire les éléments de la sous categorie boisson
            self.txtnomprod.current(0)     #on affecte la 1ere valeur comme valeur par défaut

        #ordinateur
        if self.txtsouscateg.get()=="Acer":      #Si la categorie choisie est farine
            self.txtnomprod.config(values=self.list_acer) #on affecte au formmulaire les éléments de la sous categorie acer
            self.txtnomprod.current(0)     #on affecte la 1ere valeur comme valeur par défaut
        
        if self.txtsouscateg.get()=="Dell":      #Si la categorie choisie est farine
            self.txtnomprod.config(values=self.list_dell) #on affecte au formmulaire les éléments de la sous categorie dell
            self.txtnomprod.current(0)     #on affecte la 1ere valeur comme valeur par défaut

        if self.txtsouscateg.get()=="Hp":      #Si la categorie choisie est farine
            self.txtnomprod.config(values=self.list_hp) #on affecte au formmulaire les éléments de la sous categorie hp
            self.txtnomprod.current(0)     #on affecte la 1ere valeur comme valeur par défaut

        










if __name__== "__main__":      #Cette portion de code est defini pour activer la fenetre et la laisser touner
    root = Tk()
    obj= SuperMarche(root)
    root.mainloop()
