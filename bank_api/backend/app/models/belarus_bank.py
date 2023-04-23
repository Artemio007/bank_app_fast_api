from sqlalchemy import Column, Float

from app.db.base_class import Base
from app.models.sample_banks import SampleBank
from app.models.mixin import Timestamp


class Belarusbank(SampleBank, Timestamp, Base):
    bank_sell = Column(Float, nullable=False)
    bank_buy = Column(Float, nullable=False)
