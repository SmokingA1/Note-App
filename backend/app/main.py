from fastapi import FastAPI

app = FastAPI(title="Note App")

@app.get("/", response_model=dict)
async def get_home_page():
    return {"data": "Server run successfully"}