from pydantic import BaseModel

class Terrorist(BaseModel):
    name: str
    location : str
    rate_danger : int
