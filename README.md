# Gesiele Nails — Site profissional

Site institucional responsivo para nail designer, gerado em Python com Jinja2 e publicado no GitHub Pages.

## Estrutura

- `data/site.json`: textos, contatos, cores, modelos, preços e políticas.
- `templates/`: páginas HTML em Jinja2.
- `static/`: CSS, JavaScript e imagens.
- `build.py`: gera o site estático.
- `docs/`: resultado pronto para publicação.
- `.github/workflows/pages.yml`: publicação automática.

## Executar localmente

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
python build.py
python -m http.server 8000 --directory docs
```

Abra `http://localhost:8000`.

## Personalizar

Edite `data/site.json`. Depois execute novamente:

```bash
python build.py
```

Para trocar as imagens, substitua os arquivos em `static/img/` e mantenha os mesmos nomes, ou ajuste o campo `image` em `data/site.json`.

## Publicar no GitHub Pages

1. Crie um repositório no GitHub.
2. Envie todos os arquivos para a branch `main`.
3. No repositório, abra `Settings > Pages`.
4. Em `Build and deployment > Source`, selecione `GitHub Actions`.
5. Faça um novo push ou execute o workflow manualmente em `Actions`.

O endereço será exibido no workflow concluído e na tela de configuração do Pages.
