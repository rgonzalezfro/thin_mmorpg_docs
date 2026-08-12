from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parent.parent
DESTINATION = ROOT / ".mkdocs" / "content"
EXCLUDED_DIRECTORIES = {"00_Brainstorming", ".git", ".mkdocs", "site"}


def main():
    if DESTINATION.exists():
        shutil.rmtree(DESTINATION)
    DESTINATION.mkdir(parents=True)

    for source in ROOT.rglob("*.md"):
        relative = source.relative_to(ROOT)
        if any(part in EXCLUDED_DIRECTORIES for part in relative.parts):
            continue
        target = DESTINATION / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)


if __name__ == "__main__":
    main()
