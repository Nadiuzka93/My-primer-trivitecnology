import random  # Importamos la librería random

# Para implementar puntajes, crearemos una nueva variable llamada "puntaje", la que inicializamos en 0.
puntaje = random.randint(0, 10)

# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print("\033[31mBienvenido a mi trivia sobre tecnologia\033[39m")
print("Pondremos a prueba tus conocimientos")
print("\033[32mTienes", puntaje, "puntos\033[39m")

# Agregaremos personalización para nuestros jugadores, preguntando y almacenando sus nombres en una variable

nombre = input("\033[35mIngresa tu nombre: \033[39m")

# Es importante dar instrucciones sobre cómo jugar:
# Ahora, lo personalizaremos con el nombre del jugador, diciéndole a print() que muestre el contenido de la variable "nombre". Cada cosa distinta que queremos que muestre en la pantalla, la separamos con comas
print(
    "\n Hola", nombre,
    "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n"
)

# OJO, el \n al final de la línea 6 es para dar un "salto de línea"

# Pregunta 1
print("\n1) ¿Cuál es el emoji más usado en el mundo?")
print("a) El del beso")
print("b) El de la sonrisa")
print("c) El que llora")
print("d) El de asco")

# Almacenamos la respuesta del usuario en la variable "respuesta_1"
respuesta_1 = input("\nTu respuesta: ")

while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input(
        "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

# Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
if respuesta_1 == "b":
    puntaje += 10
    print("Muy bien", nombre, "!")
else:
    print("Incorrecto", nombre, "!")

print(nombre, "llevas", puntaje, "puntos")

# Pregunta 2
print("\n2) ¿Cuál es la red social más usada del mundo?")
print("a) Instagram")
print("b) Youtube")
print("c) Twitter")
print("d) Facebook")

# Almacenamos la respuesta del usuario en la variable "respuesta_2"
respuesta_2 = input("\nTu respuesta: ")

while respuesta_2 not in ("a", "b", "c", "d"):
    respuesta_2 = input(
        "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

# Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
if respuesta_2 == "a":
    print("Incorrecto!", nombre, "Python es un lenguaje de alto nivel")
elif respuesta_2 == "b":
    print("Incorrecto!", nombre, "Java es un lenguaje de alto nivel")
elif respuesta_2 == "c":
    print("Incorrecto!", nombre, "PHP es un lenguaje de alto nivel")
else:
    puntaje += 10
    print("Muy bien", nombre, "!")

print(nombre, "llevas", puntaje, "puntos")

# Pregunta 3
print("\n1) ¿Quién inventó Google?")
print("a) Bill Gates")
print("b) Steve Jobs")
print("c) Steve wozniak")
print("d) Larry Page")

# Almacenamos la respuesta del usuario en la variable "respuesta_3"
respuesta_3 = input("\nTu respuesta: ")

while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input(
        "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

if respuesta_3 == "a":
    print("Totalmente incorrecto! ...")
    puntaje = puntaje / 2
elif respuesta_3 == "d":
    print("...")
    puntaje = puntaje + 5
elif respuesta_3 == "c":
    print("Incorrecto! ...")
    puntaje = puntaje - 5
else:
    print("Correcto! ...")
    puntaje = puntaje * 2

print("Gracias", nombre, "por jugar mi trivia, alcanzaste", puntaje, "puntos")
