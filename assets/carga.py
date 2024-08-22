import tkinter as tk
from PIL import Image, ImageTk


def show_loading_screen():
    # Crear la ventana
    root = tk.Tk()
    root.title("Pantalla de Carga")

    # Cargar la imagen
    image = Image.open("images.png")  # Reemplaza con la ruta de tu imagen
    photo = ImageTk.PhotoImage(image)

    # Crear un widget Label para mostrar la imagen
    label = tk.Label(root, image=photo)
    label.pack()

    # Configurar el tamaño de la ventana según la imagen
    root.geometry(f"{image.width}x{image.height}")

    # Mostrar la ventana durante unos segundos
    root.after(3000, root.destroy)  # 3000 ms = 3 segundos

    # Iniciar el bucle de eventos de tkinter
    root.mainloop()


# Configuración de la aplicación
if __name__ == '__main__':
    # Llamar a la función para mostrar la pantalla de carga
    show_loading_screen()
