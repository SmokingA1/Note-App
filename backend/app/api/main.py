from fastapi import APIRouter
from app.api.routes import notes

router = APIRouter()
router.include_router(notes.router)