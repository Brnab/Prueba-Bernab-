class Player :   #creacion de jugador
    
    def __init__(self, nombre):
       self.nombre=nombre
    
    def Change_name(self,Newname): #funcion para modificar el nombre
        self.nombre=Newname
        return self.nombre

    Score=0



#class Pista :
    #  def __init__ (self,n):
        #  pista=[5000,10000,12000]
        #  KP= (pista[n]) # converir el valor de la pista entero
         #  return KP
         #



class Jugar():  #definicion de la funcion jugar
    def __init__(self,NL,KP,n):
        Num=NL
        Kil=KP
        NC=n

    

    def Play(Num,NL,KP):
        print("el numero de jugadores es " +str(Num) )
        for i in range(Num):
         print("El jugador " +(NL[i])+ " en el carril " +str((i+1)))
        print("La pista elegida tiene una distancia de " + str(KP/1000)+ "KM")















Namelist=[] #arreglo de nombres de los jugadores
print("ingrse el numero de jugadores ")
n=int(input())

for i in range(n):
    NA=""
    print("ingrese el nombre del jugador " +str(i+1))
    Name=input ()
    NA=Player(Name)
    Namelist.append(NA)
    NA=NA.Change_name(Name) 
    Namelist.append(NA)  #funcion para agregar el nombre deseado

for i in range(n):
    print(Namelist[i])



for i in range(n+2):
  
    Name="Player "+ str(i+1)
    NA=Player(Name)
    NA=NA.Change_name(Name) 
    Namelist.append(NA)  #funcion para agregar el nombre deseado



for i in range(n+2):
    print(Namelist[i])


Nump=len(Namelist)


b=Jugar
b.Play(Nump,Namelist,10000)

   



