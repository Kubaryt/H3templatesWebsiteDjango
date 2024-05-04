# H3templates website 🌐

## 📄 About the project

I want to create website with Django, that will store all popular Heroes III templates. I want to create 2 modules:
- **Built-in templates patches**
- **Original templates**

### **Built-in templates patches**

This module will store all patches of built-in templates. Each template will have:
- description,
- basic meta guide,
- main version.

### **Original templates**

This module will store all popular original templates. Each template will have:
- description,
- basic meta guide,
- latest version,
- historical versions.

I want also to make auth system, so users can add their own templates.

## 🛠️ Installation guide

### Installation

1. Clone the repository
   ```sh
   git clone https://github.com/Kubaryt/H3templatesWebsiteDjango
   ```
2. Install [python-poetry](https://python-poetry.org/) and project packages with:
   ```sh
   poetry install
   ```
3. Install [pre-commit](https://pre-commit.com/) and add pre-commit hooks with:
   ```sh
   pre-commit install
   ```

### Server running

1. For now we use sqlite3, so its just:
   ```sh
   python manage.py runserver
   ```
