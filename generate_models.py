import json
import subprocess
from pathlib import Path

from jinja2 import Environment, FileSystemLoader


def to_pascal(s):
    return "".join(word.capitalize() for word in s.split("_"))


outdir = Path("models")
outdir.mkdir(parents=True, exist_ok=True)

env = Environment(
    loader=FileSystemLoader(searchpath="./"),
    extensions=["jinja2.ext.do"],
)
env.filters["to_pascal"] = to_pascal
template = env.get_template("model.py.jinja")

schema_file = Path("schema.json")
with schema_file.open() as f:
    schemas = json.load(f)

for name, spec in schemas.items():
    schema = {name: spec}
    rendered = template.render(schema=schema)

    outfile = outdir / f"{name.rstrip("s")}.py"
    outfile.write_text(rendered)
    print(f"Wrote {outfile}")

subprocess.run(["ruff", "format", str(outdir)], check=True)
subprocess.run(["ruff", "check", "--fix", str(outdir)], check=True)
