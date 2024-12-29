"""check that cause is unique per action

need to know if cause is a suitable discriminator within an action
"""
import json
from pathlib import Path

schema_file = Path("schema.json")
with schema_file.open() as f:
    schemas = json.load(f)


causes = []
for resource_list in schemas.values():
    for item in resource_list:
        for detail in item["details"]:
            causes.append(detail["cause"])

    # TODO: finish...
