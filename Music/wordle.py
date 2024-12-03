import tkinter as tk
from tkinter import messagebox, simpledialog, PhotoImage
import random
import os

number_labels = []
img_frame = None
original_geometry = "1000x400"  # Tamaño original de la ventana

def limpiar_imagenes():
    global number_labels, img_frame
    # Limpiar imágenes
    if img_frame:
        for label in number_labels:
            label.config(image=None)  # Quitar la imagen de la etiqueta
            label.image = None  # Limpiar la referencia de la imagen
        number_labels = []  # Reiniciar la lista de etiquetas
        img_frame.destroy()  # Destruir el contenedor de imágenes para reiniciar

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def game1():
    global number_labels, img_frame
    
    # Limpiar imágenes previas antes de empezar
    limpiar_imagenes()

    # Ruta de las imágenes de los números
    ruta_imagenes = os.getcwd()  # Ajusta la ruta si es necesario
    number_images = [PhotoImage(file=os.path.join(ruta_imagenes, f"{i}.png")).subsample(3, 3) for i in range(10)]
    
    # Juego: Adivina el número mejorado con niveles de dificultad
    level = simpledialog.askstring("Nivel de dificultad", "Elige nivel: 1. fácil (100-150), 2. medio (100-200), 3. difícil (100-500)").lower()
    if level == "1":
        number = random.randint(100, 150)  # Rango ajustado para nivel fácil
        max_attempts = 7
    elif level == "2":
        number = random.randint(100, 200)  # Rango ajustado para nivel medio
        max_attempts = 8
    elif level == "3":
        number = random.randint(100, 500)  # Rango ajustado para nivel difícil
        max_attempts = 10
    else:
        messagebox.showinfo("Error", "Nivel no válido. Intenta de nuevo.")
        return
    
    attempts = 0
    guess = -1
    number_str = str(number)
    
    # Crear un contenedor para las imágenes de los números
    img_frame = tk.Frame(root)
    img_frame.pack(pady=20)

    # Crear los huecos para las imágenes de los números
    number_labels = [tk.Label(img_frame) for _ in range(len(number_str))]
    for i, label in enumerate(number_labels):
        label.grid(row=0, column=i, padx=10)

    # Redimensionar la ventana según el número de dígitos
    root.geometry(f"{200 + len(number_str)*50}x400")  # Ajustar el tamaño de la ventana

    while guess != number and attempts < max_attempts:
        guess = simpledialog.askinteger("Adivina el número", f"Adivina un número. Intento {attempts + 1}/{max_attempts}")
        attempts += 1

        if guess is None:
            break  # Salir si el usuario cancela la entrada

        guess_str = str(guess)

        # Validar si el número ingresado tiene el mismo número de dígitos
        if len(guess_str) < len(number_str):  # Si el número ingresado tiene menos dígitos
            messagebox.showinfo("Error", "El número ingresado tiene menos dígitos. Intenta de nuevo.")
            continue
        elif len(guess_str) > len(number_str):  # Si el número tiene más dígitos
            messagebox.showinfo("Error", "El número ingresado tiene más dígitos. Intenta de nuevo.")
            continue

        # Mostrar las imágenes de los números ingresados
        for i, digit in enumerate(guess_str):
            number_labels[i].config(image=number_images[int(digit)])
            number_labels[i].image = number_images[int(digit)]  # Guardar referencia

        # Verificar si el número ingresado es correcto
        if guess == number:
            messagebox.showinfo("Resultado", f"¡Correcto! Adivinaste el número en {attempts} intentos.")
            break
        elif guess < number:
            messagebox.showinfo("Pista", "El número es mayor. Intenta de nuevo.")
        else:
            messagebox.showinfo("Pista", "El número es menor. Intenta de nuevo.")
    
    if guess != number:
        messagebox.showinfo("Resultado", f"Se acabaron los intentos. El número era {number}.")
    
    # Limpiar las imágenes al final del juego
    limpiar_imagenes()

    # Restaurar el tamaño original de la ventana
    root.geometry(original_geometry)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def game2():
    # Ruta donde estarán las imágenes
    ruta_imagenes = os.getcwd()  # Directorio actual, ajusta si es necesario

    # Opciones del juego
    options = ["Piedra", "Papel", "Tijera"]
    score = {"Usuario": 0, "Computadora": 0}

    # Crear un marco para las imágenes (parte superior derecha)
    img_frame = tk.Frame(root)
    img_frame.place(relx=0.7, rely=0.1)

    user_img_label = tk.Label(img_frame, text="Tu elección:")
    user_img_label.grid(row=0, column=0, padx=5, pady=5)

    user_img_display = tk.Label(img_frame)
    user_img_display.grid(row=1, column=0, padx=5, pady=5)

    computer_img_label = tk.Label(img_frame, text="Computadora:")
    computer_img_label.grid(row=0, column=1, padx=5, pady=5)

    computer_img_display = tk.Label(img_frame)
    computer_img_display.grid(row=1, column=1, padx=5, pady=5)

    def actualizar_imagenes(user_choice, computer_choice):
        # Cargar imágenes y redimensionarlas
        user_img_path = os.path.join(ruta_imagenes, f"{user_choice.lower()}.png")
        computer_img_path = os.path.join(ruta_imagenes, f"{computer_choice.lower()}.png")

        user_img = PhotoImage(file=user_img_path).subsample(3, 3)  # Redimensionar (1/3 del tamaño original)
        computer_img = PhotoImage(file=computer_img_path).subsample(3, 3)

        # Actualizar etiquetas con las imágenes
        user_img_display.config(image=user_img)
        user_img_display.image = user_img  # Guardar referencia

        computer_img_display.config(image=computer_img)
        computer_img_display.image = computer_img  # Guardar referencia

    def limpiar_imagenes():
        # Quitar imágenes y textos
        user_img_display.config(image="")
        user_img_display.image = None
        computer_img_display.config(image="")
        computer_img_display.image = None
        user_img_label.config(text="")
        computer_img_label.config(text="")

    for _ in range(3):  # Mejor de 3
        user_choice = simpledialog.askstring("Piedra, Papel o Tijera", "Elige: Piedra, Papel o Tijera").capitalize()
        if user_choice not in options:
            messagebox.showinfo("Resultado", "Opción no válida. Intenta de nuevo.")
            continue

        computer_choice = random.choice(options)
        if user_choice == computer_choice:
            result = "Es un empate."
        elif (user_choice == "Piedra" and computer_choice == "Tijera") or \
             (user_choice == "Papel" and computer_choice == "Piedra") or \
             (user_choice == "Tijera" and computer_choice == "Papel"):
            result = "¡Ganaste esta ronda!"
            score["Usuario"] += 1
        else:
            result = "Perdiste esta ronda."
            score["Computadora"] += 1

        actualizar_imagenes(user_choice, computer_choice)
        messagebox.showinfo("Resultado", result)

    final_result = "Empate" if score["Usuario"] == score["Computadora"] else ("Ganaste" if score["Usuario"] > score["Computadora"] else "Perdiste")
    messagebox.showinfo("Resultado Final", f"Marcador final:\nUsuario: {score['Usuario']}\nComputadora: {score['Computadora']}\n{final_result}")

    # Limpiar las imágenes y textos
    limpiar_imagenes()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def game3():
    words = ["python", "programacion", "algoritmo", "interfaz", "tecnologia"]
    score = 0
    
    # Tres rondas
    for _ in range(3):
        word = random.choice(words)
        scrambled = ''.join(random.sample(word, len(word)))
        
        user_guess = simpledialog.askstring("Adivina la palabra", f"Ordena estas letras: {scrambled}")
        
        if user_guess and user_guess.lower() == word:
            messagebox.showinfo("Resultado", "¡Correcto! Has ordenado la palabra.")
            score += 1
        else:
            messagebox.showinfo("Resultado", f"Incorrecto. La palabra era {word}.")
    
    messagebox.showinfo("Resultado Final", f"Juego terminado. Puntuación final: {score}/3")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def mostrar_reglas():
    reglas = """
    Reglas del Juego:
    
    1. Juego 1: Adivina el número
       - Adivina un número secreto dentro de un rango.
       - Elige un nivel de dificultad: fácil, medio o difícil.
       - Nvl Facil 100-150, Nvl Medio 100-200, Nvl Dificl 100-500
       - Tendrás un número limitado de intentos.
       - Recibirás pistas para acercarte al número correcto.
       - Queda PROIBIDO poner 2 digitos (10-99) 

    2. Juego 2: Piedra, Papel o Tijera
       - Juega contra la computadora.
       - Elige entre Piedra, Papel o Tijera.
       - Gana quien consiga más puntos en 3 rondas.

    3. Juego 3: Trivia rápida
       - Responde preguntas de diferentes categorías.
       - Cada respuesta correcta te otorga un punto.
       - Intenta obtener la mayor puntuación.

    4. Juego 4: Adivina la palabra
       - Ordena correctamente las letras de una palabra revuelta.
       - Tendrás 3 rondas para adivinar las palabras.
       - Gana puntos por cada palabra correcta.
    """
    messagebox.showinfo("Reglas del Juego", reglas)

# Configuracion de la ventana principal
root = tk.Tk()
root.title("Juego de Adivinanza")
root.geometry("1000x400")  # ajustar tamaño de la ventana

# Estilo uniforme para los botones
button_style = {"bg": "blue", "fg": "white", "font": ("Arial", 12, "bold"), "width": 30}

# Botón para el juego "Adivina el número"
btn_game1 = tk.Button(root, text="Juego 1: Adivina el número", **button_style, command=game1)
btn_game1.pack(pady=10)

# Botón para el juego "Piedra, Papel o Tijera"
btn_game2 = tk.Button(root, text="Juego 2: Piedra, Papel o Tijera", **button_style, command=game2)
btn_game2.pack(pady=10)

# Botón para el juego "Trivia rápida"
btn_game3 = tk.Button(root, text="Juego 3: Trivia rápida", **button_style, command=game3)
btn_game3.pack(pady=10)

# Botón para las reglas
btn_reglas = tk.Button(root, text="Reglas del juego", **button_style, command=mostrar_reglas)
btn_reglas.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()