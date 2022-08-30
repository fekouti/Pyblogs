# Pyblogs
***

Este proyecto web fue desarrollado por **Fernando Luna** para la comisión 31090 del curso de Python en CoderHouse.

Video en **YouTube**: https://youtu.be/_G0U6Zx4OWY

Link a **PythonAnywhere**: https://fernandoluna.pythonanywhere.com/

## Requerimientos
***
+ Python 3.9
+ Django 4.0.6
+ Pillow 9.2.0
+ django-crispy-forms 1.14.0
+ typing_extensions 4.3.0

## Notas
***
Cada persona puede registrarse y se le generará un usuario y un perfil, del mismo solo pueden editar la imagen y la biografía, y borrar su cuenta si así lo desean.

Cada usuario tiene el poder de crear un post en el blog, y solo el mismo autor o un administrador del sitio podrán editar o borrar dicho post.


En el inicio se visualiza un posteo destacado y los últimos 5 posts publicados. Los administradores pueden ingresar al panel de administración y desde allí modificar que post va a ser el destacado con una casilla de verificación, cabe destacar que al marcar un post como 'is_featured = *True*' todos los demás automáticamente pasarán a tener un valor *False*.

El cuadro de Newsletter ubicado a la derecha de cada detalle de posteo es meramente decorativo, por lo que el botón de acción esta deshabilitado. 


### Changelog
***
#### [v1.0.0]

+ Index
+ About
+ Todos los blogs
+ Perfil
+ Crear Usuario y Perfil
+ Editar Perfil
+ Eliminar Usuario
+ Crear Post
+ Editar Post
+ Eliminar Post
+ Leer Post (detalle)
+ Registro, Inicio de sesión y Cierre de sesión
+ Búsqueda 

+ En cada Perfil se visualizan los Posts realizados por ese Usuario



#### [v1.0.1]

+ Creación de Tags para los posts
+ Visualización de todos los posts con la etiqueta seleccionada
+ Creación de sistema de Likes (Dislike si el post ya está likeado)
+ Corregidos los errores mostrados si el usuario o email ya existen
+ Corregidos los errores mostrados si el usuario o contraseña son incorrectos al iniciar la sesión
+ Limpieza de código
