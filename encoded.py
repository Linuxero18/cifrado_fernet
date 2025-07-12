import os
from tkinter import Tk, filedialog
from cryptography.fernet import Fernet

Tk().withdraw()
files = filedialog.askopenfilenames(
    title="Seleccione los archivos que deseas cifrar")

os.makedirs("./keys", exist_ok=True)
os.makedirs("./keys/capa1", exist_ok=True)
os.makedirs("./keys/capa2", exist_ok=True)
os.makedirs("./files_encoded", exist_ok=True)

def nombre_unico(ruta_padre):
    carpeta_padre = os.path.basename(os.path.dirname(ruta_padre))
    archivo_sin_ext = os.path.splitext(os.path.basename(ruta_padre))[0]
    archivo_ext = os.path.splitext(ruta_padre)[1][1:]
    return f"{carpeta_padre}_{archivo_sin_ext}_{archivo_ext}".replace(" ", "_")


for ruta in files:
    name_file = nombre_unico(ruta)

    key_capa1 = Fernet.generate_key()
    fernet1 = Fernet(key_capa1)

    key_capa2 = Fernet.generate_key()
    fernet2 = Fernet(key_capa2)

    with open(ruta, 'rb') as f:
        file = f.read()

    first_encryption = fernet1.encrypt(file)
    second_encryption = fernet2.encrypt(first_encryption)

    with open(f'./files_encoded/{name_file}.encoded', 'wb') as f:
        f.write(second_encryption)

    with open(f'./keys/capa1/{name_file}.key', 'wb') as keys:
        keys.write(key_capa1)

    with open(f'./keys/capa2/{name_file}.key', 'wb') as keys:
        keys.write(key_capa2)

    with open(f'./logs_encoded.txt', 'a', encoding='utf-8') as logs:
        logs.write(str(f"✅ Cifrado doble completado para el archivo: {name_file}  -->  ruta_origen: {os.path.dirname(ruta)}\n"))
           
    print(f"✅ Cifrado doble completado para el archivo: {name_file}  -->  ruta_origen: {os.path.dirname(ruta)}")