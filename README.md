# 2026-programacion-tp5
Repositorio educativo para la materia Programación con la finalidad de poner en práctica la teoría vista en clase.

---

## <i>Trabajo Práctico 5</i>

Teniendo en cuenta la teoría de colecciones vista en clase, se propone resolver los ejercicios trabajando con archivos `.py` dentro de la carpeta `src/`.

### Requisitos:
- Tener instalado Python 3.12 o superior.
- Tener instalado el IDLE de Python o un IDE como PyCharm, VSCode o similar.
- Tener instalado Git en su máquina local.
- Tener instalado Git Bash.
- Tener una cuenta en GitHub.
- Solicitar acceso de escritura al repositorio mediante su usuario.
- Trabajar dentro de la carpeta `/src` del repositorio clonado.

### Objetivos:
- Poner en práctica el manejo de colecciones.
- Aplicar modularización y reutilización de código mediante `funciones.py`.
- Trabajar bajo la metodología de **Pair Programming** (programación en parejas).
- Practicar el flujo colaborativo de ramas y Pull Requests directamente en GitHub.
- Escribir código según las convenciones de Python y programación estructurada.

---

### Metodología: Pair Programming y Formato de Ramas

Este trabajo práctico se desarrolla en **parejas** aplicando **Pair Programming**. Ambos integrantes deben colaborar en el diseño de las soluciones, la revisión de código y la integración continua.

#### Esquema de Ramas:
```text
main (rama base limpia del TP5 - NO se mergea hacia main)
 └── feature/pareja-apellido1-apellido2 (rama base compartida de la pareja)
      ├── feature/apellido1 (rama de trabajo del Alumno 1)
      └── feature/apellido2 (rama de trabajo del Alumno 2)
```

> [!IMPORTANT]
> **La rama `main` es únicamente la base inicial del proyecto.** Ninguna pareja debe realizar Pull Requests ni merges hacia `main`. Todo el trabajo de la pareja quedará consolidado en su rama `feature/pareja-apellido1-apellido2`.

---

### Paso a Paso para el Desarrollo:

#### 1. En GitHub
**Todas las ramas se crean inicialmente desde GitHub:**

1. **Creación de la rama base de la pareja:**
   - Uno de los integrantes va a GitHub y crea una rama desde `main` con el siguiente formato:
     `feature/pareja-<apellido1>-<apellido2>` (por ejemplo: `feature/pareja-perez-gomez`).

2. **Creación de las ramas individuales de cada alumno:**
   - Estando parados sobre la rama recién creada (`feature/pareja-<apellido1>-<apellido2>`), crean la rama de cada integrante:
     - Alumno 1: `feature/<apellido1>` (por ejemplo: `feature/perez` creada a partir de `feature/pareja-perez-gomez`).
     - Alumno 2: `feature/<apellido2>` (por ejemplo: `feature/gomez` creada a partir de `feature/pareja-perez-gomez`).

---

#### 2. En su máquina local (Clonado y Checkout)

1. Elegir la carpeta donde van a trabajar y abrir Git Bash.
2. Clonar el repositorio:
   ```bash
   git clone https://github.com/fborzi/2026-programacion-tp5.git
   ```
3. Ingresar a la carpeta del proyecto:
   ```bash
   cd 2026-programacion-tp5
   ```
4. Pasarse directamente a su rama de trabajo individual (ya creada en GitHub):
   - Alumno 1:
     ```bash
     git checkout feature/apellido1
     ```
   - Alumno 2:
     ```bash
     git checkout feature/apellido2
     ```
5. Abrir la carpeta del proyecto con su editor/IDE preferido (por ejemplo `code .` para VSCode).
6. Trabajar exclusivamente dentro de la carpeta `src/`.

---

#### 3. Modo de Trabajo con Git y Commits

A medida que resuelven los ejercicios asignados en su rama:

1. Guardar los cambios realizados en los archivos dentro de `src/ejercicios/`.
2. En Git Bash, verificar los archivos modificados:
   ```bash
   git status
   ```
3. Agregar los cambios al área de preparación:
   ```bash
   git add .
   ```
4. Crear un commit con un mensaje claro y descriptivo del ejercicio resuelto:
   ```bash
   git commit -m "Resuelve ejercicio 1501 y añade función auxiliar en funciones.py"
   ```
5. Subir los cambios a su rama individual en GitHub:
   ```bash
   git push origin feature/apellido1
   ```

---

#### 4. Pull Requests e Integración entre la Pareja (Pair Review)

Cuando un alumno termina una serie de ejercicios o una funcionalidad:

1. **Abrir Pull Request en GitHub:**
   - **Base (destino):** `feature/pareja-apellido1-apellido2`
   - **Compare (origen):** `feature/apellido1` (o `feature/apellido2`)
2. **Revisión automática de GitHub Actions:**
   - Se disparan las comprobaciones de **Pruebas Unitarias** y **Compliance**.
   - Ambos integrantes revisan el resumen *Summary* en la pestaña Actions o en el PR.
3. **Revisión entre pares (Code Review):**
   - El compañero de equipo revisa el código implementado, deja comentarios o sugerencias si es necesario.
   - Una vez que todas las pruebas y controles de estilo están en verde ✅, el compañero aprueba y realiza el **Merge pull request** hacia la rama de la pareja (`feature/pareja-apellido1-apellido2`).

---

### Formato de Entrega Final

Para dar por cumplida la entrega del TP5:
- Todos los ejercicios deben estar resueltos e integrados en la rama compartida de la pareja: `feature/pareja-apellido1-apellido2`.
- El último commit en la rama de la pareja debe tener todas las comprobaciones de **GitHub Actions** en verde (tanto pruebas unitarias como compliance).
- **Recuerden:** No se hace merge hacia `main`.

---

## Criterios de Evaluación:
- **Pruebas automáticas:** Funcionamiento correcto de los ejercicios verificado mediante Pytest en GitHub Actions.
- **Calidad de código y compliance:** Cumplimiento de convenciones, anotaciones de tipos completas y docstrings obligatorios sin comentarios sueltos entre líneas.
- **Estructura del código:** Programación estructurada estricta (variables $\rightarrow$ procesamiento $\rightarrow$ salidas) y sin uso de `while True`.
- **Trabajo colaborativo (Pair Programming):** Uso correcto del flujo de ramas desde GitHub, revisiones entre pares en los Pull Requests y mensajes de commit descriptivos.
