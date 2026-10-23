"""Check local Markdown links and required curriculum sections without dependencies."""
import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
errors = []
files = [p for p in ROOT.rglob("*.md")
         if not any(part.startswith(".") for part in p.relative_to(ROOT).parts)
         and "artifacts" not in p.parts]
for path in files:
    content = path.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
        if target.startswith(("http:", "https:", "mailto:", "#")):
            continue
        target = unquote(target.split("#")[0])
        if target and not (path.parent / target).exists():
            errors.append(f"{path.relative_to(ROOT)}: missing link {target}")
required = [
    "Learning objectives", "Prerequisites", "Concepts", "Hands-on lab",
    "Architecture", "Troubleshooting", "Security considerations",
    "Customer conversation prompts", "Knowledge check", "next step",
]
modules = list((ROOT / "modules").glob("*/README.md"))
labs = list((ROOT / "labs").glob("*/README.md"))
if len(modules) != 13 or len(labs) != 11:
    errors.append("Expected 13 modules and 11 labs")
for path in modules:
    content = path.read_text(encoding="utf-8").lower()
    for section in required:
        if section.lower() not in content:
            errors.append(f"{path.relative_to(ROOT)}: missing {section}")
if errors:
    raise SystemExit("\n".join(errors))
print(f"Checked {len(files)} Markdown files, 13 modules and 11 labs")
