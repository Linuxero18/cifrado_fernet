🔐 Doble Cifrado de Archivos - Proyecto Personal

Este proyecto permite **cifrar y descifrar archivos usando dos capas de cifrado Fernet**. Está diseñado para que cada archivo tenga sus claves únicas, con una interfaz gráfica que permite descifrar múltiples archivos de forma intuitiva y segura.

---

🛠️ Tecnologías Utilizadas

🧠 Backend y Lógica
- Python 3.x
- Librería `cryptography` (Fernet)
- Módulo `tkinter` (interfaz gráfica nativa)
- Módulo `os`, `sys`, `filedialog`, `messagebox` (control de archivos y GUI)

📂 Estructura del Proyecto

```
cifrado_fernet/
├── encoded.py             # Script para cifrado doble con interfaz de selección
├── decoded.py             # Script para descifrar múltiples archivos con GUI
├── logs_encoded.txt       # Registro automático de los archivos cifrados
│
├── keys/                  # Claves Fernet generadas
│   ├── capa1/             # Claves de la primera capa
│   └── capa2/             # Claves de la segunda capa
│
├── files_encoded/         # Archivos cifrados con doble capa (extensión .encoded)
├── files_decoded/         # Archivos descifrados y restaurados
```

---

⚙️ Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/Linuxero18/cifrado_fernet.git
cd cifrado_fernet
```

2. Instala las dependencias necesarias:

```bash
pip install cryptography
```

> Nota: `tkinter` viene incluido por defecto con Python en Windows y la mayoría de sistemas Linux.

---

🚀 ¿Cómo Funciona?

🔒 Cifrado

- Ejecuta `main.py`
- Selecciona uno o más archivos
- Se aplican **dos capas de cifrado Fernet**
- Se generan dos claves distintas por archivo y se almacenan:
  - `./keys/capa1/<nombre>.key`
  - `./keys/capa2/<nombre>.key`
- Los archivos cifrados se guardan en `./files_encoded/` con extensión `.encoded`
- Se registra en `logs_encoded.txt` cada operación realizada

🔓 Descifrado

- Ejecuta `decoded.py`
- Selecciona uno o varios archivos `.encoded`
- Se abre una GUI donde debes ingresar **clave1 y clave2** por cada archivo
- El archivo se descifra en orden inverso (capa2 → capa1)
- El archivo original se restaura en `./files_decoded/` con su extensión original

---

✅ Funcionalidades

- Interfaz gráfica amigable (TKinter)
- Validación de archivos seleccionados
- Permite múltiples archivos en lote
- Verificación de extensiones `.encoded`
- Gestión visual del progreso
- Manejo robusto de errores
- Registro detallado de cada archivo cifrado

---

🔐 Seguridad

- Las claves se generan con `Fernet.generate_key()` (clave aleatoria de 32 bytes en base64).
- Cada archivo usa **claves únicas**, lo que impide que una clave se reutilice.
- No se almacenan archivos originales tras el cifrado.
- Sin claves correctas, los archivos cifrados no pueden recuperarse.

---

📦 Producción

Este sistema es local, portátil y puede adaptarse fácilmente a proyectos más grandes con interfaces web o almacenamiento en la nube.

---

📜 Licencia

Este proyecto es libre para uso educativo y personal. Puedes copiarlo, modificarlo o adaptarlo.

---

✍️ Autor

**Piter Muñoz Pérez**  
📬 Desarrollador Python | Apasionado por la seguridad y automatización de procesos
