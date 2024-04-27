from pydantic import BaseModel, Field


class Content(BaseModel):
    title: str
    link: str
    img: str
    pub_date: str
    description: str
    category: str
    text: str
    


    