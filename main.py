import sys
sys.path.append("/Users/monglels/Desktop/PythonCourse/hw_2/latexlibrary")



from catopalidi.table_generator import generate_full_latex_document
from catopalidi.image_generator import generate_latex_image

# Данные для таблицы
data = [
    ["Заголовок 1", "Заголовок 2", "Заголовок 3"],
    ["Данные 1", "Данные 2", "Данные 3"],
    ["Данные 4", "Данные 5", "Данные 6"]
]

# Генерация LaTeX кода для таблицы и изображения
latex_table = generate_full_latex_document(data)
latex_image = generate_latex_image("generated_avatar_4.png", "Пример изображения")

# Вывод сгенерированного кода
print(latex_table)
print(latex_image)
