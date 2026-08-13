---
id: TEC-002
title: "Indice publico y publicacion de documentacion"
category: Tech_Specs
status: draft
scope: Pre-Alpha
tags: [documentation, mkdocs, github-pages, publishing]
last_updated: 2026-08-13
source_brainstorm: "Conversacion del proyecto sobre el indice publico y GitHub Pages"
dependencies: []
---

# Indice publico y publicacion de documentacion

## Estado

Especificacion tecnica en revision. Define como presentar la documentacion
publica sin alterar la estructura ni el contenido fuente del vault.

## Objetivo

Proporcionar una pagina inicial con un indice general que permita navegar las
categorias formales de documentacion desde GitHub Pages.

## Estructura publica

La portada debe enlazar con los indices de:

- `01_Core_Systems/`: sistemas centrales.
- `02_Content_Entities/`: contenido y entidades.
- `03_Tech_Specs/`: especificaciones tecnicas.
- `04_Game_Loops/`: bucles de juego.
- `05_Tasks_Roadmap/`: tareas y roadmap.

La portada se genera durante la preparacion de MkDocs en
`.mkdocs/content/index.md`. No debe guardarse como un documento adicional en
la raiz del vault.

## Criterio de publicacion

El sitio publica los documentos Markdown del vault excepto:

- `00_Brainstorming/`.
- `README.md`.
- `AGENT.md`.
- `AGENTS.md`.

Los archivos excluidos permanecen disponibles en el repositorio y no se
eliminan ni se mueven por causa de la publicacion web.

## Navegacion y enlaces

- Los indices de categoria son la entrada formal de cada dominio.
- Los WikiLinks de Obsidian se convierten a enlaces Markdown relativos durante
  la preparacion del sitio.
- Los enlaces a contenido excluido se muestran como texto sin destino.
- La navegacion declarada en `.mkdocs/mkdocs.yml` debe apuntar solo a archivos
  que existan en el contenido preparado.

## Preguntas Pendientes para el Equipo

- ¿El estado `draft` de un documento debe mostrarse visualmente en el sitio?
- ¿Los documentos `deprecated` requieren una seccion historica separada?
- ¿La publicacion debe cambiar a una lista explicita de documentos cuando el
  vault crezca?

## Verificacion

La publicacion debe ejecutar `mkdocs build --strict`, comprobar que la portada
existe y confirmar que no se generan paginas para `00_Brainstorming`,
`README.md`, `AGENT.md` o `AGENTS.md`.

## Referencias

- `.mkdocs/prepare.py`
- `.mkdocs/mkdocs.yml`
- `.github/workflows/deploy-pages.yml`
