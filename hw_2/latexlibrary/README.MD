
```markdown
# LaTeXGenerator

LaTeXGenerator - это Python библиотека, предназначенная для генерации LaTeX документов, включая таблицы и изображения.

## Установка

Чтобы установить последнюю версию LaTeXGenerator, выполните следующую команду:

```bash
pip install LaTeXGenerator
```

## Использование

### Генерация таблицы

Чтобы сгенерировать таблицу в LaTeX:

```python
from latexgenerator import generate_latex_table

data = [
    ["Header 1", "Header 2", "Header 3"],
    ["Data 1", "Data 2", "Data 3"],
    ["Data 4", "Data 5", "Data 6"]
]
latex_code = generate_latex_table(data)
print(latex_code)
```

### Генерация изображений

Чтобы вставить изображение в LaTeX документ:

```python
from latexgenerator import generate_latex_image

latex_code = generate_latex_image('path/to/your/image.png', 'Описание изображения')
print(latex_code)
```

## Генерация PDF файла

Для создания PDF из вашего LaTeX файла, вам понадобится установленный LaTeX дистрибутив. После установки вы можете скомпилировать ваш `.tex` файл следующей командой:

```bash
pdflatex ваш_файл.tex
```

