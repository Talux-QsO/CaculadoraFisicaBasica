from tabulate import tabulate
import fisicas
print('******Bienvenido*******')

teoria=[['MRU',1],['MRUV',2]]
elecion=int(input(tabulate(teoria,headers=["Teorias","Opciones"])+"\n"))

if elecion==1:
    formunlas=[["Distacia","d=v*t",1],["Tiempo","t=d/v",2],["Velocidad","v=d/v",3]]
    usoFormulas=int(input(tabulate(formunlas,headers=["Resulado","Formula","Opcion"])+"\n"))
    
    if usoFormulas==1:
        fisicas.distacia()
        
    elif usoFormulas==2:
        fisicas.tiempo()
        
    elif usoFormulas==3:
        fisicas.velocidad()
        
elif elecion==2:
    formunlas=[["Velosidad Final","Distancia","Vf=Vo+at",1],["Distacia","Aceleracion","d=(Vf+Vo)/2*t",2],["Distancia","Velosidad Final","d=Vo*t+at**2/2",3],["Velosidad Final","Tiempo","Vf**2=Vo**2+2ad",4],["Acelecarion","","a=(Vf-Vo)/(tf-to)",5]]
    usoFormulas=int(input(tabulate(formunlas,headers=["Resulado","Sin","Formula","Opcion"])+"\n"))
    if usoFormulas==1:
        fisicas.sinDitacia()
        pass
    elif usoFormulas==2:
        fisicas.sinAceleracion()
        pass
    elif usoFormulas==3:
        fisicas.sinVelocidadFinal()
        pass
    elif usoFormulas==4:
        fisicas.sinTiempo()
        pass
    elif usoFormulas==5:
        fisicas.aceleracion()
        pass
else:
    print("Falta")
    pass
print("****Final*****")
    

   