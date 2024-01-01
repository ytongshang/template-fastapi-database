import os
from pathlib import Path

from clio import Workspace


def database_config():
    db_uri = os.environ.get("DATABASE_URI", None)
    if not db_uri:
        db_host = os.environ.get("DB_HOST", None)
        db_user = os.environ.get("DB_USER", None)
        db_pass = os.environ.get("DB_PASSWORD", None)
        db_name = os.environ.get("DB_NAME", None)
        db_uri = f"mysql+pymysql://{db_user}:{db_pass}@{db_host}/{db_name}"
    return db_uri


def get_log_dir() -> Path:
    return Workspace.default_workspace().get_path("cache/log")
