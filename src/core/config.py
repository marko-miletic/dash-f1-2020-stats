from dotenv import dotenv_values


def get_db_connection_url() -> str:
    config = dotenv_values(".env")
    db_connection_url = (
        f"postgresql+psycopg2://{config['POSTGRES_DB']}:{config['POSTGRES_PW']}@"
        f"{config['POSTGRES_HOST']}:{config['POSTGRES_PORT']}/postgres"
    )
    return db_connection_url
