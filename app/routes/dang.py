from fastapi import APIRouter

dang_router = APIRouter()

@dang_router.get('/')
async def index():
    return 'Hello, World from dangdang!!'