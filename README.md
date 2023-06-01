# ToDoApp

ToDoApp es una aplicación web simple y fácil de usar, diseñada para ayudar a los usuarios a mantenerse organizados y mejorar su productividad. La aplicación permite a los usuarios agregar, marcar y eliminar tareas pendientes en tiempo real, proporcionando una forma intuitiva de llevar un registro de las tareas pendientes.

## Características

- Interfaz de usuario sencilla y minimalista para una rápida adopción y facilidad de uso.
- Agregar tareas rápidamente con un solo clic.
- Marcar tareas como realizadas para llevar un seguimiento visual del progreso.
- Eliminar tareas de la lista cuando ya no sean necesarias.
- Desarrollado utilizando Flask, un micro-framework web de Python, lo que facilita su implementación y mantenimiento.

## Instalación y configuración

1. Clona este repositorio en tu máquina local.
2. Crea un entorno virtual de Python e instala las dependencias necesarias utilizando `pip install -r requirements.txt`.
3. Configura las variables de entorno `FLASK_APP` y `FLASK_ENV` según las instrucciones proporcionadas en la [documentación](https://flask.palletsprojects.com/en/2.1.x/config/#configuring-from-environment-variables) o [ChatGPT](https://chat.openai.com/share/c8662316-cd35-443c-a62d-88d43a4346b0).
4. Ejecuta `flask run` para iniciar la aplicación en modo de desarrollo.
5. Abre tu navegador y visita http://localhost:5000 para comenzar a usar la aplicación.

## Despliegue en PythonAnywhere

Para hacer un deploy de esta aplicación en [PythonAnywhere](https://www.pythonanywhere.com/), sigue los siguientes pasos:

1. Regístrate en [PythonAnywhere](https://www.pythonanywhere.com/) y crea una nueva cuenta o inicia sesión si ya tienes una.
2. Ve a la sección "Web" y crea una nueva aplicación web.
3. Elige "Flask" como el framework y selecciona la versión de Python que deseas utilizar.
4. En la pestaña "Code", haz clic en "Go to Directory" junto a "Source code" y carga los archivos de tu aplicación o clona el repositorio.
5. Asegúrate de que el archivo `requirements.txt` esté en el directorio raíz de tu aplicación y ejecuta `pip install -r requirements.txt` en la consola de PythonAnywhere para instalar las dependencias.
6. En la pestaña "Web", en la sección "Code", actualiza el campo "WSGI configuration file" con la ruta de tu archivo de configuración WSGI.
7. Reinicia tu aplicación web haciendo clic en el botón verde "Reload".

La aplicación ToDoApp ahora debería estar disponible en [https://juanmanuelroccia.pythonanywhere.com/](https://juanmanuelroccia.pythonanywhere.com/). Visita este enlace para comenzar a utilizar la aplicación.

## Contribuciones

Las contribuciones al proyecto son bienvenidas. Si deseas agregar nuevas características, mejorar el diseño o solucionar errores existentes, no dudes en enviar un pull request.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para obtener más detalles.
