from fastapi import FastAPI, Query
from weather_Service import get_weather

app = FastAPI()

@app.get("/climate/{city}")
async def climate(city: str, force: bool = Query(False)):
        return await get_weather(city, force)