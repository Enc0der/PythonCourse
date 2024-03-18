### README

This repository contains files for generating LaTeX documents from tabular data.

#### Files:
- **generate_latex.py**: This Python script provides a function to generate a LaTeX document from tabular data.
- **example_data.py**: Contains an example dataset (`data`) to demonstrate the usage of the `generate_full_latex_document` function.
- **example_output.tex**: Example LaTeX output generated from the provided data.
- **Dockerfile**: Dockerfile for creating a Docker image to run the LaTeX generation process.
- **docker-compose.yml**: Docker Compose file for orchestrating the Docker container.

#### Usage:
1. Ensure you have Python installed on your system.
2. Include the `generate_latex.py` file in your project directory.
3. Import the `generate_full_latex_document` function from `generate_latex.py` into your Python script.
4. Prepare your tabular data in a list-of-lists format.
5. Call the `generate_full_latex_document` function with your data to obtain the LaTeX document as a string.
6. Optionally, you can save the generated LaTeX document to a `.tex` file.

Example usage:
```python
from generate_latex import generate_full_latex_document

# Example data
data = [
    ["Header 1", "Header 2", "Header 3"],
    ["Data 1", "Data 2", "Data 3"],
    ["Data 4", "Data 5", "Data 6"]
]

# Generate LaTeX document
latex_document = generate_full_latex_document(data)
print(latex_document)
```

#### Docker Usage:
1. Install Docker on your system.
2. Navigate to the project directory containing the Dockerfile and docker-compose.yml.
3. Build the Docker image:
   ```bash
   docker-compose build
   ```
4. Run the Docker container:
   ```bash
   docker-compose up
   ```
5. The LaTeX document generation process will be executed within the Docker container.

#### Installation:
You can install the `catopalidi` package using pip:
```bash
pip install catopalidi
```

This package provides functionalities to generate LaTeX code for tables and documents.

#### Contribution:
- Clone the repository: `git clone https://github.com/Enc0der/PythonCourse.git`
- Make changes and submit a pull request.
