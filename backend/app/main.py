from fastapi import FastAPI
from app.api import main
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Note App")
app.include_router(main.router)


@app.get("/", response_model=dict)
async def get_home_page():
    return {"data": "Server run successfully"}



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешает запросы от всех
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
