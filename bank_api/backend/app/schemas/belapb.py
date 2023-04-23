from pydantic import BaseModel


class BelapbBaseModel(BaseModel):
    sell_currency: str
    buy_currency: str
    convert: float


class BelapbCreateModel(BelapbBaseModel):
    pass


class BelapbUpdateModel(BelapbBaseModel):
    pass


class BelapbModel(BelapbBaseModel):
    id: int

    class Config:
        orm_mode = True