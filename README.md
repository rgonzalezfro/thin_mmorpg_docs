# Documentacion del MMORPG

Vault documental del proyecto. Este repositorio conserva las ideas, decisiones
y especificaciones que sirven como referencia para el cliente, el servidor y
la integracion general.

## Proposito

- Convertir exploracion en documentacion trazable.
- Separar ideas pendientes de decisiones aprobadas.
- Mantener las especificaciones tecnicas que autorizan implementacion.
- Conservar fuentes historicas y registrar cambios de decision.

## Estructura

```text
docs/
├── AGENTS.md
├── 00_Brainstorming/     # Ideas y material de exploracion
├── 01_Core_Systems/      # Sistemas centrales
├── 02_Content_Entities/  # Entidades, habilidades y objetos
├── 03_Tech_Specs/        # Arquitectura, red, datos y herramientas
├── 04_Game_Loops/        # Bucles y flujos de juego
└── 05_Tasks_Roadmap/     # Tareas, hitos y planificacion
```

Cada categoria formal tiene un `_INDEX.md` como punto de entrada. Obsidian es
opcional; los archivos se mantienen en Markdown y se versionan con Git.

## Estados documentales

- `draft`: exploracion o contenido pendiente de aprobacion.
- `approved`: decision o especificacion confirmada y util para implementar.
- `deprecated`: contenido reemplazado que se conserva por su valor historico.

El codigo de `client` y `server` solo puede basarse en documentos `approved`.
Las ideas `draft` no son requisitos y los documentos `deprecated` no son fuente
vigente.

## Flujo de trabajo

1. Lee la fuente completa y busca conceptos existentes antes de crear documentos.
2. Clasifica el contenido y conserva su origen y contexto.
3. Actualiza el documento minimo necesario y los indices afectados.
4. Mantiene frontmatter, WikiLinks, preguntas pendientes y trazabilidad.
5. Revisa contradicciones, duplicados y enlaces antes de confirmar.

Consulta `AGENTS.md` para las reglas completas del vault.

## Sitio web

La documentacion se publica con MkDocs Material en GitHub Pages. El workflow
de GitHub Actions construye el sitio en cada push a `main` y excluye
unicamente `00_Brainstorming/`; el resto de los archivos Markdown se copia al
sitio publicado.

Para reproducir la build localmente:

```bash
python -m pip install -r requirements.txt
python .mkdocs/prepare.py
mkdocs build --strict --config-file .mkdocs/mkdocs.yml
```

La primera ejecucion requiere habilitar GitHub Pages en el repositorio usando
la fuente **GitHub Actions**. El workflow administra las publicaciones
posteriores automaticamente.
