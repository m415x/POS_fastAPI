import reflex as rx
from os import getenv


config = rx.Config(
    app_name="POS_with_Reflex_and_FastAPI",
    db_url=getenv("DB_URL"),
    env=rx.Env.DEV,
)
