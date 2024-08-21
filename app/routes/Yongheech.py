from fastapi import APIRouter

Yongheech_router = APIRouter()

@Yongheech_router.get('/')
async def index():
    return 'Hello, World!! from yongheech'