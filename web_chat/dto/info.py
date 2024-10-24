from pydantic import BaseModel


class AppInfoResponse(BaseModel):
    app_version: str