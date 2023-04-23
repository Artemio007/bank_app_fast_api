from pydantic import BaseModel


class BelkaBaseModel(BaseModel):
    sell_currency: str
    buy_currency: str
    bank_sell: float
    bank_buy: float


class BelkaCreateModel(BelkaBaseModel):
    pass


class BelkaUpdateModel(BelkaBaseModel):
    pass


class BelkaModel(BelkaBaseModel):
    id: int

    class Config:
        orm_mode = True
