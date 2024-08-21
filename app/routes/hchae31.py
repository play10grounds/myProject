from fastapi import APIRouter

hchae31_router = APIRouter()

@hchae31_router.get('/')
async def index():
    return 'Hello, World!! from hchae31'