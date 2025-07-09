from fastapi import FastAPI, HTTPException
from app.services import get_all_people_names

app = FastAPI()

@app.get("/people")
async def people():
    try:
        return await get_all_people_names()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
