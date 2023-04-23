import logging
from sqlalchemy.orm import Session
from app.models.alphabank import AlphaBank

logger = logging.getLogger('bank_aggregator')


def create_alpha_bank(db: Session, alpha: AlphaBank) -> AlphaBank:
    try:
        db_alpha = AlphaBank(
            sell_currency=alpha.sell_currency,
            buy_currency=alpha.buy_currency,
            bank_sell=alpha.bank_sell,
            bank_buy=alpha.bank_buy
        )
        db.add(db_alpha)
        db.commit()
        db.refresh(db_alpha)
        logger.info(f'Created alpha db - {db_alpha}')
        return db_alpha
    except Exception as err:
        logger.info(f"Have an error in crud/create alpha_bank {err}")


def get_alpha_by_id(db: Session, id_: int) -> AlphaBank:
    try:
        return db.query(AlphaBank).filter(AlphaBank.id == id_).first()
    except Exception as err:
        logger.error(f"Func get author_by_id have an error: {err}")


def del_alpha_by_id(db: Session, id_: int):
    try:
        res = db.query(AlphaBank).filter(AlphaBank.id == id_).first()
        db.delete(res)
        db.commit()
        return res
    except Exception as err:
        db.rollback()
        logger.error(f"Func del_alpha_by_id have an error: {err}")


