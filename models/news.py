from pydantic import BaseModel, Field
from typing import Any

class Content(BaseModel):
    title: str
    link: str
    img: Any
    pub_date: str
    description: str
    category: str
    text: str
    


    