import os
import sys
from tkinter import filedialog, ttk, messagebox
import tkinter as tk
from cryptography.fernet import Fernet

files_encoded = filedialog.askopenfilenames(title="Selecciona el archivo a descifrar")

if not files_encoded:
    sys.exit(0)

archivos_validos = [ruta for ruta in files_encoded if ruta.endswith(".encoded")]

if not archivos_validos:
    messagebox.showwarning("Advertencia", "Selecciona archivos .encoded válidos.")
    sys.exit(0)

# Variables globales para manejar el progreso
archivo_actual_index = 0
archivos_descifrados = []
window = None
archivo_actual_var = None
progreso_var = None
clave1_entry = None
clave2_entry = None

def procesar_siguiente_archivo():
    global archivo_actual_index
    
    if archivo_actual_index >= len(archivos_validos):
        # Todos los archivos procesados
        mostrar_resumen_final()
        return
    
    # Actualizar la interfaz para el archivo actual
    actualizar_interfaz()

def mostrar_resumen_final():
    global window
    
    exitosos = len([x for x in archivos_descifrados if x['exito']])
    total = len(archivos_validos)
    
    mensaje = f"✅ Proceso completado!\n"
    mensaje += f"Archivos descifrados exitosamente: {exitosos}/{total}\n\n"
    
    for resultado in archivos_descifrados:
        estado = "✅" if resultado['exito'] else "❌"
        mensaje += f"{estado} {resultado['nombre']}\n"
    
    messagebox.showinfo("Proceso Completado", mensaje)
    if window:
        window.destroy()

def actualizar_interfaz():
    global archivo_actual_var, progreso_var
    
    # Actualizar información de progreso
    progreso_var.set(f"Archivo {archivo_actual_index + 1} de {len(archivos_validos)}")
    
    # Actualizar archivo actual
    nombre_actual = os.path.basename(archivos_validos[archivo_actual_index])
    archivo_actual_var.set(f"Archivo actual: {nombre_actual}")
    
    # Limpiar campos de claves
    clave1_entry.delete(0, tk.END)
    clave2_entry.delete(0, tk.END)
    
    # Actualizar lista de archivos con estados
    actualizar_lista_archivos()
    
    # Enfocar en el primer campo
    clave2_entry.focus()

def actualizar_lista_archivos():
    # Limpiar frame de archivos
    for widget in archivos_frame.winfo_children():
        widget.destroy()
    
    for i, archivo in enumerate(archivos_validos):
        nombre = os.path.basename(archivo)
        if i == archivo_actual_index:
            estado = "→ ACTUAL"
            color = "blue"
        elif i < archivo_actual_index:
            if i < len(archivos_descifrados):
                resultado = archivos_descifrados[i]
                estado = "✅ COMPLETADO" if resultado['exito'] else "❌ ERROR"
                color = "green" if resultado['exito'] else "red"
            else:
                estado = "⏳ PENDIENTE"
                color = "gray"
        else:
            estado = "⏳ PENDIENTE"
            color = "gray"
        
        label = tk.Label(archivos_frame, text=f"{estado}: {nombre}", 
                        fg=color, anchor='w')
        label.pack(fill='x', padx=10, pady=2)

def usar_claves():
    global archivo_actual_index
    
    key2 = clave2_entry.get().strip()
    key1 = clave1_entry.get().strip()
    
    if not key1 or not key2:
        messagebox.showwarning("Campos vacíos", "Debes ingresar ambas claves.")
        return
    
    try:
        # Convertir las claves a bytes si no lo están ya
        if isinstance(key2, str):
            key2 = key2.encode()
        if isinstance(key1, str):
            key1 = key1.encode()
        
        fernet2 = Fernet(key2)
        fernet1 = Fernet(key1)
        
        # Descifrar el archivo actual
        ruta_actual = archivos_validos[archivo_actual_index]
        nombre_archivo = os.path.basename(ruta_actual)
        
        exito = descifrar_archivo(ruta_actual, fernet1, fernet2)
        
        # Guardar resultado
        archivos_descifrados.append({
            'nombre': nombre_archivo,
            'exito': exito
        })
        
        if exito:
            messagebox.showinfo("Éxito", f"✅ {nombre_archivo} descifrado correctamente.")
        else:
            messagebox.showerror("Error", f"❌ Error al descifrar {nombre_archivo}")
        
        # Pasar al siguiente archivo
        archivo_actual_index += 1
        
        # Procesar siguiente archivo
        procesar_siguiente_archivo()
        
    except Exception as e:
        messagebox.showerror("Error", f"❌ Clave inválida: {e}")

def descifrar_archivo(ruta, fernet1, fernet2):
    try:
        os.makedirs('./files_decoded', exist_ok=True)
        
        with open(ruta, 'rb') as f:
            file = f.read()
        
        # Descifrado en orden inverso: primero capa 2, luego capa 1
        first_decryption = fernet2.decrypt(file)
        second_decryption = fernet1.decrypt(first_decryption)
        
        # Obtener el nombre base sin la extensión .encoded
        nombre_base = os.path.basename(ruta).replace(".encoded", "")
        
        # Extraer la extensión original del archivo
        if "_" in nombre_base:
            partes = nombre_base.rsplit("_", 1)
            if len(partes) == 2:
                nombre_sin_ext = partes[0]
                extension = partes[1]
                name_file = f"{nombre_sin_ext}.{extension}"
            else:
                name_file = nombre_base
        else:
            name_file = nombre_base
        
        # Escribir el archivo descifrado
        ruta_salida = f'./files_decoded/{name_file}'
        with open(ruta_salida, 'wb') as f:
            f.write(second_decryption)
        
        print(f"✅ Archivo restaurado correctamente: {ruta_salida}")
        return True
        
    except Exception as e:
        print(f"❌ Error al descifrar {os.path.basename(ruta)}: {e}")
        return False

def cancelar():
    global window
    if window:
        window.destroy()
    sys.exit(0)

# Crear la ventana principal UNA SOLA VEZ
window = tk.Tk()
window.title("Descifrar archivos - Claves individuales")
window.geometry("600x450")

window.lift()
window.attributes('-topmost', True)
window.after_idle(window.attributes, '-topmost', False)

# Información de progreso
progreso_var = tk.StringVar()
ttk.Label(window, textvariable=progreso_var, font=('Arial', 12, 'bold')).pack(pady=(10, 5))

# Archivo actual
archivo_actual_var = tk.StringVar()
ttk.Label(window, textvariable=archivo_actual_var, wraplength=500, justify="center", 
          font=('Arial', 10)).pack(pady=(5, 15))

# Lista de todos los archivos
archivos_frame = ttk.LabelFrame(window, text="Archivos seleccionados:")
archivos_frame.pack(pady=(0, 15), padx=20, fill='x')

# Campos de claves
ttk.Label(window, text="Clave capa 2:", font=('Arial', 10, 'bold')).pack(pady=(15, 5))
clave2_entry = ttk.Entry(window, width=60, font=('Arial', 10))
clave2_entry.pack(pady=(0, 10))

ttk.Label(window, text="Clave capa 1:", font=('Arial', 10, 'bold')).pack(pady=(0, 5))
clave1_entry = ttk.Entry(window, width=60, font=('Arial', 10))
clave1_entry.pack(pady=(0, 15))

# Botones
frame_botones = ttk.Frame(window)
frame_botones.pack(pady=10)

ttk.Button(frame_botones, text="Descifrar este archivo", 
           command=usar_claves).grid(row=0, column=0, padx=10)
ttk.Button(frame_botones, text="Cancelar todo", 
           command=cancelar).grid(row=0, column=1, padx=10)

# Permitir Enter para continuar
window.bind('<Return>', lambda event: usar_claves())

# Protocolo para cerrar ventana
window.protocol("WM_DELETE_WINDOW", cancelar)

# Inicializar la interfaz con el primer archivo
procesar_siguiente_archivo()

# Iniciar el loop principal
window.mainloop()