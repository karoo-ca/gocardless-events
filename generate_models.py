import json
import subprocess
from pathlib import Path

from jinja2 import Environment, FileSystemLoader


def to_pascal(s):
    return "".join(word.capitalize() for word in s.split("_"))


outdir = Path("models")
outdir.mkdir(parents=True, exist_ok=True)

env = Environment(
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

subprocess.run(["ruff", "format", str(outdir)], check=True)
subprocess.run(["ruff", "check", "--fix", str(outdir)], check=True)
