# BloGastro - Leandro Montesoro

- [BloGastro - Leandro Montesoro](#blogastro---leandro-montesoro)
    - [**El blog se compone de las siguientes App's**](#el-blog-se-compone-de-las-siguientes-apps)
    - [**URL's relevantes para la navegacion:**](#urls-relevantes-para-la-navegacion)
    - [**Rúbricas**](#rúbricas)
    - [**Rúbricas navegacion**](#rúbricas-navegacion)
    - [**Credenciales \& Usuarios de prueba**](#credenciales--usuarios-de-prueba)


***

Trabajé de manera individual en la creacion de un blog referido a la gastronomía. Utilicé Django y python.

***

### **El blog se compone de las siguientes App's**

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

### **URL's relevantes para la navegacion:**
* inicio/: Home del blog
* signup/: Formulario para registración
* login/: Formulario para Login
* editProfile/: Edición del perfil del usuario logueado. Se puede utilizar directamente o bien clickeando el username o avatar (margen sup derecho) se accede.
* editUser/: Edición de datos del usuario.
* editPassword/: Edicion de password
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

### **Rúbricas**
* *Contar con algún acceso visible a la vista de "Acerca de mí" donde se contará acerca de los dueños de la página manejada en el route about/.* :  Se accede desde la url /about
* *Contar con algún acceso visible a la vista de blogs que debe alojarse en el route pages/:* Desde el home de la web se pueden visualizar todas las entradas
* *Acceder a una pantalla que contendrá las páginas. Al clickear en “Leer más” debe navegar al detalle de la page mediante un route pages/<pageId>*: Clickeando en la imagen o en el titulo de una entrada se puede acceder al detalle de la misma, o bien con la url editEntrada/<id>
* *Para crear, editar o borrar las fotos debes estar registrado como Administrador.*: Solo el ADM o el dueño de la entrada puede editar una entrada / imagen. Existen validaciones utilizando la funcion is_superuser()
* *Cada blog, es decir cada model Blog debe tener como mínimo, un título, subtítulo, cuerpo, autor, fecha y una imagen (mínimo y obligatorio, puede tener más).*: Se encuentra en el models.py, llamado "Entrada" de la AppMain.

### **Rúbricas navegacion**
* *Login:* Para las acciones de edicion, agregar entradas o borrar se implementó el @login_required.
* *Visualizar el home del blog.*: Desde la url "/"
* *Poder listar todas las páginas del blog, poder ver en detalle cada una, poder crear, editar o borrar páginas del blog*: 
  1. Se listan en el home **"/"**
  2. Se editan desde **editEntrada/<id>** (solo el usuario dueño o admin)
  3. Se crean desde **agregarEntrada/**
  4. Se borran desde **homeDeleteEntradas/** (solo el usuario dueño o admin)

* *Las páginas están formadas por un título, un contenido en editor de texto avanzado (ckeditor por ejemplo), una imagen, fecha de posteo de la imagen.*: Desde agregarEntrada/ se puede apreciar este punto o bien desde el home "/" o detalle de la entrada
* *Tener una app de registro donde se puedan registrar usuarios en el route accounts/signup, un usuario está compuesto por: email - contraseña - nombre de usuario*: La AppsignUp se encarga de este punto, accediendo desde **signup/**
* *Tener una app de login en el route accounts/login/ la cual permite loggearse con los datos de administrador o de usuario normal.*: La AppLogin se encarga de esto, accediendo desde **login/**
* *Tener una app de perfiles en el route accounts/profile/ la cual muestra la info de nuestro usuario y permite poder modificar y/o borrar: imagen - nombre - descripción -  un link a una página web - email y contraseña*:
  1. editUser/
  2. editProfile/
* *Contar con un admin en route admin/ donde se puedan manejar las apps y los datos en las apps.*
   * User: admin
   * Pass: admin

* *Tener una app de mensajería en el route messages/ para que los perfiles se puedan contactar entre sí.*: En la AppMensajeria está desarrollada esta funcionalidad. Accediendo a **chat/homeMensajes**


### **Credenciales & Usuarios de prueba**

* Administrador
  1. User: admin
  2. Pass: admin

* Usuarios
  1. User: Usuario1
  2. Pass: #coderhouse
  3. User: Usuario2
  4. Pass: #coderhouse
