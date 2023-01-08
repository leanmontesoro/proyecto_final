# BloGastro - Leandro Montesoro

Trabajé de manera individual en la creacion de un blog referido a la gastronomía. Utilicé Django y python.

***

**El blog se compone de las siguientes App's:**

- **AppLogin:** Aquí se desarrolló el modulo de login.
- **AppMain:** Aquí se encuentra el html padre del cual heredan los templates de toda la aplicación "padre.html". Se mantiene la navbar con el avatar, el logout, y la posibilidad de acceder a la edición del perfil desde un hypervinculo sobre el avatar/nombre de usuario. Además se respeta el footer que también queda estatico. Además se encuentran distintas funcionalidades:
  1. About me
  2. Agregar entrada al blog
  3. Eliminar entrada
  4. Explorar entrada
  5. Home de la app

- **AppMensajeria:** Es la App encargada de la mensajeria. Permite enviar, recibir y leer los mensajes enviados.
- **AppProfile:** Esta app permite editar datos del usuario, como también su perfil *donde podemos subir un avatar y asociarlo al usuario*.
- **AppsignUp:** App para el registro de usuario.

 
***

**URL's relevantes para la navegacion:**
* inicio/: Home del blog
* signup/: Formulario para registración
* login/: Formulario para Login
* editProfile/: Edición del perfil del usuario logueado. Se puede utilizar directamente o bien clickeando el username o avatar (margen sup derecho) se accede.
* enviarMensaje/: Formulario para envio de mensaje
* editEntrada/<id>: Utilizado para editar una entrada
* agregarEntrada/: Formulario para agregar una entrada al blog
* detailEntrada/<id>: Utilizado para seleccionar la entrada a mostrar en detalle
* homeDeleteEntradas/: Formulario para listar las entradas a eliminar por el usuario. **Filtra las entradas propias.**
* deleteEntradas/<id>: Utilizado para eliminar la entrada con el id indicado.
* homeEditEntradas/: Listado de entradas disponibles para editar. **Solamente lista las entradas cuyo autor sea el user logeado**
* about/: Info sobre el creado de la web.
* chat/homeMensajes: Home de la mensajeria.

***
