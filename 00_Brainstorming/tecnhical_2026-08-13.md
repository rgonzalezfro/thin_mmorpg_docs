La arquitectura del proyecto utilizará: 
- **Godot** como servidor autoritativo del gameplay (headless para servidor dedicado). 
- **Nakama** exclusivamente como backend de servicios de juego. 
- El problema de hosting público, NAT traversal y relay se resolverá en una etapa posterior. 
- No se utilizará Nakama Authoritative Multiplayer para ejecutar la simulación del juego. 
- El objetivo es no reescribir logica en el cliente que se pueda resolver con un servicio de nakama
- Es requisito que el servidor se pueda empaquetar en un solo ejecutable y correr en segundo plano u oculto durante el juego
- ---
## 1. Principio fundamental
Godot es el motor utilizado para desarrollar el juego y, por lo tanto, también será responsable de ejecutar la simulación autoritativa del mundo.  
### Godot Headless será responsable de: 
- Game loop 
- Física 
- Movimiento 
- Colisiones 
- Personajes 
- NPCs 
- Combate 
- Proyectiles 
- Items 
- Interacciones 
- Estado del mundo 
- Reglas del juego 
- Instancias de gameplay 
- Spawn/despawn 
- Cualquier estado que requiera simulación realtime 
El cliente Godot no será la autoridad sobre estos sistemas. 
# 2. Rol de Nakama Nakama será utilizado como **backend**, no como game server
Todas las responsabilidades que se puedan gestionar con servicios o capacidades de nakama se haran con esa logica y de ser necesario se extenderán en el server como:
- Autenticación  
- Accounts 
- Identidad de jugadores 
- Friends 
- Groups
- Chat 
- Presence 
- Notifications 
- Persistencia / Storage 
- Leaderboards
- Achievements 
- Coordinación de sesiones/instancias cuando sea apropiado 
- Otros servicios backend que Nakama proporcione y sean útiles para el proyecto

Sujeto a revision de factibilidad

La regla principal es:

> **Nakama administra servicios persistentes/sociales; Godot administra el mundo y su simulación.**

## Creacion de ejecutable 
### La Solución Óptima: Wrapper Go con `embedded-postgres`

La arquitectura más limpia y mantenible consiste en crear un binario en Go que utilice la librería `embedded-postgres`. Esta librería incluye un binario compacto de PostgreSQL dentro del mismo ejecutable de Go mediante la directiva `go:embed`.
Luego el ejecutable se iniciara desde godot como proceso en segundo plano y se cerrara al salir del juego o volver al menu principal
