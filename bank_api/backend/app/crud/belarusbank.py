import logging
from sqlalchemy.orm import Session
from app.models.belarus_bank import Belarusbank

logger = logging.getLogger('bank_aggregator')


def create_belka_bank(db: Session, belka: Belarusbank) -> Belarusbank:
    db_belka = Belarusbank(
        sell_currency=belka.sell_currency,
        buy_currency=belka.buy_currency,
        bank_sell=belka.bank_sell,
        bank_buy=belka.bank_buy,
    )
    db.add(db_belka)
    db.commit()
    db.refresh(db_belka)
    logger.info(f'Created belarusbank db -  {db_belka}')
    return db_belka


def get_belka_by_id(db: Session, id_:int) -> Belarusbank:
    try:
        return db.query(Belarusbank).filter(Belarusbank.id == id_).first()
    except Exception as err:
        logger.error(f"Func get get_belka_by_id have an error: {err}")


def del_belka_by_id(db: Session, id_: int) -> Belarusbank:
    try:
        res = db.query(Belarusbank).filter(Belarusbank.id == id_).first()
        db.delete(res)
        db.commit()
        return res
    except Exception as err:
        db.rollback()
        logger.error(f"Func del_belka_by_id have an error: {err}")
