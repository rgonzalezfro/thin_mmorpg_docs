# Protocolo de documentación del proyecto

Este archivo define cómo convertir conversaciones y material de exploración en una fuente de verdad de diseño mantenible.

## Principios

- Las fuentes de `00_Brainstorming/` contienen exploración y no son decisiones por sí mismas.
- No conviertas una opinión, referencia externa o propuesta en una decisión sin evidencia explícita del equipo.
- Conserva la incertidumbre: usa `draft` mientras una definición no esté aprobada.
- No inventes números, reglas, nombres, fórmulas, sistemas ni requisitos.
- Antes de crear un documento, busca conceptos equivalentes y reutiliza la terminología existente.
- Prefiere actualizar o dividir un documento existente antes que crear duplicados.

## Estructura del vault

```text
docs/
├── AGENTS.md
├── 00_Brainstorming/
├── 01_Core_Systems/
├── 02_Content_Entities/
├── 03_Tech_Specs/
├── 04_Game_Loops/
└── 05_Tasks_Roadmap/
```

Cada categoría formal debe tener un `_INDEX.md`. Usa subcarpetas solo cuando exista un dominio estable, suficientemente grande y con expectativa de crecimiento.

## Flujo de procesamiento

1. Lee la fuente completa y conserva su contexto, participantes y fecha cuando estén disponibles.
2. Clasifica cada elemento como idea, propuesta, pregunta abierta, decisión, especificación, cambio de decisión o referencia.
3. Compara el contenido con los documentos e índices existentes.
4. Actualiza, amplía, divide o crea el documento mínimo necesario.
5. Añade la fuente y los WikiLinks relevantes.
6. Actualiza los índices afectados.
7. Comprueba estructura, frontmatter, enlaces, duplicados, contradicciones y terminología.

## Estados

Los documentos formales usan estos estados:

- `draft`: exploración o contenido pendiente de aprobación.
- `approved`: diseño confirmado y apto para servir de base a implementación.
- `deprecated`: reemplazado; conserva el historial si tiene valor histórico.

No confundas el estado del documento con el estado de una característica del juego.

## Frontmatter formal

Todo documento formal dentro de `01` a `05` debe comenzar con este esquema:

```yaml
---
id: SYS-001
title: "Nombre claro del módulo o mecánica"
category: Core_Systems
status: draft
scope: Pre-Alpha
tags: [combat]
last_updated: 2026-08-11
source_brainstorm: "00_Brainstorming/archivo.md"
dependencies: []
---
```

Categorías válidas: `Core_Systems`, `Content_Entities`, `Tech_Specs`, `Game_Loops` y `Tasks_Roadmap`. Estados válidos: `draft`, `approved` y `deprecated`.

## Navegación y trazabilidad

- Usa WikiLinks con formato `[[Nombre del archivo|Texto]]` cuando conecten conceptos relacionados.
- Cada documento nuevo debe aparecer una sola vez en su `_INDEX.md`.
- Las fuentes históricas no deben reescribirse para mejorar su redacción.
- Si existe una contradicción sin resolver, no elijas por cuenta propia: documenta la pregunta y la fuente en conflicto.
- Los documentos obsoletos no se eliminan automáticamente; enlaza su reemplazo cuando corresponda.

## Preguntas abiertas

Cuando falte una definición importante, añade al final:

```markdown
## Preguntas Pendientes para el Equipo

- [ ] ¿Qué decisión falta tomar?
```

## Mantenimiento

Procesa las fuentes de forma incremental. No reestructures todo el vault por cada conversación y no mezcles una reorganización estructural con cambios de diseño no relacionados.
