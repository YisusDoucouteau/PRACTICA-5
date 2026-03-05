                PRACTICA NUMERO 5

Al intentar iniciar sesión en el sistema y acceder al panel de administración se producía un error relacionado con la autenticación de usuarios.

El sistema intentaba consultar la tabla user , pero esta no existia por lo que primero se tenia que realizar las migraciones correspondientes para la base de datos 
----------------------------------
Implementación de Flask-Migrate
Se integró Flask-Migrate para gestionar los cambios en la base de datos utilizando migraciones.
Esto permite:
Crear tablas automáticamente
Actualizar la estructura de la base de datos
Mantener control de cambios en el esquema
Comandos utilizados:
flask db init
flask db migrate
flask db upgrade
de esta manera el flask login lograba ingresar 
--------------------------------------
Se implementó Flask-Admin para crear un panel de administración que permite gestionar los datos de la aplicación de manera sencilla.
Dentro del panel se pueden administrar:
Usuarios
Productos
El panel se encuentra disponible en la ruta:
/admin
Además se protegió el acceso al panel para que solo los usuarios con rol administrador puedan ingresar porque generalmente en un framework deberia ser de esta manera 
------------------------------------------------------------------
Mejoras adicionales que realice para completar de mejor manera la tarea 
Mejora de la interfaz para navegar y el usuario 
Se añadieron estilos personalizados en styles.css para mejorar la apariencia del sistema.
Traducción parcial al español
Algunos elementos del panel administrativo fueron adaptados al español para que sea más fácil de usar.

Seguridad del panel admin

Se configuró Flask-Login para restringir el acceso al panel solo a usuarios autenticados con rol admin.

Mejor navegación para el backend especialmente para el panel 

Se agregaron opciones dentro del panel administrativo como:

Volver al inicio

Cerrar sesión

bueno eso seria todo inge lo realice antes de hacer mi viaje a santa cruz asi que espero que le agrade tenga buena noche 🙌

PD: para ingresar el usuario suele ser admin y la contraseña 1234