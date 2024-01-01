from clio import SQLAlchemy

from example.config.config import database_config

db_uri = database_config()

db = SQLAlchemy(db_uri or "", echo=True)
