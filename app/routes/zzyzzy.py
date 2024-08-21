from fastapi import APIRouter

zzyzzy_router = APIRouter()

@zzyzzy_router.get('/')
async def index():
    return 'Hello, World from zzyzzy!!'
