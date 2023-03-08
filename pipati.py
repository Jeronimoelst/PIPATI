import random


class PiedraPapelTijera():


    def __init__(self):
        pass


    def jugar(self):
        contador_tiradas= 0
        while contador_tiradas < 3:

            usuario = input("Elije cualquiera de las opciones para jugar, si es tijera pon (Ti), si es piedra elije (Pi) y si es papel elije (Pa). \n").lower()
            computadora = random.choice(["Ti","Pi","Pa"])
            contador_tiradas+= 1
            resultado = self.calcular_resultado(usuario.lower(), computadora.lower())
            print(resultado)
        else:    
            print( self.sumar_resultado(0, 1))
            return "listo!! se acabaron los tiros"
            

    def calcular_resultado(self,jugador,oponente):
        

        if jugador == oponente:
            #le suma uno a cada uno
            self.sumar_resultado(1, 1)
            return "Empate"
        if((jugador == 'Pi' and oponente == 'Ti') or (jugador =='Ti' and oponente =='Pa') or (jugador == 'Pa' and oponente == 'Pi')):
            #le suma al jugador
            self.sumar_resultado(1, 0)
            return "Compu sacò "+ oponente + " Ganaste!!!"
        else:
            #le suma a la compu
            self.sumar_resultado(0, 1)
            return "Compu sacò "+ oponente + " Perdiste :("

       #agregar codigo acà
        return "Jugador: " + str(contador_jugador) + ";  " +"Computadora: " + str(contador_Compu)

piedraPapelTijera =PiedraPapelTijera()

print(piedraPapelTijera.jugar())