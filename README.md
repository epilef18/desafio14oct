# Desafío - Mostrando contenido dinámico en Django

Este proyecto es parte de un desafío de Django que consiste en crear una aplicación web que muestre una lista dinámica de empleados. Los nombres de los empleados están almacenados en una lista de Python y se pasan al template HTML mediante contexto para ser mostrados en la web.

## Requisitos

- Python 3.12
- Django 5.1.2
  
## Estructura del Proyecto

desafioevaluado14oct/
├── manage.py                    # Script de gestion del proyecto
├── desafioevaluado14oct/        # Carpeta del proyecto principal
│   ├── urls.py                  # Aplicacion que define rutas
│   ├── views.py                 # Aplicacion con logica de vistas
│   ├── settings.py              # Script para configurar la app
└── templates/
    ├── empleados.html           # Plantilla html que muestra lista de empleados
    
# Documentación del proyecto

## Uso

1. Realiza las migraciones (opcional en este desafío):

    ```bash
    python manage.py migrate
    ```

2. Ejecuta el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

3. Accede a la aplicación:

    Abre tu navegador y visita `http://127.0.0.1:8000/empleados/` para ver la lista de empleados.
