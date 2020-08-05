from tkinter import*
from tkinter import messagebox
import random
from tkinter import simpledialog


listavidas=[9]
lista=[]
class carta:
    def __init__(self):
        self.valor=0
        self.posicion=0
        self.oculto=True
        self.foto=PhotoImage(file="fondo.png")
        self.puntos=0
               
class memorama:
    def __init__(self):
        self.ventana=Tk()
        self.ventana.title("WasteSorter")
        self.ventana.geometry("900x700")
        self.ventana.iconbitmap("Imagen1.ico")
        self.ventana.config(bg="gray12")
        self.ventana.config(cursor="pirate")
        self.botones=[]
        self.cartas=[]
        self.temporal=carta()
        self.a=0
        self.par=0
        self.listo=True
        self.fondo=PhotoImage(file="fondo.png")
        self.creartablero()
        self.revolver()
        self.ventana.mainloop()
        self.nombre = ""
        
    def creartablero(self):
        i=0
        contador=0
        global fondo2
        fondo2=PhotoImage(file="fondo2.png")
        fondo=Label(self.ventana, image=fondo2).place(x=0,y=0)
        global nombre
        nombre = simpledialog.askstring("jugador","escribe el nombre del jugador")
        vidas=Label(self.ventana, text="Vidas",font=("Times New Roman",20)).place(x=825,y=10)
        vidas=Label(self.ventana, text=sum(listavidas),font=("Times New Roman",20)).place(x=850,y=45)
        puntos=Label(self.ventana, text="Puntos",font=("Times New Roman",20)).place(x=725,y=10)
        texto1=Label(self.ventana, text="Debes juntar el residuo con su respectiva caneca.",font=("Times New Roman",20)).place(x=130 , y=10)
        texto2=Label(self.ventana, text="Acuerdate de utilizar lo aprendido.",font=("Times New Roman",20)).place(x=210,y=45)
        texto3=Label(self.ventana, text="Aporta tu granito de arena, el mundo te lo agradece",font=("Times New Roman",20)).place(x=120,y=80)
        puntos=Label(self.ventana, text=sum(lista),font=("Times New Roman",20)).place(x=750,y=45)
        while i<4:
            j=0
            while j<4:
                btn=Button(self.ventana,command=lambda a=contador:self.revisar(a), height=130,width=130,image=self.fondo)
                btn.place(x=(j+1)*130,y=(i+1)*130)
                self.botones.append(btn)
                j+=1
                contador+=1
            i+=1


    def revolver(self):
        i=1
        h=0
        while(i<9):
            carta1=carta()
            carta1.valor=i
            carta1.foto=PhotoImage(file=str(i)+".png")
            carta2=carta()
            h=i*10
            carta2.valor=i
            carta2.foto=PhotoImage(file=str(h)+".png")
            self.cartas.append(carta1)
            self.cartas.append(carta2)
            i+=1
        cartastemporal=[]
        while len(self.cartas)>0:
            posicion=random.randrange(0,len(self.cartas))
            cartastemporal.append(self.cartas.pop(posicion))
        self.cartas=cartastemporal

    def revisar(self,a):
        if self.listo==True and self.cartas[a].oculto==True:
            self.botones[a].config(image=self.cartas[a].foto)
            if self.par==0:
                self.temporal=self.cartas[a]
                self.cartas[a].oculto=False
                self.temporal.posicion=a
                self.par=1
                
            elif self.par==1:
                self.par=0
                if self.temporal.valor== self.cartas[a].valor:
                    self.cartas[a].oculto=False
                    bandera=True
                    self.puntos=10
                    lista.append(self.puntos)
                    puntos=Label(self.ventana, text=sum(lista),font=("Times New Roman",20)).place(x=750,y=45)
                    for elemento in self.cartas:
                        if elemento.oculto==True:
                            bandera=False
                            break
                    if bandera ==True:
                        messagebox.showinfo(message="Juego terminado!!"+"\n"+"Quizas no podamos cambiar el mundo, pero si podemos cuidar el pedacito que nos toca"+"\n"+nombre+" "+"tu puntuacion es de"+" "+str(sum(lista)), title="Waste Sorter")
                        records=open("records.txt","a")
                        records.write("\n"+nombre+"="+str(sum(lista)))
                        records.close()

                        records=open("records.txt","r")
                        records=records.read()
                        print(records)
                else:
                    if sum(listavidas)==9:
                        self.puntos=10
                        lista.append(self.puntos)
                    self.a=a
                    self.listo=False
                    self.ventana.after(500,self.tapar)
                    self.puntos=-10
                    lista.append(self.puntos)
                    puntos=Label(self.ventana, text=sum(lista),font=("Times New Roman",20)).place(x=750,y=45)
                    self.vidas=-1
                    listavidas.append(self.vidas)
                    vidas=Label(self.ventana, text=sum(listavidas),font=("Times New Roman",20)).place(x=850,y=45)
                    if sum(listavidas)>7:
                        self.puntos=10
                        lista.append(self.puntos)
                        
                    elif sum(listavidas)<=0:
                        messagebox.showinfo(message="Perdiste, intentalo de nuevo!!"+"\n"+nombre+" "+"tu puntuacion es de"+" "+str(sum(lista)), title="Waste Sorter")
                        self.ventana.destroy()
                        recordsmalos=open("recordsmalos.txt","a")
                        recordsmalos.write("\n"+nombre+"="+str(sum(lista)))
                        recordsmalos.close()

                        recordsmalos=open("recordsmalos.txt","r")
                        recordsmalos=recordsmalos.read()
                        print(recordsmalos)
                       
                    
    def tapar(self):
        self.cartas[self.temporal.posicion].oculto=True
        self.botones[self.temporal.posicion].config(image=self.fondo)
        self.botones[self.a].config(image=self.fondo)
        self.listo=True



obj=memorama()



