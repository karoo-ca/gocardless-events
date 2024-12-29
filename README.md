# gocardless event schemas

Type-safe Python models for for all GoCardless events (using Pydantic).

This is a Python implementation of the Event Actions in the [GoCardless docs](https://developer.gocardless.com/api-reference#event-actions).

1. collect html article snippets from gocardless API event docs for `./raw_data/` and clean the html so it's minimal (no `<a>` tags, no `class=`, `id=`, etc.)
1. run `split_simple.py` on each .html to split into 1 file per event into `./docs/`
1. run `generate_schema.py` to convert all split elements into a json blob `./schema.json`
1. `generate_models.py` converts the json schema into python modules with pydantic models in `./src/gocardless_events/models/`

> [!NOTE]
>
> This doesn't use a standard json-schema, that seemed like more effort (although probably would be better)

```sh
uv run ruff format .
uv run ruff check --fix .
uv run pytest
```

```sh
uv run scripts/split_simple.py --help
uv run scripts/generate_schema.py
uv run scripts/generate_models.py
```
