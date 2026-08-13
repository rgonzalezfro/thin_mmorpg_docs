---
id: TEC-005
title: "Arquitectura de servidor local, Godot y Nakama"
category: Tech_Specs
status: draft
scope: Pre-Alpha
tags: [godot, nakama, headless, server, packaging]
last_updated: 2026-08-13
source_brainstorm: "00_Brainstorming/tecnhical_2026-08-13.md"
dependencies: []
---

# Arquitectura de servidor local, Godot y Nakama

## Estado

Documento de arquitectura exploratoria. La propuesta debe validarse con prototipos
antes de convertirse en base de implementacion.

## Propuesta registrada

### Simulacion autoritativa en Godot

Godot ejecutado en modo headless seria la autoridad de la simulacion realtime del
mundo. Su alcance propuesto incluye movimiento, fisica, colisiones, personajes,
NPCs, combate, proyectiles, items, interacciones, estado del mundo, reglas de
juego, instancias y spawn/despawn.

El cliente visual no debe ser autoridad sobre esos sistemas.

### Nakama como backend

Nakama se considera exclusivamente como backend de servicios de juego, no como
servidor de simulacion. Las capacidades candidatas incluyen autenticacion,
cuentas, identidad de jugadores, amigos, grupos, chat, presencia, notificaciones,
persistencia, leaderboards, achievements y coordinacion de sesiones o instancias
cuando corresponda.

## Empaquetado y ejecucion local

Se requiere que el servidor local pueda ejecutarse como proceso independiente, en
segundo plano u oculto, y que el juego pueda iniciarlo y cerrarlo de forma
controlada.

Se propone evaluar un wrapper en Go que coordine el proceso local y, si resulta
viable, incluya una instancia de PostgreSQL embebida mediante `embedded-postgres`.

## Preguntas Pendientes para el Equipo

- ¿Godot headless puede ejecutar todas las escenas y sistemas requeridos sin
  dependencias de renderizado?
- ¿Que transporte usara el servidor local para clientes locales, relay y
  dedicado?
- ¿Nakama se ejecutara como servicio remoto, local o ambos durante desarrollo?
- ¿Que datos viven en el guardado portable de la partida y cuales en Nakama?
- ¿El wrapper Go es necesario frente a un launcher del cliente y scripts del
  sistema operativo?
- ¿La dependencia `embedded-postgres` es compatible con las plataformas y
  licencias objetivo?

## Fuente

[[../00_Brainstorming/tecnhical_2026-08-13|Brainstorming tecnico 2026-08-13]].
