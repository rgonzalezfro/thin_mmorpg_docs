---
id: TEC-004
title: "Arquitectura de simulacion Godot, backend Nakama y empaquetado"
category: Tech_Specs
status: draft
scope: Pre-Alpha
tags: [godot, headless, nakama, backend, packaging]
last_updated: 2026-08-13
source_brainstorm: "00_Brainstorming/tecnhical_2026-08-13.md"
dependencies: []
---

# Arquitectura de simulacion Godot, backend Nakama y empaquetado

## Estado

Documento de arquitectura exploratoria. La propuesta debe validarse mediante
prototipos antes de pasar a `approved` y autorizar implementacion en `client` o
`server`.

## Responsabilidades propuestas

### Godot headless

Godot ejecutado sin interfaz seria la autoridad de la simulacion realtime del
mundo, tanto en una partida local como en un servidor dedicado. Su alcance
propuesto incluye:

- Game loop, fisica, movimiento y colisiones.
- Personajes, NPCs, combate y proyectiles.
- Items, interacciones y estado del mundo.
- Reglas de juego, instancias y ciclo de spawn/despawn.

El cliente Godot visual no es autoridad sobre estos sistemas. Debe presentar el
estado recibido y enviar intenciones o entradas al proceso headless.

### Nakama

Nakama se evaluara exclusivamente como backend de servicios de juego, no como
servidor de la simulacion autoritativa. Sus responsabilidades candidatas son:

- Autenticacion, cuentas e identidad de jugadores.
- Amigos, grupos, chat, presencia y notificaciones.
- Persistencia o storage de datos que no requieran simulacion realtime.
- Leaderboards y achievements, si el producto los necesita.
- Coordinacion de sesiones o instancias cuando resulte apropiado.

Cada capacidad debe validarse por separado. No se asume que Nakama deba
gestionar todos los datos de una partida ni que sus servicios sustituyan el
guardado versionado del mundo.

## Empaquetado y ejecucion local

Es requisito que el servidor local pueda ejecutarse como proceso independiente,
en segundo plano u oculto, y que el juego pueda iniciarlo y cerrarlo de forma
controlada.

Se propone evaluar un ejecutable wrapper en Go que coordine el proceso local y,
si resulta viable, incluya una instancia de PostgreSQL embebida mediante
`embedded-postgres`. Esta propuesta no esta aprobada: deben comprobarse tamaño,
licencia, tiempos de arranque, actualizaciones, compatibilidad por plataforma,
ubicacion de datos, cierre limpio y recuperacion ante fallos.

El empaquetado no debe hacer que la logica de gameplay dependa de Go. Godot
headless mantiene la simulacion; Go solo podria coordinar procesos y servicios
auxiliares si el prototipo demuestra que es necesario.

## Integracion con TEC-003

Los modos de partida permanecen:

1. El cliente inicia Godot headless local para una partida solo o cooperativa.
2. Los invitados se conectan al proceso headless del host mediante la capa de
   transporte definida en [[TEC-003_Partidas_Privadas_Hosting_y_Migracion|TEC-003]].
3. Un servidor dedicado ejecuta la misma build headless y carga el mismo formato
   de partida.

La migracion local/dedicado requiere que la build headless y el formato de
guardado sean compatibles. Nakama puede prestar servicios de identidad o
persistencia auxiliar, pero no debe introducir una dependencia que impida
exportar y cargar una partida completa.

## Preguntas Pendientes para el Equipo

- ¿Godot headless puede ejecutar todas las escenas y sistemas requeridos sin
  dependencias de renderizado?
- ¿Que transporte usara Godot headless para clientes locales, relay y dedicado?
- ¿Nakama se ejecutara como servicio remoto, local o ambos durante desarrollo?
- ¿Que datos viven en el guardado portable de la partida y cuales en Nakama?
- ¿El wrapper Go es necesario frente a un launcher del cliente y scripts del
  sistema operativo?
- ¿La dependencia `embedded-postgres` es compatible con las plataformas y
  licencias objetivo?
- ¿Como se distribuyen, actualizan y verifican las builds headless?
- ¿Como se detecta que el proceso headless termino o quedo bloqueado?

## Fuente

[[../00_Brainstorming/tecnhical_2026-08-13|Brainstorming tecnico 2026-08-13]].
