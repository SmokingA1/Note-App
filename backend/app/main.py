from fastapi import FastAPI
from app.api import main

app = FastAPI(title="Note App")
app.include_router(main.router)


@app.get("/", response_model=dict)
async def get_home_page():
    return {"data": "Server run successfully"}