<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT Licencia][Licencia-shield]][Licencia-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/FreddyPinto/crud-cli-app-python-mongodb">
    <img src="images\live-import.png" alt="Logo" width="80" height="80">
    
  </a>

<h3 align="center">CRUD CLI app con MongoDB y Python</h3>

  <p align="center">
    Aplicación CRUD simple de interfaz de línea de comandos para la gestión de usuarios utilizando Python y MongoDB Atlas.
    <br />
    <a href="https://github.com/FreddyPinto/crud-cli-app-python-mongodb"><strong>Explorar docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/FreddyPinto/crud-cli-app-python-mongodb/issues">Reportar Bug</a>
    ·
    <a href="https://github.com/FreddyPinto/crud-cli-app-python-mongodb/issues">Request Feature</a>
  </p>
</div>



<!-- Tabla de contenido -->
<details>
  <summary>Tabla de contenido</summary>
  <ol>
    <li>
      <a href="#acerca-del-proyecto">Acerca del Proyecto</a>
      <ul>
        <li><a href="#desarrollado-con">Desarrollado con:</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerrequisitos">Prerrequisitos</a></li>
        <li><a href="#instalación">Instalación</a></li>
      </ul>
    </li>
    <li><a href="#uso">Uso</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contribuciones">Contribuciones</a></li>
    <li><a href="#licencia">Licencia</a></li>
    <li><a href="#contacto">Contacto</a></li>
    <li><a href="#agradecimientos">Agradecimientos</a></li>
  </ol>
</details>



<!-- Acerca del Proyecto -->
## Acerca del Proyecto

<p align="center">
  <img src="images\screenshot.jpg" alt="screenshot"/>
</p>

Este proyecto consiste en crear una aplicación CRUD simple de interfaz de línea de comandos utilizando Python y MongoDB Atlas para el programa Talento Cloud Pro de NEXA y AWS.

El objetivo de este proyecto es poner en práctica todo lo aprendido sobre cómo crear un cluster y una base de datos en MongoDB Atlas, cómo crear una conexión, cómo crear, consultar, actualizar y eliminar un usuario (CRUD), cómo trabajar con documentos anidados, funciones y triggers.

El resultado es una pequeña aplicación en Python que permite gestionar usuarios, con las siguientes funcionalidades:

* Crear un usuario
* Consultar un usuario
* Eliminar un usuario
* Actualizar un usuario

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>



### Desarrollado con:

* [![Python][Python]][Python-url]
* [![MongoDB][MongoDB]][MongoDB-url]
* [![VSCode][VSCode]][VSC-url]


<p align="right">(<a href="#readme-top">volver arriba</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Para ejecutar este proyecto localmente, necesitas tener instalado Python 3.9 o superior, así como una cuenta en MongoDB Atlas. Sigue estos pasos para configurar el proyecto:

### Prerrequisitos

* Instala Python 3.9 o superior en tu sistema operativo. Puedes descargarlo desde https://www.python.org/downloads/

* Crea una cuenta en MongoDB Atlas siguiendo las instrucciones de https://www.mongodb.com/cloud/atlas/register

* Crea un cluster gratuito en MongoDB Atlas siguiendo las instrucciones de https://docs.atlas.mongodb.com/tutorial/create-new-cluster/

* Crea una base de datos llamada “anycompany” y una colección llamada “users” en tu cluster siguiendo las instrucciones de https://docs.atlas.mongodb.com/data-explorer/manage-data/

* Crea un usuario con permisos de lectura y escritura para tu base de datos siguiendo las instrucciones de https://docs.atlas.mongodb.com/security-add-mongodb-users/

* Obtén la cadena de conexión a tu cluster siguiendo las instrucciones de https://docs.atlas.mongodb.com/connect-to-cluster/#connect-to-a-cluster


### Instalación

1. Clona el repositorio:
   ```sh
   git clone https://github.com/FreddyPinto/crud-cli-app-python-mongodb.git
   ```
2. Crea un entorno virtual de Python:
    ```sh
    python -m venv env
    ```
3. Activa el entorno virtual: 
    - En Windows:
      ```sh
      .\env\Scripts\activate
      ```
    - Unix o MacOS:
      ```sh
      env/bin/activate
      ```
4. Instala las dependencias:
   ```sh
   pip install -r requirements.txt
   ```
5. Configura las variables de entorno:
    * Abre el archivo [config.py](./project/config.py)
    * Reemplaza la variable `url` con la cadena de conexión a tu cluster.
    * Asigna tu passsword a la varibale de entorno `MONGODB_PASSWORD`
6. Ejecuta la aplicación:
    ```sh
    python main.py
    ```
<p align="right">(<a href="#readme-top">volver arriba</a>)</p>



<!-- USAGE EXAMPLES -->
## Uso

La aplicación te mostrará un menú con las siguientes opciones:

    A) Crear usuario
    B) Consultar usuario
    C) Eliminar usuario
    D) Actualizar usuario

Para seleccionar una opción, ingresa la letra correspondiente y presiona Enter.

- Si seleccionas la **opción A**, la aplicación te pedirá que ingreses los datos del usuario que quieres crear: nombre, edad, email y dirección (*opcional*). Luego, la aplicación insertará el usuario en la colección “users” de tu base de datos.

- Si seleccionas la **opción B**, la aplicación te pedirá que ingreses el nombre del usuario que quieres buscar te mostrará sus datos.

- Si seleccionas la **opción C**, la aplicación te pedirá que ingreses el nombre del usuario y lo eliminará de la base de datos.

- Si seleccionas la **opción D**, la aplicación te pedirá que ingreses el nombre del usuario que quieres modificar. Luego, te pedirá que ingreses los nuevos datos: nombre, edad, email y dirección. Finalmente, la aplicación actualizará el usuario en la base de datos.

Escribe **"q"** o **"quit"** para terminar la ejecución de la aplicación.


<p align="right">(<a href="#readme-top">volver arriba</a>)</p>



<!-- ROADMAP -->
## Roadmap
Estas son algunas de las mejoras que se podrían implementar en el futuro:

- [ ] Añadir validaciones de entrada para evitar errores
- [ ] Añadir una interfaz gráfica de usuario (GUI) para mejorar la experiencia de usuario
- [ ] Añadir más opciones de búsqueda y filtrado
- [ ] Añadir más opciones de reporte y gráficos
- [ ] Añadir una funcionalidad para exportar e importar los datos de los usuarios


Consulta los [issues abiertos](https://github.com/FreddyPinto/crud-cli-app-python-mongodb/issues) para proponer características (y problemas conocidos).


<p align="right">(<a href="#readme-top">volver arriba</a>)</p>



<!-- CONTRIBUTING -->
## Contribuciones

Las contribuciones son lo que hacen que la comunidad de código abierto sea un lugar increíble para aprender, inspirarse y crear. Cualquier contribución que hagas será **muy apreciada**.

Si tienes una sugerencia para mejorar este proyecto, haz un fork del repositorio y crea un pull request. También puedes simplemente abrir un issue con la etiqueta *“enhancement”*. ¡No olvides darle una estrella al proyecto! Gracias de nuevo.

1. Haz un fork del Proyecto
2. Crea tu feature Branch (`git checkout -b feature/AmazingFeature`)
3. Haz commit de tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la Branch (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>



<!-- Licencia -->
## Licencia

Distribuido bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más información.
<p align="right">(<a href="#readme-top">volver arriba</a>)</p>



<!-- Contacto -->
## Contacto

Freddy Pinto - freddypinto@outlook.com 

[![LinkedIn][linkedin-shield]][linkedin-url]

Project Link: [https://github.com/FreddyPinto/crud-cli-app-python-mongodb](https://github.com/FreddyPinto/crud-cli-app-python-mongodb)

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Agradecimientos
Quiero agradecer a las siguientes personas y recursos que me han ayudado a realizar este proyecto:

* [NEXA](https://www.nexaresources.com/) y [AWS](https://aws.amazon.com/) por ofrecer el programa Talento Cloud Pro.
* [UBITS](https://www.ubits.com/) y [Código Facilito](https://codigofacilito.com/) por impartir el módulo de NoSQL con MongoDB y Python.

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/FreddyPinto/crud-cli-app-python-mongodb.svg?style=for-the-badge
[contributors-url]: https://github.com/FreddyPinto/crud-cli-app-python-mongodb/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/FreddyPinto/crud-cli-app-python-mongodb.svg?style=for-the-badge
[forks-url]: https://github.com/FreddyPinto/crud-cli-app-python-mongodb/network/members
[stars-shield]: https://img.shields.io/github/stars/FreddyPinto/crud-cli-app-python-mongodb.svg?style=for-the-badge
[stars-url]: https://github.com/FreddyPinto/crud-cli-app-python-mongodb/stargazers
[issues-shield]: https://img.shields.io/github/issues/FreddyPinto/crud-cli-app-python-mongodb.svg?style=for-the-badge
[issues-url]: https://github.com/FreddyPinto/crud-cli-app-python-mongodb/issues
[Licencia-shield]: https://img.shields.io/github/license/FreddyPinto/crud-cli-app-python-mongodb.svg?style=for-the-badge
[Licencia-url]: https://github.com/FreddyPinto/crud-cli-app-python-mongodb/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/FreddyPinto-/
[product-screenshot]: images/screenshot.jpg
[Python]: https://img.shields.io/badge/Python-306998?logo=python&labelColor=white
[Python-url]: https://www.python.org/
[MongoDB]: https://img.shields.io/badge/MongoDB-mongodb?logo=mongodb&labelColor=white
[MongoDB-url]: https://www.mongodb.com/atlas
[VSCode]: https://img.shields.io/badge/VSCode-blue?logo=VisualStudioCode&logoColor=blue&labelColor=white
[VSC-url]: https://code.visualstudio.com/
 
