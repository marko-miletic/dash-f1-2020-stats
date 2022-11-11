from dotenv import dotenv_values
from pydantic import PostgresDsn


def assemble_db_connection() -> str:

    config = dotenv_values(".env")

    return PostgresDsn.build(
        scheme="postgresql",
        user=config["POSTGRES_USER"],
        password=config["POSTGRES_PASSWORD"],
        host="db",
        port=config["POSTGRES_PORT"],
        path=f"/{config['POSTGRES_DB'] or ''}"
    )