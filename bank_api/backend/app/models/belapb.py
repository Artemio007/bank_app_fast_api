from sqlalchemy import Column, Float
from app.db.base_class import Base
from app.models.mixin import Timestamp
from app.models.sample_banks import SampleBank


class Balapb(SampleBank, Timestamp, Base):
    convert = Column(Float, nullable=False)
