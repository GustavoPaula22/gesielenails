from __future__ import annotations

import json
import shutil
from pathlib import Path
from urllib.parse import quote

from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parent
TEMPLATES = ROOT / "templates"
STATIC = ROOT / "static"
DATA_FILE = ROOT / "data" / "site.json"
OUTPUT = ROOT / "docs"

PAGES = [
    ("index.html", "home.html", "Início", "home"),
    ("cores.html", "colors.html", "Cores de Gel", "colors"),
    ("modelos.html", "models.html", "Modelos", "models"),
    ("valores.html", "pricing.html", "Tabela de Valores", "pricing"),
    ("contato.html", "contact.html", "Contato", "contact"),
    ("404.html", "404.html", "Página não encontrada", "404"),
]


def load_data() -> dict:
    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def main() -> None:
    data = load_data()
    brand = data["brand"]
    message = quote(brand["booking_message"])
    data["brand"]["whatsapp_url"] = f"https://wa.me/{brand['whatsapp']}?text={message}"

    env = Environment(
        loader=FileSystemLoader(TEMPLATES),
        autoescape=select_autoescape(["html", "xml"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True)
    shutil.copytree(STATIC, OUTPUT / "assets")

    for filename, template_name, page_title, active_page in PAGES:
        template = env.get_template(template_name)
        html = template.render(
            **data,
            page_title=page_title,
            active_page=active_page,
            current_year=2026,
        )
        (OUTPUT / filename).write_text(html, encoding="utf-8")

    (OUTPUT / ".nojekyll").write_text("", encoding="utf-8")
    print(f"Site gerado com sucesso em: {OUTPUT}")


if __name__ == "__main__":
    main()
