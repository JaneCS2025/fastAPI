# FastAPI Project

A simple REST API built with [FastAPI](https://fastapi.tiangolo.com/).

---

## Requirements

- Python 3.10 or higher
- pip

---

## Installation (Windows)

### 1. Clone the repository

```bash
git clone https://github.com/JaneCS2025/fastAPI.git
cd fastAPI
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

```bash
venv\Scripts\activate
```

> You should see `(venv)` appear at the beginning of your terminal prompt.

### 4. Install dependencies

Install FastAPI with all standard extras:

```bash
pip install "fastapi[standard]"
```

Or install from `requirements.txt`:

```bash
pip install -r requirements.txt
```

> **Note:** If you don't need `fastapi-cloud-cli`, you can use:
>
> ```bash
> pip install "fastapi[standard-no-fastapi-cloud-cli]"
> ```

---

## Running the Development Server

Make sure your virtual environment is activated, then run:

```bash
fastapi dev main.py
```

The server will start and be available at:

| URL                           | Description                       |
| ----------------------------- | --------------------------------- |
| `http://127.0.0.1:8000`       | API root                          |
| `http://127.0.0.1:8000/docs`  | Interactive API docs (Swagger UI) |
| `http://127.0.0.1:8000/redoc` | Alternative API docs (ReDoc)      |

---

## API Endpoints

| Method | Endpoint           | Description                                  |
| ------ | ------------------ | -------------------------------------------- |
| `GET`  | `/`                | Returns a Hello World message                |
| `GET`  | `/items/{item_id}` | Get an item by ID (optional query param `q`) |
| `PUT`  | `/items/{item_id}` | Update an item by ID                         |

---

## Environment Variables

This project supports environment variables via a `.env` file.

| Variable  | Default | Description                  |
| --------- | ------- | ---------------------------- |
| `MY_NAME` | `World` | Name used in greeting output |

To set it on Windows:

```bash
set MY_NAME=Jane
python variable.py
```

Or create a `.env` file in the project root:

```
MY_NAME=Jane
```

---

## Deactivating the Virtual Environment

When you're done, deactivate the virtual environment with:

```bash
deactivate
```
