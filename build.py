"""Render both static language versions for GitHub Pages."""

import json
from html import escape
from pathlib import Path
from string import Template

ROOT = Path(__file__).resolve().parent
FORM = "https://forms.gle/fbEMRiPKKkjxS4aTA"
template = Template((ROOT / "page.html").read_text())
content = json.loads((ROOT / "content.json").read_text())

for language, copy in content.items():
    english = language == "en"
    prefix = "../" if english else "./"
    output = ROOT / "docs" / ("en/index.html" if english else "index.html")
    values = {key: escape(text) for key, text in copy.items() if key != "questions"}
    values["questions"] = "\n".join(
        f"<details><summary>{escape(question)}</summary><p>{escape(answer)}</p></details>"
        for question, answer in copy["questions"]
    )
    values.update(
        lang=language,
        direction="ltr" if english else "rtl",
        root=prefix,
        english="./" if english else "./en/",
        hebrew=prefix,
        english_current='aria-current="page"' if english else "",
        hebrew_current='' if english else 'aria-current="page"',
        form=FORM,
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(template.substitute(values))
