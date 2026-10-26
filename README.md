# PyCRUD API

## Project structure

```text
app/
  api/
    routes.py
  main.py
main.py
requirements.txt
```

Route handlers live in `app/api/routes.py`, while `app/main.py` creates the
FastAPI application and registers the API router. The root `main.py` remains as
a compatibility entry point.

## Run locally

Install dependencies and start the development server from the project root:

```powershell
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

The existing `python -m uvicorn main:app --reload` command also continues to
work.
