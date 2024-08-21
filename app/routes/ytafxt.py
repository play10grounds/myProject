from fastapi import APIRouter

ytafxt_router = APIRouter()

@ytafxt_router.get('/')
async def index():
    return 'Hello, World from ytafxt'