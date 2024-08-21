from fastapi import APIRouter

Joseph_router = APIRouter()


@Joseph_router.get('/')
async def index():
    return 'Hello, World! form Joseph!'
