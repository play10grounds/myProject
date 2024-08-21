from fastapi import APIRouter

yoon_router = APIRouter()

@yoon_router.get('/')
async def index():
    return 'Hello, World from yoon!!'