from app.db.base_class import Base
from app.models.sample_banks import SampleBank
from app.models.mixin import Timestamp
from sqlalchemy import Column, Float


class NbRb(SampleBank, Timestamp, Base):
    convert = Column(Float, nullable=False)

