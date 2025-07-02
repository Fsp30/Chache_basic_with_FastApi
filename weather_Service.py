import os
import httpx
from cachetools import TTLCache
from dotenv import load_dotenv

load_dotenv()

Api_Key = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
cache = TTLCache(maxsize=100, ttl=600)

async def get_weather(city: str, force: bool = False):
        if not force and city in cache:
                return {"Cidade": city, "cached": True, "dados": cache[city]}
        
        async with httpx.AsyncClient() as client:
                response = await client.get(BASE_URL, params ={
                        "q": city,
                        "appid": Api_Key,
                        "units": "metric",
                        "lang": "pt_br"
                })
                data = response.json()

                if response.status_code != 200:
                        return {"erro": data.get("message", "Erro desconhecido")}
                
                cache[city] = data
                return {"cidade": city, "cached": False, "dados": data}