# 🔐 Doble Cifrado de Archivos con Fernet

Este proyecto permite **cifrar y descifrar archivos usando dos capas de cifrado Fernet**. Cada archivo tiene sus propias claves únicas generadas automáticamente, proporcionando una capa adicional de seguridad. Incluye una **interfaz gráfica intuitiva** con `tkinter` que facilita tanto el cifrado como el descifrado de múltiples archivos.

---

## 🛠️ Tecnologías Utilizadas

### 🧠 Backend y Lógica
- **Python 3.x**
- [cryptography](https://cryptography.io/en/latest/) → Implementación de cifrado Fernet (AES 128-bit en modo CBC).
- **tkinter** → Interfaz gráfica nativa para selección de archivos.
- **os / sys / filedialog / messagebox** → Manejo de archivos, carpetas y ventanas de diálogo.

---

## 📂 Estructura del Proyecto

```
cifrado_fernet/
├── encoded.py               # Script para cifrar archivos con doble capa
├── decoded.py               # Script para descifrar archivos con GUI
├── logs_encoded.txt         # Registro automático de archivos cifrados
├── keys/                    # Directorio de claves generadas
│   ├── capa1/              # Claves de la primera capa de cifrado
│   └── capa2/              # Claves de la segunda capa de cifrado
├── files_encoded/           # Archivos cifrados (extensión .encoded)
├── files_decoded/           # Archivos descifrados y restaurados
└── README.md                # Documentación del proyecto
```

> 📝 Las carpetas `keys/`, `files_encoded/` y `files_decoded/` se crean automáticamente al ejecutar los scripts.

---

## ⚙️ Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Linuxero18/cifrado_fernet.git
   cd cifrado_fernet
   ```

2. Instala la dependencia necesaria:
   ```bash
   pip install cryptography
   ```

   > ⚠️ `tkinter` ya viene instalado por defecto con Python en Windows y la mayoría de distribuciones Linux.

---

## 🚀 ¿Cómo Funciona?

### 🔒 **Cifrado de Archivos**

1. Ejecuta el script de cifrado:
   ```bash
   python encoded.py
   ```

2. Se abrirá una ventana donde deberás **seleccionar uno o más archivos** para cifrar.

3. El programa realizará las siguientes acciones:
   - Aplica **dos capas de cifrado Fernet** consecutivas.
   - Genera **dos claves únicas** por archivo y las almacena en:
     - `./keys/capa1/<nombre_archivo>.key`
     - `./keys/capa2/<nombre_archivo>.key`
   - Guarda el archivo cifrado en `./files_encoded/` con extensión `.encoded`
   - Registra la operación en `logs_encoded.txt` con fecha y hora.

### 🔓 **Descifrado de Archivos**

1. Ejecuta el script de descifrado:
   ```bash
   python decoded.py
   ```

2. Se abrirá una ventana donde deberás **seleccionar uno o varios archivos `.encoded`**.

3. Aparecerá una interfaz gráfica donde deberás:
   - Ingresar la **clave de capa 1** (primera clave).
   - Ingresar la **clave de capa 2** (segunda clave).
   - El sistema descifra en orden inverso: **capa2 → capa1**.

4. El archivo original se restaura en `./files_decoded/` con su extensión y nombre originales.

---

## ✅ Funcionalidades

- **Doble capa de cifrado** para mayor seguridad.
- **Claves únicas** por archivo (no se reutilizan).
- Interfaz gráfica amigable para usuarios no técnicos.
- Soporte para **múltiples archivos** en una sola operación.
- **Registro automático** de todas las operaciones de cifrado.
- Validación de extensiones `.encoded` antes de descifrar.
- **Manejo robusto de errores** con mensajes informativos.
- Restauración completa del nombre y extensión original del archivo.

---

## 🔐 Seguridad

- Las claves se generan usando `Fernet.generate_key()` (32 bytes aleatorios en base64).
- Cada archivo utiliza **claves únicas e irrepetibles**.
- Sin las claves correctas, los archivos cifrados **no pueden recuperarse**.
- El cifrado Fernet usa **AES 128-bit** en modo CBC con autenticación HMAC.
- Los archivos originales no se conservan tras el cifrado (elimínalos manualmente si lo deseas).

> ⚠️ **Importante**: Guarda las claves en un lugar seguro. Sin ellas, **no podrás recuperar tus archivos**.

---

## 📦 Producción y Uso Real

- Compatible con **Windows, Linux y macOS**.
- Ideal para cifrar documentos sensibles, contratos, información personal o respaldos.
- Puede adaptarse a proyectos más grandes con interfaces web o almacenamiento en la nube.
- Escalable para sistemas de gestión documental empresarial.

---

## 📜 Licencia

Este proyecto se distribuye bajo la licencia [MIT](./LICENSE).  
Eres libre de usarlo, modificarlo y distribuirlo siempre que mantengas el aviso de copyright.

---

## ✍️ Autor

**Piter Muñoz Pérez**  
📬 Desarrollador Python

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto:
1. Haz un fork del repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Haz commit de tus cambios (`git commit -m 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request
