from fastapi import APIRouter
from src.api.users import router as user_router
from src.api.cars import router as cars_router

# from src.api.tags import router as tags_router
# from src.api.videos import router as videos_router

main_router = APIRouter()

# main_router.include_router(videos_router)
main_router.include_router(user_router)
main_router.include_router(cars_router)
# main_router.include_router(tags_router)
