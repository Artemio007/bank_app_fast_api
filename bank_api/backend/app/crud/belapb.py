import logging
from sqlalchemy.orm import Session
from app.models.belapb import Balapb

logger = logging.getLogger('bank_aggregator')


def create_belapb_bank(db: Session, belapb: Balapb) -> Balapb:
    db_belapb = Balapb(
        sell_currency=belapb.sell_currency,
        buy_currency=belapb.buy_currency,
        convert=belapb.convert,
    )
    db.add(db_belapb)
    db.commit()
    db.refresh(db_belapb)
    logger.info(f'Created belapb db - {db_belapb}')
    return db_belapb


def get_belapb_by_id(db: Session, id_: int) -> Balapb:
    try:
        return db.query(Balapb).filter(Balapb.id == id_).first()
    except Exception as err:
        logger.error(f"Func get get_belapb_by_id have an error: {err}")


def del_belapb_by_id(db: Session, id_: int):
    try:
        res = db.query(Balapb).filter(Balapb.id == id_).first()
        db.delete(res)
        db.commit()
        return res
    except Exception as err:
        db.rollback()
        logger.error(f"Func del_belapb_by_id have an error: {err}")
