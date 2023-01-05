# BloGastro - Issue

Se genera un error de integridad en la BD al actualizar por segunda vez el usuario. Detecté que el error lo tira en la linea 63 de proyecto_final\AppProfile\views.py cuando hace el .save() de la info, y en base a post's que fui leyendo es como si quisiese volver a generar un usuario que ya existe y pincha, creo que la mano viene que por la PK del model User.

Para repoducir el issue seguir los siguientes pasos:
* Darse de alta desde el boton SignUp (Margen sup derecho)
* Con el alta dada, el login se hace automaticamente.
* Ingresar desde la URL a http://127.0.0.1:8000/editUser/
* Cargar los datos y aceptar el formulario
* Volver a ingresar a http://127.0.0.1:8000/editUser/ e intentar cargar datos distintos. Aceptar el form y allí ocurre el error


