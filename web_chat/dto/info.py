from pydantic import BaseModel


class AppInfoSchema(BaseModel):
    app_version: str