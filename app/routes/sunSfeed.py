from fastapi import APIRouter

sunSfeed_router = APIRouter()


@sunSfeed_router.get("/")
async def index():
    return 'Hello World from SunSfeed!'