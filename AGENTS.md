# Reglas del submodulo de documentacion

Este archivo define como convertir conversaciones y material de exploracion en
una fuente de verdad de diseno mantenible. Este repositorio es la autoridad
para decisiones, especificaciones y trazabilidad del proyecto.

## Responsabilidad del repositorio

- Mantener el vault documental y su historial sin mezclarlo con codigo de cliente o servidor.
- Registrar decisiones confirmadas, propuestas, preguntas abiertas y fuentes historicas con su estado correspondiente.
- Proporcionar especificaciones aprobadas que puedan ser consumidas por los submodulos de implementacion.
- No asumir que un documento aprobado autoriza cambios fuera de su alcance.

## Limites

- No edites `client` ni `server` desde este repositorio.
- No conviertas automaticamente una idea o propuesta en una decision.
- No cambies una decision contradictoria por cuenta propia; registra la contradiccion y la pregunta pendiente.

## Principios

- Las fuentes de `00_Brainstorming/` contienen exploracion y no son decisiones por si mismas.
- No conviertas una opinion, referencia externa o propuesta en una decision sin evidencia explicita del equipo.
- Conserva la incertidumbre: usa `draft` mientras una definicion no este aprobada.
- No inventes numeros, reglas, nombres, formulas, sistemas ni requisitos.
- Antes de crear un documento, busca conceptos equivalentes y reutiliza la terminologia existente.
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

Cada categoria formal debe tener un `_INDEX.md`. Usa subcarpetas solo cuando
exista un dominio estable, suficientemente grande y con expectativa de crecimiento.

## Flujo de procesamiento

1. Lee la fuente completa y conserva su contexto, participantes y fecha cuando esten disponibles.
2. Clasifica cada elemento como idea, propuesta, pregunta abierta, decision, especificacion, cambio de decision o referencia.
3. Compara el contenido con los documentos e indices existentes.
4. Actualiza, amplia, divide o crea el documento minimo necesario.
5. Anade la fuente y los WikiLinks relevantes.
6. Actualiza los indices afectados.
7. Comprueba estructura, frontmatter, enlaces, duplicados, contradicciones y terminologia.

## Estados y frontmatter

Los documentos formales usan `draft`, `approved` o `deprecated`. Todo documento
formal dentro de `01` a `05` debe comenzar con frontmatter valido, incluyendo
`id`, `title`, `category`, `status`, `scope`, `tags`, `last_updated`,
`source_brainstorm` y `dependencies`.

- `draft`: exploracion o contenido pendiente de aprobacion.
- `approved`: diseno confirmado y apto para servir de base a implementacion.
- `deprecated`: reemplazado; conserva el historial si tiene valor historico.

Las categorias validas son `Core_Systems`, `Content_Entities`, `Tech_Specs`,
`Game_Loops` y `Tasks_Roadmap`. Los estados validos son `draft`, `approved` y
`deprecated`.

No confundas el estado del documento con el estado de una caracteristica del juego.

## Navegacion, preguntas y mantenimiento

- Usa WikiLinks con formato `[[Nombre del archivo|Texto]]` cuando conecten conceptos relacionados.
- Cada documento nuevo debe aparecer una sola vez en su `_INDEX.md`.
- Las fuentes historicas no deben reescribirse para mejorar su redaccion.
- Si existe una contradiccion sin resolver, documenta la pregunta y la fuente en conflicto.
- Cuando falte una definicion importante, anade una seccion `Preguntas Pendientes para el Equipo`.
- Los documentos obsoletos no se eliminan automaticamente; enlaza su reemplazo cuando corresponda.
- Procesa las fuentes de forma incremental y no mezcles cambios de diseno no relacionados.
- Publica el commit de este repositorio antes de actualizar el gitlink `docs` desde la raiz.
