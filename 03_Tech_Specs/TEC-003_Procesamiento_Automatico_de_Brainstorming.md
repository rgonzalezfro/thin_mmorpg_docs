---
id: TEC-003
title: "Procesamiento automatico de brainstorming"
category: Tech_Specs
status: draft
scope: Pre-Alpha
tags: [documentation, automation, github-actions, copilot]
last_updated: 2026-08-13
source_brainstorm: "Conversacion del proyecto sobre automatizacion documental"
dependencies: [TEC-002]
---

# Procesamiento automatico de brainstorming

## Estado

Especificacion tecnica en revision. Describe el workflow propuesto para
convertir nuevas fuentes de brainstorming en cambios documentales revisables.

## Flujo

1. Un push a `main` que modifique Markdown en `00_Brainstorming/` activa el workflow.
2. GitHub Agentic Workflows ejecuta GitHub Copilot con un limite de iteraciones y tiempo.
3. El agente lee las reglas y documentos relacionados.
4. El agente crea o actualiza documentos `draft` y sus indices.
5. `safe-outputs` crea un Pull Request draft.
6. El equipo revisa, corrige y decide si mezcla el Pull Request.

El agente no modifica directamente `main` ni puede aprobar decisiones de
diseno. La publicacion en GitHub Pages ocurre despues de mezclar los cambios
formales mediante el workflow de despliegue separado.

## Alcance restringido

El agente puede escribir solamente en `01` a `05`. No puede modificar la fuente
original, `AGENTS.md`, `README.md`, `.github/`, `.mkdocs/`, `client/` ni
`server/`.

## Modelo y autenticacion

El workflow usa `engine: copilot` y permite fijar el modelo mediante el campo
`model` del frontmatter. La autenticacion recomendada es la permission
`copilot-requests: write`, que usa el token de Actions si la cuenta u
organizacion tiene Copilot habilitado para Actions. Como alternativa se puede
configurar el secret `COPILOT_GITHUB_TOKEN` con un fine-grained PAT que tenga
`Copilot Requests`.

La configuracion inicial usa `model: gpt-5-mini` como compromiso entre coste y
capacidad. La disponibilidad exacta de ese identificador depende del plan y de
los modelos habilitados para Copilot en el repositorio. Para cambiarlo, edita
el campo `model` en `.github/workflows/process-brainstorming.md` y recompila
con `gh aw compile process-brainstorming`.

## Preguntas Pendientes para el Equipo

- ¿Que modelo Copilot debe fijarse para equilibrar coste y calidad?
- ¿Debe el workflow procesar varios brainstormings en un mismo Pull Request?
- ¿Se requieren validaciones deterministas adicionales antes de crear el PR?
- ¿Debe limitarse el numero de documentos modificados por ejecucion?

## Referencias

- `.github/workflows/process-brainstorming.md`
- `AGENTS.md`
- `TEC-002_Indice_Publico_y_Publicacion.md`
