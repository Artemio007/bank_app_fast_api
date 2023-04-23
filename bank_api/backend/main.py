import threading

from typing import Annotated

from fastapi import Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Form
from starlette.responses import RedirectResponse, HTMLResponse


from app.currency_bot.tg_bot import bot
from app.currency_bot.call import all_values
from app.currensy_calc.calc_nb import name_all_curr
from app.apis_all_banks.alpha_api.alpha_redis import alpha_get_from_redis
from app.apis_all_banks.belarusbank_api.belka_redis import belarusbank_get_from_redis
from app.apis_all_banks.belapb_api.belapb_redis import belapb_get_from_redis
from app.apis_all_banks.nb_rb_api.nb_rb_redis import nb_rb_get_from_redis
from app.api.api import api_router

import logging

logging.basicConfig(level=logging.INFO, filename="fastlog.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger('bank_aggregator')


app = FastAPI()
app.include_router(api_router)

app.mount("/static", StaticFiles(directory="../frontend/static"), name="static")
templates = Jinja2Templates(directory="../frontend/templates")

response_data = []


def run_bot():
    try:
        bot.infinity_polling(timeout=10, long_polling_timeout=5)
    except Exception as err:
        logger.info(f"Error in func run_bot -- {err}")


thread = threading.Thread(target=run_bot)
thread.start()


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/nb_rb", response_class=HTMLResponse)
async def index00(request: Request, val="BYN", num=10):
    logging.info("nb_rb is active")
    result = nb_rb_get_from_redis()
    try:
        if response_data:
            table_res = all_values(name_all_curr, response_data[0], response_data[1])
            context = {"request": request,
                       "result": result.split("  "), # change separator
                       "table_res": table_res}
            return templates.TemplateResponse("try_page.html", context)
        else:
            table_res = all_values(name_all_curr, val, num)
            context = {"request": request,
                       "result": result.split("  "),
                       "table_res": table_res}
            return templates.TemplateResponse("try_page.html", context)
    except Exception as err:
        logging.error(f"func 'index00' have an error: {err}")


@app.get("/items/")
def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    logging.info("items is active")
    return commons


@app.get("/users/")
def read_users(commons: Annotated[dict, Depends(common_parameters)]):
    logging.info("users is active")
    return commons


@app.get("/belarusbank")
def index1(request: Request):
    try:
        result = belarusbank_get_from_redis()
        return templates.TemplateResponse("belarusbank_page.html", {"request": request, "result": result.split("  ")})
    except Exception as err:
        logging.error(f"func 'index1' have an error: {err}")


@app.get("/belapb")
def index2(request: Request):
    result = belapb_get_from_redis()
    return templates.TemplateResponse("belapb_page.html", {"request": request, "result": result.split("  ")})


@app.get("/alpha")
def index3(request: Request):
    logging.info("An INFO")
    result = alpha_get_from_redis()
    return templates.TemplateResponse("alphabank_page.html", {"request": request, "result": result.split("  ")})


@app.post("/submitform")
def index0(currency: str = Form(...), num: int = Form(...)):
    response_data.clear()
    response_data.append(currency)
    response_data.append(num)
    return RedirectResponse("nb_rb", status_code=303)


@app.post("/regist")
async def register_form(name: str = Form(...), mail: str = Form(...), password: str = Form(...)):
    print(name)
    print(mail)
    print(password)
    return RedirectResponse("regist", status_code=303)