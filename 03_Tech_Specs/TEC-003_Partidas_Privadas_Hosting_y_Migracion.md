---
id: TEC-003
title: "Partidas privadas, hosting y migracion de mundos"
category: Tech_Specs
status: draft
scope: Pre-Alpha
tags: [sessions, hosting, coop, dedicated-server, migration]
last_updated: 2026-08-13
source_brainstorm: "Conversacion de arquitectura 2026-08-13; 00_Brainstorming/tecnhical_2026-08-13.md"
dependencies: [TEC-004]
---

# Partidas privadas, hosting y migracion de mundos

## Estado

Documento de arquitectura exploratoria. Registra decisiones de alcance del
equipo y preguntas tecnicas pendientes; no autoriza implementacion hasta pasar
a `approved`.

## Modelo de partida

- La unidad principal de juego es una partida privada aislada, no un mundo MMO
  global.
- El mundo pertenece al host que crea la partida.
- Los personajes pertenecen exclusivamente a una partida y no se comparten
  entre mundos.
- La partida puede jugarse en solitario o con invitados.
- El host debe mantener la partida abierta para que los invitados puedan jugar.
- Como alternativa, el host puede iniciar la misma partida en un servidor
  dedicado.

## Modos de ejecucion

El cliente debe usar el mismo protocolo y las mismas reglas autoritativas en
estos modos:

1. **Host local**: el cliente inicia un proceso Godot headless local y se
   conecta a el.
2. **Host cooperativo**: otros clientes se conectan al proceso Godot headless
   del host local.
3. **Servidor dedicado**: el mismo proceso Godot headless se ejecuta sin
   cliente en una maquina externa y carga la partida del host.

El proceso headless debe permanecer separado del cliente visual. Godot no debe
duplicar la simulacion autoritativa dentro del cliente para soportar el modo
solo. La separacion concreta entre ejecutable headless, wrapper y servicios de
backend queda descrita en [[TEC-004_Arquitectura_Godot_Nakama_y_Empaquetado|TEC-004]].

## Guardado y migracion

Una partida local debe poder detenerse, copiarse y cargarse en un servidor
dedicado. El flujo inverso tambien debe ser posible: el host puede descargar o
recuperar el guardado y continuar la partida localmente.

La migracion requiere como minimo:

- Un formato de guardado versionado e independiente de rutas locales.
- Identidad estable de la partida y de sus personajes.
- Cierre limpio o snapshot consistente antes de mover el guardado.
- Bloqueo para impedir que dos instancias modifiquen simultaneamente la misma
  partida.
- Validacion de compatibilidad de version antes de cargar.

No se decide aun si los guardados se cifran, firman o protegen contra
modificaciones del host. Esta decision afecta la confianza en el progreso y
debe resolverse antes de compartir recompensas competitivas.

## Invitaciones y conectividad

La primera implementacion debe usar un relay independiente como mecanismo
principal de conectividad. Su objetivo es atravesar NAT y firewalls sin exigir
configuracion de puertos al host y permitir que el sistema pueda soportar varias
plataformas.

Steam queda fuera del alcance de las etapas iniciales. Se considera una
integracion futura que podria aportar identidad de plataforma, descubrimiento de
amigos, invitaciones y, si corresponde, transporte propio o relay.

La arquitectura debe separar estas capas:

- **Descubrimiento e invitacion**: localizar una partida y autorizar invitados.
- **Identidad**: identificar al host y a los jugadores dentro de una partida.
- **Transporte**: establecer y mantener la conexion con el servidor mediante el
  relay.
- **Protocolo de juego**: intercambiar mensajes entre cliente y servidor sin
  depender de Steam ni del proveedor del relay.

Steam no debe ser un requisito del protocolo ni del formato de guardado. Cuando
se implemente, podra integrarse como proveedor adicional de descubrimiento,
invitacion e identidad, y usar el transporte existente o uno propio si resulta
necesario. La primera version puede usar un codigo o token de partida para las
invitaciones mientras no exista una integracion de plataforma.

## Preguntas Pendientes para el Equipo

- ¿Se contratara un relay independiente y cual es su coste por transferencia y
  concurrencia?
- ¿Que proveedor y protocolo de relay se usaran en la primera implementacion?
- ¿Como se generan, expiran y revocan los codigos o tokens de invitacion?
- ¿El servidor dedicado necesita autenticacion de plataforma o puede aceptar
  invitados mediante un codigo de partida?
- ¿Que ocurre si el host se desconecta durante una sesion?
- ¿La migracion requiere que todos los jugadores abandonen la partida?
- ¿Se permiten varios backups y como se restaura una version anterior?
- ¿El progreso local puede participar en PVP o tablas competitivas?
- ¿Que plataformas soportan iniciar el servidor local como proceso separado?
- ¿Que datos necesitara la futura integracion de Steam y como se asociaran a una
  identidad de partida sin modificar el protocolo de juego?

## Fuente

Decisiones registradas en la conversacion de arquitectura del 2026-08-13.
