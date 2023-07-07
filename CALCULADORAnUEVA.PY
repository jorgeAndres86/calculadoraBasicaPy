from tkinter import *

simbol ="0"
ante = 0
sig =""
root= Tk()
root.title("calculadora")
root.resizable(0,0)
root.geometry("295x310")

numeroPantalla= StringVar()
pantalla = Entry(root,text=numeroPantalla,width =22,bg= "black",fg="white",borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0,column=0,  padx=3,pady=2,columnspan=4)
sumador =0
suma2=1
contador =0
anter =""
anteTemporal=""
pant= ""
presionado = False

def enviaBoton(valor):
    global simbol
    global ante
    global presionado
    global contador


    
    
    anterior = pantalla.get()
    pantalla.delete(0,END)
    
    if valor == "←":
       valor =""
       anterior = anterior[:-1] 


    
    presionado = True
    contador =0
    
    if simbol == "":
        ante = anterior
        pantalla.insert(0,str(valor))
        simbol ="0"
        

    else:
        
        numeroPantalla.set(str(anterior) + str(valor))
    



def calcular(simbolo):
    global simbol
    global ante
    global sig
    global contador
    global anter
    global presionado
    global anteTemporal
    global pant
    
    if pantalla.get()=="":
        return
        

    contador = contador + 1
    if contador ==1:
        pant = pantalla.get()
        if presionado == True:
            anteTemporal = pant
    
    if contador == 2:
        pant = anteTemporal
    if contador >=2:
        ante = pantalla.get()
    

    if sig == "+":
        numeroPantalla.set(float(ante) + float(pant))
    

        

    if sig == "-":
        numeroPantalla.set(float(ante) - float(pant))

    if sig== "x":
        numeroPantalla.set(float(ante) * float(pant))
    
    if sig == "/":
        try:
            numeroPantalla.set(float(ante) / float(pant))
        except ZeroDivisionError:
            numeroPantalla.set("Error")
            
    if sig== "√":
        numeroPantalla.set(float(ante) ** (1/ float(pant)))
        
    if sig== "x^":
        numeroPantalla.set(float(ante) ** (float(pant)))
        
    
    
    

    sig = simbolo
    simbol =""
    presionado = False


    if simbolo == "=":
        ante =""
        sig ="" 
        contador =0




def limpiar():   
    global simbol
    global ante
    global sig
    global contador
    pantalla.delete(0,END)
    ante=""
    sig=""
    simbol=""
    contador=0



for i in range(1,10):
    
    
    boton_1 = Button(root,text=str(i), width=9,height=3,bg="white",fg="red",borderwidth=0,
                     cursor="hand2",command=lambda n=i: enviaBoton(n)).grid(row=suma2,column=sumador,padx=0,pady=1)
    sumador +=1
    if sumador == 3:
        sumador = 0
        suma2 +=1

boton_0 = Button(root,text="0", width=9,height=3,bg="white",fg="black",borderwidth=0,
                cursor="hand2",command=lambda: enviaBoton("0")).grid(row=4,column=1,padx=0,pady=1)

boton_Igual = Button(root,text="=", width=9,height=3,bg="red",fg="white",borderwidth=0,
                cursor="hand2",command=lambda: calcular("=")).grid(row=4,column=0,padx=0,pady=1)

boton_Punto = Button(root,text=".", width=9,height=3,bg="green",fg="white",borderwidth=0,
                cursor="hand2",command=lambda: enviaBoton(".")).grid(row=4,column=2,padx=0,pady=1)

boton_Mas = Button(root,text="+", width=9,height=3,bg="blue",fg="white",borderwidth=0,
                cursor="hand2",command=lambda: calcular("+")).grid(row=1,column=3,padx=0,pady=1)

boton_Menos = Button(root,text="-", width=9,height=3,bg="deep sky blue",fg="white",borderwidth=0,
                cursor="hand2",command=lambda: calcular("-")).grid(row=2,column=3,padx=0,pady=1)

boton_por = Button(root,text="x", width=9,height=3,bg="deep sky blue",fg="white",borderwidth=0,
                cursor="hand2",command=lambda: calcular("x")).grid(row=3,column=3,padx=0,pady=1)

boton_div = Button(root,text="/", width=9,height=3,bg="deep sky blue",fg="white",borderwidth=0,
                cursor="hand2",command=lambda: calcular("/")).grid(row=4,column=3,padx=0,pady=1)

boton_despejar = Button(root,text="C",width=9,height=3,bg="red",fg="white",borderwidth=0,
                cursor="hand2",command=lambda: limpiar()).grid(row=5,column=0,  padx=0,pady=1)

boton_borrar = Button(root,text="←",width=9,height=3,bg="red",fg="white",borderwidth=0,
                cursor="hand2",command=lambda: enviaBoton("←")).grid(row=5,column=1,  padx=0,pady=1)

boton_raiz = Button(root,text="√", width=9,height=3,bg="deep sky blue",fg="white",borderwidth=0,
                cursor="hand2",command=lambda: calcular("√")).grid(row=5,column=2,padx=0,pady=1)


boton_potencia = Button(root,text="x^", width=9,height=3,bg="deep sky blue",fg="white",borderwidth=0,
                cursor="hand2",command=lambda: calcular("x^")).grid(row=5,column=3,padx=0,pady=1)

root.mainloop()

    
