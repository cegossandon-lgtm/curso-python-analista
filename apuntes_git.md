# Apunte de Comandos Git — Referencia Rápida

Guía de todos los comandos Git usados en el curso, organizados por categoría, con comentarios de para qué sirve cada uno.

---

## 1. Configuración inicial (solo se hace una vez por computador)

```bash
git config --global user.name "Carlos Guzmán"
# Registra tu nombre, para que quede como "autor" en cada commit que hagas.

git config --global user.email "tu_correo@ejemplo.com"
# Registra tu correo (idealmente el mismo de tu cuenta de GitHub), asociado a cada commit.

git config --global user.name
git config --global user.email
# Sin ningún valor después: consultan qué quedó guardado actualmente (para verificar).

git --version
# Confirma que Git está instalado y accesible desde la terminal.
```

---

## 2. Iniciar un repositorio nuevo

```bash
git init
# Convierte la carpeta actual en un repositorio Git, creando una carpeta oculta .git
# donde se guarda todo el historial. Se ejecuta UNA sola vez, al empezar un proyecto nuevo.
```

---

## 3. Proteger archivos sensibles (ANTES del primer add)

```bash
# Se crea un archivo .gitignore (sin extensión, empieza con punto) en la raíz del proyecto,
# con una línea por cada archivo o patrón que NO quieres subir a GitHub. Ejemplo de contenido:

.env
__pycache__/
*.pyc
```

**Por qué "antes":** una vez que un archivo (como `.env` con contraseñas) queda en un commit,
queda para siempre en el historial, aunque lo borres después. Por eso el `.gitignore` se
crea y configura ANTES de hacer el primer `git add`.

---

## 4. El flujo básico del día a día (los 3 comandos que más vas a usar)

```bash
git status
# Muestra qué archivos cambiaste, cuáles están "preparados" (staged) y cuáles no.
# Se puede ejecutar en cualquier momento, cuantas veces quieras, no modifica nada.

git add .
# Prepara TODOS los archivos modificados/nuevos de la carpeta actual y subcarpetas,
# dejándolos listos para el próximo commit (el punto significa "todo").

git add nombre_archivo.py
# Igual que el anterior, pero solo prepara un archivo específico (más selectivo).

git commit -m "Descripción breve de qué cambió y por qué"
# Guarda un "punto de guardado" permanente en el historial, con todos los archivos
# que estaban preparados (staged). El -m permite escribir el mensaje en la misma línea.

git push
# Sube los commits guardados localmente hacia GitHub (el repositorio remoto),
# para que queden disponibles en internet.
```

**Flujo típico completo:**
```bash
git add .
git commit -m "Mensaje describiendo el cambio"
git push
```

---

## 5. Conectar tu repositorio local con GitHub (solo se hace una vez por proyecto)

```bash
git remote add origin https://github.com/usuario/nombre-repo.git
# Vincula tu repositorio local con la dirección del repositorio en GitHub,
# usando "origin" como nombre estándar para referirse a él.

git remote -v
# Muestra las URLs remotas conectadas (fetch y push), para confirmar que quedó bien vinculado.

git push -u origin master
# Sube tus commits por primera vez, y además "recuerda" la conexión
# (de ahí en adelante basta con escribir "git push", sin repetir origin/master).
```

---

## 6. Cambiar la URL remota (por ejemplo, si cambias tu nombre de usuario de GitHub)

```bash
git remote set-url origin https://github.com/nuevo-usuario/nombre-repo.git
# Actualiza la dirección remota guardada, sin perder el historial ni la conexión.

git remote -v
# Vuelve a confirmar que la nueva URL quedó registrada correctamente.
```

---

## 7. Descargar un repositorio existente (`git clone`)

```bash
git clone https://github.com/usuario/nombre-repo.git
# Descarga una copia COMPLETA de un repositorio (con todo su historial de commits)
# desde GitHub hacia tu computador. Crea automáticamente una carpeta con el nombre
# del repositorio, ya conectada a "origin" (no hace falta volver a hacer git remote add).
```

**¿Cuándo se usa?**
- Cuando empiezas a trabajar en un computador nuevo y quieres traer un proyecto que ya existe en GitHub.
- Cuando quieres tener una copia de un proyecto de otra persona (por ejemplo, para revisarlo o aportar cambios).
- A diferencia de `git init` (que crea un repositorio nuevo desde cero, vacío), `git clone` trae uno que **ya existe**, completo, listo para usar.

**Importante:** GitHub solo guarda y muestra el código — no lo ejecuta. Para correr un script de Python que está en GitHub, siempre hay que traerlo primero a un lugar con Python instalado (tu computador, un servidor, etc.), normalmente con `git clone`.

---

## Resumen visual: los 3 "estados" de Git

```
Directorio de trabajo  --git add-->  Área de preparación  --git commit-->  Historial (local)  --git push-->  GitHub (remoto)
   (editas archivos)                    (staging area)                    (commits guardados)                (en internet)
```

---

## Notas rápidas para no olvidar

- `git status` no hace daño nunca — úsalo cada vez que tengas dudas de en qué estado está todo.
- Un commit debería representar **un cambio con un propósito claro**, no una mezcla de cosas sin relación.
- El `.gitignore` se configura **antes** de subir nada sensible, nunca después.
- Si expones una contraseña por error en un commit ya subido, lo más seguro es **cambiar esa contraseña**, no solo borrar el archivo.
- `git push` sin nada más (sin `-u origin master`) solo funciona después de haber hecho esa conexión inicial una vez.
- `git clone` es para TRAER un repositorio que ya existe; `git init` es para CREAR uno nuevo desde cero.
