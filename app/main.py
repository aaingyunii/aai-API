from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Aaingyunii"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/dday")
def read_root():
    """
    """
    from dday.dday import calculate_dday

    r = calculate_dday()

    return {"프로젝트 마감일" : r}

@app.get("/djw")
def read_root():
    """
    동작구 신대방2동의 날씨 정보
    """
    from dj_weather_show.weather_show import get_weather        
    location, weather_condition, temperature = get_weather()
    
    return {"temperature" : temperature, "weather_condition" : weather_condition, "location":location}
