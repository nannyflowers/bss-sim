from pathlib import Path

OUTPUT_FILE = "project_dump.txt"

IGNORE_DIRS = {
    ".git",
    "__pycache__",
    ".vscode",
    "venv",
    "env"
}

IGNORE_FILES = {
    "dump_project.py"
}

root = Path(".")

with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
    for path in sorted(root.rglob("*.py")):
        if any(part in IGNORE_DIRS for part in path.parts):
            continue

        if path.name in IGNORE_FILES:
            continue

        out.write(f"\n{'=' * 80}\n")
        out.write(f"# FILE: {path}\n")
        out.write(f"{'=' * 80}\n\n")

        with open(path, "r", encoding="utf-8") as f:
            out.write(f.read())
            out.write("\n")
