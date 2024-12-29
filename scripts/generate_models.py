import json
import subprocess
from pathlib import Path

from jinja2 import Environment, FileSystemLoader


def to_pascal(s):
    return "".join(word.capitalize() for word in s.split("_"))


root_dir = Path("src/gocardless_events")
root_dir.mkdir(parents=True, exist_ok=True)

root_init = root_dir / "__init__.py"
root_init.touch()
root_py_typed = root_dir / "py.typed"
root_py_typed.touch()
outdir = root_dir / "models"
outdir.mkdir(parents=True, exist_ok=True)

env = Environment(  # noqa: S701
    loader=FileSystemLoader(searchpath="./templates/"),
    extensions=["jinja2.ext.do"],
)
env.filters["to_pascal"] = to_pascal
resource_template = env.get_template("{{ resource_name }}.py.jinja")

schema_file = Path("schema.json")
with schema_file.open() as f:
    schemas = json.load(f)

for name, spec in schemas.items():
    schema = {name: spec}
    rendered = resource_template.render(schema=schema)

    outfile = outdir / f"{name.rstrip("s")}.py"
    outfile.write_text(rendered)
    print(f"Wrote {outfile}")

init_template = env.get_template("__init__.py.jinja")
rendered = init_template.render(schemas=schemas)
outfile = outdir / "__init__.py"
outfile.write_text(rendered)
print(f"Wrote {outfile}")

subprocess.run(["ruff", "format", str(root_dir)], check=True)  # noqa: S603,S607
subprocess.run(["ruff", "check", "--fix", str(root_dir)], check=True)  # noqa: S603,S607
