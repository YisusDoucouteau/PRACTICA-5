PRACTICA NÚMERO 5

Aplicación de Pastelería con Flask

Problema inicial

Al intentar iniciar sesión en el sistema y acceder al panel de administración se producía un error relacionado con la autenticación de usuarios.

El sistema intentaba consultar la tabla user, pero esta tabla no existía en la base de datos.
Esto ocurría porque no se habían ejecutado las migraciones necesarias para crear las tablas definidas en los modelos.

Solución: Integración de Flask-Migrate

Para solucionar el problema se integró Flask-Migrate, que permite gestionar los cambios en la base de datos mediante migraciones.

Esto permite:

Crear las tablas automáticamente a partir de los modelos de SQLAlchemy

Actualizar la estructura de la base de datos

Mantener control de cambios en el esquema de la base de datos

Comandos utilizados:

flask db init
flask db migrate
flask db upgrade

Después de ejecutar las migraciones, las tablas se crearon correctamente y Flask-Login pudo autenticar usuarios sin problemas.

Implementación del Panel de Administración

También se integró Flask-Admin para crear un panel de administración que permite gestionar los datos de la aplicación.

Desde el panel se pueden administrar:

Usuarios

Productos

Ruta del panel administrativo:

/admin

Además, el acceso al panel está protegido para que solo usuarios con rol administrador puedan ingresar, utilizando Flask-Login.

Mejoras adicionales

Para mejorar el sistema también se realizaron algunas mejoras adicionales:

Mejora de la interfaz con estilos personalizados en styles.css

Traducción parcial del panel administrativo al español

Protección del panel admin usando Flask-Login

Mejora de la navegación agregando opciones como:

Volver al inicio

Cerrar sesión

Acceso al sistema

Usuario de prueba:

usuario: admin
contraseña: 1234
Nota

Realicé esta práctica antes de mi viaje a santa cruz, por lo que espero que el resultado sea de su agrado hasta la siguiente clase 🙌