from pydantic import BaseModel


class NbRbBaseModel(BaseModel):
    sell_currency: str
    buy_currency: str
    convert: float


class NbRbCreateModel(NbRbBaseModel):
    pass


class NbRbUpdateModel(NbRbBaseModel):
    pass


class NbRbModel(NbRbBaseModel):
    id: int

    class Config:
        orm_mode = True