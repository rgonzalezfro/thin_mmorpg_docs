from pathlib import Path
import os
import re
import shutil


ROOT = Path(__file__).resolve().parent.parent
DESTINATION = ROOT / ".mkdocs" / "content"
EXCLUDED_DIRECTORIES = {"00_Brainstorming", ".git", ".mkdocs", "site"}
EXCLUDED_FILES = {"agent.md", "agents.md", "readme.md"}
WIKILINK_PATTERN = re.compile(r"\[\[([^\]|#]+)(?:#([^\]|]+))?(?:\|([^\]]+))?\]\]")
INDEX_CONTENT = """# MMORPG 3D Low-Poly Modular

Documentacion de diseno, sistemas y especificaciones del MMORPG.

## Indice general

- [Sistemas centrales](01_Core_Systems/_INDEX.md): reglas compartidas del juego.
- [Contenido y entidades](02_Content_Entities/_INDEX.md): clases, objetos, profesiones y cosmeticos.
- [Especificaciones tecnicas](03_Tech_Specs/_INDEX.md): arquitectura, comunicacion y herramientas.
- [Bucles de juego](04_Game_Loops/_INDEX.md): progresion, economia y conflicto.
- [Tareas y roadmap](05_Tasks_Roadmap/_INDEX.md): trabajo pendiente y prioridades.

## Criterio de publicacion

Este sitio publica los documentos Markdown del vault, excepto `00_Brainstorming/`,
`README.md`, `AGENT.md` y `AGENTS.md`. El brainstorming se conserva en el
repositorio, pero no forma parte de la documentacion publica.
"""


def is_excluded(relative):
    return (
        any(part in EXCLUDED_DIRECTORIES for part in relative.parts)
        or relative.name.lower() in EXCLUDED_FILES
    )


def document_map():
    documents = {}
    for source in ROOT.rglob("*.md"):
        relative = source.relative_to(ROOT)
        if is_excluded(relative):
            continue
        documents[relative.as_posix()] = relative
        documents[relative.with_suffix("").as_posix()] = relative
        documents.setdefault(relative.name, relative)
        documents.setdefault(relative.stem, relative)
    return documents


def resolve_link(source_relative, target, documents):
    target = target.replace("\\", "/").strip()
    if target in documents:
        return documents[target]

    if not target.lower().endswith(".md"):
        target_with_extension = f"{target}.md"
        if target_with_extension in documents:
            return documents[target_with_extension]

    candidate = (source_relative.parent / target).as_posix()
    if candidate in documents:
        return documents[candidate]
    if not candidate.lower().endswith(".md") and f"{candidate}.md" in documents:
        return documents[f"{candidate}.md"]
    return None


def convert_wikilinks(text, source_relative, documents):
    def replace(match):
        target, anchor, label = match.groups()
        display = label or target.rsplit("/", 1)[-1]
        destination = resolve_link(source_relative, target, documents)
        if destination is None:
            return display

        relative_url = os.path.relpath(
            destination.as_posix(), source_relative.parent.as_posix()
        ).replace("\\", "/")
        suffix = f"#{anchor}" if anchor else ""
        return f"[{display}]({relative_url}{suffix})"

    return WIKILINK_PATTERN.sub(replace, text)


def main():
    if DESTINATION.exists():
        shutil.rmtree(DESTINATION)
    DESTINATION.mkdir(parents=True)
    documents = document_map()
    (DESTINATION / "index.md").write_text(INDEX_CONTENT, encoding="utf-8")

    for source in ROOT.rglob("*.md"):
        relative = source.relative_to(ROOT)
        if is_excluded(relative):
            continue
        target = DESTINATION / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        content = source.read_text(encoding="utf-8")
        content = convert_wikilinks(content, relative, documents)
        target.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    main()
