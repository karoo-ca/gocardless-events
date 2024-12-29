# gocardless event schemas

Cleaned docs of all Gocardless events

1. collect html article snippets from gocardless API event docs for `./raw_data/`
1. run `split_simple.py` on each .html to split into 1 file per event into `./docs/`
1. run `generate_schema.py` to convert all split elements into a json format `./schema.json`
1. `generate_models.py` converts the json format into python modules with pydantic models in `./models/`

```sh
uv run ruff format .
uv run ruff check --fix .
```

```sh
uv run scripts/split_simple.py --help
uv run scripts/generate_schema.py
uv run scripts/generate_models.py
```
