# CRUD para EGO - Documentación del proyecto

Mis datos:
Emiliano Di Campli.

- Teléfono: +3516814194
- Localidad: Buenos Aires, Argentina
- GitHub: [malhee](https://github.com/malhee)
- LinkedIn: [Emiliano Di Campli](https://www.linkedin.com/in/emiliano-di-campli-848a57235/)

Este proyecto implementa un CRUD (Create, Read, Update, Delete) para administrar autos utilizando Django y Django REST Framework.

## Rutas de API

- **GET /api/cars/**: Obtiene todos los autos disponibles.
- **GET /api/cars/{id}/**: Obtiene los detalles de un auto específico.
- **POST /api/cars/**: Crea un nuevo auto.
- **PUT /api/cars/{id}/**: Actualiza los detalles de un auto existente.
- **DELETE /api/cars/{id}/**: Elimina un auto existente.
- **GET /api/cars/sorted/asc/**: Obtiene los autos ordenados por precio de menor a mayor.
- **GET /api/cars/sorted/desc/**: Obtiene los autos ordenados por precio de mayor a menor.

## Acceso al Administrador de Django

El proyecto también proporciona un panel de administración para gestionar los datos de los autos. Para acceder al administrador de Django, sigue estos pasos:

1. Ejecuta el servidor de desarrollo de Django con el comando `python manage.py runserver`.
2. Abre un navegador web y visita `http://localhost:8000/admin/`.
3. Ingresa tus credenciales de superusuario para acceder al panel de administración.

## Funciones del CRUD

El CRUD para los autos incluye las siguientes funciones:

- **Listar autos**: La ruta GET `/api/cars/` devuelve una lista de todos los autos disponibles.
- **Obtener detalles de un auto**: La ruta GET `/api/cars/{id}/` devuelve los detalles de un auto específico.
- **Crear un nuevo auto**: La ruta POST `/api/cars/` permite crear un nuevo auto proporcionando los datos requeridos en el cuerpo de la solicitud.
- **Actualizar un auto**: La ruta PUT `/api/cars/{id}/` permite actualizar los detalles de un auto existente.
- **Eliminar un auto**: La ruta DELETE `/api/cars/{id}/` permite eliminar un auto existente.

## Funcionalidad de las Descripciones

- Agregar descripciones adicionales a cada carro, como ficha de presentación, características, etc.
- Visualizar y administrar las descripciones asociadas a cada carro en el panel de administración de Django.
- Las descripciones se muestran junto con los detalles del carro en la API RESTful.

### Agregar una Descripción a un Carro

1. Accede al panel de administración de Django en tu navegador.

2. Selecciona el carro al que deseas agregar una descripción.

3. En la sección de descripciones, haz clic en el botón "Agregar otro" para añadir una nueva descripción.

4. Ingresa el texto de la descripción en el campo proporcionado y guarda los cambios.

### Visualizar las Descripciones de un Carro

Para ver las descripciones asociadas a un carro, puedes utilizar tanto el panel de administración como la API RESTful.

- Panel de Administración:

  - Accede al panel de administración de Django en tu navegador.
  - Selecciona el carro para el cual deseas ver las descripciones.
  - En la sección de descripciones, encontrarás una lista con todas las descripciones asociadas a ese carro.

- API RESTful:
  - Realiza una solicitud GET al endpoint correspondiente para obtener los detalles de un carro específico.
  - En la respuesta JSON, encontrarás un campo llamado "descriptions" que contiene una lista con todas las descripciones asociadas a ese carro.

## Requisitos del proyecto

- Python 3.x
- Django
- Django REST Framework

## Configuración y ejecución

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias necesarias ejecutando `pip install -r requirements.txt`.
3. Aplica las migraciones con el comando `python manage.py migrate`.
4. Crea un superusuario con el comando `python manage.py createsuperuser`. (o usar admin,admin)
5. Inicia el servidor de desarrollo de Django con `python manage.py runserver`.
