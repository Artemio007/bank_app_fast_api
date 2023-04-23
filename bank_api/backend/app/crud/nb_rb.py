import logging
from sqlalchemy.orm import Session
from app.models.nb_rb import NbRb

logger = logging.getLogger('bank_aggregator')


def create_nb_rb_bank(db: Session, nb_rb: NbRb) -> NbRb:
    db_nb_rb = NbRb(
        sell_currency=nb_rb.sell_currency,
        buy_currency=nb_rb.buy_currency,
        convert=nb_rb.convert,
    )
    db.add(db_nb_rb)
    db.commit()
    db.refresh(db_nb_rb)
    logger.info(f'Created nb_rb db {db_nb_rb}')
    return db_nb_rb


def get_nb_rb_by_id(db: Session, id_: int) -> NbRb:
    try:
        return db.query(NbRb).filter(NbRb.id == id_).first()
    except Exception as err:
        logger.error(f"Func get_nb_rb_by_id have an error: {err}")


def del_nb_rb_by_id(db: Session, id_: int):
    try:
        res = db.query(NbRb).filter(NbRb.id == id_).first()
        db.delete(res)
        db.commit()
        return res
    except Exception as err:
        db.rollback()
        logger.error(f"Func del_nb_rb_by_id have an error: {err}")