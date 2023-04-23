from sqlalchemy import Column, Float
from app.db.base_class import Base
from app.models.mixin import Timestamp
from app.models.sample_banks import SampleBank


class AlphaBank(SampleBank, Timestamp, Base):
    bank_sell = Column(Float, nullable=False)
    bank_buy = Column(Float, nullable=False)
