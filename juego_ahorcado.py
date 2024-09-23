import random

def obtenerpalabra():
   palabras = ["zanahoria","farmaco","persona","ciudad","hospital","escuela"]
   palabra_secreta = random.choice(palabras)
   return palabra_secreta

def progreso(palabra_secreta,letras_acertadas):
   adivinado = ""

   for letra in palabra_secreta:
      if letra in letras_acertadas:
         adivinado += letra
      else:
         adivinado += "_"

   return adivinado
   
def juego_ahorcado():
   palabra_secreta= obtenerpalabra()
   letras_acertadas =[]
   intentos = 7
   ganado = False
   
   print(f"¡Adivina la palabra en menos de {intentos} intentos")      
   
   while not ganado and intentos > 0:
      print(progreso(palabra_secreta,letras_acertadas))
      
      letra= input("Ingresa una letra: ").lower()
      if len(letra) < 2 and letra.isalpha():  
         if letra not in palabra_secreta:
            intentos -=1
            print(f"¡Te has equivocado! Te quedan '{intentos}' intentos")
            
         elif letra in letras_acertadas:
            print("Ya has escrito esta letra, prueba otra vez")
            
         else:
            letras_acertadas.append(letra)
            print("Has acertado la letra ")
      else:
         print("El valor ingresado no es valido")
      adivinado = progreso(palabra_secreta,letras_acertadas)
      if "_" not in adivinado:
         print(f"¡Felicidades adivinaste la palabra en menos de '{intentos}' intentos!")
         ganado = True

   if intentos == 0:
      print(f"¡Has perdido! La palabra es: ¡{palabra_secreta}!")

juego_ahorcado()