"""thanks o1"""

import os
import json
import re
from bs4 import BeautifulSoup

output = {}

docs_dir = "docs"  # Directory containing the HTML files


def clean_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


# Walk through the 'docs' directory
for root, dirs, files in os.walk(docs_dir):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            # Extract resource_type and action from the file path
            relative_path = os.path.relpath(file_path, docs_dir)
            parts = relative_path.split(os.sep)
            resource_type = parts[0]
            action = os.path.splitext(parts[1])[0]  # Remove .html extension

            # Open and parse the HTML file
            with open(file_path, "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f, "html.parser")

                # Extract the <h3><code>{{ action }}</code></h3>
                h3_code = soup.find("h3").find("code").get_text(strip=True)

                # Extract the <p>{{ description }}</p>
                description_tag = soup.find("p")
                description = (
                    description_tag.get_text(strip=True) if description_tag else ""
                )

                # Extract table headers
                table = soup.find("table")
                if table:
                    headers = [
                        th.get_text(strip=True).replace(" ", "_").lower()
                        for th in table.find("thead").find_all("th")
                    ]
                    # Extract table rows
                    details = []
                    for row in table.find("tbody").find_all("tr"):
                        values = [
                            clean_whitespace(str(td.get_text(strip=True)))
                            for td in row.find_all("td")
                        ]
                        detail = dict(zip(headers, values))
                        details.append(detail)
                else:
                    details = []

                # Build the resource action dictionary
                action_dict = {
                    "action": h3_code,
                    "description": description,
                    "details": details,
                }

                # Add to output dictionary
                resource_key = resource_type + "s"
                if resource_key not in output:
                    output[resource_key] = []
                output[resource_key].append(action_dict)

# Write the output to JSON
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2)
