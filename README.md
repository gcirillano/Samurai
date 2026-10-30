# Samurai Barber · Gestión

Herramienta de gestión para la barbería de Augusto Rospini: agenda del día, ficha automática de cliente, semana, caja e inventario. Cero fricción: todo sale de lo que se toca en la grilla.

## Probarla
Abrí `index.html` con doble clic. Es un solo archivo, sin internet ni instalación. Arranca vacío: los clientes, la caja y el stock se arman solos con lo que se carga. Los datos viven solo en el navegador de cada equipo; exportá a planilla (Caja) para llevarte una copia.

## Para desarrollar
`index.html` se arma concatenando las partes de `src/`. Editá ahí y corré `python src/build.py`, o editá `index.html` directo.

El JavaScript es ES5 a propósito, por la notebook con Windows 7 (Chrome 109 como máximo): sin flechas, plantillas, `?.`, `:has()` ni `color-mix`.

## Falta
- Probar en la notebook con Windows 7 y con touch real.
- Backend: las reservas online están simuladas (turnos con `origen: online`); el sistema de reservas tiene que insertarlas.
