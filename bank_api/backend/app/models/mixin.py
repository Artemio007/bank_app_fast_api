from datetime import datetime
from sqlalchemy import DateTime, Column

from sqlalchemy.orm import declarative_mixin


@declarative_mixin
class Timestamp:
    time_get_data = Column(DateTime, default=datetime.now(), nullable=False)
