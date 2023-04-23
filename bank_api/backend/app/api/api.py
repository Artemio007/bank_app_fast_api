from fastapi import APIRouter

from app.api.endpoint.e_alpha_bank import alpha_route
from app.api.endpoint.e_nb_rb import nb_rb_route
from app.api.endpoint.e_belka import belka_route
from app.api.endpoint.e_belapb import belapb_route

from fastapi_users import FastAPIUsers

from app.auth.cookie import auth_backend
from app.schemas.user import UserRead, UserCreate
from app.auth.manager import get_user_manager
from app.models.user import User


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


api_router = APIRouter()

api_router.include_router(
    alpha_route,
    tags=["alpha bank"]

)

api_router.include_router(
    nb_rb_route,
    tags=["nb_rb bank"]

)

api_router.include_router(
    belka_route,
    tags=["belarus bank"]

)

api_router.include_router(
    belapb_route,
    tags=["belagroprom bank"]

)

api_router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

api_router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)