from sqlalchemy import Column, Integer, String


class SampleBank:
    id = Column(Integer, primary_key=True, nullable=False)
    sell_currency = Column(String(50), nullable=False)
    buy_currency = Column(String(50), nullable=False)
