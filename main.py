# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print ("Bienvenido a mi trivia sobre tecnología")
print ("Pondremos a prueba tus conocimientos")

# Agregaremos personalización para nuestros jugadores, preguntando y almacenando sus nombres en una variable

nombre = input("Ingresa tu nombre: ")

# Es importante dar instrucciones sobre cómo jugar:
# Ahora, lo personalizaremos con el nombre del jugador, diciéndole a print() que muestre el contenido de la variable "nombre". Cada cosa distinta que queremos que muestre en la pantalla, la separamos con comas
print("\n Hola", nombre, "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n")

# OJO, el \n al final de la línea 6 es para dar un "salto de línea"

# Pregunta 1
print ("1) ¿Cuál es el emoji más usado en el mundo?")
print ("a) El del beso")
print ("b) El de la sonrisa")
print ("c) El que llora")
print ("d) El de asco")

# Almacenamos la respuesta del usuario en la variable "respuesta_1"
respuesta_1 = input("\nTu respuesta: ")

while respuesta_1 not in ("a", "b", "c", "d"):
  respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: b")

# Pregunta 2
print("\n1) ¿Cuál es la red social más usada del mundo?")
print("a) Instagram")
print("b) Youtube")
print("c) Twitter")
print("d) Facebook")

# Almacenamos la rspuesta del usuario en la variable "respuesta_2"
respuesta_2 = input("\nTu respuesta: ")

while respuesta_2 not in ("a", "b", "c", "d"):
  respuesta_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

# Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
if respuesta_2 == "a":
  print("Incorrecto!", nombre)
elif respuesta_2 == "b":
  print("Incorrecto!", nombre)
elif respuesta_2 == "c":
  print("Incorrecto!", nombre,)
else:
  print("Muy bien", nombre, "!")

# Pregunta 3
print("\n1) ¿Quién inventó Google?")
print("a) Bill Gates")
print("b) Steve Jobs")
print("c) Steve wozniak")
print("d) Larry Page")

# Almacenamos la rspuesta del usuario en la variable "respuesta_3"
respuesta_3 = input("\nTu respuesta: ")

while respuesta_3 not in ("a", "b", "c", "d"):
  respuesta_3 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

# Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
if respuesta_3 == "a":
  print("Incorrecto!", nombre)
elif respuesta_3 == "b":
  print("Incorrecto!", nombre)
elif respuesta_3 == "c":
  print("Incorrecto!", nombre)
else:
  print("Muy bien", nombre, "!")
  
  # Pregunta 4
print("\n1) ¿Para qué sirve un hashtag?")
print("a) Para bloquear a una persona")
print("b) Para eliminar un contenido")
print("c) Es un servidor de publicidad online")
print("d) Para clasificar contenido en las redes sociales")

# Almacenamos la rspuesta del usuario en la variable "respuesta_4"
respuesta_4 = input("\nTu respuesta: ")

while respuesta_4 not in ("a", "b", "c", "d"):
  respuesta_4 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

# Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
if respuesta_4 == "a":
  print("Incorrecto!", nombre)
elif respuesta_4 == "b":
  print("Incorrecto!", nombre)
elif respuesta_4 == "c":
  print("Incorrecto!", nombre)
else:
  print("Muy bien", nombre, "!")