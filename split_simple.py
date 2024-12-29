import argparse
from pathlib import Path


def process_html_file(input_file: Path) -> None:
    """
    i couldn't get beautiful soup to work so i did this manually
    """
    text = input_file.read_text()
    lines = list(filter(lambda x: x, [line.strip() for line in text.splitlines()]))
    indices = [i for i, line in enumerate(lines) if line.startswith("<h3>")]
    titles = [
        line.replace("<h2>", "").replace("</h2>", "").replace(" ", "_").lower()
        for line in lines
        if line.startswith("<h2>")
    ]
    assert len(titles) == 1
    title = titles[0]
    outdir = Path(title)
    outdir.mkdir(parents=True, exist_ok=True)
    print(f"Found {len(indices)} h3 tags at lines: {indices}")
    for i, j in zip(indices, indices[1:] + [None], strict=False):
        name = lines[i].replace("<h3><code>", "").replace("</code></h3>", "")
        contents = lines[i:j]
        outfile = outdir / f"{name}.html"
        outfile.write_text("\n".join(contents))
        print(f"Wrote {outfile}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Split HTML file into sections based on h3 tags."
    )
    parser.add_argument("input_file", type=Path, help="Path to the input HTML file")
    args = parser.parse_args()

    process_html_file(args.input_file)


if __name__ == "__main__":
    main()
