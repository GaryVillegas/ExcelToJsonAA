# Excel to JSON API

Esta es una API REST construida con Flask que permite subir archivos Excel (`.xlsx` o `.xls`) y convertir su contenido a formato JSON. Es útil para procesar planillas con datos tabulares y consumirlos desde una aplicación web o móvil.

---

## Características

- Soporta archivos Excel `.xlsx` y `.xls`
- Convierte el contenido a JSON
- Limpia valores vacíos (NaN) rellenando celdas combinadas
- Compatible con React u otras interfaces frontend
- Preparado para correr en Docker

---

## Requisitos

- Python 3.8 o superior
- pip
- Docker (opcional)

---

## Instalación local

1. Clona el repositorio:

```bash
git clone https://github.com/tuusuario/excel-to-json-api.git
cd excel-to-json-api
```

2. Crea un entorno virtual e instala dependencias:

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Ejecuta la aplicacion:

```bash
python app.py
#or
flask run
```
