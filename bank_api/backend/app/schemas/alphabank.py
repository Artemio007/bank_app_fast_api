from pydantic import BaseModel


class AlphaBaseModel(BaseModel):
    sell_currency: str
    buy_currency: str
    bank_sell: float
    bank_buy: float


class AlphaCreateModel(AlphaBaseModel):
    pass


class AlphaUpdateModel(AlphaBaseModel):
    pass


class AlphaModel(AlphaBaseModel):
    id: int

    class Config:
        orm_mode = True
