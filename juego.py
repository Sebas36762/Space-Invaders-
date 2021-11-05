from tkinter import *
from os import path, write
import glob
import time                             
from time import sleep
import vlc
from threading import Thread, Timer
import random
FlagA= True
Flag = True
Fuente_global=("Comic Sans MS",10)
Nave_life=50
Boss_life=30
Score = 0
sound_player = vlc.MediaPlayer()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
VentanaPrincipal = Tk() #Se crea la ventana
VentanaPrincipal.title("SpaceInvaders")#Nombre de la ventana
VentanaPrincipal.minsize(598,799)#Margenes de la ventana
VentanaPrincipal.resizable(width=NO, height=NO)# Definimos si la ventana cambia de tamaño
C_principal = Canvas(VentanaPrincipal, width=600, height=800, bg='white')
C_principal.place(x=-2,y=0) 
reproductor=vlc.MediaPlayer()

def cargarMP3(nombre):# Cargar la musica en formato Mp3
    return path.join('Música', nombre)#Se carga la ruta donde esta la música

def reproducir_fx(archivoMP3):#Reproductor de música
    vlc.MediaPlayer(archivoMP3).play()

def reproducir_cancion(archivoMP3):
    global reproductor
    reproductor = vlc.MediaPlayer(archivoMP3)
    reproductor.audio_set_volume(30)
    reproductor.play() 
   
reproductor.music = cargarMP3('Mega Man X OST - T25 Sigma Stage 2.mp3')

music = reproducir_cancion(reproductor.music)
                                                                  
def cargar_img(nombre):#Se busca la ruta de la imagen de los fondos
    ruta  = path.join('IMG', nombre)
    img = PhotoImage(file=ruta)
    return img
def cargar_img2(nombre): #se busca la ruta la imagen de las balas
    ruta  = path.join('Animacion', nombre)
    img = PhotoImage(file=ruta)
    return img

C_principal.fondo = cargar_img('FondoInicial.png')#Se carga la imagen
Fondo1 = C_principal.create_image(0,0,anchor=NW, image=C_principal.fondo)#Se coloca el fondo

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Highscore():
    HighscoreV= Toplevel()
    HighscoreV.title("Pantalla 2")
    HighscoreV.minsize(600,400)
    HighscoreV.resizable(width=NO, height=NO)
    Canv_Hig = Canvas(HighscoreV, width=600, height=800, bg='#252235')
    Canv_Hig.place(x=-2,y=0)
    Canv_Hig.fondo = cargar_img('FondoEditable Scores.png')
    FondoHigh = Canv_Hig.create_image(0,0,anchor=NW, image=Canv_Hig.fondo)
    def Cerrar_about():#Se cierra la ventana de informacion 
        VentanaPrincipal.deiconify()
        HighscoreV.destroy()

    btn_cerrar = Button(HighscoreV, text='Cerrar',font=("Comic Sans MS",10),command=Cerrar_about, width=12, height=1,bg="#1e0238",fg="white")#Boton que activa la funcion cerrar
    btn_cerrar.place(x=430, y=320)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def About_Btn(): #Se crea la ventana para la informacion 
    VentanaPrincipal.withdraw()# se cierra la ventana principal
    VentanaInfo = Toplevel()
    VentanaInfo.title("About")
    VentanaInfo.minsize(600,500)
    VentanaInfo.resizable(width=NO, height=NO)
    about = """     Costa Rica

     Instituto Tecnologico de Costa Rica, Ingenieria en Computadores

     Taller de programacion, 2021, Grupo 02

     Milton Villegas Lemus
    
     Version 1.0

     Autor: Sebastián Chaves Ruiz

     Autores de modulos utilizados: José Fernando Morales Vargas/Ignacio Mora

     Instrucciones:

        Arriba: Flecha Arriba 

        Abajo: Flecha bajada

        Izquierda: Flecha Izquierda

        Derecho: Flecha Derecha

        Disparar: Espacio

    """
    C_about = Canvas(VentanaInfo, width=600, height=500, bg='white')
    C_about.place(x=-2,y=0)

    C_about.fondo = cargar_img('FondoAbout.png')
    Fondo2 = C_about.create_image(0,0,anchor=NW, image=C_about.fondo)

    Text= C_about.create_text(0,10,text = about, font=('Comic Sans MS', 10),anchor=NW,fill="#ffffff")
    
    def Cerrar_about():#Se cierra la ventana de informacion 
        VentanaPrincipal.deiconify()
        VentanaInfo.destroy()

    btn_cerrar = Button(VentanaInfo, text='Cerrar',font=("Comic Sans MS",10),command=Cerrar_about, width=12, height=1,bg="#1e0238",fg="white")#Boton que activa la funcion cerrar
    btn_cerrar.place(x=430, y=420)
  
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Jugar_Btn():#Se crea la ventana de seleccion de niveles

    VentanaPrincipal.withdraw()
    VentanaJugar= Toplevel()
    VentanaJugar.title("Selector de Niveles")
    VentanaJugar.minsize(600,800)
    VentanaJugar.resizable(width=NO, height=NO)

    C_Juego = Canvas(VentanaJugar, width=600, height=800, bg='#252235')
    C_Juego.place(x=-2,y=0)

    C_Juego.fondo = cargar_img('FondoSelec.png')
    Fondo3 = C_Juego.create_image(0,0,anchor=NW, image=C_Juego.fondo)
    
    E_Nombre = Entry(VentanaJugar,font=Fuente_global)
    E_Nombre.place(x=215,y=265)
    
    
    def GuardarN():
        nonlocal E_Nombre
        nombre_usuario = E_Nombre.get()
        if (nombre_usuario!=""):
            abrir=open("Highscores.txt","w")#w
            abrir.write(nombre_usuario)
            abrir.close()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------          
#-----------------------------SP1----------------------------------------------------------------------------------------------------------------------------------------------------   

        
    def Validar1():# se valida que la entrada de texto tenga algo, si no retorna nada
        nonlocal E_Nombre
        nombre_usuario = E_Nombre.get()
        if (nombre_usuario!=""):
            return Pantalla1(), GuardarN()
        
    def Pantalla1():#Se crea la ventana del lleva al nivel 1 y sus funciones
        global Flag, FlagA, Boss_life, Nave_life, Score
        Nave_life=50
        Score=0
        Boss_life=30
        FlagA= True
        Flag=True
        VentanaJugar.withdraw()
        Nivel01= Toplevel()
        Nivel01.title("Pantalla 1")
        Nivel01.minsize(600,800)
        Nivel01.resizable(width=NO, height=NO)
        Canv_Pantalla1 = Canvas(Nivel01, width=600, height=800, bg='#252235')
        Canv_Pantalla1.place(x=-2,y=0)
        RUNNING=True
        Canv_Pantalla1.fondo = cargar_img('FondoNivel1.png')
        Fondo3 = Canv_Pantalla1.create_image(0,0,anchor=NW, image=Canv_Pantalla1.fondo)
#---------------------------------------------------------------------------------------------------------------------------------------------------
        def Reloj(seg,minu):#Se crea un reloj con recursividad para determinar el tiempo de la partida
            global FlagA
            if FlagA==True:
                sleep(1)#Cada segundo, le suma 1 a la variable seg
                seg+=1
                if seg==60:#Si la variable seg es 60, la variable minu le suma 1
                    minu+=1
                    seg=0
                Reloj_L.config(text="Tiempo:"+str(minu)+":"+str(seg))
                return Reloj(seg,minu)
            
        Thread(target=Reloj,args=[0,0]).start()

        Reloj_L= Label(Nivel01, text="Tiempo:0:0",bg="#161d2f", fg="white", font=(Fuente_global,15))
        Reloj_L.place(x=480, y=60)

#---------------------------------------------------------------------------------------------------------------------------------------------------                   
        def CargarAliado(patron):#Se crea la funcion que determina la ruta de la imagen 
            frames = glob.glob('Animacion/'+patron)
            frames.sort()
            return VariasIMG_Aliado(frames, [])

        def VariasIMG_Aliado(input, listaResultado):# Se cargan varias imagenes en una lista
            if(input == []):
                return listaResultado
            else:
                listaResultado.append(PhotoImage(file=input[0]))
                return VariasIMG_Aliado(input[1:], listaResultado)

        Aliado = CargarAliado('Nave*.png')
        Aliado_Canv = Canv_Pantalla1.create_image(300,584, tags = ('NaveAliado'))
        
        def recursiveAnimation(i):
            nonlocal Aliado
            if(i==2):
                i=0
            if(RUNNING==True):
                Canv_Pantalla1.itemconfig('NaveAliado', image = Aliado[i])
                time.sleep(0.1)
                Thread(target =recursiveAnimation, args = (i+1,)).start()

        Thread(target =recursiveAnimation, args = (0,)).start()       
               
        def Mov_A(event):

            global FlagA
            if FlagA==True: 
                if event.keysym=='Up':
                    if Canv_Pantalla1.coords(Aliado_Canv)[1]>285:
                        Canv_Pantalla1.move(Aliado_Canv,0,-15)
                elif event.keysym=='Down':
                    if Canv_Pantalla1.coords(Aliado_Canv)[1]<644:
                        Canv_Pantalla1.move(Aliado_Canv,0,15)
                elif event.keysym=='Left':
                    if Canv_Pantalla1.coords(Aliado_Canv)[0]>71:
                        Canv_Pantalla1.move(Aliado_Canv,-13,0)
                elif event.keysym=='Right':
                    if Canv_Pantalla1.coords(Aliado_Canv)[0]<526:
                        Canv_Pantalla1.move(Aliado_Canv,13,0)

        Canv_Pantalla1.bind_all('<KeyPress-Up>',Mov_A)
        Canv_Pantalla1.bind_all('<KeyPress-Down>',Mov_A)
        Canv_Pantalla1.bind_all('<KeyPress-Left>',Mov_A)
        Canv_Pantalla1.bind_all('<KeyPress-Right>',Mov_A)
  
#----------------------------------------------------------------------------------------------------------------------------------------------------------
        Bullet = cargar_img2('Bullet2.png')
                
        def Mov_Bala(Bala):
            global Boss_life, reproducir_fx, Score
            Bala_box= Canv_Pantalla1.bbox(Bala)
            Jefe1box= Canv_Pantalla1.bbox(Jefe1_E)
            if Canv_Pantalla1.coords(Bala)[1]<-50: #Limite hasta donde llega la bala
                Canv_Pantalla1.delete(Bala)
            elif Bala_box[0]<Jefe1box[2] and Bala_box[2]>Jefe1box[0] and Bala_box[1]<Jefe1box[3]<Bala_box[3] and Bala_box[3] > Bala_box[1]:
                Canv_Pantalla1.delete(Bala)
                if Boss_life!=0:
                    Boss_life-=1
                    Score+=1
                    Score_L.config(text="Puntos:" + str(Score))
                    life_Jefe.config(text="❤:" + str(Boss_life))
            else:
                Canv_Pantalla1.move(Bala,0,-12) #El disparo avanza en el eje Y
                Canv_Pantalla1.after(15,Mov_Bala,Bala)
        
        def Disparar(event):

            global FlagA
            if FlagA==True:
                if event.keysym=='space': #          
                    coords= Canv_Pantalla1.coords(Aliado_Canv)
                    Bala = Canv_Pantalla1.create_image(coords[0]-20,coords[1]-50,anchor=NW,image=Bullet)
                    reproducir_fx(cargarMP3('SE_01.wav'))
                    Thread(target=Mov_Bala, args=(Bala,)).start()

        Canv_Pantalla1.bind_all('<KeyRelease-space>',Disparar)
       
#----------------------------------------------------------------------------------------------------------------------------------------------------------
        def CargarJefe1(patron):
            frames = glob.glob('Animacion/Jefe1-0/'+patron)
            frames.sort()
            return VariasIMG_Jefe1(frames, [])

        def VariasIMG_Jefe1(input, listaResultado):
            if(input == []):
                return listaResultado
            else:
                listaResultado.append(PhotoImage(file=input[0]))
                return VariasIMG_Jefe1(input[1:], listaResultado)

        Jefe1 = CargarJefe1('Jefe1*.png')
        Jefe1_E = Canv_Pantalla1.create_image(250,100, tags = ('Jefe_1')) #Donde aparece la imagen(Jefe1)

        def recursiveAnimationJefe1(i):
            nonlocal Jefe1
            if(i==20):
                i=0
            if(RUNNING==True):
                Canv_Pantalla1.itemconfig('Jefe_1', image = Jefe1[i])
                time.sleep(0.1)
                Thread(target =recursiveAnimationJefe1, args = (i+1,)).start()

        Thread(target =recursiveAnimationJefe1, args = (0,)).start()

        def Mov_Jefe1(x):

            global Flag, Nave_life
            Jefe1box= Canv_Pantalla1.bbox(Jefe1_E)
            Aliadobox= Canv_Pantalla1.bbox(Aliado_Canv)
            to_move = x
            if(Flag==True):
                if Canv_Pantalla1.coords(Jefe1_E)[0]>=475: #limite al que lleva la imagen borde derecho
                    Canv_Pantalla1.move(Jefe1_E,-5,0) #Cantidad de pixeles que se mueve a la izuiqerda
                    to_move = -5  
                elif Canv_Pantalla1.coords(Jefe1_E)[0]<=130: #Limite al que lleva la imagen borde izquierdo
                    Canv_Pantalla1.move(Jefe1_E,5,0) #Cantidad de pixeles que se mueve a la derecha
                    to_move = 5
                elif Aliadobox[0]<Jefe1box[2] and Aliadobox[2]>Jefe1box[0] and Aliadobox[1]<Jefe1box[3]<Aliadobox[3] and Aliadobox[3] > Aliadobox[1]:
                    Nave_life-=1
                    Nave_life_l1.config(text="❤:" + str(Nave_life))
                    reproducir_fx(cargarMP3('MMX18.wav'))
                else:
                    Canv_Pantalla1.move(Jefe1_E,x,0)
                     
            Canv_Pantalla1.after(25,Mov_Jefe1,to_move)

        Thread1 = Thread(target=Mov_Jefe1,args=(-5,)) #Cantidad de pixeles que se mueve la nave y la dirección inicial
        Thread1.start()  
        FlagTemp=True

        def temporizador():#Se crea una funcion que cada 2 segundos de un numero aleatorio entre el 1 y el 10
            nonlocal FlagTemp
            if (FlagTemp==True):
                time.sleep(2)
                aleatorio = random.randint(1,10)
                Embestida(aleatorio)
                temporizador()

        Thread(target = temporizador).start() 

        def bajada():#El jefe realiza la funcion de bajada
            global Nave_life, Boss_life
            Jefe1box= Canv_Pantalla1.bbox(Jefe1_E)
            Aliadobox= Canv_Pantalla1.bbox(Aliado_Canv)
            if (Canv_Pantalla1.coords(Jefe1_E)[1]<600):#Limite al que llega el jefe dentro del top level en el eje Y
                Canv_Pantalla1.move(Jefe1_E,0,5)
                Canv_Pantalla1.after(13, bajada)
            elif Jefe1box[0]<Aliadobox[0]<Jefe1box[2] and Jefe1box[0]<Aliadobox[2]<Jefe1box[2] and Jefe1box[1]<Aliadobox[1]<Jefe1box[3] and Jefe1box[1]<Aliadobox[3]<Jefe1box[3]:# Se establecen las bbox o puntos de contacto del jefe con el aliado
                Nave_life-=10
                Nave_life_l1.config(text="❤:" + str(Nave_life))
                reproducir_fx(cargarMP3('MMX18.wav'))
                subida()
            else:
                Boss_life-=1
                life_Jefe.config(text="❤:" + str(Boss_life))
                subida()
                

        def subida():#El jefe realiza la funcion de subida
            global Flag, Nave_life
            Jefe1box= Canv_Pantalla1.bbox(Jefe1_E)
            Aliadobox= Canv_Pantalla1.bbox(Aliado_Canv)
            if Canv_Pantalla1.coords(Jefe1_E)[1]>101:   #Limite al que llega el jefe dentro del top level en el eje Y
                Canv_Pantalla1.move(Jefe1_E,0,-5)
                Canv_Pantalla1.after(13, subida)
            elif Jefe1box[0]<Aliadobox[0]<Jefe1box[2] and Jefe1box[0]<Aliadobox[2]<Jefe1box[2] and Jefe1box[1]<Aliadobox[1]<Jefe1box[3] and Jefe1box[1]<Aliadobox[3]<Jefe1box[3]:# Se establecen las bbox o puntos de contacto del jefe con el aliado
                Nave_life-=10
                Nave_life_l1.config(text="❤:" + str(Nave_life))
                reproducir_fx(cargarMP3('MMX18.wav'))
            else:
                Flag=True

        def Embestida(aleatorio):#El jefe realiza la embestida cuando se cumple la funcion de temporizador
            global Flag
            if (aleatorio%3==0) and Flag:
                Flag = False
                return bajada()          
                 
#-------------------------------------------------------------------------------------------------------------------------------------------------
        life_Jefe = Label(Nivel01, text="❤:" + str(Boss_life),bg="#161d2f", fg="white", font=(Fuente_global,15))
        life_Jefe.place(x=25, y=10)
        Nave_life_l1 = Label(Nivel01, text="❤:" + str(Nave_life),bg="#161d2f", fg="white", font=(Fuente_global,15))
        Nave_life_l1.place(x=25, y=700)
        Score_L = Label(Nivel01, text="Puntos:" + str(Score),bg="#161d2f", fg="white", font=(Fuente_global,15))
        Score_L.place(x=490, y=10)
#-------------------------------------------------------------------------------------------------------------------------------------------------

        def Siguiente_N2():#Funcion que detiene las cosas y abre varias opciones para que el jugador escoja cuando los puntos de vida del jefe son 0
            global Boss_life, Flag, FlagA,Score
            nonlocal FlagTemp, Bullet
            if Boss_life==0:
                Felicidades_L=Label(Nivel01,text="Felicidades!!!",font=("Comic Sans MS",15), width=10, height=2,bg="#1e0238",fg="white")
                Felicidades_L.place(x=240, y=200)
                FlagTemp= False
                Flag=False
                FlagA= False      
                Reintentar_L=Button(Nivel01, text='Reintentar',font=("Comic Sans MS",10),command=Reintentar, width=10, height=2,bg="#1e0238",fg="white")
                Reintentar_L.place(x=240, y=500)
                Volver= Button(Nivel01, text='Volver',font=("Comic Sans MS",10),command=closeP1, width=10, height=2,bg="#1e0238",fg="white")
                Volver.place(x=120, y=350)
                Siguiente_Nivel= Button(Nivel01, text='Siguiente Nivel',font=("Comic Sans MS",10),command=Cerrar1, width=13, height=2,bg="#1e0238",fg="white")
                Siguiente_Nivel.place(x=360, y=350)
                if Nave_life==50:#Bonificacion de puntos
                    Score+=10
            
            else:
                Canv_Pantalla1.after(100,Siguiente_N2)
                    
        Thread(target=Siguiente_N2).start()
        
        def Restart():#Funcion que detiene los hilos cuando el jugador no tiene puntos de vida 
            global Nave_life, Flag, FlagA
            nonlocal FlagTemp
            if Nave_life==0:
                Perdiste_L=Label(Nivel01,text="Game Over",font=("Comic Sans MS",15), width=10, height=2,bg="#1e0238",fg="white")
                Perdiste_L.place(x=240, y=200)
                FlagTemp= False
                Flag=False
                FlagA= False      
                Reintentar_L=Button(Nivel01, text='Reintentar',font=("Comic Sans MS",10),command=Reintentar, width=10, height=2,bg="#1e0238",fg="white")
                Reintentar_L.place(x=360, y=350)
                Volver= Button(Nivel01, text='Volver',font=("Comic Sans MS",10),command=closeP1, width=10, height=2,bg="#1e0238",fg="white")
                Volver.place(x=120, y=350)
            else:
                Canv_Pantalla1.after(100,Restart)
                    
        Thread(target=Restart).start()

        def Reintentar():#Funicion que reincia el nivel
            global Score, Nave_life
            Score=0
            Nave_life=50
            Nivel01.destroy()
            Pantalla1()
            
        def Cerrar1():#Funcion que cierra el nivel
            nonlocal FlagTemp
            FlagTemp= False
            Nivel01.destroy()
            Pantalla2()

        def closeP1():#Funcion que cierra el nivel
            nonlocal FlagTemp
            global Flag
            FlagTemp=False
            Flag=False
            nonlocal RUNNING
            RUNNING=False
            Nivel01.destroy()
            VentanaJugar.deiconify()
            
        Btn_VolverP1= Button(Nivel01, text='Cerrar Partida',font=("Comic Sans MS",10),command=closeP1, width=10, height=2,bg="#1e0238",fg="white")
        Btn_VolverP1.place(x=500, y=700)

        Nivel01.protocol("WM_DELETE_WINDOW", closeP1)

#-----------------------------------------------------------------------------------------------------------------------------------------------------
 #-----------------------------SP2----------------------------------------------------------------------------------------------------------------------------------------------------   

    def Validar2():#Se verifica que la entrada tenga algun texto
        nonlocal E_Nombre
        nombre_usuario = E_Nombre.get()
        if (nombre_usuario!=""):
            return Pantalla2(), GuardarN()

    def Pantalla2():#Funcion que abre el nivel2 del juego
        global Flag, FlagA, Boss_life, Nave_life, Score
        if Score!=0:
            pass
        else:
            Score=0
        Nave_life=50
        Boss_life=40
        FlagA= True
        Flag=True  
        VentanaJugar.withdraw()
        
        Nivel02= Toplevel()
        Nivel02.title("Pantalla 2")
        Nivel02.minsize(600,800)
        Nivel02.resizable(width=NO, height=NO)
        Canv_Pantalla2 = Canvas(Nivel02, width=600, height=800, bg='#252235')
        Canv_Pantalla2.place(x=-2,y=0)
        RUNNING=True
        Canv_Pantalla2.fondo = cargar_img('FondoNivel2.png')
        Fondo4 = Canv_Pantalla2.create_image(0,0,anchor=NW, image=Canv_Pantalla2.fondo)
#---------------------------------------------------------------------------------------------------------------------------------------------------
        def Reloj(seg,minu):
            global FlagA
            if FlagA==True:
                sleep(1)
                seg+=1
                if seg==60:
                    minu+=1
                    seg=0
                Reloj_L.config(text="Tiempo:"+str(minu)+":"+str(seg))
                return Reloj(seg,minu)
            
        Thread(target=Reloj,args=[0,0]).start()

        Reloj_L= Label(Nivel02, text="Tiempo:0:0",bg="#161d2f", fg="white", font=(Fuente_global,15))
        Reloj_L.place(x=480, y=60)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                   
        def CargarAliado(patron):
            frames = glob.glob('Animacion/'+patron)
            frames.sort()
            return VariasIMG_Aliado(frames, [])

        def VariasIMG_Aliado(input, listaResultado):
            if(input == []):
                return listaResultado
            else:
                listaResultado.append(PhotoImage(file=input[0]))
                return VariasIMG_Aliado(input[1:], listaResultado)

        Aliado = CargarAliado('Nave*.png')
        Aliado_Canv = Canv_Pantalla2.create_image(300,584, tags = ('NaveAliado'))
        
        def recursiveAnimation(i):
            nonlocal Aliado
            if(i==2):
                i=0
            if(RUNNING==True):
                Canv_Pantalla2.itemconfig('NaveAliado', image = Aliado[i])
                time.sleep(0.1)
                Thread(target =recursiveAnimation, args = (i+1,)).start()

        Thread(target =recursiveAnimation, args = (0,)).start()       
               
        def Mov_A(event):
            global FlagA
            if FlagA==True: 
                if event.keysym=='Up':
                    if Canv_Pantalla2.coords(Aliado_Canv)[1]>285:
                        Canv_Pantalla2.move(Aliado_Canv,0,-15)
                elif event.keysym=='Down':
                    if Canv_Pantalla2.coords(Aliado_Canv)[1]<644:
                        Canv_Pantalla2.move(Aliado_Canv,0,15)
                elif event.keysym=='Left':
                    if Canv_Pantalla2.coords(Aliado_Canv)[0]>71:
                        Canv_Pantalla2.move(Aliado_Canv,-13,0)
                elif event.keysym=='Right':
                    if Canv_Pantalla2.coords(Aliado_Canv)[0]<526:
                        Canv_Pantalla2.move(Aliado_Canv,13,0)

        Canv_Pantalla2.bind_all('<KeyPress-Up>',Mov_A)
        Canv_Pantalla2.bind_all('<KeyPress-Down>',Mov_A)
        Canv_Pantalla2.bind_all('<KeyPress-Left>',Mov_A)
        Canv_Pantalla2.bind_all('<KeyPress-Right>',Mov_A)
  
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        Bullet = cargar_img2('Bullet2.png')
                
        def Mov_Bala(Bala):
            global Boss_life, reproducir_fx, Score
            Bala_box= Canv_Pantalla2.bbox(Bala)
            Jefe1box= Canv_Pantalla2.bbox(Jefe2_E)
            if Canv_Pantalla2.coords(Bala)[1]<-50: #Limite hasta donde llega la bala
                Canv_Pantalla2.delete(Bala)
            elif Bala_box[0]<Jefe1box[2] and Bala_box[2]>Jefe1box[0] and Bala_box[1]<Jefe1box[3]<Bala_box[3] and Bala_box[3] > Bala_box[1]:
                Canv_Pantalla2.delete(Bala)
                if Boss_life!=0:
                    Boss_life-=1
                    Score+=1
                    Score_L.config(text="Puntos:" + str(Score))
                    life_Jefe.config(text="❤:" + str(Boss_life))
            else:
                Canv_Pantalla2.move(Bala,0,-12) #El disparo avanza en el eje Y
                Canv_Pantalla2.after(15,Mov_Bala,Bala)
                
        def Disparar(event):
            global FlagA
            if FlagA==True:  
                if event.keysym=='space':           
                    coords= Canv_Pantalla2.coords(Aliado_Canv)
                    Bala = Canv_Pantalla2.create_image(coords[0]-20,coords[1]-50,anchor=NW,image=Bullet)
                    reproducir_fx(cargarMP3('SE_01.wav'))
                    Thread(target=Mov_Bala, args=(Bala,)).start()

        Canv_Pantalla2.bind_all('<KeyRelease-space>',Disparar)
       
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        def CargarJefe2(patron):
            frames = glob.glob('Animacion/Jefe2-0/'+patron)
            frames.sort()
            return VariasIMG_Jefe1(frames, [])

        def VariasIMG_Jefe1(input, listaResultado):
            if(input == []):
                return listaResultado
            else:
                listaResultado.append(PhotoImage(file=input[0]))
                return VariasIMG_Jefe1(input[1:], listaResultado)

        Jefe2 = CargarJefe2('Jefe2*.png')
        Jefe2_E = Canv_Pantalla2.create_image(250,100, tags = ('Jefe_2')) #Donde aparece la imagen(Jefe1)

        def recursiveAnimationJefe2(i):
            nonlocal Jefe2
            if(i==96):
                i=0
            if(RUNNING==True):
                Canv_Pantalla2.itemconfig('Jefe_2', image = Jefe2[i])
                time.sleep(0.1)
                Thread(target =recursiveAnimationJefe2, args = (i+1,)).start()

        Thread(target =recursiveAnimationJefe2, args = (0,)).start()

        def Mov_Jefe2():
            global Flag, Nave_life
            jefe2_X=random.randint(-200,200)
            
            if(Flag==True):
                if Canv_Pantalla2.coords(Jefe2_E)[0]+jefe2_X < 500 and Canv_Pantalla2.coords(Jefe2_E)[0]+jefe2_X >200:
                    Canv_Pantalla2.move(Jefe2_E,jefe2_X,0)
                Nivel02.after(2000,Mov_Jefe2)
        Thread(target=Mov_Jefe2()).start
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        Flag2=True
        def temporizador2():
            nonlocal Flag2
            if Flag2 == True:
                time.sleep(1)
                DisparoJefe()
                temporizador2()
        Thread(target = temporizador2).start() 

        def MovimientoD(Bala):
            global Boss_life, reproducir_fx, Score, Nave_life, FlagA
            Bala_box= Canv_Pantalla2.bbox(Bala)
            Aliadobox= Canv_Pantalla2.bbox(Aliado_Canv)
            if FlagA==True:
                if Canv_Pantalla2.coords(Bala)[1]>700: #Limite hasta donde llega la bala
                    Canv_Pantalla2.delete(Bala)
                elif Aliadobox[0]<Bala_box[2] and Aliadobox[2]>Bala_box[0] and Aliadobox[1]<Bala_box[3]<Aliadobox[3] and Aliadobox[3] > Aliadobox[1]:
                    Canv_Pantalla2.delete(Bala)
                    if Nave_life!=0:
                        Nave_life-=3
                        Nave_life_l2.config(text="❤:" + str(Nave_life))
                    if Nave_life==2:
                        Nave_life-=2
                        Nave_life_l2.config(text="❤:" + str(Nave_life))
                else:
                    Canv_Pantalla2.move(Bala,0,3) #El disparo avanza en el eje Y
                    Canv_Pantalla2.after(15,MovimientoD,Bala)

        def DisparoJefe():
            global FlagA
            if FlagA==True:
                coords= Canv_Pantalla2.coords(Jefe2_E)
                Bala1 = Canv_Pantalla2.create_image(coords[0]+80,coords[1]-55,anchor=NW,image=Bullet)
                Bala2 = Canv_Pantalla2.create_image(coords[0]-100,coords[1]-55,anchor=NW,image=Bullet)
                Bala3 = Canv_Pantalla2.create_image(coords[0]-35,coords[1]+50,anchor=NW,image=Bullet)
                reproducir_fx(cargarMP3('SE_01.wav'))
                Thread(target=MovimientoD, args=(Bala1,)).start()
                Thread(target=MovimientoD, args=(Bala2,)).start()
                Thread(target=MovimientoD, args=(Bala3,)).start()
                 
#-------------------------------------------------------------------------------------------------------------------------------------------------
        life_Jefe = Label(Nivel02, text="❤:" + str(Boss_life),bg="#161d2f", fg="white", font=(Fuente_global,15))
        life_Jefe.place(x=25, y=10)
        Nave_life_l2 = Label(Nivel02, text="❤:" + str(Nave_life),bg="#161d2f", fg="white", font=(Fuente_global,15))
        Nave_life_l2.place(x=25, y=700)
        Score_L = Label(Nivel02, text="Puntos:" + str(Score),bg="#161d2f", fg="white", font=(Fuente_global,15))
        Score_L.place(x=490, y=10)
#-------------------------------------------------------------------------------------------------------------------------------------------------

        def Siguiente_N2():
            global Boss_life, Flag, FlagA, Score

            if Boss_life==0:
                coords= Canv_Pantalla2.coords(Aliado_Canv)        
                Bala = Canv_Pantalla2.create_image(coords[0]-20,coords[1]-50,anchor=NW,image=Bullet)
                Canv_Pantalla2.delete(Bala)
                Felicidades_L=Label(Nivel02,text="Felicidades!!!",font=("Comic Sans MS",15), width=10, height=2,bg="#1e0238",fg="white")
                Felicidades_L.place(x=240, y=200)
                Flag=False
                FlagA= False      
                Reintentar_L=Button(Nivel02, text='Reintentar',font=("Comic Sans MS",10),command=Reintentar, width=10, height=2,bg="#1e0238",fg="white")
                Reintentar_L.place(x=240, y=500)
                Volver= Button(Nivel02, text='Volver',font=("Comic Sans MS",10),command=closeP2, width=10, height=2,bg="#1e0238",fg="white")
                Volver.place(x=120, y=350)
                Siguiente_Nivel= Button(Nivel02, text='Siguiente Nivel',font=("Comic Sans MS",10),command=Cerrar2, width=13, height=2,bg="#1e0238",fg="white")
                Siguiente_Nivel.place(x=360, y=350)
                if Nave_life==50:
                    Score+=10
            else:
                Canv_Pantalla2.after(100,Siguiente_N2)
                    
        Thread(target=Siguiente_N2).start()
        
        def Restart2():
            global Nave_life, Flag, FlagA
            if Nave_life==0:
                Perdiste_L=Label(Nivel02,text="Game Over",font=("Comic Sans MS",15), width=10, height=2,bg="#1e0238",fg="white")
                Perdiste_L.place(x=240, y=200)
                Flag=False
                FlagA= False      
                Reintentar_L=Button(Nivel02, text='Reintentar',font=("Comic Sans MS",10),command=Reintentar, width=10, height=2,bg="#1e0238",fg="white")
                Reintentar_L.place(x=360, y=350)
                Volver= Button(Nivel02, text='Volver',font=("Comic Sans MS",10),command=closeP2, width=10, height=2,bg="#1e0238",fg="white")
                Volver.place(x=120, y=350)
            else:
                Canv_Pantalla2.after(100,Restart2)
                    
        Thread(target=Restart2).start()

        def Reintentar():
            global Score, Nave_life
            Score=0
            Nave_life=50
            Nivel02.destroy()
            Pantalla2()

        def Cerrar2():
            Nivel02.destroy()
            Pantalla3()   

        def closeP2():
            global Flag, Score,Nave_life
            Score=0
            Nave_life=50
            Flag=False
            nonlocal RUNNING
            RUNNING=False
            Nivel02.destroy()
            VentanaJugar.deiconify()


        Btn_VolverP2= Button(Nivel02, text='Cerrar Partida',font=("Comic Sans MS",10),command=closeP2, width=10, height=2,bg="#1e0238",fg="white")
        Btn_VolverP2.place(x=500, y=700)
        Nivel02.protocol("WM_DELETE_WINDOW", closeP2)
 #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------           
 #-----------------------------SP3----------------------------------------------------------------------------------------------------------------------------------------------------   
    def Validar3():
        nonlocal E_Nombre
        nombre_usuario = E_Nombre.get()
        if (nombre_usuario!=""):
            return Pantalla3(),GuardarN()
    
    def Pantalla3():#Se crea la ventana del lleva al nivel 1 y sus funciones

        global Flag, FlagA, Boss_life, Nave_life, Score
        Nave_life=50
        Score=0
        Boss_life=30
        FlagA= True
        Flag=True
        VentanaJugar.withdraw()
        Nivel03= Toplevel()
        Nivel03.title("Pantalla 1")
        Nivel03.minsize(600,800)
        Nivel03.resizable(width=NO, height=NO)
        Canv_Pantalla3 = Canvas(Nivel03, width=600, height=800, bg='#252235')
        Canv_Pantalla3.place(x=-2,y=0)
        RUNNING=True
        Canv_Pantalla3.fondo = cargar_img('FondoNivel3.png')
        Fondo5 = Canv_Pantalla3.create_image(0,0,anchor=NW, image=Canv_Pantalla3.fondo)
#---------------------------------------------------------------------------------------------------------------------------------------------------
        def Reloj3(seg,minu):#Se crea un reloj con recursividad para determinar el tiempo de la partida
            global FlagA
            if FlagA==True:
                sleep(1)#Cada segundo, le suma 1 a la variable seg
                seg+=1
                if seg==60:#Si la variable seg es 60, la variable minu le suma 1
                    minu+=1
                    seg=0
                Reloj_L.config(text="Tiempo:"+str(minu)+":"+str(seg))
                return Reloj3(seg,minu)
            
        Thread(target=Reloj3,args=[0,0]).start()

        Reloj_L= Label(Nivel03, text="Tiempo:0:0",bg="#161d2f", fg="white", font=(Fuente_global,15))
        Reloj_L.place(x=480, y=60)

#---------------------------------------------------------------------------------------------------------------------------------------------------                   
        def CargarAliado(patron):#Se crea la funcion que determina la ruta de la imagen 
            frames = glob.glob('Animacion/'+patron)
            frames.sort()
            return VariasIMG_Aliado(frames, [])

        def VariasIMG_Aliado(input, listaResultado):# Se cargan varias imagenes en una lista
            if(input == []):
                return listaResultado
            else:
                listaResultado.append(PhotoImage(file=input[0]))
                return VariasIMG_Aliado(input[1:], listaResultado)

        Aliado = CargarAliado('Nave*.png')
        Aliado_Canv = Canv_Pantalla3.create_image(300,584, tags = ('NaveAliado'))
        
        def recursiveAnimation(i):
            nonlocal Aliado
            if(i==2):
                i=0
            if(RUNNING==True):
                Canv_Pantalla3.itemconfig('NaveAliado', image = Aliado[i])
                time.sleep(0.1)
                Thread(target =recursiveAnimation, args = (i+1,)).start()

        Thread(target =recursiveAnimation, args = (0,)).start()       
               
        def Mov_A(event):

            global FlagA
            if FlagA==True: 
                if event.keysym=='Up':
                    if Canv_Pantalla3.coords(Aliado_Canv)[1]>285:
                        Canv_Pantalla3.move(Aliado_Canv,0,-15)
                elif event.keysym=='Down':
                    if Canv_Pantalla3.coords(Aliado_Canv)[1]<644:
                        Canv_Pantalla3.move(Aliado_Canv,0,15)
                elif event.keysym=='Left':
                    if Canv_Pantalla3.coords(Aliado_Canv)[0]>71:
                        Canv_Pantalla3.move(Aliado_Canv,-13,0)
                elif event.keysym=='Right':
                    if Canv_Pantalla3.coords(Aliado_Canv)[0]<526:
                        Canv_Pantalla3.move(Aliado_Canv,13,0)

        Canv_Pantalla3.bind_all('<KeyPress-Up>',Mov_A)
        Canv_Pantalla3.bind_all('<KeyPress-Down>',Mov_A)
        Canv_Pantalla3.bind_all('<KeyPress-Left>',Mov_A)
        Canv_Pantalla3.bind_all('<KeyPress-Right>',Mov_A)
  
#----------------------------------------------------------------------------------------------------------------------------------------------------------
        Bullet = cargar_img2('Bullet2.png')
                
        def Mov_Bala(Bala):
 
            global Boss_life, reproducir_fx, Score
            Bala_box= Canv_Pantalla3.bbox(Bala)
            Jefe1box= Canv_Pantalla3.bbox(Jefe3_E)
            if Canv_Pantalla3.coords(Bala)[1]<-50: #Limite hasta donde llega la bala
                Canv_Pantalla3.delete(Bala)
            elif Bala_box[0]<Jefe1box[2] and Bala_box[2]>Jefe1box[0] and Bala_box[1]<Jefe1box[3]<Bala_box[3] and Bala_box[3] > Bala_box[1]:
                Canv_Pantalla3.delete(Bala)
                if Boss_life!=0:
                    Boss_life-=1
                    Score+=1
                    Score_L.config(text="Puntos:" + str(Score))
                    life_Jefe.config(text="❤:" + str(Boss_life))
            else:
                Canv_Pantalla3.move(Bala,0,-12) #El disparo avanza en el eje Y
                Canv_Pantalla3.after(15,Mov_Bala,Bala)
        
        def Disparar(event):
            global FlagA
            if FlagA==True:
                 
                if event.keysym=='space':           
                    coords= Canv_Pantalla3.coords(Aliado_Canv)
                    Bala = Canv_Pantalla3.create_image(coords[0]-20,coords[1]-50,anchor=NW,image=Bullet)
                    reproducir_fx(cargarMP3('SE_01.wav'))
                    Thread(target=Mov_Bala, args=(Bala,)).start()

        Canv_Pantalla3.bind_all('<KeyRelease-space>',Disparar)
       
#----------------------------------------------------------------------------------------------------------------------------------------------------------
        def CargarJefe3(patron):
            frames = glob.glob('Animacion/Jefe3-0/'+patron)
            frames.sort()
            return VariasIMG_Jefe3(frames, [])

        def VariasIMG_Jefe3(input, listaResultado):
            if(input == []):
                return listaResultado
            else:
                listaResultado.append(PhotoImage(file=input[0]))
                return VariasIMG_Jefe3(input[1:], listaResultado)

        Jefe3 = CargarJefe3('Jefe3*.png')
        Jefe3_E = Canv_Pantalla3.create_image(250,100, tags = ('Jefe_3')) #Donde aparece la imagen(Jefe1)

        def recursiveAnimationJefe1(i):
            nonlocal Jefe3
            if(i==45):
                i=0
            if(RUNNING==True):
                Canv_Pantalla3.itemconfig('Jefe_3', image = Jefe3[i])
                time.sleep(0.1)
                Thread(target =recursiveAnimationJefe1, args = (i+1,)).start()

        Thread(target =recursiveAnimationJefe1, args = (0,)).start()

        def Mov_Jefe3(x):
            global Flag, Nave_life
            Jefe1box= Canv_Pantalla3.bbox(Jefe3_E)
            Aliadobox= Canv_Pantalla3.bbox(Aliado_Canv)
            to_move = x
            if(Flag==True):
                if Canv_Pantalla3.coords(Jefe3_E)[0]>=475: #limite al que lleva la imagen borde derecho
                    Canv_Pantalla3.move(Jefe3_E,-5,0) #Cantidad de pixeles que se mueve a la izuiqerda
                    to_move = -5  
                elif Canv_Pantalla3.coords(Jefe3_E)[0]<=130: #Limite al que lleva la imagen borde izquierdo
                    Canv_Pantalla3.move(Jefe3_E,5,0) #Cantidad de pixeles que se mueve a la derecha
                    to_move = 5
                elif Aliadobox[0]<Jefe1box[2] and Aliadobox[2]>Jefe1box[0] and Aliadobox[1]<Jefe1box[3]<Aliadobox[3] and Aliadobox[3] > Aliadobox[1]:
                    Nave_life-=1
                    Nave_life_l3.config(text="❤:" + str(Nave_life))
                    reproducir_fx(cargarMP3('MMX18.wav'))
                else:
                    Canv_Pantalla3.move(Jefe3_E,x,0)
                     
            Canv_Pantalla3.after(25,Mov_Jefe3,to_move)

        Thread1 = Thread(target=Mov_Jefe3,args=(-5,)) #Cantidad de pixeles que se mueve la nave y la dirección inicial
        Thread1.start()  
        FlagTemp=True

        def temporizador():
            nonlocal FlagTemp
            if (FlagTemp==True):
                time.sleep(2)
                aleatorio = random.randint(1,10)
                Embestida(aleatorio)
                temporizador()

        Thread(target = temporizador).start() 

        def bajada():
            global Nave_life, Boss_life
            Jefe1box= Canv_Pantalla3.bbox(Jefe3_E)
            Aliadobox= Canv_Pantalla3.bbox(Aliado_Canv)
            if (Canv_Pantalla3.coords(Jefe3_E)[1]<600):
                Canv_Pantalla3.move(Jefe3_E,0,5)
                Canv_Pantalla3.after(13, bajada)
            elif Jefe1box[0]<Aliadobox[0]<Jefe1box[2] and Jefe1box[0]<Aliadobox[2]<Jefe1box[2] and Jefe1box[1]<Aliadobox[1]<Jefe1box[3] and Jefe1box[1]<Aliadobox[3]<Jefe1box[3]:
                Nave_life-=10
                Nave_life_l3.config(text="❤:" + str(Nave_life))
                reproducir_fx(cargarMP3('MMX18.wav'))
                subida()
            else:
                Boss_life-=1
                life_Jefe.config(text="❤:" + str(Boss_life))
                subida()
                

        def subida():
            global Flag, Nave_life
            Jefe1box= Canv_Pantalla3.bbox(Jefe3_E)
            Aliadobox= Canv_Pantalla3.bbox(Aliado_Canv)
            if Canv_Pantalla3.coords(Jefe3_E)[1]>101:   
                Canv_Pantalla3.move(Jefe3_E,0,-5)
                Canv_Pantalla3.after(13, subida)
            elif Jefe1box[0]<Aliadobox[0]<Jefe1box[2] and Jefe1box[0]<Aliadobox[2]<Jefe1box[2] and Jefe1box[1]<Aliadobox[1]<Jefe1box[3] and Jefe1box[1]<Aliadobox[3]<Jefe1box[3]:
                Nave_life-=10
                Nave_life_l3.config(text="❤:" + str(Nave_life))
                reproducir_fx(cargarMP3('MMX18.wav'))
            else:
                Flag=True

        def Embestida(aleatorio):
            global Flag
            if (aleatorio%3==0) and Flag:
                Flag = False
                return bajada()

        Flag3=True
        def temporizador3():
            nonlocal Flag3
            if Flag3 == True:
                time.sleep(1)
                DisparoJefe()
                temporizador3()

        Thread(target = temporizador3).start() 
        def MovimientoD(Bala):
            global Boss_life, reproducir_fx, Score, Nave_life, FlagA
            Bala_box= Canv_Pantalla3.bbox(Bala)
            Aliadobox= Canv_Pantalla3.bbox(Aliado_Canv)
            if FlagA==True:
                if Canv_Pantalla3.coords(Bala)[1]>700: #Limite hasta donde llega la bala
                    Canv_Pantalla3.delete(Bala)
                elif Aliadobox[0]<Bala_box[2] and Aliadobox[2]>Bala_box[0] and Aliadobox[1]<Bala_box[3]<Aliadobox[3] and Aliadobox[3] > Aliadobox[1]:
                    Canv_Pantalla3.delete(Bala)
                    if Nave_life!=0:
                        Nave_life-=3
                        Nave_life_l3.config(text="❤:" + str(Nave_life))
                    if Nave_life==2:
                        Nave_life-=2
                        Nave_life_l3.config(text="❤:" + str(Nave_life))
                else:
                    Canv_Pantalla3.move(Bala,0,3) #El disparo avanza en el eje Y
                    Canv_Pantalla3.after(15,MovimientoD,Bala)

        def DisparoJefe():
            global FlagA
            if FlagA==True:
                coords= Canv_Pantalla3.coords(Jefe3_E)
                Bala1 = Canv_Pantalla3.create_image(coords[0]+80,coords[1]-55,anchor=NW,image=Bullet)
                Bala2 = Canv_Pantalla3.create_image(coords[0]-100,coords[1]-55,anchor=NW,image=Bullet)
                Bala3 = Canv_Pantalla3.create_image(coords[0]-35,coords[1]+50,anchor=NW,image=Bullet)
                reproducir_fx(cargarMP3('SE_01.wav'))
                Thread(target=MovimientoD, args=(Bala1,)).start()
                Thread(target=MovimientoD, args=(Bala2,)).start()
                Thread(target=MovimientoD, args=(Bala3,)).start()                
                          
                 
#-------------------------------------------------------------------------------------------------------------------------------------------------
        life_Jefe = Label(Nivel03, text="❤:" + str(Boss_life),bg="#161d2f", fg="white", font=(Fuente_global,15))
        life_Jefe.place(x=25, y=10)
        Nave_life_l3 = Label(Nivel03, text="❤:" + str(Nave_life),bg="#161d2f", fg="white", font=(Fuente_global,15))
        Nave_life_l3.place(x=25, y=700)
        Score_L = Label(Nivel03, text="Puntos:" + str(Score),bg="#161d2f", fg="white", font=(Fuente_global,15))
        Score_L.place(x=490, y=10)
#-------------------------------------------------------------------------------------------------------------------------------------------------

        def Siguiente_N3():
            global Boss_life, Flag, FlagA,Score
            nonlocal FlagTemp, Bullet, Flag3
            if Boss_life==0:
                Felicidades_L=Label(Nivel03,text="Felicidades!!!",font=("Comic Sans MS",15), width=10, height=2,bg="#1e0238",fg="white")
                Felicidades_L.place(x=240, y=200)
                FlagTemp==False
                Flag=False
                FlagA=False      
                Flag3=False
                Reintentar_L=Button(Nivel03, text='Reintentar',font=("Comic Sans MS",10),command=Reintentar, width=10, height=2,bg="#1e0238",fg="white")
                Reintentar_L.place(x=240, y=500)
                Volver= Button(Nivel03, text='Volver',font=("Comic Sans MS",10),command=closeP1, width=10, height=2,bg="#1e0238",fg="white")
                Volver.place(x=120, y=350)
                Siguiente_Nivel= Button(Nivel03, text='Highscore',font=("Comic Sans MS",10),command=Cerrar1, width=13, height=2,bg="#1e0238",fg="white")
                Siguiente_Nivel.place(x=360, y=350)
                if Nave_life==50:
                    Score+=10
            
            else:
                Canv_Pantalla3.after(100,Siguiente_N3)
                    
        Thread(target=Siguiente_N3).start()
        
        def Restart3():
            global Nave_life, Flag, FlagA
            nonlocal FlagTemp
            if Nave_life<=0:
                Perdiste_L=Label(Nivel03,text="Game Over",font=("Comic Sans MS",15), width=10, height=2,bg="#1e0238",fg="white")
                Perdiste_L.place(x=240, y=200)
                FlagTemp= False
                Flag=False
                FlagA= False      
                Reintentar_L=Button(Nivel03, text='Reintentar',font=("Comic Sans MS",10),command=Reintentar, width=10, height=2,bg="#1e0238",fg="white")
                Reintentar_L.place(x=360, y=350)
                Volver= Button(Nivel03, text='Volver',font=("Comic Sans MS",10),command=closeP1, width=10, height=2,bg="#1e0238",fg="white")
                Volver.place(x=120, y=350)
            else:
                Canv_Pantalla3.after(100,Restart3)
                    
        Thread(target=Restart3).start()

        def Reintentar():
            global Score, Nave_life
            Score=0
            Nave_life=50
            Nivel03.destroy()
            Pantalla3()
            
        def Cerrar1():
            global Highscore
            nonlocal FlagTemp, VentanaJugar
            FlagTemp= False
            Nivel03.destroy()
            Highscore()

        def closeP1():
            nonlocal FlagTemp
            global Flag
            FlagTemp=False
            Flag=False
            nonlocal RUNNING
            RUNNING=False
            Nivel03.destroy()
            VentanaJugar.deiconify()
            
        Btn_VolverP1= Button(Nivel03, text='Cerrar Partida',font=("Comic Sans MS",10),command=closeP1, width=10, height=2,bg="#1e0238",fg="white")
        Btn_VolverP1.place(x=500, y=700)

        Nivel03.protocol("WM_DELETE_WINDOW", closeP1)


 #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    Nivel1 = Button(VentanaJugar, text='Nivel 1',font=("Comic Sans MS",10),command=Validar1, width=10, height=2,bg="#1e0238",fg="white")
    Nivel1.place(x=255, y=325)
    Nivel2 = Button(VentanaJugar, text='Nivel 2',font=("Comic Sans MS",10),command=Validar2, width=10, height=2,bg="#1e0238",fg="white")
    Nivel2.place(x=255, y=425)
    Nivel3 = Button(VentanaJugar, text='Nivel 3',font=("Comic Sans MS",10),command=Validar3, width=10, height=2,bg="#1e0238",fg="white")
    Nivel3.place(x=255, y=525)

    def Cerrar_juego():
         VentanaJugar.destroy()
         VentanaPrincipal.deiconify()
    btn_cerrarJ = Button(VentanaJugar, text='Volver',font=("Comic Sans MS",10),command=Cerrar_juego, width=12, height=1,bg="#1e0238",fg="white")
    btn_cerrarJ.place(x=430, y=680)  
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Btn_info = Button(VentanaPrincipal, text='About/info',font=("Comic Sans MS",10),command=About_Btn, width=10, height=2,bg="#1e0238",fg="white")
Btn_info.place(x=425, y=325)

Btn_Jugar = Button(VentanaPrincipal,text="Jugar",font=("Comic Sans MS",10),command=Jugar_Btn,width=10, height=2,bg="#1e0238",fg="white")
Btn_Jugar.place(x=85, y=325)

Btn_HS= Button(VentanaPrincipal,text="High Scores", font=("Comic Sans MS",10),command=Highscore,width=10, height=2,bg="#1e0238",fg="white")
Btn_HS.place(x=255, y=325)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
VentanaPrincipal.mainloop()