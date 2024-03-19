def generate_full_latex_document(data):
    """
    Generates a full LaTeX document with a table from a two-dimensional list.
    :param data: Two-dimensional list containing the data for the table.
    :return: String with the complete LaTeX document.
    """
    # Generate the table part
    header = data[0]  # Assumes the first row contains headers
    rows = data[1:]   # The remaining rows are data
    table_latex = "\\begin{table}[h!]\n\\centering\n"
    table_latex += "\\begin{tabular}{|" + "l|" * len(header) + "}\n\\hline\n"
    table_latex += " & ".join(header) + " \\\\\\hline\n"  # Add the table header
    for row in rows:  # Add the data rows
        table_latex += " & ".join(row) + " \\\\\\hline\n"
    table_latex += "\\end{tabular}\n"
    table_latex += "\\caption{Тестовая таблица для Python Backend Course}\n"
    table_latex += "\\end{table}\n"
    
    # Combine with the rest of the document
    full_document = f'''\documentclass{{article}}
\\usepackage[T2A]{{fontenc}} % Добавлено для поддержки кодировки шрифта
\\usepackage[utf8]{{inputenc}} % Уже не обязательно для новых версий LaTeX
\\usepackage[russian]{{babel}} % Поддержка русского языка
\\usepackage{{graphicx}} % Required for inserting images

\\title{{Python}}
\\author{{Aleksandra Topalidi}}
\\date{{March 2024}}

\\begin{{document}}

\\maketitle

\\section{{Introduction}}

{table_latex}

\\begin{{figure}}[h!]
\\centering
\\includegraphics[width=0.5\\textwidth]{{generated_avatar_4.png}}
\\caption{{Пример изображения}}
\\end{{figure}}

\\end{{document}}
'''
    
    return full_document




